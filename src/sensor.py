from abc import ABC, abstractmethod


class SensorABC(ABC):
    @abstractmethod
    def get_data():
        pass
