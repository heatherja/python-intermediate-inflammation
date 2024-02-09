import pytest
"""Tests for statistics functions within the Model layer."""


import numpy as np
import numpy.testing as npt

@pytest.mark.parametrize(
    "test,expected",
    [
        ([ [0,0], [0,0], [0,0] ], [0,0]),
        ([ [1,2], [3,4], [5,6] ], [3,4]),
    ])
def test_daily_mean(test,expected):
    """Test that mean function works for an array of zeros and positive integers."""
    from inflammation.models import daily_mean

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test), expected)


@pytest.mark.parametrize(
    "test,expected",
    [
        ([ [0,0], [0,0], [0,0] ], [0,0]),
        ([ [1,2], [3,4], [5,6] ], [1,2]),
        ([ [1,2], [np.nan,4], [5,6] ], [np.nan,2]),
    ])
def test_daily_min_integers(test,expected):
    """Test that min function works for an array of zeros and positive 
    integers and nans."""
    from inflammation.models import daily_min
    
# Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test), expected)


@pytest.mark.parametrize(
    "test,expected",
    [
        ([ [0,0], [0,0], [0,0] ], [0,0]),
        ([ [1,2], [3,4], [5,6] ], [5,6]),
        ([ [1,2], [np.nan,4], [5,6] ], [np.nan,6]),
    ])
def test_daily_max_integers(test,expected):
    """Test that max function works for an array of zeros and positive 
    integers and nans."""
    from inflammation.models import daily_max

# Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test), expected)

def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello','there'],['General','Kenobi']])
