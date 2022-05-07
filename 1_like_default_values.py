# 1_like_default_values.py

class A:
    x: int = 100

if __name__ == '__main__':
    a = A()
    print(f"{a.x = }")
    # a.x = 100
    a.x = -1
    print(f"{a.x = }")
    # a.x = -1
    a2 = A()
    print(f"{a2.x = }")
