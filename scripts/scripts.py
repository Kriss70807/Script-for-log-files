"""
Содержит:
- функцию для получения данных лог-файлов (get_log_file_data);
- класс для работы с лог-файлами (LogData);
"""

from email.policy import default
import json
import re
from typing import Any

from tabulate import tabulate


REPORT_AVERAGE: str = "average"
HEADERS_REPORT_AVERAGE: list[str] = ["", "handler", "total", "avg_response_time"]


def get_log_file_data(log_files: tuple[str], date: str | None) -> list[dict[str, Any]]:
    data_logs: list[dict[str, Any]] = list()

    for log_file in log_files:
        with open(file=log_file, mode="r", encoding="utf-8") as log:
            for row in log:
                if row != "":
                    row: dict[str, str | float] = json.loads(row)

                    # ???ЕСЛИ ЭТО ВДРУГ ВАЖНО???
                    # ТОГДА СНАЧАЛА if row["status"] == 200: И ТОЛЬКО ПОТОМ ОСТАЛЬНОЕ

                    if date and row["@timestamp"][:10] != date:
                        continue

                    cropped_row: dict[str, str | float] = {
                        "date": row["@timestamp"][:10],
                        "handler": row["url"],
                        "response_time": row["response_time"],
                        "user_agent": row["http_user_agent"],
                    }

                    data_logs.append(cropped_row)

    return data_logs


def get_report_data(data_logs: list[dict[str, Any]]) -> list[list[str | int | float]]:
    total_data: dict[str, int] = dict()
    time_data: dict[str, float] = dict()
    for data_log in data_logs:
        key: str = data_log["handler"]
        total_data[key] = total_data.setdefault(key, 0) + 1
        time_data[key] = (
            time_data.setdefault(key, 0.0) + data_log["response_time"]
        )

    processed_data: list[list[str | int | float]] = list()
    for key, value in time_data.items():
        processed_data.append([key, total_data[key], value / total_data[key]])

    return sorted(processed_data, key=lambda pd: pd[1], reverse=True)


class LogData:
    def __init__(
        self, log_files: tuple[str], report: str, date: str | None = None
    ) -> None:
        self.__data_logs: list[dict[str, Any]] = get_log_file_data(
            log_files=log_files, date=date
        )
        self.__report_method: str = report

    def get_average_report(self):
        if self.__report_method == REPORT_AVERAGE:
            self.report: list[list[str | int | float]] = get_report_data(
                self.__data_logs
            )
            return tabulate(
                tabular_data=self.report,
                headers=HEADERS_REPORT_AVERAGE,
                showindex="always",
                floatfmt=".3f",
                tablefmt='simple'
            )
