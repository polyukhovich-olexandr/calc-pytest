from calc import *


def test_add():
    assert add(2, 3) == 5
    assert add(-1, -5) == -6
    assert add(5, 5) == 10
    assert add(2, 5) == 7
    assert add(3, 3) == 6
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(3, 3) == 0
    assert subtract(-1, -5) == 4
    assert subtract(-1, -1) == 0
    assert subtract(-1, 1) == -2
    assert subtract(25, 7) == 18


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, -3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(2, -3) == -6
    assert multiply(7, 7) == 49
    assert multiply(7, 0) == 0


def test_divide():
    assert divide(5, 5) == 1
    assert divide(25, 5) == 5
    assert divide(5, -1) == -5
    assert divide(625, 5) == 125
    assert divide(-1, -1) == 1
    assert divide(2, -2) == -1


def test_int_division():
    assert int_division(5, 3) == 1
    assert int_division(629, 5) == 125
    assert int_division(9, 3) == 3
    assert int_division(2, 2) == 1
    assert int_division(629, 125) == 5
    assert int_division(53, 7) == 7


def test_mod():
    assert mod(5, 3) == 2
    assert mod(629, 5) == 4
    assert mod(99, 9) == 0
    assert mod(25, 4) == 1
    assert mod(7, 3) == 1
    assert mod(52, 50) == 2
