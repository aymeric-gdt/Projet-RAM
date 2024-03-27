from classes import MachineUniverselle

ram = MachineUniverselle()

ram.build(path_of_ram_machine="example.ram")

ram.print_tasks()

ram.start()