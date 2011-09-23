pushconst 5
popaddr $counter
.label
pushaddr $counter
int 1
jmp .label