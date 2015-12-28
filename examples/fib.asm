pushconst 1
popaddr $value1

pushconst 1
popaddr $value2

pushconst 0
popaddr $counter

.loop
# fib calculation
    pushaddr $value2
    popaddr $temp

    pushaddr $value1
    pushaddr $value2
    add
    popaddr $value2

    pushaddr $temp
    popaddr $value1

    pushaddr $value1
    int 1

# counter handling
    pushconst 1
    pushaddr $counter
    add
    popaddr $counter

    pushaddr $counter
    pushconst 10
    jne .loop
