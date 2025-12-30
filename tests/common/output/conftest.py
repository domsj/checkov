from __future__ import annotations
from typing import Any

import pytest
from checkov.common.bridgecrew.check_type import CheckType
from checkov.common.output.report import Report


# SECRETS framework removed - secrets_report fixture no longer needed


@pytest.fixture()
def json_reduced_check() -> dict[str, Any]:
    return {
        "check_id": "CKV_GHA_1",
        "check_name": "Ensure ACTIONS_ALLOW_UNSECURE_COMMANDS isn\u0027t true on environment variables",
        "check_result": {
            "result": "PASSED",
            "results_configuration": {}
        },
        "resource": "jobs(container-test-job)",
        "file_path": "/.github/workflows/image_no_violation.yml",
        "file_line_range": [
            7,
            7
        ],
        "file_abs_path": "/tmp/checkov/elturgeman6/elturgeman/supplygoat1/main/src/.github/workflows/image_no_violation.yml",
        "code_block": [
            [
                7,
                "    runs-on: ubuntu-latest\n"
            ],
        ],
        "bc_check_id": "BC_REPO_GITHUB_ACTION_1",
        "inspected_key_line": None,
        "evaluated_keys": None,
        "inspected_key": "",
        "inspected_value": ""
    }

@pytest.fixture()
def json_reduced_report() -> dict[str, Any]:
    return {
        "checks": {
            "passed_checks": [
                {
                    "check_id": "CKV_GHA_1",
                    "check_name": "Ensure ACTIONS_ALLOW_UNSECURE_COMMANDS isn\u0027t true on environment variables",
                    "check_result": {
                        "result": "PASSED",
                        "results_configuration": {}
                    },
                    "resource": "jobs(container-test-job)",
                    "file_path": "/.github/workflows/image_no_violation.yml",
                    "file_line_range": [
                        7,
                        7
                    ],
                    "file_abs_path": "/tmp/checkov/elturgeman6/elturgeman/supplygoat1/main/src/.github/workflows/image_no_violation.yml",
                    "code_block": [
                        [
                            7,
                            "    runs-on: ubuntu-latest\n"
                        ],
                    ],
                    "bc_check_id": "BC_REPO_GITHUB_ACTION_1",
                    "inspected_key_line": None,
                    "evaluated_keys": None,
                    "inspected_key": "",
                    "inspected_value": ""
                }
            ],
            "failed_checks": [
                {
                    "check_id": "CKV_GHA_2",
                    "check_name": "Ensure ACTIONS_ALLOW_UNSECURE_COMMANDS isn\u0027t true on environment variables",
                    "check_result": {
                        "result": "FAILED",
                        "results_configuration": {}
                    },
                    "resource": "jobs(container-test-job)",
                    "file_path": "/.github/workflows/image_no_violation.yml",
                    "file_line_range": [
                        7,
                        7
                    ],
                    "file_abs_path": "/tmp/checkov/elturgeman6/elturgeman/supplygoat1/main/src/.github/workflows/image_no_violation.yml",
                    "code_block": [
                        [
                            7,
                            "    runs-on: ubuntu-latest\n"
                        ],
                    ],
                    "bc_check_id": "BC_REPO_GITHUB_ACTION_1",
                    "inspected_key_line": None,
                    "evaluated_keys": None,
                    "inspected_key": "",
                    "inspected_value": ""
                }
            ],
            "skipped_checks": []
        },
        "image_cached_results": []
    }