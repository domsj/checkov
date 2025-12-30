import pytest

from checkov.common.bridgecrew.check_type import CheckType
from checkov.common.models.enums import CheckResult
from checkov.common.output.record import Record
from checkov.common.output.report import Report
from checkov.common.util.secrets_omitter import SecretsOmitter, SecretsOmitterStatus


@pytest.mark.parametrize(
    "r1,r2,expected_result",
    [
        ([10, 20], [15, 17], True),
        ([10, 20], [18, 21], True),
        ([10, 20], [9, 12], True),
        ([10, 20], [20, 25], True),
        ([10, 20], [30, 40], False)
    ],
)
def test_line_ranges_overlap(r1, r2, expected_result):
    assert expected_result == SecretsOmitter._line_range_overlaps(r1, r2)


@pytest.mark.parametrize(
    "code_block,expected_range,expected_lines",
    [
        ([(1, 'ab***'), (2, 'abcd')], [1, 1], ['ab***']),
        ([(1, 'abcd'), (2, 'abc')], [-1, -1], []),
        ([(1, 'ab***'), (2, 'bc*'), (3, 'efg******')], [1, 3], ['ab***', 'bc*', 'efg******'])
    ],
)
def test_get_secret_lines(code_block, expected_range, expected_lines):
    line_range, lines = SecretsOmitter.get_secret_lines(code_block)
    assert line_range == expected_range
    assert lines == expected_lines


@pytest.mark.parametrize(
    "reports",
    [
        ([Report(CheckType.GITHUB_ACTIONS)])
    ],
)
def test_omit_insufficient_reports(reports):
    # SECRETS framework removed - SecretsOmitter now always returns INSUFFICIENT_REPORTS
    assert SecretsOmitter(reports).omit() == SecretsOmitterStatus.INSUFFICIENT_REPORTS


def test_omit():
    # SECRETS framework removed - SecretsOmitter no longer works without secrets reports
    file_path = 'filepath'
    record = Record(check_id='b', check_name='b', check_result={"result": CheckResult.PASSED},
                    code_block=[(2, 'SECRET'), (3, 'SECRET'), (4, 'abcd'), (5, 'abc')],
                    file_path=file_path, file_line_range=[2, 5], resource='', evaluations={}, check_class='',
                    file_abs_path=''
                    )
    report = Report(CheckType.GITHUB_ACTIONS)
    report.add_record(record)

    res = SecretsOmitter([report]).omit()

    # Without secrets report, should return INSUFFICIENT_REPORTS
    assert res == SecretsOmitterStatus.INSUFFICIENT_REPORTS


def test_omit_should_skip():
    """
    SECRETS framework removed - this test verifies SecretsOmitter returns INSUFFICIENT_REPORTS
    """
    file_path = 'filepath'
    record = Record(check_id='b', check_name='b', check_result={"result": CheckResult.PASSED},
                    code_block=[(2, 'SECRET'), (3, 'SECRET'), (4, 'abcd'), (5, 'abc')],
                    file_path=file_path, file_line_range=[2, None], resource='', evaluations={}, check_class='',
                    file_abs_path=''
                    )
    report = Report(CheckType.GITHUB_ACTIONS)
    report.add_record(record)

    res = SecretsOmitter([report]).omit()
    # Without secrets report, should return INSUFFICIENT_REPORTS
    assert res == SecretsOmitterStatus.INSUFFICIENT_REPORTS

def test_omit_with_abs_file_path():
    # SECRETS framework removed - SecretsOmitter no longer works without secrets reports
    abs_file_path = 'abs/filepath'
    record = Record(check_id='b', check_name='b', check_result={"result": CheckResult.PASSED},
                    code_block=[(2, 'SECRET'), (3, 'SECRET'), (4, 'abcd'), (5, 'abc')],
                    file_path='different_file_path', file_line_range=[2, 5], resource='', evaluations={}, check_class='',
                    file_abs_path=abs_file_path
                    )
    report = Report(CheckType.GITHUB_ACTIONS)
    report.add_record(record)

    res = SecretsOmitter([report]).omit()

    # Without secrets report, should return INSUFFICIENT_REPORTS
    assert res == SecretsOmitterStatus.INSUFFICIENT_REPORTS