# 1-D Elastic Collision Simulator

-summary
1 - Algorithm Description
2 - Variables
3 - Limitations
4 - Formula


- Algorithm Description
This algorithm is able to calculate and simulate a one-dimensional elastic collision.

In a collision characterized as elastic, the combined kinetic energy of the two colliding entities remains unchanged both prior to and subsequent to the collision. In the context of an elastic collision, the preservation of kinetic energy is upheld.


- Variables
The variables used for the calculation are: Initial speed of object A, Mass of object A, Initial speed of object B and Mass of object B. The algorithm uses these values ​​to calculate the final velocities of each object (after they collide with each other)


- Limitations
The velocity entered for object A will always be positive and the velocity entered for object B will always be negative (even if you apply positive values ​​to both). This will always make each element advance towards the other.

Thus, allowed values ​​for mass are: "0<m<50", and allowed values ​​for velocity are: "0<v<16".


-FORMULA:
Vfa = [(ma - mb)*via + 2 * mb * vib]/(ma + mb)
Vfa = [2 * ma * via (ma - mb) * vib]/(ma + mb)




