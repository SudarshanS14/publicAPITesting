import pytest

def test_testCase_002():
    print("hello World - 2 \n")


def test_test_005():
    print("hello World - 5 \n")

def test_newtest_006():
    print("hello world - 6 \n")

@pytest.mark.skip("Skipping now for understanding")
def test_testCase_003():
    print("hello World - 3 \n")

a=101
@pytest.mark.skipif(a>100,reason="Skip only if a is greater than 100")
def test_testCase_004():
    print("hello world - 4 \n")