from .positionInterface import positionInterface
from typing import Any, Dict, Set, Iterable
class accountInterface():
    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        pass

    #Return the account's name
    def getName(self) -> str:
        pass

    #Return all positions currently within the account
    def getAllPositions(self) -> Iterable[positionInterface]:
        pass

    #Return all positions that contain a security in a given input set
    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        pass

    #Add positions to the account
    def addPositions(self, positions: Set[positionInterface]) -> None:
        pass
    
    #Remove a number of positions from this account if they represent a security in a given input set
    def removePositions(self, securities: Set) -> None:
        pass
