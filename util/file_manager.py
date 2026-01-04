import pandas as pd


class CSVFileManager:
  def __init__(self,path: str):
    self.path = path
  def read(self) -> str:
    return pd.read_csv(self.path)  
  def write(dataFrame):
    with open('llista_info.txt','w') as f: 
      f.write('Hola, mundo!')


pass

