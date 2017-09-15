import pytest

def nameIsString(name):
    return type(name)

print nameIsString("Joern")
print nameIsString(1)