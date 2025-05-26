import random


def get_random_int(min_ms: int, max_ms: int) -> int:
    return random.randint(min_ms, max_ms)


def wait_one_to_three() -> int:
    return get_random_int(1000, 3000)


def wait_two_to_five() -> int:
    return get_random_int(2000, 5000)


def wait_three_to_seven() -> int:
    return get_random_int(3000, 7000)


def wait_seven_to_ten() -> int:
    return get_random_int(7000, 10000)


def wait_one_to_ten() -> int:
    return get_random_int(1000, 10000)


def wait_keystroke() -> int:
    return get_random_int(150, 500)


def wait_next_button() -> int:
    return get_random_int(500, 1000)
