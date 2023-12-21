# DESAFIO PRÁTICO

# Sistema de Cadastro de Alunos - passo 1
# Cadastro de Alunos: O programa deve permitir ao usuário
#cadastrar alunos. Cada aluno terá as seguintes
# informações: nome, idade e 2 notas em três disciplinas:
# Matemática, Ciências e História. Os dados de cada aluno
# devem ser armazenados em um dicionário com as
# seguintes chaves:nome,idade,'notas.As notas devem ser armazenadas em uma tupla.

# Sistema de Cadastro de Alunos - passo 2
# Visualização de Alunos: O programa deve permitir ao usuário visualizar todos os alunos cadastrados, exibindo suas informações de 
#forma organizada.
#  O programa deve calcular a média das notas de cada aluno e exibi-la.
# O programa deve identificar e exibir o aluno com a melhor média de notas.

# Working with classes and function for validating:

def gradeValidation(grade):
    # print(grade)
    while grade >10 or grade <0:
        grade = float(input("\n Invalid grade, please insert a grade between 0 and 10: "))
      
    return grade
 
list_of_students ={
}

#while loop to add the students information
    # 1° option yes:
        # ask for the name,age, 1st grade and 2nd grade for math, science and history  and validate the numbers' inputs
        # add information to the dictionary with a number

    # 2° option no:
        #finish the loop and move foward:
i=1
while True:
    user_choice= input("\n Do you want to add another student?\n'y' for yes or 'n' for no : ")
    if user_choice== "n":
        break
    elif user_choice=="y":
        print("\n Provide the following information: ")
        student_name = input("\n Name: ")
        student_age = int(input("\n Age: ")) 
        while student_age >150 or student_age<6: print("\nInvalid Age, please insert a age between 6 and 100: ");student_age= int(input("\n Age: "))
       
        student_1st_grade_MATH = float(input("\n What's the student's first grade in math: "))
        student_1st_grade_MATH= gradeValidation(student_1st_grade_MATH) 


        student_2nd_grade_MATH = float(input("\n What's the student's second grade in math: "))
        student_2nd_grade_MATH= gradeValidation(student_2nd_grade_MATH)

        student_1st_grade_SCIENCE = float(input("\n What's the student's first grade in science: "))
        student_1st_grade_SCIENCE = gradeValidation(student_1st_grade_SCIENCE)

        student_2nd_grade_SCIENCE = float(input("\n What's the student's second grade in science: "))
        student_2nd_grade_SCIENCE = gradeValidation(student_2nd_grade_SCIENCE)
        
        student_1st_grade_HISTORY = float(input("\n What's the student's first grade in history: "))
        student_1st_grade_HISTORY =  gradeValidation(student_1st_grade_HISTORY)

        student_2nd_grade_HISTORY = float(input("\n What's the student's second grade in history: "))
        student_2nd_grade_HISTORY =gradeValidation(student_2nd_grade_HISTORY) 

        mathgrades=(student_1st_grade_MATH,student_2nd_grade_MATH)
        sciencegrades=(student_1st_grade_SCIENCE,student_2nd_grade_SCIENCE)
        historygrades=(student_1st_grade_HISTORY,student_2nd_grade_HISTORY)
        student_average=round(((student_1st_grade_MATH + student_2nd_grade_MATH + student_1st_grade_SCIENCE + student_2nd_grade_SCIENCE + student_1st_grade_HISTORY + student_2nd_grade_HISTORY)/6),2)
        student_info = {i:[student_name,student_age,(student_1st_grade_MATH,student_2nd_grade_MATH),(student_1st_grade_SCIENCE,student_2nd_grade_SCIENCE),(student_1st_grade_HISTORY,student_2nd_grade_HISTORY),student_average]}
        list_of_students.update(student_info)
        i+=1
    else:
        print ("\n Invalid input, please try again")

print(list_of_students)
#show all the students registered
for i in list_of_students:
    print(">"*10,
          f"\n {i}",
          f"\n   Name: {list_of_students.get(i)[0]}",
          f"\n   age: {list_of_students.get(i)[1]}",
          f"\n   Math 1: {list_of_students.get(i)[2][0]}",f"   Math 2: {list_of_students.get(i)[2][1]}",
          f"\n   Science 1: {list_of_students.get(i)[3][0]}",f"   Science 2: {list_of_students.get(i)[3][1]}"
          f"\n   History 1: {list_of_students.get(i)[4][0]}",f"   History 2: {list_of_students.get(i)[4][1]}"
          f"\n   Grades average: {list_of_students.get(i)[5]}"
          )
    
#Show the averages
for i in list_of_students:
    print("\n   Students average:",
          f"\n   Name: {list_of_students.get(i)[0]}",f" >>> Grades average: {list_of_students.get(i)[5]}"
          )  
    
#show the best student
best_average = 0
for i in list_of_students:
    if list_of_students.get(i)[5] > best_average:
        best_average = list_of_students.get(i)[5]
        best_students_name = list_of_students.get(i)[0]

print(f"\nBest student is {best_students_name} with a {best_average} grades average.")
