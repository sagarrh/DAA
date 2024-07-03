#!/usr/bin/env python3
# modified_6502_assembler.py

"""
A comprehensive 6502-style assembler

This script processes assembly-like code with the following structure:

variable=value           ; Variable assignment

label:   INSTRUCTION ADDR; Labeled instruction and address
         INSTRUCTION ADDR; Instruction and address

Supported addressing modes:

         #value          ; immediate mode (8-bit value)
         @value          ; zero-page mode
         @value,X        ; zero-page X indexed
         @value,Y        ; zero-page Y indexed
         value           ; absolute
         value,X         ; absolute X indexed
         value,Y         ; absolute Y indexed
         {value}         ; indirect
         {value,X}       ; indirect, X indexed
         {value,Y}       ; indirect, Y indexed

Values and labels can be any Python expression, but must evaluate to an integer.
Numeric labels can be used to set the memory location for following instructions.
"""

from collections.abc import Callable
import re

# Custom exception for errors
class AssemblerError(Exception): pass

# Functions used in the creation of object code (used in the table below)
def BYTE_LOW(pc, value):
    return value & 0xff

def BYTE_HIGH(pc, value):
    return (value & 0xff00) >> 8

def RELATIVE_JUMP(pc, value):
    offset = value - (pc + 2)
    return offset & 0xff

