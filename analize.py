from generaterb import GenerateRB
from generatekruskal import GenerateKruskal
from generateprims import GeneratePrims

size = 25
count = 10

rb = GenerateRB(size)
rb.analyze(count)

p = GeneratePrims(size)
p.analyze(count)

k = GenerateKruskal(size)
k.analyze(count)

kruskal_maze = "mazes/Kruskal-25x25-0.01229s.png"
prim_maze = "mazes/Primms-25x25-0.00358s.png"
rb_maze = "mazes/RB-25x25-0.00228s.png"