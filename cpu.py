from instruction_set import instruction_set

instr_set = {}

for key, value in instruction_set.items():
    instr_set[value] = key
    
f = file('input/program.bin')
lines = f.readlines()
f.close()

stack = []


for i in range(0, len(lines)):
    line = lines[i]
    
    if line == instr_set['add']:
        pass    
    elif line == instr_set['sub']:
        pass
    elif line == instr_set['div']:
        pass
    elif line == instr_set['mul']:
        pass
    elif line == instr_set['mod']:
        pass
    elif line == instr_set['inc']:
        pass
    elif line == instr_set['or']:
        pass
    elif line == instr_set['and']:
        pass
    elif line == instr_set['not']:
        pass
    elif line == instr_set['xor']:
        pass
    elif line == instr_set['pushaddr']:
        pass
    elif line == instr_set['pushconst']:
        pass
    elif line == instr_set['pop']:
        pass
    elif line == instr_set['popaddr']:
        pass
    elif line == instr_set['jmp']:
        pass
    elif line == instr_set['jeq']:
        pass
    elif line == instr_set['jne']:
        pass
    elif line == instr_set['jlt']:
        pass
    elif line == instr_set['jgt']:
        pass
    elif line == instr_set['int']:
        pass