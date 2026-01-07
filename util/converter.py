#Importar modul abc.
from abc import ABC, abstractmethod
#Importar llibreria panda.
import pandas as pd
#Importa informació dels paquets users i products.
from users import *
from products import *


#Craear classe abstracta converter amb metodes abstractes convert i print.
class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass 
  def print(self, objects):
    for item in objects:
      print(item.describe(self, list))

#Crear classes CashierConverter, CustomerConverter i ProductConverter amb metodes convert i print.
class CashierConverter(Converter): 
  #La funcio convert converteix el dataFrame en una llista.
  def convert(dataFrame, numberofcashiers): 
    # 1. Crear llista buida caixer.   
    cashier_list = [] 
    # 2. Iniciar index a 0.
    x = 0
    # 3. Per cada index del dataFrame dels caixers afegir la informacio del caixer a la llista de caixers previament creada.
    for x in range (0, numberofcashiers):
        cashier_list.append(Cashier(name= dataFrame.at[x, 'name'], dni = dataFrame.at[x, 'dni'], age = dataFrame.at[x, 'age'], timeTable = dataFrame.at[x, 'timetable'], salary = dataFrame.at[x, 'salary']))
        # Sumar 1 al valor del index
        x = x + 1 
    # 4.Retornar llista caixers.        
    return cashier_list
  # La funció print imprimeix la info de la llista utilitzant la funcio describe previament definida.
  def print(cashier_list):
    for z in cashier_list:
        print(Cashier.describe(z))
    pass

class CustomerConverter(Converter):
  # La classe CustomerConverter es analoga a la de CashierConverter.
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
  # La classe CustomerConverter es analoga a la de CashierConverter.
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




