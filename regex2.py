import re
text = input().strip()
pattern = r"\bE?[- ]?\d{4}[- ]?[A-Z]{3}\b"
results = re.findall(pattern, text)
for match in results:
	print(match)