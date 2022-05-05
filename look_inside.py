# look_inside.py

def attributes(d):
    return ", ".join(
        [f"{k}: {v}" for k, v in vars(d).items()
         if not k.startswith("__")]) or "Empty"

def show_object(klass: type, obj: object, obj_name: str):
    print(f"[Class {klass.__name__}] {attributes(klass)}")
    print(f"[Object {obj_name}] {attributes(obj)}\n")