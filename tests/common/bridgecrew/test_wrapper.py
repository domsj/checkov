
# SECRETS framework removed - test no longer applicable

import pytest
from checkov.common.output.report import Report
from checkov.common.bridgecrew.check_type import CheckType
from checkov.common.models.enums import CheckResult
from checkov.common.output.record import Record


@pytest.fixture
def report() -> Report:
    """Simple report fixture for testing"""
    record = Record(
        check_id='CKV_TEST_1',
        check_name='Test check',
        check_result={"result": CheckResult.FAILED},
        code_block=[],
        file_path='test.tf',
        file_line_range=[1, 1],
        resource='test.resource',
        evaluations={},
        check_class='',
        file_abs_path='test.tf'
    )
    report = Report(CheckType.GITHUB_ACTIONS)
    report.add_record(record)
    return report


def test_reduce_scan_reports(report):
    from checkov.common.bridgecrew.wrapper import reduce_scan_reports
    from checkov.common.typing import _ReducedScanReportCheck, _ReducedScanReport
    from checkov.common.bridgecrew.check_type import CheckType

    report.check_type = CheckType.GITHUB_ACTIONS
    reduced_report: _ReducedScanReport = reduce_scan_reports([report])[CheckType.GITHUB_ACTIONS]

    checks: _ReducedScanReportCheck = reduced_report["checks"]
    all_checks = checks["passed_checks"] + checks["failed_checks"] + checks["skipped_checks"]

    reduced_keys = ('check_id', 'check_result', 'resource', 'file_path', 'file_line_range')

    assert all(reduced_key in check.keys() for check in all_checks for reduced_key in reduced_keys)
    assert all('validation_status' not in check.keys() for check in all_checks)
