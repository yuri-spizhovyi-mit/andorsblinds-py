from playwright.sync_api import Page
import time
import random
from utils.geolocation import get_random_location
from utils.useragents import get_random_user_agent_and_viewport
from utils import timegenerator


def detect_viewport(page: Page) -> bool:
    viewport = page.viewport_size
    if viewport:
        print(f"Viewport detected: {viewport['width']}x{viewport['height']}")
        is_mobile = viewport["width"] <= 768
        print("Mobile view detected" if is_mobile else "Desktop view detected")
        return is_mobile
    else:
        print("No viewport size detected")
        return False


def scroll_page(
    page: Page,
    direction: str = "down",
    min_step: int = 450,
    max_step: int = 1850,
    delay_between_scrolls: int = 500
):
    scroll_script = """
        async ({ direction, minStep, maxStep, delayBetweenScrolls }) => {
            const totalHeight = document.body.scrollHeight;
            let scrollPosition = window.scrollY;

            const getNextStep = () => {
                const step = Math.floor(Math.random() * (maxStep - minStep + 1)) + minStep;
                return direction === "down" ? step : -step;
            };

            while (
                (direction === "down" && scrollPosition < totalHeight) ||
                (direction === "up" && scrollPosition > 0)
            ) {
                const step = getNextStep();
                window.scrollBy(0, step);
                scrollPosition += step;
                await new Promise(resolve => setTimeout(resolve, delayBetweenScrolls));
            }
        }
    """
    page.evaluate(scroll_script, {
        "direction": direction,
        "minStep": min_step,
        "maxStep": max_step,
        "delayBetweenScrolls": delay_between_scrolls
    })


def find_and_click_link(page: Page, link_text: str, expected_base_url: str, google_page):
    skip_keywords = ["facebook.com", "fb.com", "Facebook"]
    page_count = 0
    max_pages = 15

    expected_base_url = expected_base_url.replace("https://", "").replace("http://", "")
    found = False

    while not found and page_count < max_pages:
        google_page.dismiss_location_popup_if_visible()
        links = page.locator(f'a:has-text("{link_text}")')
        count = links.count()
        print(f"Found {count} links matching '{link_text}' on page {page_count + 1}")

        for i in range(count):
            link = links.nth(i)
            href = link.get_attribute("href") or ""
            normalized = href.replace("https://", "").replace("http://", "")

            if normalized.startswith(expected_base_url) and not any(k in href for k in skip_keywords):
                print(f"Clicking valid link: {href}")
                link.click()
                found = True
                break

        if not found:
            next_button = page.locator("a#pnnext")
            if next_button.is_visible():
                delay = timegenerator.wait_next_button()
                print(f"Waiting {delay}ms before clicking 'Next'")
                page.wait_for_timeout(delay)
                next_button.click()
                page.wait_for_load_state("load")
                scroll_page(page)
            else:
                print("No more results. Link not found.")
                break

        page_count += 1

    return found


def create_random_context(browser):
    random_ua = get_random_user_agent_and_viewport()
    location = get_random_location()
    return browser.new_context(
        geolocation={"latitude": location["lat"], "longitude": location["lon"]},
        permissions=["geolocation"],
        viewport=random_ua["viewport"],
        user_agent=random_ua["userAgent"]
    )


def navigate_slides(page: Page, next_selector: str, prev_selector: str, delay_func):
    next_button = page.locator(next_selector).first
    prev_button = page.locator(prev_selector).first
    available_slides = 0

    while next_button().is_visible():
        next_button().click()
        available_slides += 1

    for _ in range(available_slides):
        page.keyboard.press("ArrowLeft")

    slides_to_navigate = random.randint(0, available_slides)
    print(f"Navigating {slides_to_navigate} slides...")

    for _ in range(slides_to_navigate):
        if next_button().is_visible():
            next_button().click()
            page.wait_for_load_state("domcontentloaded")
            delay = delay_func()
            print(f"Waiting {delay}ms")
            page.wait_for_timeout(delay)

    if random.random() < 0.5:
        back_steps = int(slides_to_navigate * random.uniform(0.1, 1.0))
        print(f"Going back {back_steps} slides...")
        for _ in range(back_steps):
            if prev_button().is_visible():
                prev_button().click()
                page.wait_for_load_state("domcontentloaded")
                delay = delay_func()
                page.wait_for_timeout(delay)
