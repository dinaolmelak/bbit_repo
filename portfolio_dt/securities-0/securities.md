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

# Securities Learning Item

### What is a security?

A security is an instrument or object that represents some sort of ownership or relationship of an entity which holds some monetary value. This may sound very ambiguous and that's because securities as a term are ambiguous. A security can be a stock like AAPL, shares that represent an ownership stake in a corporation, debt (such as a mortgage or corporate bond), or even new types of securities such as cryptocurrencies.

### Problem Definition

We want to create a class that can be used to represent a security. Securities have names which are unique identifiers of what they represent. Additionally securities have a monetary value associated with them but for now we'll ignore any valuations. The class we create should satisfy the following.

- Allow for the name of a security to be stored on object construction & via a setter function
- Allow for the name of the security to be retrieved via a getter

### Provided Tools

#### *Data Source*

For this section no data generators are provided

#### *Solution Interface*

Your solution will need to follow the interface provided in the lab. Below is a snippet of the interface for securities that you can inherit from. The methods that will be tested are displayed & will need to be overwritten with your implementation. You're free to add more methods then what is displayed in the interface! 

```python
#filename interfaces.securityInterface.py
#Security Class Interface
class securityInterface():
    def __init__(self, name: str) -> None:
        pass
    
    def getName(self) -> str:
        return "Implement Me!"
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
- Saved code to file **implementations/securitySolution.py**
- Create a class with the name **security** that inherits from **securityInterface**

### Stretch Goals

If you complete your class & have a solution with valid tests try completing the following stretch goals 

- Add custom implementation for class's __str__ method & creating a new unit test to validate your updated method.


```python
#%%writefile ../implementations/securitySolution.py 
#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security
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
    
import implementations.securitySolution
import importlib
importlib.reload(implementations.securitySolution)

def test_securityInit():
    #GIVEN
    EXPECTED_NAME = "DSAQ US Equity"

    #WHEN
    testObj = implementations.securitySolution.security(EXPECTED_NAME)

    #EXPECT
    assert (testObj.getName() == EXPECTED_NAME)
```
