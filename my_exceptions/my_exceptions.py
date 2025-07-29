"""
Содержит пользовательские исключения на случай:
- отсутствия лог-файла в системе (LogFileNotExistError);
- ошибочного ввода условия report (ReportError);
- ошибочного ввода условия date (DateError).
"""


class LogFileNotExistError(FileNotFoundError):
    """
    Исключение для обработки тех случаев, когда файла с конкретным именем
    нет в системе, либо когда пользователь неверно его указал.
    """

    def __init__(self, log_file: str) -> None:
        self.message: str = f"Файл {log_file} не найден."

    def __str__(self) -> str:
        return (
            f"{self.message} Проверьте правильность ввода имени файла или пути к нему."
        )


class ReportError(ValueError):
    """
    Исключение для обработки тех случаев, когда пользователь передал неверное
    значение в аргумент report.
    """

    def __init__(self, report: str) -> None:
        self.message: str = f"{report} недопустимое значение для аргумента report."

    def __str__(self) -> str:
        return f"{self.message} Допустимое значение - average."


class DateError(ValueError):
    """
    Исключение для обработки тех случаев, когда пользователь передал неверное
    значение в аргумент date.
    """

    def __init__(self, date: str) -> None:
        self.message: str = f"Формат даты {date} недопустим."

    def __str__(self) -> str:
        return f"{self.message} Допустимый формат даты - ГГГГ-ДД-ММ."
