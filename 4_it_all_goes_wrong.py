# 4_it_all_goes_wrong.py

class A:
    x: int = 100
    y: int = 200

def oops():
    A.x = 999999
    A.y = 313

def reset():
    A.x = 100
    A.y = 200

if __name__ == '__main__':
    a1: A = None
    a2: A = None
    a3: A = None
    def display():
        if a1:
            print(f"{a1.x = }, {a1.y = }")
        if a2:
            print(f"{a2.x = }, {a2.y = }")
        if a3:
            print(f"{a3.x = }, {a3.y = }")

    a1 = A()
    display()
    # a1.x = 100, a1.y = 200
    a1.x = -1
    a1.y = -2
    display()
    # a1.x = -1, a1.y = -2
    a2 = A()
    display()
    # a1.x = -1, a1.y = -2
    # a2.x = 100, a2.y = 200
    a2.y = 17
    display()
    # a1.x = -1, a1.y = -2
    # a2.x = 100, a2.y = 17
    oops()
    a3 = A()
    display()
    # a1.x = -1, a1.y = -2
    # a2.x = 999999, a2.y = 17
    # a3.x = 999999, a3.y = 313
    reset()
    display()
    # a1.x = -1, a1.y = -2
    # a2.x = 100, a2.y = 17
    # a3.x = 100, a3.y = 200
