from abc import ABC, abstractmethod
from datetime import datetime

class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self,rider):
        self.riders.append(rider)
    
    def add_driver(self, driver):
        self.drivers.append(driver)
    
    def __repr__(self) -> str:
        return f'Company Name: {self.company_name} with riders {len(self.riders)} and drivers {len(self.drivers)}'
        
class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        self.__nid = nid
        self.__id = 0
        self.wallet = 0
    
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

#customer / passenger
class Rider(User): 
    def __init__(self, name, email, nid, current_location, initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount 
        self.current_location = current_location
        super().__init__(name, email, nid)
    
    def display_profile(self):
        print(f'Rider Name: {self.name} and Email: {self.email}')
    
    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def ride_req(self, ride_sharing, destination):
        if not self.current_ride:
            ride_request = Ride_Request(self, destination)
            ride_mathcer = Ride_Matching(ride_sharing.drivers)
            self.current_ride = ride_mathcer.find_driver(ride_request)
    
    def show_current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, nid, curren_location) -> None:
        self.current_location = curren_location
        super().__init__(name, email, nid)
    
    def display_profile(self):
        print(f'Driver Name: {self.name} and Email: {self.email}')

    def accept_ride(self, ride):
        ride.set_driver(self) 

class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None
    
    def set_driver(self, driver):
        self.driver = driver
    
    def start_ride(self):
        self.start_time = datetime.now()
    
    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f'Ride Details. Start from {self.start_location} to {self.end_location}'

class Ride_Request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location

class Ride_Matching:
    def __init__(self, drivers) -> None:
        self.available_drivers = drivers
    
    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride

class Vehicle(ABC):
    speed = {
        'car' : 50,
        'bike' : 40,
        'cng' : 15
    }

    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'available'
    
    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status = 'unavailable'

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status = 'unavailable'

# check the class

niye_jaw = Ride_Sharing('Niye Jaw')
sakib = Rider('Sakib Khan', 'sakib@lal.com', 1245, 'Mohakhali', 1200)
niye_jaw.add_rider(sakib)
raja = Driver('Raja chandra', 'raja@kala.com', 1223344, 'Gulshan')
niye_jaw.add_driver(raja)
print(niye_jaw)
sakib.ride_req(niye_jaw, 'Farme Gate')
sakib.show_current_ride()
