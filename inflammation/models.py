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

def daily_stdev(data):
    """Calculates the standard deviation of axis 0 of an input
    data array.
    Parameters
    ----------
    data: numpy array
        input array that want std dev taken over
 
    Returns
    -------
    not assigned to variable: numpy array
        std dev over axis 0
    """
    return np.std(data, axis=0)

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
    if not isinstance(data,np.ndarray):
        raise TypeError("Inflammation input should be an ndarray")
    print(np.shape(data))
    if len(np.shape(data))!=2:
        raise TypeError("Inflammation input should two-dimensional")

    max_value = np.nanmax(data,axis=1)
    with np.errstate(invalid="ignore",divide="ignore"):
        normalised = data/max_value[:,np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised<0] = 0
    return normalised

from functools import reduce
def daily_above_threshold(data,rownum,threshold):
    """determine whether values for each day in a given row of data exceed
    the provided threshold.
    Parameters
    ----------
    data: 2D array
    rownum : integer
        indicating which row of data (corresponding to patient) want to 
        evaluate
    threshold : float
        reference value that want to evaluate daily values against

    Returns
    -------
    result : list of booleans
    """
    result = map(lambda x: x>threshold,data[rownum])
    count = reduce(lambda x,y: x+1 if y else x,list(result),0) 
    return list(result)

import sys
def attach_names(data,names):
    '''attach_names takes an input 2D dataset and creates a 1D list of 
    dictionaries with name and corresponding row of data based on input
    order
    Parameters
    ----------
    data: np.array
        input data with same number of rows as length of names and multiple
        columns  
    names: 1D list
        list of names associated w/ rows of data

    Returns
    -------
    labelled_data: list of dictionaries
        list of dictionaries including a name field and multiple values
        labelled as data per dictionary
    '''
    numPeople = len(names)
    if np.shape(data)[0]!=numPeople:
        sys.exit("number of names does not match number of rows of data")

    labelled_data = []
    for val in range(numPeople):
        out_dict = {'name':names[val],'data':data[val]}
        labelled_data.append(out_dict)
    return labelled_data

