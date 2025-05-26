import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    executable_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # ✅ your real Chrome path

    browser = playwright_instance.chromium.launch(
        executable_path=executable_path,
        headless=False,
        slow_mo=120,  # mimic human speed
    )
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def context():
    user_data_dir = (
        "C:/Users/yspizhoviy/playwright-profile"  # ✅ your custom profile path
    )
    executable_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # ✅ your real Chrome path

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            slow_mo=120,
            executable_path=executable_path,
        )
        yield context
        context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
