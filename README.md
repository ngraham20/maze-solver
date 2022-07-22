# Maze Algorithms Final Project
The actual assignment was to study the difference between multiple different algorithms for a given problem, but I found it hard to explain how exactly the algorithms exactly worked, so I integrated a system to produce the choice history of which pixels were joined with each other. Here is the result:
### Kruskal's Algorithm on a 25x25 pixel grid
<img src="examples/Kruskal-25x25.gif" width="300" style="image-rendering: pixelated;"/>

### And an A-Star search algorithm to solve it!
<img src="examples/AS-Kruskal-25x25.gif" width="300" style="image-rendering: pixelated;"/>

### Prim's Algorithm on a 25x25 pixel grid
<img src="examples/Prims-25x25.gif" width="300" style="image-rendering: pixelated;"/>

### And a Recursive Backtracking algorithm to solve this one!
<img src="examples/RB-Prims-25x25.gif" width="300" style="image-rendering: pixelated;"/>

### Just so you don't think I didn't try, this is a 1001x1001 pixel grid that was solved with an A-Star algorithm. This may or may not have used 12Gb of ram to solve. The solution path starts in the upper right corner and transitions slowly from red, through purple, to blue in the lower left corner.
<img src="examples\solutionAStar-1001x1001-3.45774s.png"/>