# 6_do_instead.py
from look_inside import show
from dataclasses import dataclass

class A:
    def __init__(self, x: int = 100, y: int = 200, z: int = 300):
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
    show(A, a, "a")
    # [Class A] Empty
    # [Object a] x: 100, y: 200, z: 300
    a.x = -1
    a.y = -2
    a.z = -3
    show(A, a, "a")
    # [Class A] Empty
    # [Object a] x: -1, y: -2, z: -3

    aa = AA()
    print(aa)
    # AA(x=100, y=200, z=300)
    show(AA, aa, "aa")
    # [Class AA] x: 100, y: 200, z: 300
    # [Object aa] x: 100, y: 200, z: 300
    aa.x = -1
    aa.y = -2
    aa.z = -3
    show(AA, aa, "aa")
    # [Class AA] x: 100, y: 200, z: 300
    # [Object aa] x: -1, y: -2, z: -3
    aa2 = AA(-1, -2, -3)
    show(AA, aa2, "aa2")
    # [Class AA] x: 100, y: 200, z: 300
    # [Object aa2] x: -1, y: -2, z: -3

    # Even if we modify the class attributes, the
    # constructor default arguments stay the same:
    AA.x = 42
    AA.y = 74
    AA.z = 22
    aa3 = AA()
    show(AA, aa3, "aa3")
    # [Class AA] x: 42, y: 74, z: 22
    # [Object aa3] x: 100, y: 200, z: 300