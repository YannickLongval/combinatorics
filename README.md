# combinatorics
Applying the concepts I learned in my **MAT344: Introduction to Cominatorics** class to create various programs related to combinatorics. An overview of each program is provided below.

# graphs/kruskalsAlgo.py
Kruskal's algorithm is used to find the minimal weight spanning tree of a connected, undirected, weighted graph (this project assumes the graph is connected). More about the algorithm can be found here: [https://en.wikipedia.org/wiki/Kruskal%27s_algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
<br/><br/>
This program implements Kruskal's, and visualizes the graph with the spanning tree. An example is of the visualizer output is shown below.
<p align="center">
<img width="400" src="/graphs/Kruskals.png"/>
</p>

# inclusion_exclusion/venn_diagram.py
Create venn diagrams for n-sets can get rather complicated. Inuitively, it seems reasonable to just add another circle to the 3-set venn diagram to create a 4-set venn diagram like so:
<p align="center">
<img width="400" src="/inclusion_exclusion/wrongFourSetVD.png"/>
</p>
The issue with this diagram is that there are groups that are mission. For example, the group of data that are in A&cap;B'&cap;C&cap;D' (or just AC, the elements in set A and C, but not B or D) is not in the diagram. One valid 4-set venn diagram can be created like so:
<br/>
<br/>
<p align="center">
<img width="400" src="/inclusion_exclusion/rightFourSetVD.svg"/>
</p>
The key here is that the shape has been changed from a circle to an ellipse. The reason this is important is because a circle can only interect with itself at two point, whereas an ellipse can create up to 4 intersections. The number of potential intersections contributes to the number of groups, which is why an ellipse can be used to create the 4-set venn diagram.
<br/>
<br/>
While an ellipse is sufficient for 4 and 5 set venn diagrams, it cannot create any n-set venn digram. The reason is that the number of groups that a shape can create grows polynomially, whereas the number of groups grows exponentially. As a result, the number of possible intersection must increase as the number of sets increase. 
<br/>
<br/>
This is where this program comes in. The python script calculates how many groups are needed for an n-set venn diagram, and determines how many intersections the shape must be able to make to create enough groups for the venn diagram. The turtle library is then used to draw the shape. An example for a potential shape for a 6-set venn diagram is shown below:
<br/>
<br/>
<p align="center">
<img width="400" src="/inclusion_exclusion/sixSetVDShape.png"/>
</p>

# generating_functions/dice.py
The Sicherman dice are a variation to the traditional pair of six-sided dice, where the numbers on the faces are different, but the probabilities when rolling for the sum of the dice, are equal to the regular dice. More about the Sicherman dice can be found here [https://en.wikipedia.org/wiki/Sicherman_dice](https://en.wikipedia.org/wiki/Sicherman_dice)
<br/>
<br/>
The purpose of this program was to look for the "Sicherman dice" of any n-sided die. This is done by creating the generating functions for the regular n-sided die, then playing with the factors of these generating functions to create new pairs of dice. 

# binomial_theorem/BinomialThm.py
A simple program that uses brute force to validate the binomial theorem. 

