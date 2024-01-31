from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, timeout=10000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://combinedbrain-test.acrossmatrix.com/")
    page.get_by_placeholder("Email Address").click()
    page.get_by_placeholder("Email Address").fill("tdena@acrosshealthcare.com")
    page.get_by_placeholder("Password").fill("Awesom44$")
    page.get_by_role("button", name="Sign in").click()
    # ---------------------


with sync_playwright() as playwright:
    run(playwright)
