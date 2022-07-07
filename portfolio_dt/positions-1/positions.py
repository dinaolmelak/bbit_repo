%%writefile ../implementations/positionSolution.py 
#Uncomment line above & run cell to save solution
#TODO Define class that implements positionInterface & allows for the management of a position
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)


from interfaces.positionInterface import positionInterface

class position(positionInterface):
    def __init__(self, name, value, secured):
        self.name = name
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
        #TODO: throw error
        if newPosition < 0:
            raise Exception
        else:
            self.value = newPosition
    # add to existing position
    def addPosition(self,positionToAdd):
        self.value += positionToAdd
    # set the position value
    def setPosition(self,positionToSet):
        self.value = positionToSet
