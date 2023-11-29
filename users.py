from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, id, email, nid) -> None:
        self.name = name
        self.__id = 0
        self.email = email
        self.__nid = nid
        self.__wallet = 0
    
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, id, email, nid) -> None:
        super().__init__(name, id, email, nid)
    def display_profile(self):
        print(f'Rider: with name {self.name} and email {self.email}')