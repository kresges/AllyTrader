'''
All brokerage api must inherit from this abstract base class. 
This enforces a common interface!
'''

from abc import ABC, abstractmethod

class BrokerageInterface(ABC):
    @abstractmethod
    def get_user(self):
        pass
