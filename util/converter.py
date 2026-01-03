from abc import ABC, abstractmethod
from file_manager import *
import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/lib")

import user


#Write your code here


class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass 
  def print(self, objects):
    for item in objects:
      print(item.describe(self, list))

class CashierConverter(Converter): 
  def convert(self,dataFrame):    
    

    #Write your code here
    pass

class CustomerConverter(Converter):
  #Write your code here
  pass

class ProductConverter(Converter):
  #Write your code here
  pass


