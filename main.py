class LocalizationHelper:
    def __init__(self, language):
        self.language = language
        self.error_messages = {
            'en': {
                'invalid_input': 'Invalid input',
                'missing_required_field': 'Missing required field',
                'invalid_email': 'Invalid email',
                'invalid_password': 'Invalid password'
            },
            'ru': {
                'invalid_input': 'Некорректный ввод',
                'missing_required_field': 'Отсутствует обязательное поле',
                'invalid_email': 'Некорректный адрес электронной почты',
                'invalid_password': 'Некорректный пароль'
            },
            'uz': {
                'invalid_input': 'Noto\'g\'ri kirish',
                'missing_required_field': 'Talab qilinadigan maydon yo\'q',
                'invalid_email': 'Noto\'g\'ri elektron pochta',
                'invalid_password': 'Noto\'g\'ri parol'
            }
        }

    def get_error_message(self, error_code):
        return self.error_messages.get(self.language, {}).get(error_code, 'Unknown error')

# Misol:
localization_helper = LocalizationHelper('en')
print(localization_helper.get_error_message('invalid_input'))  # Chiqaradi: Invalid input
print(localization_helper.get_error_message('invalid_email'))  # Chiqaradi: Invalid email
print(localization_helper.get_error_message('unknown_error'))  # Chiqaradi: Unknown error
