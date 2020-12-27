from abc import ABC, abstractmethod
# определяет общий интерфейс для создания объектов в суперкласса


class Cars_Factory(ABC):
    pass

    @abstractmethod
    def create_sedan(self):
        pass

    @abstractmethod
    def create_coupe(self):
        pass

class BMW_factory(Cars_Factory):
    def create_sedan(self):
        return BMW_sedan()

    def create_coupe(self):
        return BMW_coupe()


class Mersedes_factory(Cars_Factory):
    def create_sedan(self):
        return Mersedes_sedan()

    def create_coupe(self):
        return Mersedes_coupe()

class Sedan(ABC):
    @abstractmethod
    def sedan_unique_function(self):
        pass

class BMW_sedan(Sedan):
    def sedan_unique_function(self):
        return f'Sedan of BMW'

class Mersedes_sedan(Sedan):
    def sedan_unique_function(self):
        return f'Sedan of Mersedes'

class Coupe(ABC):
    @abstractmethod
    def coupe_unique_function(self):
        pass

    def another_function(self, collaborator: Sedan):
        pass

class BMW_coupe(Coupe):
    def coupe_unique_function(self):
        return f'Coupe of BMW'

    def another_function(self, collaborator: Sedan):
        result = collaborator.sedan_unique_function()
        return f"The result of the coupe of BMW collaborating with the ({result})"

class Mersedes_coupe(Coupe):
    def coupe_unique_function(self):
        return f'Coupe of Mersedes'

    def another_function(self, collaborator: Sedan):
        result = collaborator.sedan_unique_function()
        return f"The result of the coupe of Mersedes collaborating with the ({result})"

def client_code(factory: Cars_Factory):
    sedan = factory.create_sedan()
    coupe = factory.create_coupe()

    print(f"{sedan.sedan_unique_function()}")
    print(f"{coupe.another_function(sedan)}", end="")

if __name__ == "__main__":
    print("BMW factory type:")
    client_code(BMW_factory())

    print("\n")

    print("Mersedes factory type:")
    client_code(Mersedes_factory())
