import pytest

actual_value="hello World"

def test_check_assertion(fixture_code):
    print("Before assertion check \n")
    assert actual_value == "Testing","Actual value should be Hello World"
    print("After assertion check \n")


def test_001(fixture_code):
    print("By World \n")


@pytest.fixture(scope="module")
def fixture_code():
    
    print("\n Excute before other test case are run \n")
    print("------------------------------------- \n")
    yield
    print("\n Excute After other test case are run \n")
    print("------------------------------------- \n")