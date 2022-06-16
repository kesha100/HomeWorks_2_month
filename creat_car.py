class Car:
    def __init__(self, title, model):
        self.title = title
        self.model = model

    def start_engine(self):
        pass

    def stop_engine(self):
        pass

    def get_car_info(self):
        pass

class Cars(Car):
    def __init__(self, title, model, max_sp):
        super().__init__(title, model)
        self.max_sp = max_sp
    def start_engine(self):
        print('ENGINE started!!!')

    def stop_engine(self):
        print('ENGINE stopped!!!')

    def get_car_info(self):
        print(f"""
        Title: {self.title}
        Model: {self.model}
        Max Speed: {self.max_sp}
        """)