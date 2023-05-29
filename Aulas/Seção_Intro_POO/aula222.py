# Herança Simples
class A:
    def __init__(self) -> None:
        pass

    def method(self):
        print('A')

class B(A):
    def method(self):
        print('B')

class C(B):
    def method(self):
        super(B, self).method()
        B.method(self)
        print('C')

c = C()
c.method()