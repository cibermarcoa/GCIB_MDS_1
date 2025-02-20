import re

text = input().strip()
pattern = r"\b(\d{4})-(\d{2})-(\d{2})\b"
replacement = r"\3.\2.\1"
new_text = re.sub(pattern, replacement, text)
print(new_text)
