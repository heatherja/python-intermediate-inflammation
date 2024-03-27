class Book:
    '''a class describing the properties of a book'''
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return self.title+" by "+self.author

class Observation:
    def __init__(self,day,value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

class Person:
    def __init__(self,name):
        self.name = name
 
    def __str__(self):
        return self.name

class Patient(Person):
    def __init__(self,name,observations=None):
        super().__init__(name)
        self.observations = []

        if observations is not None:
          self.observations = observations
 
    def add_observation(self,value,day=None):
        if day is None:
            try:
                day = self.observations[-1].day+1
            except IndexError:
                day = 0
        new_observation = Observation(day,value)
        self.observations.append(new_observation)
        return new_observation

class Doctor(Person):
    ''' a class defining attributes of a doctor - a name and patients'''
    def __init__(self,name):
        super().__init__(name) 
        self.patients = []

    def add_patient(self,pname):
        new_patient = Patient(pname)
        self.patients.append(new_patient)
        return new_patient
