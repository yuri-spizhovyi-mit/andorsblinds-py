from playwright.sync_api import Page
from utils import timegenerator
from utils.helper import scroll_page


class GoogleSearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.accept_cookies_button = page.locator('button:has-text("I agree")')
        self.search_input = page.locator("textarea[name='q'], input[name='q']")
        self.not_now_button = page.locator("button:has-text('Not now')")
        self.next_button = page.locator(
            "span.oeN89d", has_text="Next"
        )  # ✅ Centralized here

    def navigate_to_google(self):
        self.page.goto("https://www.google.com/")
        self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def accept_cookies_if_visible(self):
        if self.accept_cookies_button.is_visible():
            self.accept_cookies_button.click()
            self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def perform_search(self, keyword: str):
        print(f"Selected Search Query: {keyword}")
        self.search_input.click()

        for char in keyword:
            self.page.keyboard.press(char)
            self.page.wait_for_timeout(150)  # Human typing delay

        # ✅ Fix: Click first visible "Google Search" button
        search_button = self.page.locator('input[name="btnK"]').first
        if search_button.is_visible():
            print("Clicking Google Search button")
            # ✅ Wrap in wait_for_navigation
            with self.page.expect_navigation(wait_until="domcontentloaded"):
                search_button.click()
        else:
            print("Search button not visible. Fallback to pressing Enter.")
            with self.page.expect_navigation(wait_until="domcontentloaded"):
                self.page.keyboard.press("Enter")

        self.page.wait_for_timeout(3000)

    def scroll_page(page, direction="down"):
        scroll_script = """
            async ({ direction }) => {
                const totalHeight = document.body.scrollHeight;
                let scrollPosition = 0;

                while (scrollPosition < totalHeight) {
                    const step = Math.floor(Math.random() * (150 - 60 + 1)) + 60;
                    window.scrollBy(0, direction === "down" ? step : -step);
                    scrollPosition += step;
                    await new Promise(resolve => setTimeout(resolve, 150 + Math.random() * 100));
                }
            }
        """
        page.evaluate(scroll_script, {"direction": direction})

    def find_andors_link(self, max_pages=5) -> bool:
        """Search across pages for andorsblinds.ca, clicking if found."""
        for page_num in range(max_pages):
            print(f"🔍 Checking Google page {page_num + 1}")
            self.page.wait_for_timeout(2000)

            links = self.page.locator("a").all()
            for link in links:
                href = link.get_attribute("href")
                if href and "andorsblinds.ca" in href and "facebook.com" not in href:
                    print(f"✅ Found: {href}")
                    link.scroll_into_view_if_needed()
                    self.page.wait_for_timeout(500)
                    link.click()
                    return True

            print("📜 Scrolling before checking 'Next'...")
            scroll_page(self.page, direction="down")
            self.page.wait_for_timeout(1000)

            if self.next_button and self.next_button.is_visible():
                print("➡️ Clicking Next button")
                self.next_button.scroll_into_view_if_needed()
                self.next_button.click()
                self.page.wait_for_load_state("domcontentloaded")
                self.page.wait_for_timeout(2000)
            else:
                print("❌ No 'Next' button or end of results")
                return False

        print("🔚 Max pages reached without finding link.")
        return False

    def dismiss_location_popup_if_visible(self):
        """Click 'Not now' button if Google shows location permission dialog"""
        try:
            not_now_button = self.page.get_by_role("button", name="Not now")
            if not_now_button.is_visible():
                print('Clicking "Not now" button.')
                not_now_button.click()
                self.page.wait_for_timeout(1000)
        except Exception as e:
            print(f'"Not now" button not found or not clickable: {e}')
