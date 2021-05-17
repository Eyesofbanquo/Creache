import creache
import incrementer


long_version = 1.3000000000000003


def test_increment():
    assert (
        incrementer.increment(initialValue=long_version, addedValue=0.1, sig=2) == 1.40
    )
