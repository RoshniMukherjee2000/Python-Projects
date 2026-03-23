import math

def calculate_attempts(start, end):
    """Calculate max attempts using log2 logic."""
    range_size = end - start + 1
    return int(math.log2(range_size)) + 1
