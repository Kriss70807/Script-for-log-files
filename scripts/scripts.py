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
    Документация...
    """

    def __init__(
        self, log_files: list[str], report_method: str, date_filter: str | None = None
    ) -> None:
        self.log_files: list[str] = log_files
        self.report_method: str = report_method
        self.date_filter: str | None = date_filter

    def _get_log_files_data(self) -> list[dict[str, str | int | float]]:
        """
        Документация...
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

    def _present_report(self, table, headers) -> None:
        """
        Документация...
        """
        print(
            tabulate(
                tabular_data=table,
                headers=headers,
                showindex="always",
                floatfmt=".3f",
                tablefmt="simple",
            )
        )

    @abstractmethod
    def report(self) -> None:
        """
        Документация...
        """
        pass


class LogAvgReporter(LogDataAnalyzer):
    """
    Документация...
    """

    def report(self) -> None:
        """
        Документация...
        """
        data_logs: list[dict[str, str | int | float]] = self._get_log_files_data()

        total_data: dict[str, int] = dict()
        time_data: dict[str, float] = dict()
        for data_log in data_logs:
            key: str = data_log["url"]
            total_data[key] = total_data.setdefault(key, 0) + 1
            time_data[key] = time_data.setdefault(key, 0.0) + data_log["response_time"]

        processed_data: list[list[str | int | float]] = list()
        for key, value in time_data.items():
            processed_data.append([key, total_data[key], value / total_data[key]])
            processed_data.sort(key=lambda pd: pd[1], reverse=True)

        self._present_report(
            table=processed_data, headers=["", "handler", "total", "avg_response_time"]
        )
