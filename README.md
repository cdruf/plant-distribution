# plant-distribution
Simulation for inversive plant distribution.

The simulation is built in Python using the SimPy library. Initially plants (green dots) are placed on a *n* x *n* grid, and a few other plants (weeds) are placed in the bottom left corner of the grid (red dots). 3 parameters determine the proliferation of both types of plants:

* Average lifetime,
* Average time till offspring is created, and
* Maximum distance of the offspring.

The weed has a shorter lifetime, but proliferates quickly. 

The images below are taken from the animation that visualizes the simulation. It can be observed that the weed (in red) spreads and displaces the original plants (green). 

<img src="img/Figure_1.png" alt="Figure_3" width="25%" />&nbsp;&nbsp;&nbsp;<img src="img/Figure_2.png" alt="Figure_2" width="25%" />&nbsp;&nbsp;&nbsp;<img src="img/Figure_3.png" alt="Figure_1" width="25%" />

<img src="img/Figure_4.png" alt="Figure_7" width="25%" />&nbsp;&nbsp;&nbsp;<img src="img/Figure_5.png" alt="Figure_4" width="25%" />&nbsp;&nbsp;&nbsp;<img src="img/Figure_6.png" alt="Figure_5" width="25%" />



The simulation is a simplified system for illustration. Realistic scenarios include additional assumptions to fine-tune the behavior of the system.  

