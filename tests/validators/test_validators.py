import pytest
from my_exceptions.my_exceptions import DateError, LogFileNotExistError, ReportError
from tests.validators.conftest import NAMES_TEST_LOG_FILES
from validators.validators import date_validation, files_exists, report_validation


@pytest.mark.parametrize("log_files, result", [(NAMES_TEST_LOG_FILES, None)])
def test_files_validator_good(create_log_file, log_files, result) -> None:
    assert files_exists(log_files) is result


@pytest.mark.parametrize(
    "log_files, result",
    [("test_log_file.log", LogFileNotExistError("test_log_file.log"))],
)
def test_files_validator_bad(log_file, result) -> None:
    assert files_exists(log_file) == result


@pytest.mark.parametrize(
    "report, result",
    [
        ("average", None),
        ("Average", None),
        ("  AVERAGE  ", None),
        ("AVARAGA", ReportError("AVARAGA")),
    ],
)
def test_report_validation_good(report, result) -> None:
    assert report_validation(report) is result


@pytest.mark.parametrize(
    "date, result", [("2025-22-06", None), ("06-22-2025", DateError("06-22-2025"))]
)
def test_date_validation_good(date, result) -> None:
    assert date_validation(date) is result
