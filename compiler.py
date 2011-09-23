from instruction_set import instruction_set
import re

REGEX_INSTR_NO_ARG =    '\s*([a-z]+).*'
REGEX_INSTR_STR_ARG =  '\s*([a-z]+)\s+([\.\$][a-z]+).*'
REGEX_INSTR_ADDR_ARG =  '\s*([a-z]+)\s+\#([0-9]+).*'
REGEX_INSTR_NUM_ARG = '\s*([a-z]+)\s+([0-9]+).*'
REGEX_LABEL =           '\s*(\.[a-z]+).*'



fin = file('input/program.asm', 'r')
lines = fin.readlines()
fin.close()

fout = file('input/program.bin', 'w')


program = []
for line in lines:
	match  = re.match(REGEX_INSTR_STR_ARG, line)
	if match is not None:
		tuple = (instruction_set[match.group(1)], match.group(2))
		program.append(tuple)
		continue
	match  = re.match(REGEX_INSTR_ADDR_ARG, line)
	if match is not None:
		tuple = (instruction_set[match.group(1)], int(match.group(2)))
		program.append(tuple)
		continue
	match  = re.match(REGEX_INSTR_NUM_ARG, line)
	if match is not None:
		tuple = (instruction_set[match.group(1)], int(match.group(2)))
		program.append(tuple)
		continue
	match  = re.match(REGEX_LABEL, line)
	if match is not None:
		program.append(match.group(1))
		continue
	match  = re.match(REGEX_INSTR_NO_ARG, line)
	if match is not None:
		tuple = (instruction_set[match.group(1)])
		program.append(instruction_set[match.group(1)])

# search labels
labels = {}
cleaned_program = []
instr_pointer = 0
for instr in program:
	if isinstance(instr, basestring):
		labels[instr] = instr_pointer
	else:
		cleaned_program.append(instr)
		instr_pointer += 1	



variables = {}
instructions = []

for instr in cleaned_program:
	if isinstance(instr, int):  # instruction without argument
		instructions.append(instr)
	else:
		instructions.append(instr[0])
		if isinstance(instr[1], int): # instruction with hardcoded values, e.g. pushconst
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