import pandas as pd
from datetime import datetime
from products import *
from users import *
from orders import *

# Crear classe CVFileManager amb funcions read i write.
class CSVFileManager:
  def __init__(self,path: str):
    self.path = path

  # Llegeix dades de csv i les converteix en un Panda DataFrame.
  def read(self) -> str:
    return pd.read_csv(self.path) 
  
  # Les funcions writeusers i writeproducts creen fitxers txt i escriuen la informació dels users i dels products utilitzant les funcions describe prèviament descrites.
  def writeusers(cashiers_list, cashiers, customer_list, customer):
    with open('llista_users.txt','w') as f: 
      f.write("List of users:\n")
      f.write(" \n")
      f.write("List of ")
      f.write(cashiers)
      f.write(":\n")
      for z in cashiers_list:
        f.write(Cashier.describe(z))
        f.write("\n")
      f.write(" \n")
      f.write("List of ")
      f.write(customer)
      f.write(":\n")
      for z in customer_list:
        f.write(Customer.describe(z))
        f.write("\n")

  def writeproducts(hamburgers_list, hamburgers, happymeals_list, happymeals, drinks_list, drinks,  sodas_list, sodas):
    with open('llista_productes.txt','w') as f: 
      f.write("List of products:\n")
      f.write(" \n")
      f.write("List of ")
      f.write(hamburgers)
      f.write(":\n")
      for z in hamburgers_list:
        f.write(Product.describe(z))
        f.write("\n")
      f.write(" \n")
      f.write("List of ")
      f.write(happymeals)
      f.write(":\n")
      for z in happymeals_list:
        f.write(Product.describe(z))
        f.write("\n")
      f.write(" \n")
      f.write("List of ")
      f.write(drinks)
      f.write(":\n")
      for z in drinks_list:
        f.write(Product.describe(z))
        f.write("\n")
      f.write(" \n")
      f.write("List of ")
      f.write(sodas)
      f.write(":\n")
      for z in sodas_list:
        f.write(Product.describe(z))
        f.write("\n")

  # La funció write_order escriu un resum de la informació de la comanda en un fitxer csv.
  def write_order(df_caixer_a, df_customer_a, preu_total):
    # Obrir fitxer order.csv
    with open('order.csv','w') as f: 

      # Escriure DNI caixer
      # 1. Crea llita amb dni del caixer.
      dni_l = df_caixer_a['dni'].tolist()
      # 2. Iniciar variable dni.
      dni = 0
      # 3. Guardar dni a la variable dni.
      for x in dni_l:
        dni = dni + x
      # 4. Escriure variable al fitxer.
      f.write("DNI del caixer : ")
      f.write(str(dni))

      f.write("\n")
      f.write(" \n")

      # Escriure DNI client (anàleg al dni caixer).
      dni_c = df_customer_a['dni'].tolist()
      dni = 0
      for x in dni_c:
        dni = dni + x
      f.write("DNI del comprador : ")
      f.write(str(dni))

      f.write("\n")
      f.write(" \n")

      # Escriure data i hora en la qual s'ha fet la comanda.
      current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
      f.write("Data i hora de la venda : ")
      f.write(str(current_datetime))
      
      f.write("\n")
      f.write(" \n")

      # Escriure preu total.
      f.write("Total : ")
      f.write(str(preu_total))


pass

