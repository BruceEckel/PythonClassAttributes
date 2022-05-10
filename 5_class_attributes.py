# 5_class_attributes.py
from look_inside import show

class A:
    x: int = 100

class B:
    x: int = 100
    def __init__(self, x_init: int):
        # Shadows the class attribute name:
        self.x = x_init

if __name__ == '__main__':
    a = A()
    show(a, "a")
    # [Class A] x: 100
    # [Object a] Empty
    a.x = 1
    show(a, "a")
    # [Class A] x: 100
    # [Object a] x: 1

    b = B(-99)
    show(b, "b")
    # [Class B] x: 100
    # [Object b] x: -99

