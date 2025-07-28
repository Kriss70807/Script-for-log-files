"""
Содержит:
- функцию для получения данных лог-файлов (get_log_file_data);
- класс для работы с лог-файлами (LogData);
"""

from abc import ABC, abstractmethod
import json
from tabulate import tabulate


class LogDataAnalyzer(ABC):
    """
    Абстрактный класс для работы с лог-файлами.

    Атрибуты:
     log_files (list): Список имён лог-файлов.
     report_method (str): Метод обработки данных лог-файлов.
     date_filter (str): Дата для фильтрации данных лог-файлов.
    Методы:
     get_log_files_data(): Возвращает данные лог-файлов в формате JSON.
     present_report(): Возвращает сведённые в таблицу обработанные данные лог-файлов.
     report(): Абстрактный метод для обработки лог-файлов (ДОЛЖЕН БЫТЬ ПЕРЕОПРЕДЕЛЁН В ДОЧЕРНИХ КЛАССАХ).
    """

    def __init__(
        self, log_files: list[str], report_method: str, date_filter: str | None = None
    ) -> None:
        self.log_files: list[str] = log_files
        self.report_method: str = report_method
        self.date_filter: str | None = date_filter

    def get_log_files_data(self) -> list[dict[str, str | int | float]]:
        """
        Возвращает данные лог-файлов в формате JSON.
        """
        data_logs: list[dict[str, str | int | float]] = list()
        for log_file in self.log_files:
            with open(file=log_file, mode="r", encoding="utf-8") as log:
                for row in log:
                    if row != "":
                        data_log: dict[str, str | float] = json.loads(row)
                        if (
                            self.date_filter
                            and row["@timestamp"][:10] != self.date_filter
                        ):
                            continue
                        data_logs.append(data_log)
        return data_logs

    def present_report(self, table, headers) -> str:
        """
        Возвращает сведённые в таблицу обработанные данные лог-файлов.
        """
        return tabulate(
            tabular_data=table,
            headers=headers,
            showindex="always",
            floatfmt=".3f",
            tablefmt="simple",
        )

    @abstractmethod
    def report(self) -> None:
        """
        Абстрактный метод для обработки лог-файлов (ДОЛЖЕН БЫТЬ ПЕРЕОПРЕДЕЛЁН В ДОЧЕРНИХ КЛАССАХ).
        """
        return None


class LogAvgReporter(LogDataAnalyzer):
    """
    Класс для работы с лог-файлами.

    Методы:
     report(): Переопределённый абстрактный метод родительского класса LogDataAnalyzer.
     Формирует данные со списком эндпоинтов, количеством запросов по каждому эндпоинту и
     средним временем ответа.
    """

    def report(self) -> str:
        """
        Переопределённый абстрактный метод родительского класса LogDataAnalyzer.
        
        Формирует данные со списком эндпоинтов, количеством запросов по каждому эндпоинту и
        средним временем ответа.
        """
        data_logs: list[dict[str, str | int | float]] = self.get_log_files_data()

        total_data: dict[str, int] = dict()
        time_data: dict[str, float] = dict()
        for data_log in data_logs:
            key: str = data_log["url"]
            total_data[key] = total_data.setdefault(key, 0) + 1
            time_data[key] = time_data.setdefault(key, 0.0) + float(
                data_log["response_time"]
            )

        processed_data: list[list[str | int | float]] = list()
        for key, value in time_data.items():
            processed_data.append([key, total_data[key], value / total_data[key]])
            processed_data.sort(key=lambda pd: pd[1], reverse=True)

        return self.present_report(
            table=processed_data, headers=["", "handler", "total", "avg_response_time"]
        )
