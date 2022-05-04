class A:
    x = 100
    y = 200
    z = 300


if __name__ == '__main__':
    a = A()
    print(f"{a.x = }, {a.y = }, {a.z = }")
    a.x = "zip"
    a.y = "zop"
    a.z = "zap"
    print(f"{a.x = }, {a.y = }, {a.z = }")
