class A:
    x = 100

if __name__ == '__main__':
    a = A()
    print(f"{a.x = }")
    # a.x = 100
    a.x = -1
    print(f"{a.x = }")
    # a.x = -1
