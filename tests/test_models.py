import pytest
"""Tests for statistics functions within the Model layer."""

import os
import numpy as np
import numpy.testing as npt
import pytest

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

@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
         ([[1,1,1],[1,1,1],[1,np.nan,2]],[[1,1,1],[1,1,1],[0.5,0,1]],None),
         ([[1,1,1],[0.0000001,10,2],[1,1,1]],[[1,1,1],[0,1,0.2],[1,1,1]],None),
         ([[99999999,1,4],[1,1,1],[1,1,1]], [[1,0,0],[1,1,1],[1,1,1]],None),
         ([[0,0,0], [0,0,0], [0,0,0]], [[0,0,0],[0,0,0],[0,0,0]],None),
         ([0,0,0], [0,0,0],TypeError),
         ([[-1,1,1], [1,1,1], [1,1,1]], [[-1,1,1], [0,1,1], [1,1,1]], ValueError),
         ([[1,2,3], [4,5,6], [7,8,9]], [[0.33,0.67,1],[0.67,0.83,1],[0.78,0.89,1]],None),
         ("hello you!",0,TypeError)
    ])
def test_patient_normalise(test,expected,expect_raises):
    """test normalisation works for arrays of one and positive integers.
    assumption that test accuracy of two decimal places is sufficient. """
    from inflammation.models import patient_normalise
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            npt.assert_almost_equal(patient_normalise(np.array(test)),np.array(expected),decimal=2)
    else:
        npt.assert_almost_equal(patient_normalise(np.array(test)),np.array(expected),decimal=2)

@pytest.mark.parametrize('data, expected_standard_deviation', [
    ([0, 0, 0], 0.0),
    ([1.0, 1.0, 1.0], 0),
    ([0.0, 2.0], 1.0)
])
def test_daily_standard_deviation(data, expected_standard_deviation):
    result_data = np.std(data)
    npt.assert_approx_equal(result_data, expected_standard_deviation)
