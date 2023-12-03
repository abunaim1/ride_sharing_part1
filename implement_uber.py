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
        self.curren_location = current_location
        super().__init__(name, email, nid)
    
    def display_profile(self):
        print(f'Rider Name is {self.name} and mail is {self.email}')


    