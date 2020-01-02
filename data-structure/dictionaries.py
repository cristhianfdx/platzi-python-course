
qualifications = {}

qualifications['algoritmos'] = 9.0
qualifications['matematicas'] = 10.0
qualifications['prog_web'] = 8.0
qualifications['bases_datos'] = 8.0

for key in qualifications:
    print(key)

# bases_datos
# algoritmos
# matematicas
# prog_web

for value in qualifications.values():
    print(value)

# 8.0
# 9.0
# 10.0
# 8.0

for key, value in qualifications.items():
    print('key: {}, value: {}'.format(key, value))

# key: bases_datos, value: 8.0
# key: algoritmos, value: 9.0
# key: matematicas, value: 10.0
# key: prog_web, value: 8.0

sum_qly = 0

for value in qualifications.values():
    sum_qly += value

average = float(sum_qly / len(qualifications.values()))

print('El promedio de calificaciones es {}'.format(average))

# El promedio de calificaciones es 8.75