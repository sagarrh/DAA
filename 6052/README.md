# Modified 6502 Assembler

This project provides a custom assembler for a 6502-style instruction set. It translates assembly language into machine code, supporting various addressing modes and a full set of 6502-inspired opcodes.

## Features

- Supports all standard 6502 addressing modes
- Full set of 6502-inspired opcodes
- Generates both binary and hexadecimal output
- Includes example assembly programs

## Installation

1. Clone this repository:

git clone https://github.com/sagarr/6052

2. Navigate to the project directory:

cd 6052

3. Install required packages:

pip install -r requirements.txt

## Usage

To assemble a file:

python run_assembler.py examples/simple_add.asm

This will generate both `.bin` and `.hex` files in the `output/` directory.

## Running Tests

To run the test suite:
python -m unittest tests/test_assembler.py


## Examples

Check the `examples/` directory for sample assembly programs.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
.


