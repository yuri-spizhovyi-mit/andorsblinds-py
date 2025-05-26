import random

# Viewports by category
desktop_viewports = [
    {"width": 1280, "height": 720},
    {"width": 1366, "height": 768},
    {"width": 1440, "height": 900},
    {"width": 1920, "height": 1080},
    {"width": 1600, "height": 900},
    {"width": 2560, "height": 1440},
    {"width": 1680, "height": 1050},
    {"width": 1536, "height": 864},
    {"width": 1360, "height": 768},
    {"width": 1920, "height": 1200},
]

iphone_viewports = [
    {"width": 375, "height": 812},
    {"width": 414, "height": 896},
    {"width": 390, "height": 844},
    {"width": 414, "height": 736},
    {"width": 375, "height": 667},
    {"width": 428, "height": 926},
    {"width": 430, "height": 932},
]

android_tablet_viewports = [
    {"width": 800, "height": 1280},
    {"width": 962, "height": 601},
    {"width": 1280, "height": 800},
    {"width": 1200, "height": 1920},
    {"width": 1200, "height": 2000},
]

ipad_viewports = [
    {"width": 768, "height": 1024},
    {"width": 810, "height": 1080},
    {"width": 834, "height": 1112},
    {"width": 834, "height": 1194},
    {"width": 1024, "height": 1366},
    {"width": 820, "height": 1180},
]

# Sample of realistic user agents
user_agents = [
    {"userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...", "deviceType": "desktop"},
    {"userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5)...", "deviceType": "desktop"},
    {"userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X)...", "deviceType": "mobile", "tabletType": "ipad"},
    {"userAgent": "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-T515)...", "deviceType": "tablet", "tabletType": "android"},
    # Add more from original .ts if needed
]


def get_random_element(array):
    return random.choice(array)


def get_random_user_agent_and_viewport():
    ua = get_random_element(user_agents)
    device_type = ua["deviceType"]

    if device_type == "desktop":
        viewport = get_random_element(desktop_viewports)
    elif device_type == "mobile":
        viewport = get_random_element(iphone_viewports if ua.get("tabletType") != "ipad" else ipad_viewports)
    elif device_type == "tablet":
        viewport = get_random_element(android_tablet_viewports if ua.get("tabletType") == "android" else ipad_viewports)
    else:
        viewport = {"width": 1280, "height": 720}  # fallback

    return {"userAgent": ua["userAgent"], "viewport": viewport}
