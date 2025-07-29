from scripts.scripts import LogAvgReporter
from tests.scripts.conftest import NAMES_TEST_LOG_FILES, TEST_LIST_DATA_LOGS, TEST_REPORT

def test_logavgreporter_get_log_files_data_good(create_log_files) -> None:
    test_reporter: LogAvgReporter = LogAvgReporter(NAMES_TEST_LOG_FILES, 'test')
    assert test_reporter.get_log_files_data() == TEST_LIST_DATA_LOGS


def test_logavgreporter_report_without_date_filter_good(create_log_files) -> None:
    test_reporter: LogAvgReporter = LogAvgReporter(NAMES_TEST_LOG_FILES, 'test')
    assert test_reporter.report() == TEST_REPORT
    