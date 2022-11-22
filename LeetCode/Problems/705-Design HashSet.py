class MyHashSet:

    def __init__(self):
        self.keys=[]

    def add(self, key: int) -> None:
        if key not in self.keys:
            self.keys.append(key)

    def remove(self, key: int) -> None:
        if key in self.keys:
            self.keys.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.keys