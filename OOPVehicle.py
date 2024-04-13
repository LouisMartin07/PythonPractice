class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year    
        
class Aircraft(Vehicle):
    def __init__(self, make, model, year, aircraft_type, max_altitude, range):
        super().__init__(make, model, year)
        self.aircraft_type = aircraft_type
        self.max_altitude = max_altitude
        self.range = range
        
class AircraftModel(Aircraft):
    def __init__(self, make, model, year, aircraft_type, max_altitude, range, engine_type):
        super().__init__(make, model, year, aircraft_type, max_altitude, range)
        self.engine_type = engine_type
    
class Car(Vehicle):
    def __init__(self, make, model, year, body_style, transmission):
        super().__init__(make, model, year)
        self.body_style = body_style
        self.transmission = transmission
        
class CarModel(Car):
    def __init__(self, make, model, year, body_style, transmission, name, steering, catalog_description, top_speed, average_mileage, colors):
        super().__init__(make, model, year, body_style, transmission)
        self.name = name
        self.steering = steering
        self.catalog_description = catalog_description
        self.top_speed = top_speed
        self.average_mileage = average_mileage
        self.colors = colors


my_car = CarModel(
    make="Hyundai",
    model="Genesis",
    year=2021,
    body_style="SUV",
    transmission="Automatic",
    name="GV-80",
    steering="Power",
    catalog_description="Bougie car with large trunk space for midsize families, terrible mileage",
    top_speed=150,
    average_mileage=16.5,
    colors=["black", "White"]
)

my_aircraft = AircraftModel(
    make="Lockheed",
    model="KC-130T",
    year=1998,
    aircraft_type="Military",
    max_altitude='Depends on the atmospheric conditions',
    range='How crazy is the pilot?',
    engine_type="Turbo Prop"
)