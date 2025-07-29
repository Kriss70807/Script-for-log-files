import os
from typing import Generator
import pytest


NAMES_TEST_LOG_FILES: list[str] = [
    "test_log_file1.log",
    "test_log_file2.log",
    "test_log_file3.log",
]

TEST_LIST_DATA_LOGS_WITHOT_DATE_FILTER: list[dict[str, str]] = [
    {
        "url": "test_log_file1",
        "response_time": "1.0",
        "@timestamp": "2025-06-22T13:57:34+00:00",
    },
    {
        "url": "test_log_file1",
        "response_time": "1.0",
        "@timestamp": "2024-05-11T13:57:34+00:00",
    },
    {
        "url": "test_log_file2",
        "response_time": "2.0",
        "@timestamp": "2025-06-22T13:57:34+00:00",
    },
    {
        "url": "test_log_file2",
        "response_time": "2.0",
        "@timestamp": "2024-05-11T13:57:34+00:00",
    },
    {
        "url": "test_log_file3",
        "response_time": "3.0",
        "@timestamp": "2025-06-22T13:57:34+00:00",
    },
    {
        "url": "test_log_file3",
        "response_time": "3.0",
        "@timestamp": "2024-05-11T13:57:34+00:00",
    },
]

TEST_LIST_DATA_LOGS_WITH_DATE_FILTER: list[dict[str, str]] = [
    {
        "url": "test_log_file1",
        "response_time": "1.0",
        "@timestamp": "2025-06-22T13:57:34+00:00",
    },
    {
        "url": "test_log_file2",
        "response_time": "2.0",
        "@timestamp": "2025-06-22T13:57:34+00:00",
    },
    {
        "url": "test_log_file3",
        "response_time": "3.0",
        "@timestamp": "2025-06-22T13:57:34+00:00",
    },
]

TEST_PROCESSED_DATA: list[list[str | int | float]] = [
    ["test_log_file1", 1, 1.0],
    ["test_log_file2", 1, 2.0],
    ["test_log_file3", 1, 3.0],
]

TEST_REPORT_WITHOUT_DATE_FILTER: str = (
    "    handler           total    avg_response_time\n--  --------------  -------  -------------------\n 0  test_log_file1        2                1.000\n 1  test_log_file2        2                2.000\n 2  test_log_file3        2                3.000"
)

TEST_REPORT_WITH_DATE_FILTER: str = (
    "    handler           total    avg_response_time\n--  --------------  -------  -------------------\n 0  test_log_file1        1                1.000\n 1  test_log_file2        1                2.000\n 2  test_log_file3        1                3.000"
)

CURRENT_DATE: str = "2025-22-06"

TEST_DATES: tuple[str] = ("2025-06-22T13:57:34+00:00", "2024-05-11T13:57:34+00:00")


@pytest.fixture
def create_log_files() -> Generator[str]:
    for name in NAMES_TEST_LOG_FILES:
        with open(name, "w", encoding="utf-8") as test_log_file:
            for test_date in TEST_DATES:
                test_data: dict[str, str | float] = dict()
                test_data["url"] = f"{name[:14]}"
                test_data["response_time"] = f"{float(name[13])}"
                test_data["@timestamp"] = test_date
                s: str = f"{test_data}\n".replace("'", '"')
                test_log_file.write(s)
    yield
    for name in NAMES_TEST_LOG_FILES:
        os.remove(name)
