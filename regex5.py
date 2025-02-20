import re
text = input().strip()
pattern = r"\b(C\/|Calle) +([A-ZÑÁÉÚÍÓ][a-zñáéíóúü]*),? +([Nn]º?)?[ ]?(\d+), +(\d{5})\b"
results = re.findall(pattern, text)
for match in results:
	print(f"{match[4]}-{match[1]}-{match[3]}")



