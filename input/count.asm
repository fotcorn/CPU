pushconst 1
popaddr $counter

.loop
    pushaddr $counter
    int 1
    pushconst 1
    pushaddr $counter
    add
    popaddr $counter

    pushaddr $counter
    pushconst 6
    jne .loop
