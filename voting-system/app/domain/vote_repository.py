import abc
from typing import List

from app.domain.vote import Vote

# como un meta manager de Django? 
# Realmente es una interfaz, aun no la implementamos
class VoteRepository(metaclasss=abc.ABCMeta): 
    @abc.abstractmethod
    def add(self, vote: Vote) -> Vote:
        raise NotImplementedError
    
    @abc.abstractmethod
    def all(self) -> List[Vote]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def total(self) -> int:
        raise NotImplementedError
    