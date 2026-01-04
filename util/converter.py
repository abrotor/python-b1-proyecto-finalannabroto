from abc import ABC, abstractmethod
import pandas as pd
from users import *


#Write your code here


class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass 
  def print(self, objects):
    for item in objects:
      print(item.describe(self, list))

class CashierConverter(Converter): 
  def convert(dataFrame):    
    cashier_list = [] 
    x = 0
    for x in range (0, 5):
        cashier_list.append(Cashier(name= dataFrame.at[x, 'name'], dni = dataFrame.at[x, 'dni'], age = dataFrame.at[x, 'age'], timeTable = dataFrame.at[x, 'timetable'], salary = dataFrame.at[x, 'salary']))
        x = x + 1         
    return cashier_list
  def print(cashier_list):
    for z in cashier_list:
        print(Cashier.describe(z))
    pass

class CustomerConverter(Converter):
  #Write your code here
  pass

class ProductConverter(Converter):
  #Write your code here
  pass


