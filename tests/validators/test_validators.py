from my_exceptions.my_exceptions import DateError, LogFileNotExistError, ReportError
from tests.validators.conftest import NAMES_TEST_LOG_FILES
from validators.validators import date_validation, files_exists, report_validation


def test_files_validator_good(create_log_file) -> None:
    assert files_exists(NAMES_TEST_LOG_FILES) is None


def test_files_validator_bad() -> None:
    assert files_exists("test_log_file.log") == LogFileNotExistError(
        "test_log_file.log"
    )


def test_report_validation_good() -> None:
    assert report_validation("AVERAGE") is None


def test_report_validation_bad() -> None:
    assert report_validation("AVARAGA") == ReportError("AVARAGA")


def test_date_validation_good() -> None:
    assert date_validation("2025-22-06") is None


def test_date_validation_bad() -> None:
    assert date_validation("06-22-2025") == DateError("06-22-2025")
