

import pytest

@pytest.mark.sanity
def test_testCase_012():
    print("Sanity test case file 003 \n")

@pytest.mark.smoke
@pytest.mark.regression
def test_testCase_013():
    print("Smoke test case file 003 \n")


