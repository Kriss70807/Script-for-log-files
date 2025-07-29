import pytest
from scripts.scripts import LogAvgReporter
from tests.scripts.conftest import (
    NAMES_TEST_LOG_FILES,
    TEST_LIST_DATA_LOGS_WITHOT_DATE_FILTER,
    TEST_LIST_DATA_LOGS_WITH_DATE_FILTER,
    TEST_REPORT_WITHOUT_DATE_FILTER,
    TEST_REPORT_WITH_DATE_FILTER,
    CURRENT_DATE,
)

@pytest.mark.parametrize(
    "log_files, report_method, date_filter, result",
    [
        (
            NAMES_TEST_LOG_FILES,
            "average",
            None,
            TEST_REPORT_WITHOUT_DATE_FILTER
        ),
        (
            NAMES_TEST_LOG_FILES,
            "average",
            CURRENT_DATE,
            TEST_REPORT_WITH_DATE_FILTER,
        ),
    ],
)
def test_logavgreporter_report_without_date_filter_good(log_files, report_method, date_filter, result, create_log_files) -> None:
    test_reporter: LogAvgReporter = LogAvgReporter(log_files=log_files, report_method=report_method, date_filter=date_filter)
    assert test_reporter.report() == result


@pytest.mark.parametrize(
    "log_files, report_method, date_filter, result",
    [
        (
            NAMES_TEST_LOG_FILES,
            "average",
            None,
            TEST_LIST_DATA_LOGS_WITHOT_DATE_FILTER
        ),
        (
            NAMES_TEST_LOG_FILES,
            "average",
            CURRENT_DATE,
            TEST_LIST_DATA_LOGS_WITH_DATE_FILTER,
        ),
    ],
)
def test_get_log_files_data(
    log_files, report_method, date_filter, result, create_log_files
) -> None:
    test_reporter: LogAvgReporter = LogAvgReporter(
        log_files=log_files, report_method=report_method, date_filter=date_filter
    )
    assert test_reporter.get_log_files_data() == result
