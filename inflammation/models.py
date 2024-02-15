"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):  
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculates the mean of axis 0 of an input data array.
    Parameters
    ----------
    data: numpy array
        input array that want mean taken over
 
    Returns
    -------
    not assigned to variable: numpy array
        mean over axis 0
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculates the max of axis 0 of an input data array.
    Parameters
    ----------
    data: numpy array
        input array that want max taken over
 
    Returns
    -------
    not assigned to variable: numpy array
        max over axis 0
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculates the min of axis 0 of an input data array.
    Parameters
    ----------
    data: numpy array
        input array that want max taken over
 
    Returns
    -------
    not assigned to variable: numpy array
        min over axis 0
    """
    return np.min(data, axis=0)

def patient_normalise(data):
    """Normalise patient data from 2D inflammation data array.
    NaN values are ignored and normalised to 0.
    Negative values are rounded to 0."""
    if np.any(data<0):
        raise ValueError("Inflammation values should not be negative")
    if not isinstance(data,ndarray):
        raise TypeError("Inflammation input should be an ndarray")
        

    max = np.nanmax(data,axis=1)
    with np.errstate(invalid="ignore",divide="ignore"):
        normalised = data/max[:,np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised<0] = 0
    return normalised
