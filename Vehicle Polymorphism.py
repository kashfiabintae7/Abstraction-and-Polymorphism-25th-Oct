class Ferrari:
    def model(self):
        print("Ferrari FXX Evoluzione")
        
    def engine_type(self):
        print("6262 cm3 V12 engine")
        
    def max_speed(self):
        print("Top Speed: 249 mph")
        
class BMW:
    def model(self):
        print("M4 CSL (G82)")
        
    def engine_type(self):
        print("3.0-liter BMW M TwinPower Turbo inline-6 cylinder")
        
    def max_speed(self):
        print("Top Speed: 191 mph")
        
class Porsche:
    def model(self):
        print("911 Turbo S")
        
    def engine_type(self):
        print("Ditwin-turbocharged 3.7-liter flat-six")
        
    def max_speed(self):
        print("Top Speed: 205 mph")

class Audi:
    def model(self):
        print("Audi R8 V10")
        
    def engine_type(self):
        print("5.2L V10 engine")
        
    def max_speed(self):
        print("Top Speed: 331 mph")

class Bugatti:
    def model(self):
        print("Chiron Super Sport")
        
    def engine_type(self):
        print("8.0-liter quad-turbocharged W16")
        
    def max_speed(self):
        print("Top Speed: 304.7 mph")
        
class Mercedes:
    def model(self):
        print("Mercedes-AMG® ONE")
        
    def engine_type(self):
        print("1.6-litre V6 turbo petrol")
        
    def max_speed(self):
        print("Top Speed: 352 km/h")
        

ferrari = Ferrari()
bmw = BMW()
porsche = Porsche()
audi = Audi()
bugatti = Bugatti()
mercedes = Mercedes()

for car in (ferrari, bmw, porsche, audi, bugatti, mercedes):
    
    car.model()
    car.engine_type()
    car.max_speed()
    print()