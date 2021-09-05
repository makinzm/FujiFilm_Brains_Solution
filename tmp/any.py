from typing import Any

a = None    # type: Any
a = []      # OK
a = 2       # OK

s = ''      # type: str
##s = a       # OK

def foo(item: Any) -> int:
    ora: JoJo
    # Typechecks; 'item' could be any type,
    # and that type might have a 'bar' method
    return len(item)
print(foo(s))