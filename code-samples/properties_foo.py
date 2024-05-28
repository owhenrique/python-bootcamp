class Foo:
    def __init__(self, valor=None):
        self._x = valor
    
    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, valor):
        _x  = self._x or 0
        _valor = valor or 0
        self._x = _x + _valor

    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)
foo.x = 1
print(foo.x)