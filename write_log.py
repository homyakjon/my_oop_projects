from datetime import datetime


class Writer:
    FILE_PATH = 'add_string.csv'

    @classmethod
    def write(cls, new_string, file_path=None):
        if file_path is None:
            file_path = cls.FILE_PATH
        with open(file_path, 'a') as file:
            file.write(f"{new_string}\n")


class Logger:
    @classmethod
    def write(cls, exception: Exception, file_path=None):
        error_number = len(cls.get_errors(file_path)) + 1
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        error_class = exception.__class__.__name__
        error_message = str(exception)
        log_entry = f"{error_number}, {timestamp}, {error_class}, {error_message}"

        Writer.write(log_entry, file_path)

    @staticmethod
    def get_errors(file_path=None):
        if file_path is None:
            file_path = Writer.FILE_PATH

        try:
            with open(file_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []


def logger(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            Logger.write(e)
            raise e

    return wrapper
