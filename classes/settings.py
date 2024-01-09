import json
from types import SimpleNamespace

class Settings():
    @classmethod
    def load(self, path: str = 'settings.json'):
        with open(path, "r", encoding="utf8") as file:
            data = json.load(file, object_hook=lambda d: SimpleNamespace(**d))
        return data