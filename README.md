# BlueSky - The Open Air Traffic Simulator

From : https://github.com/TUDelft-CNS-ATM/bluesky

To launch the program:
python BlueSky.py

To check that Python installation is the right one:
python check.py


## Changements due to RL

To change the number of iterations : plugins/dataRL.py --> maxIter

To change the number of sets for noise : plugins/dataRL.py --> nbRandom

To change the set of aircraft : plugins/plugin_init.py --> in createScn.create(...)

To change the file to use : plugins/createScn.py in function create(...)

To apply learning after a learning process : settings.cfg --> change INIT by INIT2 and to set the set of aircraft : plugins/plugin_init2.py --> in createScn.create(...)

