class Foo:
    def __init__(self, x=None):
        self._x = x
    
    """Acessando o atributo"""
    @property   
    def x(self):
        return self._x or 0
    
foo = Foo(10)
print(foo.x)   