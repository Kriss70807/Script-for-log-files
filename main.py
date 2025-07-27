"""
Считывание данных log-файлов и формирование отчёта со списком
эндпоинтов, количеством запросов по каждому эндпоинту и средним
временем ответа.

Вызывается из терминала командой
    python main.py --file <полный путь/имена файлов> --report avarage
"""

import argparse

from scripts.scripts import LogAvgReporter
from validators.validators import files_exists, report_validation, date_validation


def get_report_on_log_files(
    *log_files: list[str], report: str = "average", date: str | None = None
) -> None:
    """
    Документация...
    """

    # Проверяем валидность аргументов report и date
    report_validation(report=report)
    if date:
        date_validation(date)

    # Создаём объект LogAvgReporter для работы с лог файлами
    if report == "average":
        data_logs = LogAvgReporter(
            log_files=log_files, report_method=report, date_filter=date
        )
        # Формируем и возвращаем отчёт по данным лог файлов
        data_logs.report()


if __name__ == "__main__":
    get_report_on_log_files("example1.log", "example2.log", report="average")

    # Создаём объект анализатора аргументов
    parser_object = argparse.ArgumentParser(
        add_help="Тут описание скрипта для обработы log файлов."
    )

    # Создаём пространство имён с именованными аргументами
    parser_object.add_argument(
        "--file", nargs="+", help="Имена log файлов или пути к ним", required=True
    )
    parser_object.add_argument(
        "--report", help="Тип отчёта по log файлам.", required=True
    )
    parser_object.add_argument(
        "--date",
        help="Значение даты по которой необходимо получить данные из log файлов.",
        default=None,
    )
    named_arguments = parser_object.parse_args()

    # Запускаем функцию get_formatted_table
    get_report_on_log_files(
        named_arguments.file, named_arguments.where, named_arguments.aggregate
    )
