from src.main import add,substract

def test_cases_addition():
    assert add(2,3)==5
    assert add(3,4)==7
    assert add(0,0)==0

def test_cases_substraction():
    assert substract(2,3)==-1
    assert substract(6,4)==2
    assert substract(0,0)==0