

class Pkg:
    def __init__(self):
        ...

    def __or__(self, other):
        ...

    def __and__(self, other):
        ...

    def __enter__(self):
        ...

    def __eq__(self, other):
        ...

    def __str__(self):
        ...

    def __repr__(self):
        ...

    class Packages:
        def __init__(self, *package: str) -> None:
            self.packages: tuple = package

        def __iter__(self):
            ...

        def __next__(self):
            ...

