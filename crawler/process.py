import sys
import uuid
import logging

from job import Job
from db import DynamoDB
from bs4 import BeautifulSoup
from utils import get_value


class Process:

    def __init__(self, browser):
        self.browser = browser

    async def crawl_job_ads(self):
        logger = logging.getLogger('process')
        logger.setLevel(logging.DEBUG)
        logger.info("started collecting job ads")
        pg = await self.browser.launch_browser()
        await self.browser.go_to(pg)
        await self.browser.pg_click(pg, 'button#__search_button')

        no_of_jobs_html = await pg.inner_html('#__result_summary_bar')
        no_of_jobs_soup = BeautifulSoup(no_of_jobs_html, 'html.parser')
        number_of_jobs = int(no_of_jobs_soup.find(
            'span').text.replace('(', '').split()[0])
        job_ads = []

        while True:
            if len(job_ads) >= number_of_jobs:
                break

            html = await pg.inner_html('#__list_jobs')
            soup = BeautifulSoup(html, 'html.parser')
            new_jobs = soup.select(
                'div.uk-card.uk-card-small.uk-card-default.uk-card-body.uk-margin-bottom')
            job_ads.extend(new_jobs)
            for job in new_jobs:

                j = Job(str(uuid.uuid4()),
                        get_value(job, 'h2'),
                        get_value(job, 'p.uk-h4.uk-margin-remove'),
                        get_value(job, 'p.uk-margin-remove-bottom'),
                        get_value(job, 'p.job__desc'),
                        get_value(job, 'p.uk-margin-remove.uk-text-bold')
                        ).to_dict()

                DynamoDB(j).add_item()

            new_jobs.clear()
            if len(job_ads) >= int(sys.argv[1]):
                break
            await pg.locator("[aria-label='Sledeća stranica']").click()
