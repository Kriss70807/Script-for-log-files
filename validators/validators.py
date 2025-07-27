"""
Содержит функции валидации для:
- проверки существования файлов в системе (files_exists);
- проверки правильности ввода условия report (report_validation);

"""

from os.path import exists
import re
from typing import Any

from my_exceptions.my_exceptions import LogFileNotExistError, ReportError, DateError


DATE_PATTERN = r'\d{4}-\d{2}-\d{2}'


def files_exists(log_files: list[str]) -> True | LogFileNotExistError:
    for log_file in log_files:
        if not exists(log_file):
            raise LogFileNotExistError(log_file)
    return True


def report_validation(report: str) -> None | ReportError:
    if report.lower().strip() != "average":
        raise ReportError(report)


def date_validation(date: str) -> None | DateError:
    if re.fullmatch(DATE_PATTERN, date) is None:
        raise DateError(date)
