from classes import operation, RegistreManager

rm = RegistreManager()

tasks = [('ADD',5,0,rm.get_registre_from_name('r1')), ('MULT',rm.get_registre_from_name('r1'),2,rm.get_registre_from_name('r1'))]

print(rm)
for task in tasks:
    ope, x, y, z = task
    operation(ope, x, y, z)
    print(rm)

for i in range(10):
    ope, x, y, z = tasks[1]
    operation(ope, x, y, z)
    print(rm)