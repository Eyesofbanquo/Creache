def increment(initialValue: float, addedValue: float = 0.0, sig: int = 2) -> float:
    """
    A function that will take an initial value and add an addedValue to
    a number of sig digits

    Default sig digits is 2
    """
    return round(initialValue + addedValue, sig)
