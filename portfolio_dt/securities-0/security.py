%%writefile ../implementations/securitySolution.py 
#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
from interfaces.securityInterface import securityInterface
class security(securityInterface):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
