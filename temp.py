from classes.Inquirer import Inquirer
import unittest


class Test(unittest.TestCase):
    def test_prompt_list(self):
        message = "how old are you"
        choices = [11, 22, 33]
        result_answer = Inquirer.promot_list(message, choices)
        self.assertEqual(result_answer, 11)

    def test_prompt_text(self):
        message = "how old are you"
        result_answer = Inquirer.prompt_text(message)
        self.assertEqual(result_answer, '11')

    def test_prompt_confirm(self):
        message = "are you 11 years old"
        result_answer = Inquirer.prompt_confirm(message)
        self.assertEqual(result_answer, True)


if __name__ == '__main__':
    unittest.main()
