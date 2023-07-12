import asyncio

from process import Process
from browser import BrowserClass


browser = BrowserClass('https://poslovi.infostud.com')
proces = Process(browser)

asyncio.run(proces.crawl_job_ads())
