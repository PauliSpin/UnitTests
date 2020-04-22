import unittest
from unittest.mock import patch
from employee import Employee


# class TestEmployee(unittest.TestCase):

#     def test_email(self):
#         # Create two employees giving their names and pay
#         emp_1 = Employee('Corey', 'Schafer', 50000)
#         emp_2 = Employee('Sue', 'Smith', 60000)
#         # Creation should already have set up the emails, so test for that
#         self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
#         self.assertEqual(emp_2.email, 'Sue.Smith@email.com')
#         # Change their first names
#         emp_1.first = 'John'
#         emp_2.first = 'Jane'
#         # Test if their emails have changed after changing their first names
#         self.assertEqual(emp_1.email, 'John.Schafer@email.com')
#         self.assertEqual(emp_2.email, 'Jane.Smith@email.com')

#     def test_fullname(self):
#         emp_1 = Employee('Corey', 'Schafer', 50000)
#         emp_2 = Employee('Sue', 'Smith', 60000)

#         self.assertEqual(emp_1.fullname, 'Corey Schafer')
#         self.assertEqual(emp_2.fullname, 'Sue Smith')

#         emp_1.first = 'John'
#         emp_2.first = 'Jane'
#         # Check that the fullnames change when the first names are altered
#         self.assertEqual(emp_1.fullname, 'John Schafer')
#         self.assertEqual(emp_2.fullname, 'Jane Smith')

#     def test_apply_raise(self):
#         emp_1 = Employee('Corey', 'Schafer', 50000)
#         emp_2 = Employee('Sue', 'Smith', 60000)

#         emp_1.apply_raise()
#         emp_2.apply_raise()
#         # Check that the raise of the pay worked
#         self.assertEqual(emp_1.pay, 52500)
#         self.assertEqual(emp_2.pay, 63000)


# if __name__ == '__main__':
#     unittest.main()

###### With Prints ######


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        # Using patch as a context manager,
        # want to mock the request.get and didn't import request into our test
        # since we want to test our request within the object
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()


###### setUpClass and tearDownClass ######

# @classmethod
# def setUpClass(cls):
#     print('setupClass')


# @classmethod
# def tearDownClass(cls):
#     print('teardownClass')


# ##### Mocking #####
# def monthly_schedule(self, month):
#     response = requests.get(f'http://company.com/{self.last}/{month}')
#     if response.ok:
#         return response.text
#     else:
#         return 'Bad Response!'
