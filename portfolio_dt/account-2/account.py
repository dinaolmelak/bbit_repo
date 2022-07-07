%%writefile ../implementations/accountSolution.py 
#Uncomment line above & run cell to save solution
#TODO Define class that implements accountInterface & allows for the management of an account
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from interfaces.securityInterface import securityInterface

# create an account class to hold multiple positions and account name
class account(securityInterface):
    def __init__(self,name, security):
        self.acountName = name
        self.security = security
        self.positions = {}
        
    # method getAccountName() return account name
    def getAccountName(self):
        return self.accountName
    
    # method getAllPositions() returns multiple positions
    def getAllPositions(self):
        return self.positions
    
    # method addPositions() add a set of position objects
    def addPositions(positionsToAdd):
        for position in positionsToAdd:
            self.positions[position.getSecurity()] = position
            
    # method getPositionsForSecurity that returns map with query value
    def getPositionsForSecurity(inputSecurity):
        positionsForSecurity = []
        inSecurity = security()
        if type(inputSecurity) == str:
            inSecurity = security(inputSecurity)

        for security in self.positions:
            if security == inSecurity:
                positionsForSecurity.append(security)
        return positionsForSecurity
    
    # method removePosition() remove position from account with set of security names/security objects. ignore if not available
    def removePosition(securities):
        for secure in securities:
            currentSecurity = security()
            if type(secure) == str:
                currentSecurity = security(secure)
                self.positions.pop(currentSecurity)
    for secure in securities:
      currentSecurity = security()
      if type(secure) == str:
        currentSecurity = security(secure)
      self.positions.pop(currentSecurity)
    
  
