  pushconst 1
  popaddr $counter
.loopstart
  pushaddr $counter
  pushconst 15
  jlt 5
  jmp .endloop
  pushaddr $counter
  int 1
  pushaddr $counter
  inc
.endloop


