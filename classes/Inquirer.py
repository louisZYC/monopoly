import inquirer
from inquirer import errors


class Inquirer:
    def promot_list(message='', choices=[]):
        questions = [
            inquirer.List('key', message=message, choices=choices,)
        ]
        answers = inquirer.prompt(questions)
        return answers['key']

    def prompt_text(message='', validate=None):
        if(validate == None):
            def validate(answers, current):
                return True

        questions = [
            inquirer.Text('key', message=message, validate=validate)
        ]
        answers = inquirer.prompt(questions)
        return answers['key']

    def prompt_confirm(message=''):

        questions = [
            inquirer.Confirm('key', message=message)
        ]
        answers = inquirer.prompt(questions)
        return answers['key']
