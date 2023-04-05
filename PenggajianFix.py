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
        name= input("Nama karyawan               : ")
        if name.strip() != "":
            break
        else:
            print("Nama karyawan tidak boleh kosong.")

    while True:
        try:
            salary= float(input("Gaji pokok                  : "))
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    while True:
        try:
            grade= int(input("Golongan (1/2/3/4/5/6)      : "))
            if grade>= 1 and grade <= 6:
                break
            else:
                print("Golongan hanya boleh diisi angka 1-6.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    while True:
        try:
            num_children= int(input("Jumlah anak                 : "))
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    while True:
        married = input("Sudah Menikah? Masukan 1/2 \n1.Sudah \n2.Belum                     : ").lower()
        if married == "1":
            married= True
            break
        elif married == "2":
            married= False
            break
        else:
            print("Input tidak valid.Masukkan '1' atau '2'.")

    #objek karyawan
    employee = Employee(name, salary, grade, num_children, married)

    allowance_grade, allowance_children, allowance_spouse, bonus, tax, total_salary= employee.get_salary()

    print("===="*20)
    print("Gaji Karyawan")
    print("===="*20)
    print("Nama                    : "+(name))
    print("Gaji Pokok              : "+str(salary))
    print("Tunjangan golongan      : Rp" + str(allowance_grade))
    print("Tunjangan anak          : Rp" + str(allowance_children))
    print("Tunjangan istri/suami   : Rp" + str(allowance_spouse))
    print("Bonus                   : Rp" + str(bonus))
    print("Pajak                   : Rp" + str(tax))
    print("Total gaji              : Rp" + str(total_salary))
    print("===="*20)

    while True:
        hitung_lagi = input("Apakah ingin menghitung lagi? (y/n): ").lower()
        if hitung_lagi == "y":
            break
        elif hitung_lagi == "n":
            quit()
        else:
            print("Input tidak valid. Masukkan 'y' atau 'n'.")


