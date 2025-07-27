"""
Содержит пользовательские исключения на случай:
- отсутствия лог-файла в системе (LogFileNotExistError);
- ошибочного ввода условия report (ReportError);

"""


class LogFileNotExistError(FileNotFoundError):
    def __init__(self, log_file: str) -> None:
        self.message: str = f"Файл {log_file} не найден."

    def __str__(self) -> str:
        return (
            f"{self.message} Проверьте правильность ввода имени файла или пути к нему."
        )


class ReportError(ValueError):
    def __init__(self, report: str) -> None:
        self.message: str = f"{report} недопустимое значение для аргумента report."

    def __str__(self) -> str:
        return f"{self.message} Допустимое значение - average."


class DateError(ValueError):
    def __init__(self, date: str):
        self.message: str = f'Формат даты {date} недопустим.'
    
    def __str__(self) -> str:
        return f'{self.message} Допустимый формат даты - ГГГГ-ММ-ДД.'