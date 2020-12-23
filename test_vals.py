import pytest
import app

def test_quadraticfive():
    latex, (x_1,x_2) = app.quadratic(1,-10,0)
    assert x_1 == 10.0