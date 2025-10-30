def calculate_wage(category, days_worked):
    if category == 'A':
        if days_worked == 25:
            return 25 * 900
        elif days_worked < 25:
            return days_worked * 750
        else:
            return (25 * 900) + ((days_worked - 25) * 900)
    elif category == 'B':
        if days_worked == 25:
            return 25 * 600
        elif days_worked < 25:
            return days_worked * 450
        else:
            return (25 * 600) + ((days_worked - 25) * 1200)
    elif category == 'C':
        if days_worked == 25:
            return 25 * 200
        elif days_worked < 25:
            return days_worked * 100
        else:
            return (25 * 200) + ((days_worked - 25) * 900)
    else:
        return None
name = input("ENTER WORKER'S NAME: ")
category = input("ENTER WORKER'S CATEGORY (A/B/C):")
days_worked = int(input("ENTER NUMBER OF DAYS WORKED: "))
total_wage = calculate_wage(category, days_worked)
if total_wage is not None:
    print("***Worker Wage Summary*** ")
    print(f"Name: {name}")
    print(f"Category: {category}")
    print(f"Days Worked: {days_worked}")
    print(f"Total Wage: KES {total_wage}")
else:
    print("Invalid category entered. Please use A, B, or C.")
        
        