# Table of 6502-style opcodes and supported addressing modes
opcodes_table = {
    'STORE' : {
        'immediate' :   [BYTE_LOW],
        },
    'ADD' : {
        'immediate' :   [0x69, BYTE_LOW],
        'zeropage' :    [0x65, BYTE_LOW],
        'zeropage_x' :  [0x75, BYTE_LOW],
        'absolute' :    [0x6D, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0x7D, BYTE_LOW, BYTE_HIGH],
        'absolute_y' :  [0x79, BYTE_LOW, BYTE_HIGH],
        'indirect_x' :  [0x61, BYTE_LOW],
        'indirect_y' :  [0x71, BYTE_LOW],
        },
    'AND' : {
        'immediate' :   [0x29, BYTE_LOW],
        'zeropage' :    [0x25, BYTE_LOW],
        'zeropage_x' :  [0x35, BYTE_LOW],
        'absolute' :    [0x2D, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0x3D, BYTE_LOW, BYTE_HIGH],
        'absolute_y' :  [0x39, BYTE_LOW, BYTE_HIGH],
        'indirect_x' :  [0x21, BYTE_LOW],
        'indirect_y' :  [0x31, BYTE_LOW],
        },
    'ASL' : {
        'accumulator' : [0x0a],
        'zeropage' :    [0x06, BYTE_LOW],
        'zeropage_x' :  [0x16, BYTE_LOW],
        'absolute' :    [0x0e, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0x1e, BYTE_LOW, BYTE_HIGH],
        },
    'BIT' : {
        'zeropage' :    [0x24, BYTE_LOW],
        'absolute' :    [0x2c, BYTE_LOW, BYTE_HIGH],
       },
    'BRANCH_PLUS' : {
        'immediate' :   [0x10, BYTE_LOW],
        'absolute' :    [0x10, RELATIVE_JUMP],
        },
    'BRANCH_MINUS' : {
        'immediate' :   [0x30, BYTE_LOW],
        'absolute' :    [0x30, RELATIVE_JUMP],
        },
    'BRANCH_OVERFLOW_CLEAR' : {
        'immediate' :   [0x50, BYTE_LOW],
        'absolute' :    [0x50, RELATIVE_JUMP],
        },
    'BRANCH_OVERFLOW_SET' : {
        'immediate' :   [0x70, BYTE_LOW],
        'absolute' :    [0x70, RELATIVE_JUMP],
        },
    'BRANCH_CARRY_CLEAR' : {
        'immediate' :   [0x90, BYTE_LOW],
        'absolute' :    [0x90, RELATIVE_JUMP],
        },
    'BRANCH_CARRY_SET' : {
        'immediate' :   [0xb0, BYTE_LOW],
        'absolute' :    [0xb0, RELATIVE_JUMP],
        },
    'BRANCH_NOT_EQUAL' : {
        'immediate' :   [0xd0, BYTE_LOW],
        'absolute' :    [0xd0, RELATIVE_JUMP],
        },
    'BRANCH_EQUAL' : {
        'immediate' :   [0xf0, BYTE_LOW],
        'absolute' :    [0xf0, RELATIVE_JUMP],
        },
    'BREAK' : {
        'accumulator' : [0x00],
        'immediate' :   [0x00, BYTE_LOW],
        },
    'COMPARE' : {
        'immediate' :   [0xc9, BYTE_LOW],
        'zeropage' :    [0xc5, BYTE_LOW],
        'zeropage_x' :  [0xd5, BYTE_LOW],
        'absolute' :    [0xcD, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0xdD, BYTE_LOW, BYTE_HIGH],
        'absolute_y' :  [0xd9, BYTE_LOW, BYTE_HIGH],
        'indirect_x' :  [0xc1, BYTE_LOW],
        'indirect_y' :  [0xd1, BYTE_LOW],
        },
    'COMPARE_X' : {
        'immediate' :   [0xe0, BYTE_LOW],
        'zeropage' :    [0xe4, BYTE_LOW],
        'absolute' :    [0xec, BYTE_LOW, BYTE_HIGH],
        },
    'COMPARE_Y' : {
        'immediate' :   [0xc0, BYTE_LOW],
        'zeropage' :    [0xc4, BYTE_LOW],
        'absolute' :    [0xcc, BYTE_LOW, BYTE_HIGH],
        },
    'DECREMENT' : {
        'zeropage' :    [0xc6, BYTE_LOW],
        'zeropage_x' :  [0xd6, BYTE_LOW],
        'absolute' :    [0xce, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0xde, BYTE_LOW, BYTE_HIGH],
        },
    'XOR' : {
        'immediate' :   [0x49, BYTE_LOW],
        'zeropage' :    [0x45, BYTE_LOW],
        'zeropage_x' :  [0x55, BYTE_LOW],
        'absolute' :    [0x4D, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0x5D, BYTE_LOW, BYTE_HIGH],
        'absolute_y' :  [0x59, BYTE_LOW, BYTE_HIGH],
        'indirect_x' :  [0x41, BYTE_LOW],
        'indirect_y' :  [0x51, BYTE_LOW],
        },
    'CLEAR_CARRY' : {
        'accumulator' : [0x18],
        },
    'SET_CARRY' : {
        'accumulator' : [0x38],
        },
    'CLEAR_INTERRUPT' : {
        'accumulator' : [0x58],
        },
    'SET_INTERRUPT' : {
        'accumulator' : [0x78],
        },
    'CLEAR_OVERFLOW' : {
        'accumulator' : [0xb8],
        },
    'CLEAR_DECIMAL' : {
        'accumulator' : [0xd8],
        },
    'SET_DECIMAL' : {
        'accumulator' : [0xf8],
        },
    'INCREMENT' : {
        'zeropage' :    [0xe6, BYTE_LOW],
        'zeropage_x' :  [0xf6, BYTE_LOW],
        'absolute' :    [0xee, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0xfe, BYTE_LOW, BYTE_HIGH],
        },
    'JUMP' : {
        'absolute' :    [0x4c, BYTE_LOW, BYTE_HIGH],
        'indirect' :    [0x6c, BYTE_LOW, BYTE_HIGH]
        },
    'JUMP_SUBROUTINE' : {
        'absolute' :    [0x20, BYTE_LOW, BYTE_HIGH],
        },
    'LOAD_A' : {
        'immediate' :   [0xA9, BYTE_LOW],
        'zeropage' :    [0xA5, BYTE_LOW],
        'zeropage_x' :  [0xB5, BYTE_LOW],
        'absolute' :    [0xAD, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0xBD, BYTE_LOW, BYTE_HIGH],
        'absolute_y' :  [0xB9, BYTE_LOW, BYTE_HIGH],
        'indirect_x' :  [0xA1, BYTE_LOW],
        'indirect_y' :  [0xB1, BYTE_LOW],
        },
    'LOAD_X' : {
        'immediate' :   [0xa2, BYTE_LOW],
        'zeropage' :    [0xa6, BYTE_LOW],
        'zeropage_y' :  [0xb6, BYTE_LOW],
        'absolute' :    [0xae, BYTE_LOW, BYTE_HIGH],
        'absolute_y' :  [0xbe, BYTE_LOW, BYTE_HIGH],
        },
    'LOAD_Y' : { 
        'immediate' :   [0xa0, BYTE_LOW],
        'zeropage' :    [0xa4, BYTE_LOW],
        'zeropage_x' :  [0xb4, BYTE_LOW],
        'absolute' :    [0xac, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0xbc, BYTE_LOW, BYTE_HIGH],
        },
    'SHIFT_RIGHT' : {
        'accumulator' : [0x4a],
        'zeropage' :    [0x46, BYTE_LOW],
        'zeropage_x' :  [0x56, BYTE_LOW],
        'absolute' :    [0x4e, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0x5e, BYTE_LOW, BYTE_HIGH],
        },
    'NO_OP' : {
        'accumulator' : [0xea],
        },
    'OR' : {
        'immediate' :   [0x09, BYTE_LOW],
        'zeropage' :    [0x05, BYTE_LOW],
        'zeropage_x' :  [0x15, BYTE_LOW],
        'absolute' :    [0x0D, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0x1D, BYTE_LOW, BYTE_HIGH],
        'absolute_y' :  [0x19, BYTE_LOW, BYTE_HIGH],
        'indirect_x' :  [0x01, BYTE_LOW],
        'indirect_y' :  [0x11, BYTE_LOW],
        },
    'TRANSFER_A_X' : {
        'accumulator' : [0xaa],
        },
    'TRANSFER_X_A' : {
        'accumulator' : [0x8a],
        },
    'DECREMENT_X' : {
        'accumulator' : [0xca],
        },
    'INCREMENT_X' : {
        'accumulator' : [0xe8],
        },
    'TRANSFER_A_Y' : {
        'accumulator' : [0xa8],
        },
    'TRANSFER_Y_A' : {
        'accumulator' : [0x98],
        },
    'DECREMENT_Y' : {
        'accumulator' : [0x88],
        },
    'INCREMENT_Y' : {
        'accumulator' : [0xc8],
        },
    'ROTATE_LEFT' : {
        'accumulator' : [0x2a],
        'zeropage' :    [0x26, BYTE_LOW],
        'zeropage_x' :  [0x36, BYTE_LOW],
        'absolute' :    [0x2e, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0x3e, BYTE_LOW, BYTE_HIGH],
        },
    'ROTATE_RIGHT' : {
        'accumulator' : [0x6a],
        'zeropage' :    [0x66, BYTE_LOW],
        'zeropage_x' :  [0x76, BYTE_LOW],
        'absolute' :    [0x6e, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0x7e, BYTE_LOW, BYTE_HIGH],
        },
    'RETURN_INTERRUPT' : {
        'accumulator' : [0x40],
        },
    'RETURN_SUBROUTINE' : {
        'accumulator' : [0x60],
        },
    'SUBTRACT' : {
        'immediate' :   [0xe9, BYTE_LOW],
        'zeropage' :    [0xe5, BYTE_LOW],
        'zeropage_x' :  [0xf5, BYTE_LOW],
        'absolute' :    [0xeD, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0xfD, BYTE_LOW, BYTE_HIGH],
        'absolute_y' :  [0xf9, BYTE_LOW, BYTE_HIGH],
        'indirect_x' :  [0xe1, BYTE_LOW],
        'indirect_y' :  [0xf1, BYTE_LOW],
        },
    'STORE_A' : {
        'zeropage' :    [0x85, BYTE_LOW],
        'zeropage_x' :  [0x95, BYTE_LOW],
        'absolute' :    [0x8D, BYTE_LOW, BYTE_HIGH],
        'absolute_x' :  [0x9D, BYTE_LOW, BYTE_HIGH],
        'absolute_y' :  [0x99, BYTE_LOW, BYTE_HIGH],
        'indirect_x' :  [0x81, BYTE_LOW],
        'indirect_y' :  [0x91, BYTE_LOW],
        },
    'TRANSFER_X_STACK' : {
        'accumulator' : [0x9a],
        },
    'TRANSFER_STACK_X' : {
        'accumulator' : [0xba],
        },
    'PUSH_A' : {
        'accumulator' : [0x48],
        },
    'PULL_A' : {
        'accumulator' : [0x68],
        },
    'PUSH_STATUS' : {
        'accumulator' : [0x08],
        },
    'PULL_STATUS' : {
        'accumulator' : [0x28],
        },
    'STORE_X' : {
        'zeropage' :    [0x86, BYTE_LOW],
        'zeropage_y' :  [0x96, BYTE_LOW],
        'absolute' :    [0x8e, BYTE_LOW, BYTE_HIGH],
        },
    'STORE_Y' : {
        'zeropage' :    [0x84, BYTE_LOW],
        'zeropage_x' :  [0x94, BYTE_LOW],
        'absolute' :    [0x8c, BYTE_LOW, BYTE_HIGH],
        },
    }

