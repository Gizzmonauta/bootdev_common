import re

# -----------------------------------------------------------------------------
# STRATEGY: THE "FILTER CHAIN" WITH ROBUST REGEX
#
# 1. Compilation (The "Chef" Analogy):
#    Think of a Regex Pattern as a cooking recipe written in a foreign language.
#    Think of the Python Regex Engine as a Chef.
#
#    - Direct calls (re.sub): You hand the Chef the foreign text every time 
#      you order the dish. The Chef has to translate it, understand it, and 
#      then cook it. This is fine for one meal (small scripts), as the 
#      translation is fast.
#
#    - Compiling (re.compile): You translate the recipe into the Chef's native 
#      language ONCE and hand them a laminated card. The Chef can now cook 
#      that dish 1,000 times instantly without reading the confusing text again.
#      
#    *Performance Note*: For small inputs or single-use functions, compiling 
#    is irrelevant because Python's 're' module internally caches the last few 
#    patterns used. However, for "Enterprise" scale (loops, big data), explicit 
#    compilation is best practice.
#
# 2. Verbose Regex (re.X):
#    Complex regexes are write-only languages (impossible to read later).
#    Using re.VERBOSE allows us to break the pattern into multiple lines and
#    add comments explaining each part.
#
# 3. Quantifiers for Chaos:
#    Users are unpredictable.
#    - We use '?' for optional characters (like parenthesis).
#    - We use '*' (zero or more) for separators to handle cases where users
#      double-tap the space bar or omit separators entirely.
# -----------------------------------------------------------------------------

# PHONE PATTERN
# Matches:
# (555) 123-4567   (Standard)
# 555.123.4567     (Dots)
# 5551234567       (Compact)
# (555)  123 4567  (Sloppy Spaces)
PHONE_PATTERN = re.compile(r"""
    \(?          # Optional open parenthesis
    \d{3}        # Area code (3 digits)
    \)?          # Optional close parenthesis
    [\s.-]* # Separator 1: Zero or MORE spaces, dots, or dashes
    \d{3}        # Prefix (3 digits)
    [\s.-]* # Separator 2: Zero or MORE spaces, dots, or dashes
    \d{4}        # Line number (4 digits)
""", re.VERBOSE)

# EMAIL PATTERN
# Standard email extraction
EMAIL_PATTERN = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")

def anonymize_user_input_robust(text: str) -> str:
    """
    Scrub PII (Personally Identifiable Information) from text.
    Handles messy phone number formats and standard emails.
    """
    # Filter 1: Phones
    # We replace any sequence matching the robust phone pattern
    text = PHONE_PATTERN.sub("[REDACTED PHONE]", text)
    
    # Filter 2: Emails
    # We run the cleaner text through the email filter
    text = EMAIL_PATTERN.sub("[REDACTED EMAIL]", text)
    
    return text

def main():
    # Test Data: A nightmare of user formatting
    messy_comment = """
    URGENT!! Contact list:
    1. Standard: 555-123-4567
    2. Parenthesis: (555) 123-4567
    3. Dots: 555.123.4567
    4. Compact: (555)1234567
    5. Sloppy Spaces: (555)  123   4567
    
    Email me at: john.doe@email.com or jane_doe123@sub.corp.org
    """
    
    print("--- ORIGINAL TEXT ---")
    print(messy_comment)
    
    print("\n--- SCRUBBED TEXT ---")
    print(anonymize_user_input_robust(messy_comment))

if __name__ == "__main__":
    main()