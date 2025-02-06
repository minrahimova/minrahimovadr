class Person:
    def __init__(self, name: str, age: int): #инициализация (создание)
        self.name = name
        self.age = age
    def __str__(self): #вывод строкой инфу о челе
        return f"Person: {self.name}, Age: {self.age}"
        
    def __eq__(self,other): #сравниваем людей 
        return self.name == other.name and self.age == other.age 
    def __lt__(self,other): #cравниваем явл наш чел меньше чем другой по возрасту  
        return self.age < other.age 
    def __gt__(self,other): #cравниваем явл наш чел больше чем другой по возрасту  
        return self.age > other.age
        
class Collection: #список в котором наши люди
    def __init__(self, people: list):
        self.people = people
    def __add__(self, person): #добавляем человека в нашу коллекцию
        self.people.append(person)
        return self
    def __len__(self): #кол-во людей в коллекции 
        return len(self.people)
    def __getitem__(self,index): #выведет чела с каким-то индексом 
        return self.people[index]
    def __call__(self): #возр имена наших людей из коллекции 
        return [i.name for i in self.people]
    def __contains__(self,other): #проверяет есть ли человек в нашей коллекции
        return other in self()
    
c = Collection([Person("Alice", 25), Person("Bob", 30)]) #вывод, проверка
print("Alice" in c) # True
print("Charlie" in c) # False
c = Collection([Person("Alice", 25), Person("Bob", 30)])
print(c()) # ["Alice", "Bob"]  
c = Collection([Person("Alice", 25), Person("Bob", 30)])
print(c[0]) # "Person: Alice, Age: 25"
c = Collection([Person("Alice", 25), Person("Bob", 30)])
print(len(c)) # 2
c = c + Person("Charlie", 22)
print(len(c)) # 3
print(Person("Alice", 25)>(Person("Bob", 30)))
