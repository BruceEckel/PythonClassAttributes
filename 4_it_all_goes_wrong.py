# 4_it_all_goes_wrong.py

class A:
    x: int = 100
    y: int = 200

class B:
    a: A = A()

def oops():  A.x = 999999
def reset(): A.x = 100

if __name__ == '__main__':
    a = A()
    print(f"{a.x = }, {a.y = }")
    # a.x = 100, a.y = 200
    a.x = -1
    a.y = -2
    print(f"{a.x = }, {a.y = }")
    # a.x = -1, a.y = -2
    print(f"{A.x = }, {A.y = }")
    # A.x = 100, A.y = 200
    a2 = A()
    print(f"{a2.x = }, {a2.y = }")
    # a2.x = 100, a2.y = 200
    oops()
    print(f"{a.x = }, {a.y = }")
    # a.x = -1, a.y = -2
    print(f"{a2.x = }, {a2.y = }")
    # a2.x = 999999, a2.y = 200
    a3 = A()
    print(f"{a3.x = }, {a3.y = }")
    # a3.x = 999999, a3.y = 200
    reset()
    print(f"{a.x = }, {a.y = }")
    # a.x = -1, a.y = -2
    print(f"{a2.x = }, {a2.y = }")
    # a2.x = 100, a2.y = 200
    a3 = A()
    print(f"{a3.x = }, {a3.y = }")
    # a3.x = 100, a3.y = 200

    b = B()
    b.a.y = 22
    print(f"{b.a.x = }, {b.a.y = }")
    # b.a.x = 100, b.a.y = 22
    oops()
    print(f"{b.a.x = }, {b.a.y = }")
    # b.a.x = 999999, b.a.y = 22
