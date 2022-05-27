hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
overtime_rate = 1.5 * rate
normal_hrs = 40

if hrs > normal_hrs:
    overtime_hrs = hrs - normal_hrs
    pay = normal_hrs * rate + overtime_hrs * overtime_rate

if hrs < 40:
    pay = hrs * rate

print(hrs, rate)
print(pay)