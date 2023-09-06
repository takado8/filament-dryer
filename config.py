import ujson

CONFIG_FILE_PATH = "config.json"


def load_config():
    try:
        with open(CONFIG_FILE_PATH, "r") as file:
            config = ujson.load(file)
            api_key = config.get("api_key", "")
            ssid = config.get("ssid", "")
            password = config.get("password", "")
            return api_key, ssid, password
    except Exception as e:
        print("Error loading config:", str(e))
        return "", "", ""
