import re
from typing import List
from datetime import datetime

def extract_error_messages(log_lines: List[str]) -> List[str]:
    r"""
    Step 2: Constructing the Regex
    To build a regex, we move from left to right, translating the "human" format into "regex" symbols.

    We are targeting this exact structure: 2025-01-01 12:01:00 [ERROR] Failed to load config

    Here is the mental process to convert that into a pattern:

    1. The Anchors (The Start and End)
    We want to match the entire line to ensure it's a valid log.

    Start of line: ^

    End of line: $

    2. The Timestamp (The Date & Time)
    We need to match YYYY-MM-DD HH:MM:SS.

    Digits: Regex uses \d for a single digit (0-9).

    Counts: We use {n} to say "exactly n times".

    YYYY becomes \d{4}

    MM becomes \d{2}

    DD becomes \d{2}

    Separators: The hyphens -, colons :, and spaces are just literal characters.

    Result for timestamp: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}

    3. The Level (The Filter)
    We encounter [ERROR].

    Brackets: In regex, [ and ] have special meanings (they define character sets). 
    Because we want to match a real bracket, we must "escape" them using a backslash: \[ and \].

    The Text: Since we only care about ERROR lines, we can hardcode the word ERROR right into our regex. 
    This is a smart move—it means our regex will automatically fail (and ignore) lines with [INFO] 
    or [WARN].

    Result for level: \[ERROR\]

    4. The Message (The Target)
    This is the part we want to keep.

    Space: There is a space after the closing bracket.

    The Text: The message can be anything (letters, numbers, symbols) and goes until the end of the line.

    Wildcard: The dot . matches any character (except newlines).

    Quantifier: The star * means "0 or more times". So .* means "everything else".

    Capture Group: We wrap this in parentheses ( ... ). This tells Python: "Match the whole line, 
    but save this specific part into a variable for me."

    Result for message: (.*)

    The Final Regex
    Putting it all together, here is the expression we will use. I have added spaces in the visual 
    below just to make it readable, but the regex itself is one continuous string.

    ^ \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[ERROR\] (.*) $

    In Python string format:

    Python

    r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[ERROR\] (.*)$"
    (Note: The r before the quote stands for "raw string," which helps Python handle backslashes correctly.)
        """
    # 1. Create a list to hold the results
    errors = []
    
    # 2. Define the Regex Pattern
    # We use re.compile for efficiency since we use it inside a loop.
    # Note the 'r' before the string, and the parentheses around the message part.
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[ERROR\] (.*)$")
    
    # 3. Loop through every log line
    for line in log_lines:
        # 4. Attempt to match the line against the pattern
        match = pattern.search(line)
        
        # 5. Check if we found a match
        if match:
            # If match is not None, it means:
            # a) The format was correct
            # b) It was an [ERROR] line (because our regex demands it)
            
            # 6. Extract the message (Group 1) and add to list
            message = match.group(1)
            errors.append(message)
            
    return errors


def extract_errors_then_warnings(log_lines: List[str]) -> List[str]:
    r"""
    To capture both [ERROR] and [WARN], we need to change the part of the regex that strictly 
    looks for "ERROR".

    1. The "OR" Operator
    In Regex, the pipe symbol | means OR. So, ERROR|WARN matches "ERROR" OR "WARN".

    2. Grouping
    We can't just write \[ERROR|WARN\] because regex might get confused about where the "OR" 
    starts and ends. We usually wrap the options in parentheses so the "OR" stays contained.

    New Level Pattern: \[(ERROR|WARN)\]

    3. The Consequence: Shifting Groups
    Here is the tricky part that catches many developers off guard.

    When you add parentheses (ERROR|WARN) to handle the logic, you create a new Capture Group.

    The regex engine sees the first set of parentheses (ERROR|WARN) and calls it Group 1.

    It sees the second set of parentheses (.*) (the message) and now calls it Group 2.

    The Updated Regex
    Python

    r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[(ERROR|WARN)\] (.*)$"
    """
    # 1. Create two separate buckets
    errors = []
    warnings = []
    
    # 2. Update pattern to capture the Level (Group 1) AND Message (Group 2)
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[(ERROR|WARN)\] (.*)$")
    
    for line in log_lines:
        match = pattern.search(line)
        
        if match:
            # Group 1 is the Level ("ERROR" or "WARN")
            level = match.group(1)
            # Group 2 is the Message
            message = match.group(2)
            
            # 3. Sort into buckets based on Group 1
            if level == "ERROR":
                errors.append(message)
            else:
                warnings.append(message)
    
    # 4. Combine them (Errors first, as requested)
    return errors + warnings

def extract_errors_then_warnings_named(log_lines: List[str]) -> List[str]:
    r"""
    Extracts message text from ERROR and WARN log lines, returning all errors first, 
    followed by warnings.
    
    The "Senior Developer" Upgrade: Named Groups
    In the code we just wrote, we used group(1) and group(2). This works, but it’s fragile. 
    If you come back in 6 months and decide to add a timestamp capture group at the beginning, 
    your indices shift:

    Old Group 1 -> New Group 2
    Old Group 2 -> New Group 3
    
    You would have to rewrite all your Python code to match the new numbers.
    
    The Solution: You can name your groups right inside the regex.
    Syntax: (?P<name>...)
    Instead of (ERROR|WARN), you write (?P<level>ERROR|WARN).
    Instead of (.*), you write (?P<msg>.*).

    Args:
        log_lines (List[str]): A list of raw log strings containing timestamps, levels, and messages.

    Returns:
        List[str]: A combined list of message strings (Errors first, then Warnings).
    """
    
    errors = []
    warnings = []
    
    # We define the names 'level' and 'msg' directly inside the pattern
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[(?P<level>ERROR|WARN)\] (?P<msg>.*)$")
    
    for line in log_lines:
        match = pattern.search(line)
        
        if match:
            # We access the data using the names we defined in the regex
            # This makes the code self-documenting and resistant to future regex changes
            level = match.group('level')
            message = match.group('msg')
            
            if level == "ERROR":
                errors.append(message)
            else:
                warnings.append(message)
                
    return f"{'#'*20}\nHere are the errors:\n{errors}\n\n{'#'*20}\nHere are the warnings:\n{warnings}"

