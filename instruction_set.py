
instruction_set = {
    # Arithmetic
    'add': 0x01,
    'sub': 0x02,
    'div': 0x03,
    'mul': 0x04,
    'mod': 0x05,
    'inc': 0x06,

    # Logic
    'or': 0x11,
    'and': 0x12,
    'not': 0x13,
    'xor': 0x14,

    # Stack
    'pushaddr': 0x21,
    'pushconst': 0x22,
    'pop': 0x23,
    'popaddr': 0x24,

    # Jumps
    'jmp': 0x31,
    'jeq': 0x32,
    'jne': 0x33,
    'jlt': 0x34,
    'jgt': 0x35,

    # Misc
    'int': 0x41,
}
