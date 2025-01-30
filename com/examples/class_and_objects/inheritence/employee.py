class Employee:
    __id = 0
    name = ""
    locations = []
    salary_hist = {
2020: 1000000,
2021: 1200000,
2022: 1800000,
2023: 2400000,
2024: 3200000
}

    _salary = 0 # protected variable (single '_')  - only child class will have access to this variable
    dept_name = ""

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    # protected method (single '_') - only child class will have access to this method
    def _set_salary(self, new_sal):
        self.salary = new_sal

    def set_id(self, initial_id):
        if self.__id == 0:
            self.__id = initial_id
        else:
            print("Employee already has Id. Reassigning id is not recommended.")


class HR(Employee):

    def _set_salary(self, new_sal):
        super()._set_salary(new_sal)