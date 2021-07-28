emp_statuses_dict = dict((('ACTIVE', "Активен"), ("VACATION", "Отпуск"), ("FIRED", "Уволен")))


class EmployeeDto:
    def __init__(self, name, position_name, status):
        self.name = name
        self.position_name = position_name
        self.status = emp_statuses_dict[status]


def toEmployeesDto(emps):
    list = []
    for emp in emps:
        list.append(EmployeeDto(emp.name, emp.position.name, emp.status))
    return list