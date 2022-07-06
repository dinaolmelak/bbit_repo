```python
# Copyright 2022 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
```

# Positions Learning Item

### What is a position?

Now that we understand what a security is, the next logical entity in our position manager is positions! A position is the representation of how *much* of a particular security is owned by an individual or financial firm. Simply put, it lets you know how much Y you own.

For example, you could have a position like this:

A position of ***2,000*** shares of ***MSFT USD***!

You may think that all positions are positive numbers, but you can actually have positions that are negative, which represents that you "own" a negative amount of something. This is called a *short* position versus a positive position amount that is *long*. For the focus of this lab, we'll assume and expect that all positions are long. 

### Problem Definition

We want to build a class that represents a position. We should be able to construct a position with a security object we created, as well as a seed or initial position. We may also want to create a position without constructing a security object by using the security name we'd like our position to represent.

We'd expect the ability to get the security object the position represents along with the current position value. Lastly we'd want to be able to update the position value with the ability to add to the existing position & set the position value. If a position seed or update results in a short position we'd expect an error to be thrown.

- Allow for a position to be created with a security name or object and a seed position value
- Allow for gathering of the position's security and position value
- Allow for updating of the position's size via addition & setting

### Provided Tools

#### *Data Source*

No data is required for creating your position class but there is a data generator class *positionUpdates* which can be used to generate a few random position updates for testing. On creation this class will generate a list of numerical values that will always be positive when iterating and adding. The class has three methods that can be used isNextAvailable(), getNextTransaction() and getTransactionList(). Below is a snippet of the class and examples of how each method could be used in creating a test

```python
#Import our data generator
from generators.positionDataGenerator import positionUpdates
positionUpdates
posUpdater = positionUpdates()

#Check if there is an available position update
if posUpdater.isNextAvailable()
    #Get the current position update value
    print(posUpdater.getNextTransaction())

#Return the list of all positions update generated
posList = posUpdater.getTransactionList()
```

#### *Solution Interface*

Your solution will need to follow the interface provided in the lab. Below is a snippet of the interface for securities that you can inherit from. The methods that will be tested are displayed & will need to be overwritten with your implementation. You're free to add more methods then what is displayed in the interface!

```python
#filename interfaces.positionInterface.py
#Position Class Interface

from securityInterface import securityInterface
class positionInterface():
    def __init__(self, security, initialPosition: int) -> None:
        pass

    def getSecurity(self) -> securityInterface:
        pass

    def getPosition(self) -> int:
        pass
    
    def setPosition(self, inputValue: int) -> None:
        pass
    
    def addPosition(self, inputValue: int) -> None:
        pass
```

To successfully import the interface into your solution cell you'll need to add the below code snippet. Due to the filesystem layout in the current Jupyter notebook, importing relative .pys requires us to adjust the system path.

```python
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
```

#### *Testing*

Once you have completed & saved your solution you can run the test file to validate that your solution works as expected. For the test to run the following need to be true.
- Saved code to file **implementations/positionSolution.py**
- Create a class with the name **position** that inherits from **positionInterface**

### Stretch Goals

If you complete your class & have a solution with valid tests try completing the following stretch goals 

- Add custom implementation for class's __str__ method. The position print method shouldn't reimplement the security's print str method but should utilize it.
- Develop a test for your new __str__ method.


```python
#%%writefile ../implementations/positionSolution.py 
#Uncomment line above & run cell to save solution
#TODO Define class that implements positionInterface & allows for the management of a position
```


```python
#Run this cell before running the your testing cell. This will setup the ipytest cell magic command. If you're running this notebook locally you may need to install ipytest from pip or conda
#%conda install ipytest
#%pip install ipytest
import ipytest

ipytest.autoconfig()
```


```python
%%ipytest -qq

#Testing Cell
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

import pytest
import implementations.positionSolution
from implementations.securitySolution import security
from generators.positionDataGenerator import positionUpdates
import importlib
importlib.reload(implementations.positionSolution)

def test_positionManagerInits():
    #GIVEN
    EXPECTED_NAME = "DSAQ US Equity"
    EXPECTED_POSITION = 1000
    INPUT_SEC = security(EXPECTED_NAME)

    #WHEN
    testObjA = implementations.positionSolution.position(INPUT_SEC, EXPECTED_POSITION)
    testObjB = implementations.positionSolution.position(EXPECTED_NAME, EXPECTED_POSITION)

    #EXPECT
    assert (testObjA.getSecurity().getName() == EXPECTED_NAME)
    assert (testObjB.getSecurity().getName() == EXPECTED_NAME)
    assert (testObjA.getPosition() == EXPECTED_POSITION)
    assert (testObjB.getPosition() == EXPECTED_POSITION)

def test_positionUpdates():
    #GIVEN
    secData = positionUpdates()
    EXPECTED_POSITION = sum(secData.getTransactionList())
    
    #WHEN
    testObj = implementations.positionSolution.position("TEST", 0)
    for update in secData.getTransactionList():
        testObj.addPosition(update)

    #EXPECT
    assert (testObj.getPosition() == EXPECTED_POSITION)

def test_positionSet():
    #GIVEN
    testObj = implementations.positionSolution.position("TEST", 0)
    EXPECTED_POSITION = 1000
    
    #WHEN
    testObj.setPosition(EXPECTED_POSITION)

    #EXPECT
    assert (testObj.getPosition() == EXPECTED_POSITION)
    
def test_positionUpdateShortBlock():
    #GIVEN
    BASE_POSITION = 100
    UPDATE_POSITION = -101
    testObj = implementations.positionSolution.position("TEST", BASE_POSITION)


    #EXPECT
    with pytest.raises(Exception):
        testObj.addPosition(UPDATE_POSITION)
```
