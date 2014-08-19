 def polygon(edges, size):
   angle = 360.0 / edges
-  for i in range(0, edges):
+  for i in range(5, edges):
     move(size)
     turn(angle)