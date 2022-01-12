from pydantic import BaseModel


class Package(BaseModel):
    command: str
    id: str = ""
    message: str = ""


class Storage(dict):
    def __init__(self):
        super().__init__()
        self._keys = []

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._keys.append(key)

    def __delitem__(self, key):
        super().__delitem__(key)
        self._keys.remove(key)

    def pop(self, key):
        self._keys.remove(key)
        return super().pop(key)

    def values(self):
        for key in self._keys:
            yield self.__getitem__(key)
