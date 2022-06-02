from bhaskara import get_delta, get_first_x, get_second_x
from pytest import approx
import pytest

   

def test_get_delta():
    #Verify that Delta's calculate works
    assert get_delta(2,5,6) == -23
    assert get_delta(4,3,-7) == 121
    assert get_delta(8,12,0) == 144

def test_get_first_x():
    assert get_first_x(2, 5, 23) == -0.2041684766872809
    assert get_first_x(-5, 3, 7) == 0.8856217223385232
    assert get_first_x(8, -4, 5) == 24.94427190999916

def test_get_second_x():
    assert get_second_x(8, -4, 5) == 7.055728090000841
    assert get_second_x(-5, 6, 8) == 22.071067811865476
    assert get_second_x(12, 6, 3) == -46.392304845413264




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])