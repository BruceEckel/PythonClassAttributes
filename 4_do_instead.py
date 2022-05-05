from look_inside import show_object
from dataclasses import dataclass

class A:
    def __init__(self, x = 100, y = 200, z = 300):
        self.x = x
        self.y = y
        self.z = z

# OR:

@dataclass
class AA:
    x: int = 100
    y: int = 200
    z: int = 300

if __name__ == '__main__':
    a = A()
    show_object(A, a, "a")
    a.x = -1
    a.y = -2
    a.z = -3
    show_object(A, a, "a")

    aa = AA()
    print(aa)
    show_object(AA, aa, "aa")
    aa = AA(-1, -2, -3)
    show_object(AA, aa, "aa")

"""

"""