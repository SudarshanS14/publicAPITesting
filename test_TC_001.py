import pytest

def test_testCase_001():
    print("hello World \n")

@pytest.mark.smoke
def test_testCase_010():
    print("Smoke test case file 001 \n")

@pytest.mark.sanity
def test_testCase_011():
    print("Sanity test case file 001 \n")

@pytest.mark.topsmokeTest
def test_testCase_010():
    print("Smoke test case file 001 \n")

@pytest.mark.TopsanityTest
def test_testCase_011():
    print("Sanity test case file 001 \n")