import unittest
from lab5 import Student, GradeBook, Payment, StudentAccount

class TestStudent(unittest.TestCase):

 def test_add_score(self):
    student = Student(1, "Ali", "ТИИ 25-21")
    student.add_score(80)
    student.add_score(90)
    self.assertEqual(student.average, 85)
def test_invalid_score(self):
    student = Student(1, "Ali", "ТИИ 25-21")
    with self.assertRaises(ValueError):
        student.add_score(150)

class TestGradeBook(unittest.TestCase):

 def test_register_student(self):
    book = GradeBook()
    student = Student(1, "Ali", "ТИИ 25-21")
    book.register(student)
    self.assertIs(book.find(1), student)

class TestPayment(unittest.TestCase):

 def test_valid_payment(self):
    payment = Payment("начисление", 10000)
    self.assertEqual(payment.amount, 10000)
def test_invalid_payment(self):
    with self.assertRaises(ValueError):
        Payment("начисление", -100)

class TestStudentAccount(unittest.TestCase):

 def test_charge_and_pay(self):
    account = StudentAccount("Ali")
    account.charge(10000)
    account.pay(3000)
    self.assertEqual(account.balance, 7000)

if __name__ == "__main__":
 unittest.main() 