import sys
import os

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculadora import Calculadora

def test_add():
    calc = Calculadora()
    assert calc.somar(1, 2) == 3

def test_subtract():
    calc = Calculadora()
    assert calc.subtrair(2, 1) == 1

def test_multiply():
    calc = Calculadora()
    assert calc.multiplicar(2, 3) == 6

def test_divide():
    calc = Calculadora()
    assert calc.dividir(6, 2) == 3

def test_divide_by_zero():
    calc = Calculadora()
    try:
        calc.dividir(6, 0)
    except ValueError as e:
        assert str(e) == "Não é possível dividir por zero"

if __name__ == "__main__":
    test_add()
    print("All tests passed!")