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
    x = 100
    y = 200
    z = 300

if __name__ == '__main__':
    a = A()
    show_object(A, a, "a")
    # [Class A] x: 100, y: 200, z: 300
    # [Object a] Empty
    a.x = -1
    a.y = -2
    a.z = -3
    show_object(A, a, "a")
    # [Class A] x: 100, y: 200, z: 300
    # [Object a] x: -1, y: -2, z: -3