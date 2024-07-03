import sys
from src.asm import asm, clean_lines
import os

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file.asm", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    base_name = os.path.splitext(os.path.basename(input_file))[0]

    # Read the entire file content
    with open(input_file, 'r') as f:
        file_content = f.read()

    # Process the lines
    lines = clean_lines(file_content.splitlines())

    # Assemble the code
    assembled_code = asm(lines)

    # Create binary output
    binary_output = bytearray()
    for _, _, opcode in assembled_code:
        binary_output.extend(opcode)

    # Ensure the output directory exists
    os.makedirs('output', exist_ok=True)

    # Write binary output
    with open(f"output/{base_name}.bin", 'wb') as f:
        f.write(binary_output)

    # Write hex output
    with open(f"output/{base_name}.hex", 'w') as f:
        for line_num, pc, opcode in assembled_code:
            hex_str = ' '.join(f'{op:02x}' for op in opcode)
            f.write(f"{pc:04x}: {hex_str}\n")

    print(f"Assembly complete. Output written to output/{base_name}.bin and output/{base_name}.hex")

if __name__ == "__main__":
    main()