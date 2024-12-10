# Setup Guideline
```
mkdir catkin_ws
cd catkin_ws
mkdir src
catkin_make
cd src
mkdir scripts
cd scripts
touch talker.py
chmod +x talker.py
code .
```
It will get things done for start coding. We will do everything in the src folder. Do not alter anything in devel folder. 
The talker.py has been attached.

For listener-
```
cd catkin_ws/src/scripts
touch listener.py
chmod +x listener.py
```
# Initiate the simulation
```
roscore
```
Then in another terminal
```
python3 talker.py
```
Open another terminal and run -
```
python3 listener.py
```
