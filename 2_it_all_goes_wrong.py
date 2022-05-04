class A:
    x = 100
    y = 200
    z = 300


if __name__ == '__main__':
    a = A()
    print(f"{a.x = }, {a.y = }, {a.z = }")
    a.x = -1
    a.y = -2
    a.z = -3
    print(f"{a.x = }, {a.y = }, {a.z = }")
