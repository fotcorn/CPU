  pushconst 1
  popaddr $counter
.loopstart
  pushaddr $counter
  pushconst 15
  jlt .next
  jmp .endloop
.next
  pushaddr $counter
  int 1
  pushaddr $counter
  inc
.endloop


