# Importar mòdul abc.
from abc import ABC, abstractmethod
# Importar la llibreria panda.
import pandas as pd
# Importa informació dels paquets users i products.
from users import *
from products import *


# Crear classe abstracta Converter amb mètodes abstractes convert i print.
class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass 
  def print(self, objects):
    for item in objects:
      print(item.describe(self, list))

# Crear classes CashierConverter, CustomerConverter i ProductConverter amb mètodes convert i print.
class CashierConverter(Converter): 
  # La funció convert converteix el dataFrame Cashier en una llista.
  def convert(dataFrame, numberofcashiers): 
    # 1. Crear llista buida caixer.   
    cashier_list = [] 
    # 2. Iniciar índex a 0.
    x = 0
    # 3. Per cada índex del dataFrame dels caixers afegir la informació del caixer a la llista de caixers prèviament creada.
    for x in range (0, numberofcashiers):
        cashier_list.append(Cashier(name= dataFrame.at[x, 'name'], dni = dataFrame.at[x, 'dni'], age = dataFrame.at[x, 'age'], timeTable = dataFrame.at[x, 'timetable'], salary = dataFrame.at[x, 'salary']))
        # Sumar 1 al valor del índex.
        x = x + 1 
    # 4. Retornar llista caixers.        
    return cashier_list
  # La funció print imprimeix la informació de la llista utilitzant la funció describe prèviament definida.
  def print(cashier_list):
    for z in cashier_list:
        print(Cashier.describe(z))
    pass

class CustomerConverter(Converter):
  # La classe CustomerConverter és anàloga a la de CashierConverter.
  def convert(dataFrame, numberofcustomers):    
    customer_list = [] 
    x = 0
    for x in range (0, numberofcustomers):
        customer_list.append(Customer(name = dataFrame.at[x, 'name'], dni = dataFrame.at[x, 'dni'], age = dataFrame.at[x, 'age'], email = dataFrame.at[x, 'email'], postalCode = dataFrame.at[x, 'postalcode']))
        x = x + 1         
    return customer_list
  def print(customer_list):
    for z in customer_list:
        print(Customer.describe(z))
    pass


class ProductConverter(Converter):
  # La classe CustomerConverter és anàloga a la de CashierConverter. S'ha afegit la variable d'entrada product que indica quin és el tipus de cada producte.
  def convert(dataFrame, numberofproducts, product):    
    product_list = [] 
    x = 0
    for x in range (0, numberofproducts):
        product_list.append(product(id = dataFrame.at[x, 'id'], name = dataFrame.at[x, 'name'], price = dataFrame.at[x, 'price']))
        x = x + 1         
    return product_list
  def print(product_list):
    for z in product_list:
        print(Product.describe(z))




