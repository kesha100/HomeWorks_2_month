class Car:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):

    def info(self):
        print(f"""
Title: {self.title}
Model: {self.model}
Weight: {self.weight}
Hp: {self.hp}
Nm: {self.nm}
Max_spped: {self.max_speed}
Color: {self.color}
        """)


bmw = Car("BMW", "M4", 2040, 900, 750, 540, "Purple")
mer = Car("Mercedes", "E200", 1500, 400, 600, 390, "White")
toy = Car("Toyota", "Camry70", 2000, 550, 500, 350, "Red")

bmw.info()