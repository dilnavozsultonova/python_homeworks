class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species  
    
    def eat(self):
        print(f"{self.name} is eating!")
    
    def sleep(self):
        print(f"{self.name} is sleeping!")
    
    def display_Info(self):
        
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Species: {self.species}")



class Cow(Animal):
    def __init__(self, name, age, species, milk_production_rate):
        super().__init__(name, age, species)  
        self.milk_production_rate = milk_production_rate
    
    def produce_milk(self):
        print(f"{self.name} produces milk!")
    
    def display_Info(self):
        super().display_Info()  
        print(f"Milk production rate: {self.milk_production_rate} liters per day")



class Chicken(Animal):
    def __init__(self, name, age, species, egg_count):
        super().__init__(name, age, species)  
        self.egg_count = egg_count
    
    def lay_eggs(self):
        print(f"{self.name} can lay eggs!")
    
    def display_Info(self):
        super().display_Info()  
        print(f"Number of eggs: {self.egg_count}")


class Pig(Animal):
    def __init__(self, name, age, species, weight):
        super().__init__(name, age, species)  
        self.weight = weight
    
    def root_around(self):
        print(f"{self.name} is sniffing the ground!")
    
    def display_Info(self):
        super().display_Info()  
        print(f"Weight: {self.weight} kg")



cow = Cow("Bessie", 5, "Cow", 12)
chicken = Chicken("Clucky", 2, "Chicken", 50)
pig = Pig("Porky", 3, "Pig", 150)


print("Cow Details:")
cow.eat()
cow.produce_milk()
cow.display_Info() 

print("\nChicken Details:")
chicken.eat()
chicken.lay_eggs()
chicken.display_Info()  

print("\nPig Details:")
pig.eat()
pig.root_around()
pig.display_Info()  

    


        
 
