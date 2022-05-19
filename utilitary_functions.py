def present_schools(schools):
    print("-" * 40)
    print("Alura Content:")
    for item in schools.items():
        print(f"{item[0]} - {item[1]}")
    print("-" * 40)
    print("Selecione uma escola: ")
