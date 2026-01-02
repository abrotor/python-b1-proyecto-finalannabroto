from abc import ABC, abstractmethod
#Write your code here

class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(FoodPackage):  
  #Write your code here
  def pack(self):
    return "Food Wrap Paper" 
  def material(self):
    return "Aluminium"
  pass

class Bottle(FoodPackage):
  def pack(self):
    return "Bottle" 
  def material(self):
    return "Plastic"
  #Write your code here
  pass
      
class Glass(FoodPackage):  
  #Write your code here
  pass

class Box(FoodPackage):  
  #Write your code here
  pass