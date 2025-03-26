from abc import ABC, abstractmethod

class BaseScraper(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def parse_data(self, data):
        pass

    def scrape(self):
        data = self.fetch_data()
        return self.parse_data(data)
