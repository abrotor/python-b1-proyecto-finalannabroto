import pandas as pd


class CSVFileManager:
  def __init__(self,path: str):
    self.path = path
  def read(self) -> str:
    dataFrame = pd.read_csv(self.path)  
    return dataFrame
  def write(self,dataFrame):
    self.dataFrame = dataFrame

    pass

