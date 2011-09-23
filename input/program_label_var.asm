 1: pushconst 1
 2: popaddr $4000
 3: pushaddr $4000
 4: pushconst 15
 5: jlt 5
 6: jmp 10
 7: pushaddr $4000
 8: int 1
 9: pushaddr $4000
10: inc
11: popaddr $4000
12: jmp 3
13: int 0
