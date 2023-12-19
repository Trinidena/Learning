from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=5000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://combinedbrain-test.acrossmatrix.com/")
    page.screenshot(
        path="C:\\Users\\Trinidad Dena\\repos\\playwright\\screenshots\\example.png"
    )
    # Interact with login form
    page.get_by_placeholder("Email Address").fill("tdena@acrosshealthcare.com")
    page.get_by_placeholder("Password").fill("Awesom44$")
    page.get_by_role("button", name="Sign in").click()
    # Continue with the test
    browser.close()
