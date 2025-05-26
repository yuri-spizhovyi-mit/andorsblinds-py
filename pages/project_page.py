from playwright.sync_api import Page
from utils import timegenerator


class ProjectPage:
    def __init__(self, page: Page):
        self.page = page

        # Navigation links
        self.home_link = page.get_by_role("link", name="Home")
        self.about_link = page.get_by_role("link", name="About")
        self.contacts_link = page.get_by_role("link", name="Contacts")
        self.products_link = page.get_by_role("link", name="Products")
        self.services_link = page.get_by_role("link", name="Services")
        self.insights_link = page.get_by_role("link", name="Insights")
        self.contact_us_link = page.locator("a:has-text('Contact Us')")

        # Social media
        self.facebook_link = page.locator("//a[img[@alt='Facebook logo']]")
        self.from_facebook_link = page.locator("span:has-text('andorsblinds.ca')")
        self.instagram_link = page.locator("//a[img[@alt='Instagram logo']]")
        self.from_instagram_link = page.locator('a[href="https://andorsblinds.ca/"]')

        # Hamburger menu
        self.hamburger_menu_button = page.locator("//button[@aria-label='Toggle navigation menu']")

    # Navigation methods
    def navigate_to_home(self):
        self.home_link.click()
        self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def navigate_to_about(self):
        self.about_link.click()
        self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def navigate_to_contacts(self):
        self.contacts_link.click()
        self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def navigate_to_products(self):
        self.products_link.click()
        self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def navigate_to_services(self):
        self.services_link.click()
        self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def navigate_to_insights(self):
        self.insights_link.click()
        self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def navigate_through_contact_us(self):
        self.contact_us_link.click()
        self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def navigate_to_facebook(self):
        self.facebook_link.click()
        self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def navigate_from_facebook(self):
        self.from_facebook_link.click()
        self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def navigate_to_instagram(self):
        self.instagram_link.click()
        self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def navigate_from_instagram(self):
        self.from_instagram_link.click()
        self.page.wait_for_timeout(timegenerator.wait_one_to_three())

    def open_hamburger_menu(self):
        if self.hamburger_menu_button.is_visible():
            print("Hamburger menu detected, opening it.")
            self.hamburger_menu_button.click()
            self.page.wait_for_timeout(timegenerator.wait_one_to_three())
        else:
            print("Hamburger menu not visible.")

    def close_hamburger_menu_if_visible(self):
        if self.hamburger_menu_button.is_visible():
            print("Hamburger menu detected, closing it.")
            self.hamburger_menu_button.click()
            self.page.wait_for_timeout(timegenerator.wait_one_to_three())
        else:
            print("Hamburger menu not visible.")
