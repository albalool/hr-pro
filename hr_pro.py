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

    def get_bonus(self, bonus_percentage):
        return bonus_percentage * self.salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years}, Bounus: {self.bonus_percentage}"




def main():
        employee_one = Employee("Lateefa", 33, 1500, 10)
        employee_two = Employee("Mohammad", 32, 1800, 8)
        employee_list = [employee_one, employee_two]
        manager_one = Manager("Laila", 40, 2000, 15, 2)
        manager_two = Manager("Shereen", 35, 1900, 12, 2)
        managers_list = [manager_one, manager_two]

        print(employee_one)
        print(employee_two)
        print(manager_one)
        print(manager_two)
        print(employee_list)
        print(managers_list)

        
        def show_options():
            list_of_options = ["Show Employees", "Show Managers", "Add An Employee", "Add A Manager", "Exit"]
            print("Welcome to HR Prop")
            print("Your options:")
            for index, option in enumerate(list_of_options, 1):
                print(f"{index}. {option}")
                
        def get_options():
            toDo = int(input("What would you like to do? "))
            if toDo == 1:
                print(employee_list)
            elif toDo == 2:
                print(managers_list)
            elif toDo == 3:
                for employee in employee_list:
                   print("Add employee details")
                   name = input("Name: " )
                   age = int(input("age: " ))
                   salary = int(input("Salary: " ))
                   employment_years = int(input("Employement years: " ))
                   print("Employee added succesfully")
                   employee = Employee(name, age, salary, employment_years)
                   employee_list.append[employee]
                   print(f"Name: {name}, Age: {age}, Salary: {salary}, Working Years: {employment_years}")
                 #  print(employee)
            elif toDo == 4:
                for manager in managers_list:
                   print("Add Manager details")
                   name = print(input("Name: "))
                   age = print(int(input("age: ")))
                   salary = print(int(input("Salary: ")))
                   employment_years = print(int(input("Employement years: ")))
                   Bonus = print(float(input("Bonus Percentage: ")))
                   print("Manager added succesfully")
                   manager = Manager(name,age,salary,employment_years, Bonus)
                   managers_list.append[manager]
                   print(f"Name: {name}, Age: {age}, Salary: {salary}, Working Years: {employment_years}, Bounus: {Bonus}")
                 #  print(manager)


        # print(show_options())
        # print(get_options())




if __name__ == '__main__':
	main()
