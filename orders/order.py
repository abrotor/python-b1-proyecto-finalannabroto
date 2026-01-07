# Importar llibreria panda.
import pandas as pd
# Importar informació dels paquets users, products i util.
from users import *
from products import *
from util import *

# Crear classe Order amb diferents funcions per crear comandes.

class Order:

  def __init__(self, cashier:Cashier, customer:Customer, df_productes_afegits, llista_afegits):
    self.cashier = cashier
    self.customer = customer
    self.df_productes_afegits = df_productes_afegits
    self.df_productes_afegits = []
    self.llista_afegits = llista_afegits

# La funció add afegeix un nou producte al dataFrame format pels productes ja afegits i retorna un nou dataFrame amb el nou producte afegit.
  def add(df_productes_afegits, df_producte_nou) -> float:
    df_productes_afegits = pd.concat([df_productes_afegits, df_producte_nou])
    return df_productes_afegits   
    pass

  # La funció calcilateTotal calcula el preu de la comanda.
  def calculateTotal(df_productes_afegits):
    # 1. Fa una llista amb els preus de tots els productes afegits.
    price = df_productes_afegits['price'].tolist()
    # 2. Summa cada preu a la variable preu_total.
    preu_total = 0
    for x in price:
      preu_total = preu_total + x
    return preu_total
    pass

  # La funció show mostra un resum de la informació de la comanda.
  def show(cashier, customer, df_productes_afegits, llista_afegits):
    # 1. Utilitzant la funció converter imprimeix la informació del client, el caixer i els productes de la comanda.  
    print("Hello") 
    CustomerConverter.print(customer)

    print("Was attended by : ")
    CashierConverter.print(cashier)

    print("List of products : ")
    ProductConverter.print(llista_afegits)

    # 2. Utilitzant la funció calculateTotal imprimeix el preu total de la comanda.
    print(f"Total price : {Order.calculateTotal(df_productes_afegits)}")











class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass 
  def print(self, objects):
    for item in objects:
      print(item.describe(self, list))

class CashierConverter(Converter): 
  def convert(dataFrame, numberofcashiers):    
    cashier_list = [] 
    x = 0
    for x in range (0, numberofcashiers):
        cashier_list.append(Cashier(name= dataFrame.at[x, 'name'], dni = dataFrame.at[x, 'dni'], age = dataFrame.at[x, 'age'], timeTable = dataFrame.at[x, 'timetable'], salary = dataFrame.at[x, 'salary']))
        x = x + 1         
    return cashier_list
  def print(cashier_list):
    for z in cashier_list:
        print(Cashier.describe(z))
    pass

class CustomerConverter(Converter):
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