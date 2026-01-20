def format_duration(seconds):
    factors = {"years": 31536000, "days": 86400, "hours": 3600, "minutes": 60, "seconds": 1}
    result = []
    for factor in factors:
        count = seconds // factors.get(factor)
        seconds = seconds % factors.get(factor)
        if count == 1:
            result.append(f"{count} {factor[:-1]}")
        elif count > 1:
            result.append(f"{count} {factor}")

    if len(result) == 0:
        return "now"
    elif len(result) == 1:
        return result[0]
    elif len(result) == 2:
        return " and ".join(result)
    else:
        return ", ".join(result[:-1]) + " and " + result[-1]
    
def format_duration_refactored(seconds):
    """
    Refactored version of format_duration with improved readability and efficiency.

    Key Improvements Made
    divmod(): Instead of performing // and % in two separate steps, divmod(seconds, unit_seconds) 
    returns both the quotient (count) and the remainder (new seconds) in a single operation. 
    This is cleaner and slightly more efficient.

    List of Tuples vs. Dictionary: While modern Python dictionaries preserve insertion order, using a
    list of tuples ([("year", ...)]) makes the intent of ordered iteration explicit and strictly 
    enforceable across all Python versions.

    Key Iteration: The original code iterated over keys and then called .get() effectively doing a 
    lookup twice. Unpacking for unit_name, unit_seconds in units: accesses both values immediately 
    without overhead.

    Pluralization Logic: The original code stored plural keys ("years") and sliced the string to make 
    them singular (factor[:-1]). The refactor stores singular keys ("year") and appends an "s" if 
    count > 1. This prevents bugs if you ever introduce a unit where the singular isn't just the 
    plural minus the last letter (though not applicable to standard time, it is better practice).

    Removed Side Effects: The debug print statement inside the loop was removed.

    Edge Case Handling: Added an immediate check if seconds == 0 at the top to exit early, avoiding 
    unnecessary loop processing.
    """
    if seconds == 0:
        return "now"

    # List of tuples ensures strict ordering and pairs names with values
    units = [
        ("year", 31536000),
        ("day", 86400),
        ("hour", 3600),
        ("minute", 60),
        ("second", 1)
    ]

    parts = []
    
    for unit_name, unit_seconds in units:
        # divmod calculates both the integer division and remainder at once
        count, seconds = divmod(seconds, unit_seconds)
        
        if count > 0:
            # Handle pluralization logically rather than slicing strings
            suffix = 's' if count > 1 else ''
            parts.append(f"{count} {unit_name}{suffix}")

    # Handling the output formatting
    if not parts:
        return "now"
    if len(parts) == 1:
        return parts[0]
    
    # "Oxford comma" style join
    return ", ".join(parts[:-1]) + " and " + parts[-1]

def main():
    print(f"3662 seconds are {format_duration(3662)}")
    print(f"40,000,000 seconds are {format_duration(40000000)}")
    print(f"62 seconds are {format_duration(62)}")
    print(f"2 seconds are {format_duration(2)}")
    print(f"94716060 seconds are {format_duration(94716060)}")
    print(f"0 seconds are {format_duration(0)}")
    print(f"15731080 seconds are {format_duration(15731080)}")
    print(f"3600 seconds are {format_duration(3600)}")
    print(f"120 seconds are {format_duration(120)}")
    print(f"\n{'*' * 15} REFACTORED {'*' * 15}\n")
    print(f"3662 seconds are {format_duration_refactored(3662)}")
    print(f"40,000,000 seconds are {format_duration_refactored(40000000)}")
    print(f"62 seconds are {format_duration_refactored(62)}")
    print(f"2 seconds are {format_duration_refactored(2)}")
    print(f"94716060 seconds are {format_duration_refactored(94716060)}")
    print(f"0 seconds are {format_duration_refactored(0)}")
    print(f"15731080 seconds are {format_duration_refactored(15731080)}")
    print(f"3600 seconds are {format_duration_refactored(3600)}")
    print(f"120 seconds are {format_duration_refactored(120)}")  

if __name__ == "__main__":
    main()