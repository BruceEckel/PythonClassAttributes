def attributes(d):
    return ", ".join([f"{k}: {v}" for k, v in vars(d).items() if not k.startswith("__")]) or "Empty"


def show_object(klass: type, obj: object, obj_name: str):
    print(f"[Class {klass.__name__}] {attributes(klass)}")
    print(f"[Object {obj_name}] {attributes(obj)}\n")


class A:
    x = 100
    y = 200
    z = 300


if __name__ == '__main__':
    a = A()
    show_object(A, a, "a")
    a.x = -1
    a.y = -2
    a.z = -3
    show_object(A, a, "a")
