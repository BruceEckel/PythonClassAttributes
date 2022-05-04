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

class ScaleReading:
    units = "a"
    stable = "b"
    weight = "c"
    def __init__(self, m, n):
        self.m = m
        self.n = n
    def __str__(self):
        return "[class] " + showDict(self.__class__.__dict__) + "\n" +\
            "[object] " + showDict(self.__dict__)
    def show(self):
        print(f"{self.units=}, {self.stable=}, {self.weight=}")

if __name__ == '__main__':
    a = A()
    print(f"{a.x=} {a.y=} {a.z=}")
    show_object(A, a, "a")
