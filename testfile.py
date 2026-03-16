def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "agent".upper() == "AGENT"

if __name__ == "__main__":
    print("Running tests...")
    test_addition()
    test_string()
    print("All tests passed!")
