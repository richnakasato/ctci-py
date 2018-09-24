import heapq

class Employee():

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __lt__(self, other):
        return self.level < other.level


class Respondent(Employee):

    def __init__(self, name):
        super().__init__(name, 1)


class Manager(Employee):

    def __init__(self, name):
        super().__init__(name, 2)


class Director(Employee):

    def __init__(self, name):
        super().__init__(name, 3)


class CallCenter():

    def __init__(self):
        self.employees = set()
        self.available = list()
        self.busy = set()

    def hire(employees):
        for employee in employees:
            self.employees.add(employee)
            self.available.append(employee)
        heapq.heapify(self.available)

    def dispatch_call():
        if not len(self.available):
            raise Exception('nobody is available to take call!')
        else:
            now_busy = heapq.heappop(self.available)
            self.busy.add(now_busy)

    def complete_call(employee):
        if employee not in self.busy:
            raise Exception('was not taking a call!')
        else:
            now_available = self.busy.pop(employee)
            self.available.append(now_available)
            heapq.heapify(self.available)
