from _play import *

m = MarkerMethods(**base_fields)
# h = HandleInput()
# m.f(dict(some_other_stuff=100, signer_pkey='hello', validator='', voteNum=0))


def f():
    ...


def g():
    ...


m = {f: "hello from F", g: "Hello from G"}

print(m[f])


class A:

    x = 1

    def f(self):
        d = {"x": 3}
        for k, v in d.items():
            self.__dict__[k] = 4
        print(self.x)


A().f()


c = "systemctl enable atlasNode.service && service atlasNode start"

print(c.split())