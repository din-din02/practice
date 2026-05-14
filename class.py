from enum import Enum
from abc import ABC
import pandas as pd
class Weekday(Enum):
    MONDAY=1
    TUESDAY=2
    SUNDAY=7

class Face(Enum):
    FIZ='физ.лицо'
    YOUR='юр.лицо'

class Operathion:
    def __init__(self, week_day:Weekday):
        self.week_day=week_day
    

class Abstract_Operathion_Validator(ABC): 
    @ABC.abstractmethod
    def validate(lst:list)-> Operathion:
        pass
    @ABC.abstractmethod
    def validate_operation_type():
        pass

def validate_csv(path:str, validator:Abstract_Operathion_Validator)->list[Operathion]:


