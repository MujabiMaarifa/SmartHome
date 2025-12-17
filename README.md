Smart Home Automation Rule Based System

goal: Smart home aims to automate home activities, enhance security and recommend actions to be taken by users when issues are detected.

Tech used:
    Prolog: to write knowledge base that stores facts and rules of our system. * it is found in "smart_home.pl" file *
    python: enhance querying of the prolog knowledge base and enhance interactivity * python file "smart_home.py" file *

NB: combining python and prolog forms hybrid rule based system

Libraries used:
   from pyswip import Prolog - enhance connectivity of the python and prolog

//Change the function calls with different arguments to check the different actions and states in the smart home system based rule
//can also edit the facts and rules defined in the "smart_home.pl" 

How to run the program:
    git clone https://github.com/MujabiMaarifa/SmartHome
    
    -- ensure python library pyswipl is insatalled in the virtual environment using:
        pip install pyswip

    run the python file:
        python smart_home.py
        or
        python3 smart_home.py

System designed by MujabiMaarifa.
