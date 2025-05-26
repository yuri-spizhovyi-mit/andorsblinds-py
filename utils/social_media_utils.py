from playwright.sync_api import Page
from pages.project_page import ProjectPage
import random


def open_random_social_media(page: Page, project_page: ProjectPage):
    open_facebook = random.random() < 0.5

    if open_facebook:
        print("Opening Facebook page")
        with page.expect_popup() as popup_info:
            project_page.facebook_link.click(force=True)
        popup = popup_info.value
        popup.wait_for_timeout(2000)
        popup.close()
        print("Facebook popup closed")
    else:
        print("Opening Instagram page")
        with page.expect_popup() as popup_info:
            project_page.instagram_link.click()
        popup = popup_info.value
        popup.wait_for_timeout(2000)
        popup.close()
        print("Instagram popup closed")
