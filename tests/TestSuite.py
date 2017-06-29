import unittest
import sys

sys.path.append("..")
from src.ExcelSheetColumn import ExcelSheetColumn


class TestSuite(unittest.TestCase):
    def test_excel_column_converter(self):
        converter = ExcelSheetColumn()
        self.assertEqual(converter.convert_to_title(1), "A")
        self.assertEqual(converter.convert_to_title(703), "AAA")
        self.assertEqual(converter.convert_to_index("A"), 1)
        self.assertEqual(converter.convert_to_index("AAA"), 703)


if __name__ == '__main__':
    unittest.main()
