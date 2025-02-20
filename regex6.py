import re

text = input().strip()

regex = r"\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d{3}\s+([A-Z]+)\s+\d+\s+---\s+\[([\w]+)\]\s+(?:[\w]+\.)*([\w]+)\s+:\s+(.*)"

data = re.findall(regex, text)
for (a, b, c, d) in data:
    print(f'"{a}","{b}","{c}","{d}"')
