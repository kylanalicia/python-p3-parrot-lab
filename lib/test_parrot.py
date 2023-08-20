from parrot import parrot

def test_parrot():
    # Test with a specific string
    assert parrot("Hello, World!") == "Hello, World!"

    # Test with the default string
    assert parrot() == "Squawk!"
