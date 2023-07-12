from playwright.async_api import async_playwright as p


class BrowserClass:

    def __init__(self, url=''):
        self.url = url

    async def launch_browser(self):
        apw = await p().start()
        browser = await apw.chromium.launch()
        page = await browser.new_page()
        return page

    async def go_to(self, page):
        await page.goto(self.url)
        return page

    async def pg_click(self, object, selector):
        await object.click(selector)
