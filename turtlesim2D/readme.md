# Guideline for setup
Run the following command. It will open the simulation.
```roscore```
In a new terminal
```
rosrun turtlesim turtlesim_node
```
Use rostopic and rosmsg for additional information. (Of course in a new terminal)
```
rostopic list
rostopic info <topic name>
rosmsg info <msg name>
```

Open a new folder and create a py file 
```
mkdir TurtleSim
cd TrurtleSim
touch avoidWall.py
chmod +x avoidWall.py
```

