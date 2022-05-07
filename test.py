from pprint import pprint
from dataclasses import dataclass

@dataclass
class Frob:
    snork: bool
    snick: int
    snack: float

if __name__ == '__main__':
    f = Frob(True, 1, 3.14159)
    print("dir(f) = ")
    pprint(dir(f))
    print("vars(f) = ")
    pprint(vars(f))

    print("dir(Frob) = ")
    pprint(dir(Frob))
    print("vars(Frob) = ")
    pprint(vars(Frob))