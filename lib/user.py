

class User:
    def __init__(self, name: str, home_dir: str, groups: list):
        self.name: str = name
        self.home_dir: str = home_dir
        self.groups: list = groups
        ...


