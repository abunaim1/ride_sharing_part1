from abc import ABC, abstractmethod
class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)
    
    #dander method
    def __repr__(self) -> str:
         return f'{self.company_name} has {len(self.riders)} riders and {len(self.drivers)} drivers'

class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        self.nid = nid
    
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        self.current_location = current_location
        self.wallet = 0
        super().__init__(name, email, nid)
    
    def display_profile(self):
        print(f'Driver Name is {self.name} and mail is {self.email}')

class Rider(User):
    def __init__(self, name, email, nid, current_location) -> None:
        self.current_location = current_location
        self.current_ride = None
        super().__init__(name, email, nid)
    
    def display_profile(self):
        print(f'Rider Name is {self.name} and mail is {self.email}')

    def ride_request(self, uber, destination):
        if not self.current_ride:
            ob = Ride_Matching(uber.drivers)
            res = ob.start_riding(self, destination)
            print("Your result is, ", res)
            self.current_ride = res
            return True
        else:
            return False

class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
    
    def start_ride(self):
        pass

    def start_end(self):
        pass

    def __repr__(self) -> str:
        return f'Ride start from {self.start_location} and end to {self.end_location}'

class Ride_Matching:
    def __init__(self, drivers) -> None:
        self.drivers = drivers
    
    def start_riding(self, fahad, destination):
        if len(self.drivers) > 0:
            ride = Ride(fahad.current_location, destination)
            return ride
        else:
            return 'Sorry, Driver not found!'

uber = Ride_Sharing('UBER')
alice = Driver('Alice', 'alice55@gmail.com', 113421423, 'Chittagang1')
fahad = Rider('Fahad Al Hossain', 'fahad@gmail.com', 10030029933, 'Chittagang2')
uber.add_driver(alice)
uber.add_rider(fahad)

if fahad.ride_request(uber, 'Dhaka'):
    print('Let''s Go!')
else:
    print('No Ride Today')