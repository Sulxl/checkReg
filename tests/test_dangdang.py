from unittest import TestCase
import unittest
from src.checkreg import dangdang


class Test(TestCase):
    def test_check_phone(self):
        phone = '971547725729'
        result = dangdang.check_phone(phone)
        self.assertEqual(result['if_exist'], False)
    


if __name__ == '__main__':
    unittest.main()