# Parse address modes for various 6502-style instructions
def parse_addressing_mode(mode):
    # Accumulator or implicit. Example: INCREMENT
    if not mode or mode == 'A':    return ("accumulator","0")  

    # Immediate value. Example : LOAD_A #13  
    if mode.startswith("#"):       return ("immediate", mode[1:]) 

    # Strip unneeded whitespace if not an immediate value
    mode = mode.replace(' ','')

    # Zero-page address with indexing. Example : LOAD_A @25, X
    if mode.startswith("@"):
        if mode.endswith(",X"):    return ("zeropage_x", mode[1:-2])
        elif mode.endswith(",Y"):  return ("zeropage_y", mode[1:-2])
        else:                      return ("zeropage", mode[1:])

    # Indirect addressing. Example : LOAD_A {0xFF00, X}
    if mode.startswith("{"):   
        if mode.endswith(",X}"):   return ("indirect_x", mode[1:-3])
        elif mode.endswith(",Y}"): return ("indirect_y", mode[1:-3])
        elif mode.endswith("}"):   return ("indirect", mode[1:-1])

    # Absolute address, with indexing. Example : LOAD_A 0xFF00, X
    if mode.endswith(",X"):        return ("absolute_x", mode[:-2])
    elif mode.endswith(",Y"):      return ("absolute_y", mode[:-2])
    else:                          return ("absolute", mode)

