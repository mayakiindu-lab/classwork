print("welcome to HEALTHCHECK USSD SERVICE")
print("-------------------------------------")

print("SYMPTOM OPTIONS:")
print("1.fever,headache and fatigue")
print("2.cough,sore throat and cough")
print("3.stomach,pain,diarrhea and nausea")
print("4.joint pain,skin rash and red eyes")

symptomchoice=(input("SELECT YOUR SYMPTOMS (1-4)\n"))

if symptomchoice == "1":
    print("\nPossible diseases:")
    print("- Food poisoning")
    print("- Gastroenteritis")
    print("- Cholera")

elif symptomchoice == "2":
    print("\nPossible diseases:")
    print("- Common cold")
    print("- COVID-19")
    print("- Pneumonia")

elif symptomchoice == "3":
    print("\nPossible diseases:")
    print("- Malaria")
    print("- Typhoid")
    print("- Influenza")

elif symptomchoice == "4":
    print("\nPossible diseases:")
    print("- Dengue fever")
    print("- Chikungunya")
    print("- Allergic reaction")

else:
    print("INVALID INPUT!")