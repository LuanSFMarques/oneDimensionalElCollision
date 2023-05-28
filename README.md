# 1-D Elastic Collision Simulator

+--------------------------------------------------------------------------------------------+
|                         1-D Elastic Collision Calculator                                   |
+--------------------------------------------------------------------------------------------+

-summary

1 - Algorithm Description

2 - Variables

3 - Limitations

4 - Formula

5 - creation background


- Algorithm Description

This algorithm is able to calculate and simulate a one-dimensional elastic collision.

In a collision characterized as elastic, the combined kinetic energy of the two colliding entities remains unchanged both prior to and subsequent to the collision. In the context of an elastic collision, the preservation of kinetic energy is upheld.



- Variables

The variables used for the calculation are: Initial Velocity of object A, Mass of object A, Initial Velocity of object B and Mass of object B. The algorithm uses these values ​​to calculate the final velocities of each object (after they collide with each other)



- Limitations

The velocity entered for object A will always be positive and the velocity entered for object B will always be negative (even if you apply positive values ​​to both). This will always make each element advance towards the other.



Thus, allowed values ​​for mass are: "0<m<50", and allowed values ​​for velocity are: "0<v<16".


- FORMULA

Vfa = [(ma - mb)*via + 2 * mb * vib]/(ma + mb)
Vfa = [2 * ma * via (ma - mb) * vib]/(ma + mb)



- Creation Background

As you can see, this algorithm has some shortcomings. I'm an amateur developer and I'm still getting to know this vast world of programming! My interest in this project came when I thought of making some minimally complex algorithm using my basic knowledge and physics, so this is a love project!



##That's all!



