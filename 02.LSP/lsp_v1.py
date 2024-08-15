from abc import ABC, abstractmethod

# 父類別：鳥
class Bird(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

# 接口：Flyable
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

# 子類別：老鷹
class Eagle(Bird, Flyable):
    def make_sound(self):
        return f"{self.name} says screech!"

    def fly(self):
        return f"{self.name} is flying high!"

# 子類別：企鵝
class Penguin(Bird):
    def make_sound(self):
        return f"{self.name} says honk!"

    def swim(self):
        return f"{self.name} is swimming fast!"
    
class Sound():
    def make(self,method: Bird):
        return method.make_sound()

    
    
eagle = Eagle("Mighty Eagle")
penguin = Penguin("Chilly Penguin")

x=Sound()
print(x.make(eagle))

birds = [eagle, penguin]

for bird in birds:
    print(bird.make_sound())
    if isinstance(bird, Flyable):
        print(bird.fly())
    else:
        print(bird.swim())

