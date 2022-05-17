# 6_like_default_values_shown.py
from look_inside import show

class A:
    x: int = 100

if __name__ == '__main__':
    a = A()
    show(a, "a")
    # [Class A] x: 100
    # [Object a] Empty
    print(f"{a.x = }")
    # a.x = 100
    a.x = -1
    show(a, "a")
    # [Class A] x: 100
    # [Object a] x: -1
    print(f"{a.x = }")
    # a.x = -1
    a2 = A()
    show(a2, "a2")
    # [Class A] x: 100
    # [Object a2] Empty
    print(f"{a2.x = }")
    # a2.x = 100
