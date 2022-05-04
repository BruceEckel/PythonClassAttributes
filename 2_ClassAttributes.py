def showDict(d):
    v = vars(d)
    return " ".join([f"{k}: {v} " for k, v in v.items() if not k.startswith("__") and k != "show"])


def show_object(klass: type, obj: object, obj_name: str):
    print(f"Class {klass.__name__}: {showDict(klass)}")
    print(f"Object {obj_name}: {showDict(obj)}")


class A:
    x = 100
    y = 200
    z = 300


if __name__ == '__main__':
    a = A()
    print(f"{a.x=} {a.y=} {a.z=}")
    show_object(A, a, "a")
    a.x = "zip"
    a.y = "zop"
    a.z = "zoom"
    print(f"{a.x=} {a.y=} {a.z=}")
    show_object(A, a, "a")
