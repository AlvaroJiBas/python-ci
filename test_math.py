from mathe import add
from mathe import minus

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(10,20) == 30
def test_minus():
    assert minus(5,6) == -1
    assert minus(0,0) == 0
    assert minus(7,5) == 2


