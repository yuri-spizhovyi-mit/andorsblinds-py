import pytest
from pages.google_search_page import GoogleSearchPage
from pages.project_page import ProjectPage
from utils.keywords import get_random_keyword
from utils.helper import detect_viewport, scroll_page
from utils.navigation_utils import navigate_pages_with_scrolling
from utils.social_media_utils import open_random_social_media
import os
import pytest

skip_in_ci = pytest.mark.skipif(
    os.getenv("CI") == "true", reason="Skip Google tests in CI due to CAPTCHA"
)


@skip_in_ci
def test_smoke_google_to_project(page):
    """Smoke test"""
    keyword = get_random_keyword()
    print(f"\n🔍 Searching: {keyword}")

    # Step 1: Google Search
    search_page = GoogleSearchPage(page)
    search_page.navigate_to_google()
    search_page.accept_cookies_if_visible()
    search_page.dismiss_location_popup_if_visible()
    search_page.perform_search(keyword)

    print("🖱️ Scrolling down then up...")
    scroll_page(page, direction="down")
    scroll_page(page, direction="up")

    # Step 2: Search for the andorsblinds.ca link across pages
    found = search_page.find_andors_link()
    assert found, "Andors Blinds link not found in search results."

    # Step 3: On landing page, navigate through project pages
    project_page = ProjectPage(page)
    is_mobile = detect_viewport(page)

    navigate_pages_with_scrolling(project_page, page, is_mobile)

    # Step 4: Optionally visit social media links
    open_random_social_media(page, project_page)

    print("✅ Test completed successfully")
