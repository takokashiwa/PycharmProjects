class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('first')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self.enable_atuo_run = enable_auto_run
    def run(self):
        print('super first')

telsa_car = TeslaCar()
print(telsa_car.enable_atuo_run)
