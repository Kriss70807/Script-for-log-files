"""
Считывание данных log-файлов и формирование отчёта со списком
эндпоинтов, количеством запросов по каждому эндпоинту и средним
временем ответа.

Вызывается из терминала командой
    python main.py --file <полный путь/имена файлов> --report avarage
"""

from scripts.scripts import LogData
from validators.validators import files_exists, report_validation, date_validation


def get_report_on_log_files(
    *log_files: tuple[str], report: str = "average", date: str | None = None
) -> None:

    # Проверяем существование файлов в системе
    # и валидность аргументов report и date
    files_exists(log_files=log_files)
    report_validation(report=report)
    if date:
        date_validation(date)

    # Создаём объект LogData для работы с лог файлами
    data_logs = LogData(log_files=log_files, report=report, date=date)

    # Формируем и возвращаем отчёт по данным лог файлов
    print(data_logs.get_average_report())


if __name__ == "__main__":
    get_report_on_log_files("example1.log", "example2.log", report="average")
