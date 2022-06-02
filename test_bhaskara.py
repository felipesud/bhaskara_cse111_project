from bhaskara import get_delta, get_first_x, get_second_x
from pytest import approx
import pytest

   

def test_get_delta():
    #Verify that Delta's calculate works
    assert get_delta(2,5,6) == -23
    assert get_delta(4,3,-7) == 121
    assert get_delta(8,12,0) == 144

def test_get_first_x():
    assert get_first_x(2, 5, 23) == -0.05104211917182022
    assert get_first_x(-5, 3, 7) == 0.03542486889354093
    assert get_first_x(8, -4, 5) == 0.38975424859373686

def test_get_second_x():
    assert get_second_x(8, -4, 5) == 0.11024575140626314
    assert get_second_x(-5, 6, 8) == 0.882842712474619
    assert get_second_x(12, 6, 3) == -0.3221687836487032




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])