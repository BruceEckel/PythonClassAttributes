class Hello(Exception):
   def __init__(self, name):
       self._name = name
   def __str__(self):
       return 'error: %s!' % (self._name,)

async def hello(name):
    raise Hello(name)

if __name__ == '__main__':

    task = hello('world')
    print(task)
    # task.send(None)
    try:
        task.send(None)
    except Exception as error:
        # NEW: exception will be propagated here!
        print(error)
    # Hello, world!