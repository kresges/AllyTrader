'''
All info types must inherit from this abstract base class. 
This enforces a common interface!
'''

from abc import ABC, abstractmethod

class InfoInterface(ABC):
    def __str__(self):
        rep = ""
        for key, val in self.__dict__.items():
            rep += "\t{} : {}\n".format(key, val)
        return rep

    def __repr__(self):
        rep = ""
        for key, val in self.__dict__.items():
            rep += "\t{} : {}\n".format(key, val)
        return rep

    @abstractmethod
    def get_type(self):
        pass