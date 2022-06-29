# qwalk-visualizations
Implementation and visualization of quantum walks, submitted as a poster presentation for QCE Quantum Week 2023.

Authors:
- Addie Jordon, aedjordon@gmail.com, University of Victoria
- Austin Hawkins-Seagram, hawkins.aus@gmail.com, University of Victoria

Under the supervision of:
- Dr. Ulrike Stege, ustege@uvic.ca, University of Victoria

## Acknowledgements
We acknowledge the NSERC CREATE in Quantum Computing Program, grant number 543245.

## Quantum Walks
Quantum walks are the quantum analogue to classical random walks, wherein a walker tosses a coin to decide which direction to go when they come to a fork in the road. Quantum walkers, however, can exist in a superposition of positions and quantum coins can land both heads and tails. 

## Our implementation
We implement quantum walks where the coin operation is simply the Hadamard gate. We create visualizations of the walk at each step, where darker squares represent a higher probability of the walker being at that position upon measurement.

We also introduce Sticky Walk, a quantum walk variant where the walker 'sticks' to target states upon their discovery. 

Our walks currently are only carried out on uniform structures, namely lattices and cubes. Additionally, we allow these structures to have 'wrap-around' functionality; that is, if the walker walks off of one side, they will appear on the other. 
