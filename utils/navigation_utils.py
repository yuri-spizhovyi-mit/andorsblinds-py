import random
from utils.helper import scroll_page


# 🔀 Available site pages to visit
page_projects = [
    "Home",
    "About",
    "Contacts",
    "Products",
    "Services",
    "Insights",
]


def get_random_page_project() -> str:
    return random.choice(page_projects)


def should_open_facebook() -> bool:
    return random.random() < 0.5  # 50% chance


def should_open_instagram() -> bool:
    return random.random() < 0.5  # 50% chance


def navigate_to_random_page(project_page, page_name: str):
    """Navigate using page object methods based on page name."""
    navigation_methods = {
        "Home": project_page.navigate_to_home,
        "About": project_page.navigate_to_about,
        "Contacts": project_page.navigate_to_contacts,
        "Products": project_page.navigate_to_products,
        "Services": project_page.navigate_to_services,
        "Insights": project_page.navigate_to_insights,
    }

    nav_method = navigation_methods.get(page_name)
    if nav_method:
        nav_method()
        print(f"Navigated to {page_name}")
    else:
        print(f"Unknown page: {page_name}")


def navigate_pages_with_scrolling(project_page, page, is_mobile_view: bool):
    number_of_pages = random.randint(2, 6)
    print(f"Navigating between {number_of_pages} pages")

    for i in range(number_of_pages):
        page_name = get_random_page_project()
        print(f"Navigating to the {page_name} page (Step {i + 1})")

        if is_mobile_view:
            project_page.open_hamburger_menu()

        # Dynamically call navigation method like navigate_to_home
        method_name = f"navigate_to_{page_name.lower()}"
        getattr(project_page, method_name)()

        # Scroll down then up
        print("Scrolling down...")
        scroll_page(page, direction="down")
        print("Scrolling up...")
        scroll_page(page, direction="up")

        # Add realistic pause
        delay = random.randint(1000, 4000)
        print(f"Delaying for {delay} ms to simulate human behavior")
        page.wait_for_timeout(delay)
