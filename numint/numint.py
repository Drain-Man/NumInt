def num_int(function: callable,lower: float,upper: float,intervals: int,sumtype: str="center"):
    """
    Approximate a definite integral using numerical methods.

    Parameters
    ----------
    function : callable
        Single-variable function f(x)
    lower : float
        Lower bound of the interval
    upper : float
        Upper bound of the interval
    intervals : int
        Number of subintervals
    sumtype : str
        Method: 'left', 'right', 'center', 'trapezoid', 'simpson'

    Returns
    -------
    float
        Approximation of the definite integral
    """
    sumtype = sumtype.lower()
    valid = {"left", "right", "center", "trapezoid", "simpson"}

    if sumtype not in valid:
        raise ValueError(f"Invalid approximation type: '{sumtype}'")

    if (not isinstance(intervals,int)) or (intervals <= 0):
        raise ValueError(
            f"Invalid number of subintervals: {intervals}\n"
            "(Number of subintervals must be a non-zero integer)"
        )

    f = function
    w = (upper - lower) / intervals
    total = 0

    if sumtype == "left":
        for i in range(intervals):
            x = lower + i * w
            total += f(x)
        total *= w
    elif sumtype == "right":
        for i in range(1, intervals + 1):
            x = lower + i * w
            total += f(x)
        total *= w
    elif sumtype == "center":
        for i in range(intervals):
            x = lower + (i + 0.5) * w
            total += f(x)
        total *= w
    elif sumtype == "trapezoid":
        total = (f(lower) + f(upper)) / 2
        for i in range(1, intervals):
            x = lower + i * w
            total += f(x)
        total *= w
    elif sumtype == "simpson":
        if intervals % 2 != 0:
            raise ValueError("Simpson's rule requires an even number of intervals.")
        total = f(lower) + f(upper)
        for i in range(1, intervals):
            x = lower + i * w
            total += (4 if i % 2 else 2) * f(x)
        total *= w / 3
        
    return total