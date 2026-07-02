from playwright.sync_api import sync_playwright

URL = "https://big-tech-stocks-hq5dwkokv7hxmger5sbljs.streamlit.app"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(URL, wait_until="networkidle", timeout=60000)
    page.screenshot(path="Screenshot_app_streamlit_live.png", full_page=True)
    browser.close()

print("Screenshot saved as Screenshot_app_streamlit_live.png")
