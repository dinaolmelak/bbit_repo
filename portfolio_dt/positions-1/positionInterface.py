from securityInterface import securityInterface
class positionInterface(security):
    def __init__(self, security, initialPosition: int) -> None:
        self.secure = security
        self.currentPos = initialPosition

    def getSecurity(self) -> securityInterface:
        return self.secure

    def getPosition(self) -> int:
        return self.currentPos
    
    def setPosition(self, inputValue: int) -> None:
        self.currentPos = inputValue
    
    def addPosition(self, inputValue: int) -> None:
        currentPos += inputValue
