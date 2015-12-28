from instruction_set import instruction_set
import re
import sys

REGEX_INSTR_NO_ARG = '\s*([a-z]+).*'
REGEX_INSTR_STR_ARG = '\s*([a-z]+)\s+([\.\$][a-z]+).*'
REGEX_INSTR_ADDR_ARG = '\s*([a-z]+)\s+\#([0-9]+).*'
REGEX_INSTR_NUM_ARG = '\s*([a-z]+)\s+([0-9]+).*'
REGEX_LABEL = '\s*(\.[a-z]+).*'


def compile_file(path):
    print path
    fin = file(path, 'r')
    lines = fin.readlines()
    fin.close()

    if path.endswith('.asm'):
        output_path = path.replace('asm', 'bin')
    else:
        output_path = path + '.asm'
    print output_path
    fout = file(output_path, 'w')

    program = []
    for line in lines:
        match = re.match(REGEX_INSTR_STR_ARG, line)
        if match is not None:
            t = (instruction_set[match.group(1)], match.group(2))
            program.append(t)
            continue
        match = re.match(REGEX_INSTR_ADDR_ARG, line)
        if match is not None:
            t = (instruction_set[match.group(1)], int(match.group(2)))
            program.append(t)
            continue
        match = re.match(REGEX_INSTR_NUM_ARG, line)
        if match is not None:
            t = (instruction_set[match.group(1)], int(match.group(2)))
            program.append(t)
            continue
        match = re.match(REGEX_LABEL, line)
        if match is not None:
            program.append(match.group(1))
            continue
        match = re.match(REGEX_INSTR_NO_ARG, line)
        if match is not None:
            t = (instruction_set[match.group(1)])
            program.append(t)

    # search labels
    labels = {}
    cleaned_program = []
    instr_pointer = 0
    for instr in program:
        if isinstance(instr, basestring):
            labels[instr] = instr_pointer
        elif isinstance(instr, int):
            cleaned_program.append(instr)
            instr_pointer += 1
        else:
            cleaned_program.append(instr)
            instr_pointer += 2

    variables = {}
    instructions = []

    for instr in cleaned_program:
        if isinstance(instr, int):  # instruction without argument
            instructions.append(instr)
        else:
            instructions.append(instr[0])
            if isinstance(instr[1], int):  # instruction with hardcoded values, e.g. pushconst
                instructions.append(instr[1])
            else:
                if instr[1].startswith('$'):
                    if instr[1] not in variables:
                        pointer = 4000 + len(variables)
                        variables[instr[1]] = pointer
                        instructions.append(pointer)
                    else:
                        instructions.append(variables[instr[1]])
                elif instr[1].startswith('.'):
                    instructions.append(labels[instr[1]])
        instr_pointer += 1

    for data in instructions:
        fout.write(str(data) + '\n')

    fout.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python compiler.py <asm file>'
        exit(1)

    compile_file(sys.argv[1])
