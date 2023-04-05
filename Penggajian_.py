class Employee:

    def __init__(self, name, salary, grade, num_children, married):
        self.name = name
        self.salary = salary
        self.grade = grade
        self.num_children = num_children
        self.married = married

    def get_salary(self):
        allowance_grade=0
        # Hitung tunjangan golongan
        if self.grade == 1:
            allowance_grade = 0.05 * self.salary
        elif self.grade == 2:
            allowance_grade = 0.1 * self.salary
        elif self.grade == 3:
            allowance_grade = 0.15 * self.salary
        elif self.grade == 4:
            allowance_grade = 0.2 * self.salary
        elif self.grade == 5:
            allowance_grade = 0.25 * self.salary
        else:
            allowance_grade = 0.3 * self.salary

        # Hitung tunjangan anak
        if self.num_children > 0:
            allowance_children = 0.02 * self.salary * self.num_children
        else:
            allowance_children = 0    

        # Hitung tunjangan istri
        if self.married:
            allowance_spouse = 0.1 * self.salary
        else:
            allowance_spouse = 0       

        # Hitung total gaji sebelum pajak
        total_salary = self.salary + allowance_grade + allowance_children + allowance_spouse  

        # Hitung pajak
        if total_salary <= 5000000:
            tax = 0.05 * total_salary
        elif total_salary <= 10000000:
            tax = 0.1 * total_salary
        else:
            tax = 0.15 * total_salary    

        # Hitung bonus
        bonus=0
        if self.grade == 1 and self.num_children >= 1:
            bonus = 250000
        elif self.grade == 2 and self.num_children >= 2:
            bonus = 500000
        elif self.grade == 3 and self.num_children >= 3:
            bonus = 500000
        elif self.grade == 4 and self.num_children >= 4:
            bonus = 750000
        elif self.grade == 5 and self.num_children >= 5:
            bonus = 1000000
        elif self.grade == 6 and self.num_children >= 6:
            bonus = 1500000
        else:
            bonus = 0

        # Hitung total gaji setelah pajak dan bonus
        total_salary = total_salary - tax + bonus

        # return all values
        return (allowance_grade, allowance_children, allowance_spouse, bonus, tax, total_salary)

print("Selamat datang di program perhitungan gaji karyawan!")

while True:
    print("\nSilahkan masukkan data karyawan: ")
    while True:
        employee_name= input("Nama karyawan: ")
        if employee_name.strip() != "":
            break
        else:
            print("Nama karyawan tidak boleh kosong.")

    while True:
        try:
            employee_salary= float(input("Gaji pokok: "))
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    while True:
        try:
            employee_grade= int(input("Golongan (1/2/3/4/5/6): "))
            if employee_grade>= 1 and employee_grade <= 6:
                break
            else:
                print("Golongan hanya boleh diisi angka 1-6.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    while True:
        try:
            employee_num_children= int(input("Jumlah anak: "))
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    while True:
        employee_married = input("Status pernikahan (y/n): ").lower()
        if employee_married == "y":
            employee_married= True
            break
        elif employee_married == "n":
            employee_married= False
            break
        else:
            print("Input tidak valid. Masukkan 'y' atau 'n'.")

    #objek karyawan
    employee = Employee(employee_name, employee_salary, employee_grade, employee_num_children, employee_married)

    allowance_grade, allowance_children, allowance_spouse, bonus, tax, total_salary = employee.get_salary()

    print("Tunjangan golongan: Rp" + str(round(allowance_grade)))
    print("Tunjangan anak: Rp" + str(round(allowance_children)))
    print("Tunjangan istri/suami: Rp" + str(round(allowance_spouse)))
    print("Bonus: Rp" + str(round(bonus)))
    print("Pajak: Rp" + str(round(tax)))
    print("Total gaji: Rp" + str(round(total_salary)))

    while True:
        hitung_lagi = input("Apakah ingin menghitung lagi? (y/n): ").lower()
        if hitung_lagi == "y":
            break
        elif hitung_lagi == "n":
            quit()
        else:
            print("Input tidak valid. Masukkan 'y' atau 'n'.")



