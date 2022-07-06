from securities import security

class position(security):
    def __init__(self, value, secured):
        self.value = value
        self.secured = secured
    # get the security object
    def getSecurity(self):
        return secured
    # get current position value
    def getPosition(self):
        return self.value
    # update position value
    def updatePosition(self,newPosition):
        # if update of position value results to short
            # throw error
        try:
            self.value = newPosition
        except positionShort as error:
            print("New Position causes a short")
        self.value = newPosition
    # add to existing position
    def addPosition(self,positionToAdd):
        self.value += positionToAdd
    # set the position value
    def setPosition(self,positionToSet):
        self.value = positionToSet
        
        