def extract_filtered_errors_then_warnings(log_lines: List[str], start_date: str, end_date: str) -> str:
    r"""
    Extracts ERROR and WARN messages that occurred within a specific date range,
    returning all Errors first, followed by Warnings.

    STRATEGY: THE "PARSER VS CALCULATOR" APPROACH
    
    1. Python Sanitization:
       We use line.strip() to handle leading/trailing whitespace. This protects us 
       from indented logs without making the regex more complex.
    
    2. Regex is the Parser: 
       Regex is excellent at identifying structure ("Grab the text that looks like a date"), 
       but terrible at evaluating value ("Is this date after Jan 15th?").
       We use Regex to extract the 'timestamp', 'level', and 'message' into named groups.

    3. Python is the Calculator:
       We use Python's datetime module to convert the string "2025-01-01" into a real 
       Date Object. This allows us to use logical operators (>=, <=) to filter the logs 
       accurately without writing complex and fragile regex patterns for date ranges.

    4. Single-Pass Bucket Sort:
       We iterate through the logs only once. As we validate each line, we sort it into 
       either an 'errors' list or a 'warnings' list immediately. Finally, we concatenate 
       them to ensure the requested order (Errors first).

    Args:
        log_lines (List[str]): A list of raw log strings.
        start_date (str): The start of the range (inclusive) in 'YYYY-MM-DD' format.
        end_date (str): The end of the range (inclusive) in 'YYYY-MM-DD' format.

    Returns:
        str: A formatted string listing filtered errors followed by filtered warnings.
    """
    
    # 1. Prepare the Buckets
    filtered_errors = []
    filtered_warnings = []
    
    # 2. Convert string arguments to Date Objects for comparison
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    # 3. Compile the Regex
    # We capture:
    #   - timestamp: To compare against start/end dates
    #   - level: To sort into Error or Warning buckets
    #   - msg: The actual text we want to return
    pattern = re.compile(r"^(?P<timestamp>\d{4}-\d{2}-\d{2}) \d{2}:\d{2}:\d{2} \[(?P<level>ERROR|WARN)\] (?P<msg>.*)$")
    
    for line in log_lines:
        # STRATEGY: Clean the data before the regex sees it.
        # This handles indentation (leading space) and newlines (trailing space).
        clean_line = line.strip()

        match = pattern.search(clean_line)
        
        if match:
            # 4. Extract Data using Named Groups
            log_date_str = match.group('timestamp')
            level = match.group('level')
            message = match.group('msg')
            
            # 5. Convert log timestamp to Date Object
            try:
                log_date = datetime.strptime(log_date_str, "%Y-%m-%d")
            except ValueError:
                continue # Skip lines with invalid dates if any
            
            # 6. The Logic: Date Filter
            if start <= log_date <= end:
                
                # 7. Sort into appropriate bucket
                if level == "ERROR":
                    filtered_errors.append(message)
                else:
                    filtered_warnings.append(message)
    
    # 8. Format the Output
    # We return a single string representation for easy reading
    return f"{'#'*20}\nDATE RANGE: {start_date} to {end_date}\n\n[ERRORS]\n{filtered_errors}\n\n[WARNINGS]\n{filtered_warnings}"


def main():
    # Test Data: A mix of dates, levels, and some out-of-range entries
    logs = [
        "2025-01-01 12:00:00 [INFO] System Start",           # Ignored (INFO)
        "2025-01-05 14:00:00 [ERROR] Connection Failed",     # KEEP (In range)
        "2025-01-10 09:00:00 [WARN] High Latency",           # KEEP (In range)
        "2025-01-12 10:00:00 [ERROR] Database Locked",       # KEEP (In range)
        "2025-01-15 11:00:00 [WARN] Disk Space Low",         # KEEP (In range)
        "2025-01-20 12:00:00 [ERROR] Out of Memory",         # SKIP (Date too late)
        "2024-12-31 23:59:00 [ERROR] Pre-historic Error",    # SKIP (Date too early)
    ]

    # Test Case 1: Filter from Jan 5th to Jan 15th
    print("Running Test Case: Filter Jan 05 to Jan 15...")
    result = extract_filtered_errors_then_warnings(logs, "2025-01-05", "2025-01-15")
    print(result)
    print("\n" + "="*50 + "\n")
    sample_logs = [
        "2025-01-01 12:01:00 [ERROR] Failed to load config",
        "2025-01-01 12:02:00 [WARN] Low disk space",
        "2025-01-01 12:03:00 [INFO] System rebooted",
        "2025-01-01 12:04:00 [ERROR] Unable to connect to database",
        "2025-01-01 12:05:00 [WARN] High memory usage detected"
    ]
    
    print("Extracted ERROR messages:")
    print(extract_error_messages(sample_logs))
    
    print("\nExtracted ERROR and WARN messages:")
    print(extract_errors_then_warnings(sample_logs))
    
    print("\nExtracted ERROR and WARN messages using named groups:")
    print(extract_errors_then_warnings_named(sample_logs))

if __name__ == "__main__":
    main()