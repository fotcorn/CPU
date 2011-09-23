from instruction_set import instruction_set
   
f = file('input/program.bin')
lines = f.readlines()
f.close()

stack = []
memory = {}
instr_pointer = 0

while True:
    instr = int(lines[instr_pointer])
    
    if instr == instruction_set['add']:
        pass    
    elif instr == instruction_set['sub']:
        pass
    elif instr == instruction_set['div']:
        pass
    elif instr == instruction_set['mul']:
        pass
    elif instr == instruction_set['mod']:
        pass
    elif instr == instruction_set['inc']:
        pass
    elif instr == instruction_set['or']:
        pass
    elif instr == instruction_set['and']:
        pass
    elif instr == instruction_set['not']:
        pass
    elif instr == instruction_set['xor']:
        pass
    elif instr == instruction_set['pushaddr']:
        instr_pointer += 1
        address = int(lines[instr_pointer])
        stack.append(memory[address])
    elif instr == instruction_set['pushconst']:
        instr_pointer += 1
        instr = int(lines[instr_pointer])
        stack.append(instr)
    elif instr == instruction_set['pop']:
        pass
    elif instr == instruction_set['popaddr']:
        instr_pointer += 1
        address = int(lines[instr_pointer])
        memory[address] = stack.pop()      
    elif instr == instruction_set['jmp']:
        instr_pointer += 1
        pointer = int(lines[instr_pointer])
        instr_pointer = pointer - 1
    elif instr == instruction_set['jeq']:
        pass
    elif instr == instruction_set['jne']:
        pass
    elif instr == instruction_set['jlt']:
        pass
    elif instr == instruction_set['jgt']:
        pass
    elif instr == instruction_set['int']:
        instr_pointer += 1
        interrupt_nr = int(lines[instr_pointer])
        if interrupt_nr == 1:
            print stack.pop()
    else:
        print "unknown instruciton: " + hex(int(instr))
                                            
    instr_pointer += 1