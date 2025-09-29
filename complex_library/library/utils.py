# Some extra functions to increase complexity

def calculate_fine(days_late):
    if days_late < 0:
        raise ValueError("Days late cannot be negative")
    if days_late <= 5:
        return days_late * 1
    elif days_late <= 10:
        return days_late * 2
    else:
        return days_late * 5

def risky_division(a, b):
    # Hotspot: division without checking
    return a / b

def duplicate_function(a):
    return a * 2

def duplicate_function(a):  # intentional duplicate
    return a * 2
