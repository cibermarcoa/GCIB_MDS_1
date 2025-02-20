import re

text = input().strip()

alumno_regex = r"([a-z])\.([a-z]{2,})\.(\d{4})@alumnos\.urjc\.es"
profe_regex = r"([a-z]+)\.([a-z]+)@urjc\.es"

alumnos = re.findall(alumno_regex, text)
profesores = re.findall(profe_regex, text)

for (_, apellido, año) in alumnos:
	print(f"alumno {apellido} matriculado en {año}")

for (nombre, apellido) in profesores:
	print(f"profesor {nombre} apellido {apellido}")
