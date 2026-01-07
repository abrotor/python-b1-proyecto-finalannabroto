# Importar mòdul abc.
from abc import ABC, abstractmethod

# Crear classe abstracta FoodPackage amb mètode pack, material i describe.
class FoodPackage(ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"    
    
# Crear classes Warpping, Bottle, Glass i Box amb mètodes pack i material.
class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper" 
  def material(self):
    return "Aluminium"
  pass

class Bottle(FoodPackage):
  def pack(self):
    return "Bottle" 
  def material(self):
    return "Glass"
  pass
      
class Glass(FoodPackage):
  def pack(self):
    return "Glass" 
  def material(self):
    return "Cardboard"
  pass

class Box(FoodPackage): 
  def pack(self):
    return "Box" 
  def material(self):
    return "Cardboard"
  pass