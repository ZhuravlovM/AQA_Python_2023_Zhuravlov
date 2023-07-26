import re

demo_string = ["example (.com)", "github (.com)", "stackoverflow (.com)"]

pattern = '\s*\([^)]*\)'

for clean_up in demo_string:
    remove_bracket = re.sub(pattern, '', clean_up)
    print(remove_bracket.strip())
