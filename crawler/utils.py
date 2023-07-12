import logging


def get_value(job,selector):
    try: 
        value = job.select_one(selector).text.strip()
        logger = logging.getLogger('utils')
        logger.setLevel(logging.DEBUG)
        logger.info('got value successfully')
    except:
        value = ''
        logging.error('no value for selected job_ad')

    return value
