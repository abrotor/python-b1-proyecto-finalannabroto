import pandas as pd
from data import *

class CSVFileManager:
  def __init__(self,path: str):
    self.path = path
  def read(self) -> str:
    return pd.read_csv(self.path)  
  def write(self,dataFrame):
    self.dataFrame = dataFrame

    pass

