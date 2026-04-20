import json
import requests


def get_url(diff: int = 3, length: int = 6) -> str:
    url = "https://random-word-api.herokuapp.com/word?"
    param_diff = "&diff=3"
    param_length = "&length=6"
    if 1 <= diff <= 5:
        param_diff = f"&diff={diff}"
    if 2 <= length <= 15:
        param_length = f"&length={length}"
    return url + param_diff + param_length


def get_word(diff: int = 3, length: int = 6) -> str:
    url = get_url(diff, length)
    try:
        request = requests.get(url)
        word = request.json()[0]
    except:
        word = "error"
    return word


def save_settings(diff: int = 3, length: int = 6):
    settings = {"diff": diff, "length": length}
    with open("settings.json", "w", encoding="UTF-8") as file:
        json.dump(settings, file, indent=4)


def check_settings(diff: int, length: int) -> dict:
    if not (1 <= diff <= 5):
        diff = 3
    if not (2 <= length <= 15):
        length = 6
    return {"diff": diff, "length": length}


def load_settings() -> dict:
    try:
        with open("settings.json", "r", encoding="UTF-8") as file:
            settings = json.load(file)
    except:
        settings = {"diff": 3, "length": 6}
    if "diff" not in settings or "length" not in settings:
        settings = {"diff": 3, "length": 6}
    settings = check_settings(int(settings["diff"]), int(settings["length"]))
    return settings