class A:
    x = 100
    y = 200
    z = 300

class B:
    a = A()

def oops(): A.x = 999999

if __name__ == '__main__':
    a = A()
    print(f"{a.x = }, {a.y = }, {a.z = }")
    # a.x = 100, a.y = 200, a.z = 300
    a.x = -1
    a.y = -2
    a.z = -3
    print(f"{a.x = }, {a.y = }, {a.z = }")
    # a.x = -1, a.y = -2, a.z = -3
    b = B()
    b.a.y = 22
    b.a.z = 33
    print(f"{b.a.x = }, {b.a.y = }, {b.a.z = }")
    # b.a.x = 100, b.a.y = 22, b.a.z = 33
    oops() # Has no reference to object 'b'
    print(f"{b.a.x = }, {b.a.y = }, {b.a.z = }")
    # b.a.x = 999999, b.a.y = 22, b.a.z = 33
    print(f"{a.x = }, {a.y = }, {a.z = }")
    # a.x = -1, a.y = -2, a.z = -3
