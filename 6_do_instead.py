from look_inside import show
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
    show(A, a, "a")
    a.x = -1
    a.y = -2
    a.z = -3
    show(A, a, "a")

    aa = AA()
    print(aa)
    show(AA, aa, "aa")
    aa.x = -1
    aa.y = -2
    aa.z = -3
    show(AA, aa, "aa")
    aa = AA(-1, -2, -3)
    show(AA, aa, "aa")

"""
# [Class A] Empty
# [Object a] x: 100, y: 200, z: 300
# 
# [Class A] Empty
# [Object a] x: -1, y: -2, z: -3
# 
# AA(x=100, y=200, z=300)
# [Class AA] x: 100, y: 200, z: 300
# [Object aa] x: 100, y: 200, z: 300
# 
# [Class AA] x: 100, y: 200, z: 300
# [Object aa] x: -1, y: -2, z: -3
# 
# [Class AA] x: 100, y: 200, z: 300
# [Object aa] x: -1, y: -2, z: -3
"""