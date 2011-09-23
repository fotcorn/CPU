
instruction_set = {}

#Arithmetic
instruction_set['add'] = 0x01
instruction_set['sub'] = 0x02
instruction_set['div'] = 0x03
instruction_set['mul'] = 0x04
instruction_set['mod'] = 0x05
instruction_set['inc'] = 0x06

# Logic
instruction_set['or'] = 0x11
instruction_set['and'] = 0x12
instruction_set['not'] = 0x13
instruction_set['xor'] = 0x14

# Stack
instruction_set['pushaddr'] = 0x21
instruction_set['pushconst'] = 0x22
instruction_set['pop'] = 0x23
instruction_set['popaddr'] = 0x24

# Jumps
instruction_set['jmp'] = 0x31
instruction_set['jeq'] = 0x32
instruction_set['jne'] = 0x33
instruction_set['jlt'] = 0x34
instruction_set['jgt'] = 0x35

# Misc
instruction_set['int'] = 0x41
