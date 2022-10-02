class Employee:
    def __init__(self, name, age, salary, employment_years):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_years = employment_years

    def get_annual_salary(self, salary):
        return self.salary * 12

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years}"

class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
        super().__init__(name, age, salary, employment_years)
        self.bonus_percentage = bonus_percentage

    def __str__(self):
        return f"Name: {Employee.name}, Age: {Employee.age}, Salary: {Employee.salary}, Working Years: {Employee.employment_years}, Bounus: {self.bonus_percentage}"

    
#     def main():
# 	# main code here

# # if __name__ == '__main__':
# # 	main()
