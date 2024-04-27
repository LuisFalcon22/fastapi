from abc import ABC, abstractmethod


class UniversidadStrategy(ABC):

    @abstractmethod
    def get_reconocimiento(self, estrellas: int) -> int:
        pass

    @abstractmethod
    def get_cost(self, valor_matricula:float) -> float:
        pass

    @abstractmethod
    def get_time(self, origin: int, destination: int) -> float:
        pass


class Unimag(UniversidadStrategy):
     def get_reconocimiento(self, estrellas: int) -> int:
        return 4
     def get_cost(self, valor_matricula:float) -> float:
        return 800000


     def get_time(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 2, 2)



class UCC(UniversidadStrategy):
      def get_reconocimiento(self, estrellas:int) -> int:
        return 3
      def get_cost(self, valor_matricula:float) -> float:
        return 3000000
      def get_time(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 6, 2)



class UAN(UniversidadStrategy):
     def get_reconocimiento(self, estrellas: int) -> int:
        return 3



     def get_cost(self, valor_matricula:float) -> float:
        return 4000000


     def get_time(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 4, 2)
