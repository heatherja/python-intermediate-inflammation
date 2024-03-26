"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.classes import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name
    return p

def test_create_doctor():
    from inflammation.classes import Doctor 

    name = 'Felix'
    d = Doctor(name=name)
    assert d.name==name
    return d

def test_add_observation(p):
    from inflammation.classes import Observation,Patient 

    day = 3
    value = 4.7
    p.add_observation(value,day)
    print(p)
    assert p.observations[-1].day==day
    assert p.observations[-1].value==value

def test_add_patient(d):
    from inflammation.classes import Patient,Doctor 
    pname = "Alice"
    d.add_patient(pname)
    print(d)
    assert d.patients[-1].name ==pname
    
