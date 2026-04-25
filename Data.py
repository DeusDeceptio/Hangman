import json
import requests
import random


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


def validate_settings(diff: int, length: int) -> dict:
    if not (1 <= diff <= 5):
        diff = 3
    if not (2 <= length <= 15):
        length = 6
    return {"diff": diff, "length": length}


def get_settings() -> dict:
    default = {"diff": 3, "length": 6}
    try:
        with open("settings.json", "r", encoding="UTF-8") as file:
            settings = json.load(file)
    except:
        return default
    if "diff" not in settings or "length" not in settings:
        return default
    return validate_settings(int(settings["diff"]), int(settings["length"]))


def validate_record(record: dict) -> dict:
    name = record.get("name", "Unknown")
    score = record.get("score", 0)
    time = record.get("time", 999)
    if not isinstance(name, str):
        name = "Unknown"
    if not isinstance(score, int) or score < 0:
        score = 0
    if not isinstance(time, int) or time < 0:
        time = 999
    return {"name": name, "score": score, "time": time}


def validate_leaderboard(leaderboard: list) -> list:
    if not isinstance(leaderboard, list):
        return []
    for i in range(len(leaderboard)):
        record = leaderboard[i]
        if not isinstance(record, dict):
            record = {}
        leaderboard[i] = validate_record(record)
    return leaderboard


def get_leaderboard() -> list:
    try:
        with open("leaderboard.json", "r", encoding="UTF-8") as file:
            leaderboard = json.load(file)
    except:
        return []
    return validate_leaderboard(leaderboard)


def save_leaderboard(leaderboard: list):
    with open("leaderboard.json", "w", encoding="UTF-8") as file:
        json.dump(leaderboard, file, indent=4)


def add_record(name: str, score: int, time: int):
    leaderboard = get_leaderboard()
    record = validate_record({"name": name, "score": score, "time": time})
    leaderboard.append(record)
    save_leaderboard(leaderboard)


def sort_leaderboard(leaderboard: list) -> list:
    return sorted(leaderboard, key=lambda x: (-x["score"], x["time"]))


def clear_leadeboard():
    save_leaderboard([])
