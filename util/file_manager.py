import pandas as pd
from products import *


class CSVFileManager:
  def __init__(self,path: str):
    self.path = path
  def read(self) -> str:
    return pd.read_csv(self.path)  
  def write(product_list):
    with open('llista_info.txt','w') as f: 
      f.write("List of", str(product_list))
      f.write("\n")
      for z in product_list:
        f.write(Product.describe(z))
        f.write("\n")


pass