# Parse an opcode line into intermediate object code. Returns a tuple
# (value, objcode) where value is a string to be evaluated in the 2nd pass
def parse_opcode(line):
    fields = line.split(None,1)
    opcode = fields[0]
    arg = fields[1] if len(fields) == 2 else ""
    mode, value = parse_addressing_mode(arg)
    opcode_modes = opcodes_table.get(opcode)
    if not opcode_modes:
        raise AssemblerError(f"Unknown opcode '{opcode}'")
    objcode = opcode_modes.get(mode)
    if not objcode:
        raise AssemblerError(f"Invalid addressing mode '{arg}' for opcode {opcode}")
    return (value, list(objcode))

# Takes a sequence of lines and strip comments and blanks
def clean_lines(lines):
    for line in lines:
        comment_index = line.find(";")
        if comment_index >= 0:
            line = line[:comment_index]
        line = line.strip()
        if line:  # only yield non-empty lines
            yield line

assignment_pattern = re.compile(r'(\s*)([a-zA-Z_][a-zA-Z0-9_]*)(\s*=)')

# Parse lines into intermediate object code
def process_lines(lines, symbols):
    for line_num, line in enumerate(lines, 1):
        if assignment_pattern.match(line):
            exec(line, symbols)
        else:
            label, *colon, statement = line.rpartition(":")
            try:
                yield line_num, label, parse_opcode(statement) if statement else (None, None)
            except AssemblerError as e:
                print(f"{line_num:4d} : Error : {e}")

# Assemble a sequence of lines into binary
def asm(lines, pc=0):
    objcode = []
    symbols = {}
    symbols['HIGH'] = lambda x : (x & 0xff00) >> 8
    symbols['LOW'] = lambda x : x & 0xff

    # Pass 1 : Parse instructions and create intermediate code
    for line_num, label, (value, icode) in process_lines(lines, symbols):
        # Try to evaluate numeric labels and set the PC
        if label:
            try:
                pc = int(eval(label, symbols))
            except (ValueError, NameError):
                symbols[label] = pc

        # Store the resulting objcode for later expansion
        if icode:
            objcode.append((line_num, pc, value, icode))
            pc += len(icode)

    # Pass 2 : Create final object code by evaluating expressions
    final_code = []
    for line_num, pc, value, icode in objcode:
        # Evaluate the value string
        try:
            symbols['PC'] = pc
            real_value = eval(value, symbols)
            if isinstance(real_value, str):
                real_value = ord(real_value) & 0xff
            if not isinstance(real_value, int):
                raise TypeError(f"Integer expected in {value}")
        except Exception as e:
            print(f"{line_num:4d} : Error : {e}", file=sys.stderr)
            real_value = 0
        ecode = [op(pc, real_value) if isinstance(op, Callable) else op
                 for op in icode]
        final_code.append((line_num, pc, ecode))
    return final_code

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print(f"Usage {sys.argv[0]} input_file.asm", file=sys.stderr)
        raise SystemExit(1)
    lines = clean_lines(open(sys.argv[1]))
    for line_num, pc, opcode in asm(lines):
        print(f"{pc:04x} : {' '.join(format(op, '02x') for op in opcode)}")