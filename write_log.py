from datetime import datetime


class Writer:
    def __init__(self, file_path='add_string.csv') -> None:
        self.file_path = file_path

    def write(self, new_string):
        with open(self.file_path, 'a') as file:
            file.write(f"{new_string}\n")


class Logger:
    def __init__(self, writer: Writer = None) -> None:
        self.writer = writer

    def write(self, exception: Exception):
        error_number = len(Logger.get_errors()) + 1
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        error_class = exception.__class__.__name__
        error_message = str(exception)
        log_entry = f"{error_number}\t{timestamp}\t{error_class}\t{error_message}"

        if self.writer:
            self.writer.write(log_entry)

    @staticmethod
    def get_errors():
        try:
            with open('add_string.csv', 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []


def logger(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            log_writer = Writer()
            log = Logger(log_writer)
            log.write(e)
            raise e

    return wrapper