import pytest


@pytest.mark.parametrize("point1, point2, input_x, expected", [[(5,5),(10,10), 15, 15],[(10,5),(5, 15), 8, 9]])
def test_linear_function(point1, point2, input_x, expected): 
    import linear_function
    answer = linear_function.linear_function(point1, point2, input_x)
    assert answer == expected
    