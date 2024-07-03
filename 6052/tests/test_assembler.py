import unittest
from src.asm import asm, clean_lines

class TestAssembler(unittest.TestCase):
    def test_simple_add(self):
        asm_code = """
        LOAD_A #10
        ADD #5
        STORE_A @20
        BREAK
        """
        lines = clean_lines(asm_code.split('\n'))
        result = asm(lines)
        expected = [
            (1, 0, [0xA9, 0x0A]),
            (2, 2, [0x69, 0x05]),
            (3, 4, [0x85, 0x14]),
            (4, 6, [0x00])
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()