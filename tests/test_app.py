import sys
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, mult, div, log, square, sin, cos, sqrt, percent


def test_add():
    assert add(5, 6) == 11
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 6) == -1
    assert sub(6, 5) == 0

def test_mult():
    assert mult(5, 6) == 30
    assert mult(0, 99999999999) == 0
    assert mult(-1, 5) == -5

def test_div_normal():
    assert div(6, 2) == 3
    assert div(-1, 1) == -1
    assert div(5, 0) == "error: cannot divide by 0"


def test_log_natural():
    assert log(0) == "error: a must be > 0"
    assert log(-10) == "error: a must be > 0"
    assert log(10, 1) == "error: base must be > 1"
    assert log(10, 0) == "error: base must be > 1"
    assert log(10, -9) == "error: base must be > 1"
    assert round(log(8, 2), 5) == 3


def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0

def test_sin():
    assert round(sin(0), 5) == 0
    assert round(sin(math.pi / 2), 5) == 1
    assert round(sin(-math.pi / 2), 5) == -1

def test_cos():
    assert round(cos(0), 5) == 1
    assert round(cos(math.pi / 2), 5) == 0
    assert round(cos(math.pi), 5) == -1

def test_sqrt_valid_and_boundary():
    assert sqrt(0) == 0
    assert sqrt(9) == 3
    assert sqrt(-9) == "error: value must be > 0"


def test_percent():
    assert percent(200, 10) == 20
    assert percent(50, 0) == 0          
    assert percent(80, -25) == -20      