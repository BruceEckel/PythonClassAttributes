# 5_class_attributes.py
from look_inside import show

class A:
    x: int = 100
    y: int = 200
    z: int = 300

class B:
    x: int = 100
    def __init__(self, x_init: int):
        # You CAN shadow a class attribute name:
        self.x = x_init

if __name__ == '__main__':
    a = A()
    show(A, a, "a")
    # [Class A] x: 100, y: 200, z: 300
    # [Object a] Empty
    a.x = -1
    a.y = -2
    a.z = -3
    show(A, a, "a")
    # [Class A] x: 100, y: 200, z: 300
    # [Object a] x: -1, y: -2, z: -3

    b = B(-1)
    show(B, b, "b")
    # [Class B] x: 100
    # [Object b] x: -1

"""
Just like Java and C++,
If an object attribute doesn't exist, Python looks for a class
attribute of the same name.
Unlike Java and C++, Python allows you to shadow the class attribute
name with an identical object attribute name.
"""