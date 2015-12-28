import sys

from instruction_set import instruction_set


def run(path):
    f = file(path)
    lines = f.readlines()
    f.close()

    stack = []
    memory = {}
    instr_pointer = 0

    while True:
        if instr_pointer >= len(lines):
            break
        instr = int(lines[instr_pointer])

        if instr == instruction_set['add']:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif instr == instruction_set['sub']:
            a = stack.pop()
            b = stack.pop()
            stack.append(a - b)
        elif instr == instruction_set['div']:
            a = stack.pop()
            b = stack.pop()
            stack.append(a / b)
        elif instr == instruction_set['mul']:
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif instr == instruction_set['mod']:
            a = stack.pop()
            b = stack.pop()
            stack.append(a % b)
        elif instr == instruction_set['inc']:
            value = stack.pop
            value += 1
            stack.append(value)
        elif instr == instruction_set['or']:
            a = stack.pop()
            b = stack.pop()
            stack.append(a | b)
        elif instr == instruction_set['and']:
            a = stack.pop()
            b = stack.pop()
            stack.append(a & b)
        elif instr == instruction_set['not']:
            value = stack.pop()
            stack.append(~value)
        elif instr == instruction_set['xor']:
            a = stack.pop()
            b = stack.pop()
            stack.append(a ^ b)
        elif instr == instruction_set['pushaddr']:
            instr_pointer += 1
            address = int(lines[instr_pointer])
            stack.append(memory[address])
        elif instr == instruction_set['pushconst']:
            instr_pointer += 1
            instr = int(lines[instr_pointer])
            stack.append(instr)
        elif instr == instruction_set['pop']:
            stack.pop()
        elif instr == instruction_set['popaddr']:
            instr_pointer += 1
            address = int(lines[instr_pointer])
            memory[address] = stack.pop()
        elif instr == instruction_set['jmp']:
            instr_pointer += 1
            pointer = int(lines[instr_pointer])
            instr_pointer = pointer - 1
        elif instr == instruction_set['jeq']:
            instr_pointer += 1
            a = stack.pop()
            b = stack.pop()
            if a == b:
                pointer = int(lines[instr_pointer])
                instr_pointer = pointer - 1
        elif instr == instruction_set['jne']:
            instr_pointer += 1
            a = stack.pop()
            b = stack.pop()
            if a != b:
                pointer = int(lines[instr_pointer])
                instr_pointer = pointer - 1
        elif instr == instruction_set['jlt']:
            instr_pointer += 1
            a = stack.pop()
            b = stack.pop()
            if a < b:
                pointer = int(lines[instr_pointer])
                instr_pointer = pointer - 1
        elif instr == instruction_set['jgt']:
            instr_pointer += 1
            a = stack.pop()
            b = stack.pop()
            if a > b:
                pointer = int(lines[instr_pointer])
                instr_pointer = pointer - 1
        elif instr == instruction_set['int']:
            instr_pointer += 1
            interrupt_nr = int(lines[instr_pointer])
            if interrupt_nr == 1:
                print stack.pop()
        else:
            print "unknown instruciton: " + hex(int(instr))

        instr_pointer += 1

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python compiler.py <asm file>'
        exit(1)

    run(sys.argv[1])
