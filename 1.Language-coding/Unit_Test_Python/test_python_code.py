import unittest
from Unit_Test_Python.working_student import WorkingStudent
from Unit_Test_Python.calculator import Calculator


class TestWorkingStudent(unittest.TestCase):
    """Test cases """

    def test_get_age(self):
        """ This test case will test get_age"""
        obj = WorkingStudent("suman", "banjerjee", "22-05-2020", 100)
        self.assertEqual(obj.get_age()[0], 1, "Year should be one")
        self.assertEqual(obj.get_age()[1], 2, "Months should be two")

    def test_increase_pay(self):
        """ This test case will test increae_pay"""
        obj = WorkingStudent("suman", "banjerjee", "22-05-2020", 100)
        self.assertEqual(obj.increase_pay(5), 105.0)

    def test_get_full_name(self):
        """ This test case will test get_full_name"""
        obj = WorkingStudent("suman", "banerjee", "22-05-2020", 100)
        self.assertEqual(obj.get_full_name(), "Suman Banerjee")

        obj = WorkingStudent("Rohit", "Roy", "22-05-2020", 100)
        self.assertEqual(obj.get_full_name(), "Rohit Roy")

    def test_division(self):
        c = Calculator()
        with self.assertRaises(ZeroDivisionError):
            c.divide(12, 0)
