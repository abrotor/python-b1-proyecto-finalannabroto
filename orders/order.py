from users import *
from products import *
from util import *

class Order:

  def __init__(self, cashier:Cashier, customer:Customer, df_productes_afegits, llista_afegits):
    self.cashier = cashier
    self.customer = customer
    self.df_productes_afegits = df_productes_afegits
    self.df_productes_afegits = []
    self.llista_afegits = llista_afegits

  def add(df_productes_afegits, df_producte_nou) -> float:
    df_productes_afegits = pd.concat([df_productes_afegits, df_producte_nou])
    return df_productes_afegits   
    pass

  def calculateTotal(df_productes_afegits):
    price = df_productes_afegits['price'].tolist()
    preu_total = 0
    for x in price:
      preu_total = preu_total + x
    return preu_total
    pass

  def show(cashier, customer, df_productes_afegits, llista_afegits):    
    print("Hello") 
    CustomerConverter.print(customer)

    print("Was attended by : ")
    CashierConverter.print(cashier)

    print("List of products : ")
    ProductConverter.print(llista_afegits)

    print(f"Total price : {Order.calculateTotal(df_productes_afegits)}")


