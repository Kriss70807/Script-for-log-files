import pytest
from my_exceptions.my_exceptions import DateError, LogFileNotExistError, ReportError
from tests.validators.conftest import NAMES_TEST_LOG_FILES
from validators.validators import date_validation, files_exists, report_validation


@pytest.mark.parametrize("log_files, result", [(NAMES_TEST_LOG_FILES, True)])
def test_files_validator_good(create_log_file, log_files, result) -> None:
    assert files_exists(log_files) is result


@pytest.mark.parametrize(
    "log_file, result",
    [("test_log_file.log", LogFileNotExistError)],
)
def test_files_validator_bad(log_file, result) -> None:
    with pytest.raises(result):
        files_exists(log_file)


@pytest.mark.parametrize(
    "report, result",
    [("average", None), ("Average", None), ("  AVERAGE  ", None)],
)
def test_report_validation_good(report, result) -> None:
    assert report_validation(report) is result


@pytest.mark.parametrize(
    "report, result",
    [
        ("AVARAGA", ReportError),
    ],
)
def test_report_validation_bad(report, result) -> None:
    with pytest.raises(result):
        report_validation(report)


@pytest.mark.parametrize(
    "date, result",
    [
        ("2025-22-06", None),
    ],
)
def test_date_validation_good(date, result) -> None:
    assert date_validation(date) is result


@pytest.mark.parametrize("date, result", [("06-22-2025", DateError)])
def test_date_validation_bad(date, result) -> None:
    with pytest.raises(result):
        date_validation(date)
