import os
from typing import Generator
import pytest


NAMES_TEST_LOG_FILES: list[str] = [
    "test_log_file1.log",
    "test_log_file2.log",
    "test_log_file3.log",
    "test_log_file4.log",
    "test_log_file5.log",
    ]

@pytest.fixture
def create_log_file() -> Generator[list[str]]:
    for name in NAMES_TEST_LOG_FILES:
        with open(name, "w", encoding="utf-8") as test_log_file:
            for i in range(1, 11):
                test_log_file.write(f"Строка № {i}\n")
    yield NAMES_TEST_LOG_FILES
    for name in NAMES_TEST_LOG_FILES:
        os.remove(name)
