import requests
import json


def extract_offline(path_1, path_2):
    with open(path_1, "r") as file:
        top_250 = json.load(file)

    with open(path_2, "r") as file:
        top_250_details = json.load(file)
    return top_250, top_250_details


class Expired(Exception):
    pass


class ConnectionError(Exception):
    pass


def extract(path_1, path_2):
    try:
        url = "https://imdb236.p.rapidapi.com/imdb/top250-movies"

        headers = {
            "x-rapidapi-key": "444fd57ac6msh6712acfe9750aa2p187eaajsn55068261c767",
            "x-rapidapi-host": "imdb236.p.rapidapi.com",
        }

        response = requests.get(url, headers=headers)
    except Exception:
        print(
            ConnectionError(
                "Review your code or Check your internet connection \n\nSwitching to Extract_offline\n\n"
            )
        )
        return False
    if "message" in response.json():
        print(Expired("API key has expired \n\nSwitching to Extract_offline\n\n"))
        return False

    with open(path_1, "w") as file:
        json.dump(response.json(), file, indent=4)

    with open(path_1, "r") as file:
        top_250 = json.load(file)

    id_list = [each_movie["id"] for each_movie in top_250]
    new_json = []

    for each_id in id_list:
        try:
            url = f"https://imdb236.p.rapidapi.com/imdb/{each_id}"
            headers = {
                "x-rapidapi-key": "980f9d0edamsh3e0dedd6ca5e0c8p1e68a2jsna81200c7c416",
                "x-rapidapi-host": "imdb236.p.rapidapi.com",
            }
            response = requests.get(url, headers=headers)
        except Exception:
            print(
                ConnectionError(
                    "Review your code or Check your internet connection \n\nSwitching to Extract_offline\n\n"
                )
            )
            return False
        if "message" in response.json():
            print(
                Expired(
                    "API key has expired in loop \n\nSwitching to Extract_offline\n\n"
                )
            )
            return False
        new_json.append(response.json())
        with open(path_2, "a") as f:
            json.dump(new_json, f, indent=4)

    with open(path_2, "r") as file:
        top_250_details = json.load(file)
    return top_250, top_250_details
