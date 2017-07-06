#part 1
employees = [('Bob', 40, 18.25), ('Mary', 10, 20.00), ('John', 0, 100.90),\
             ('Carl', 19, 17.21), ('Meg', 60, 22.10)]

paid = [(name, hours * wage) for (name, hours, wage) in employees if hours > 0]

