student_list = []
dict_of_students = {'rollnum':111,'studname':'abcd','english':56,
'hindi':45,'maths':35,
'physics':85,'chemistry':75}
student_list.append(dict_of_students)
def info():
    

    
    # if ro_input is not int:
    #     print("roll number should be numric ")
    # else:
    
    try:
        dict_of_students = {}  
        ro_input=int(input("enter roll number \n"))

        if  ro_input in dict_of_students.keys():
            print("roll num already exist  ")
        else:
            dict_of_students['rollnum'] = ro_input
            dict_of_students['studname'] = input("enter student name \n")
            dict_of_students['english'] = int(input('enter english marks \n'))
            dict_of_students['hindi'] = int(input('enter hindi marks \n'))
            dict_of_students['maths'] = int(input('enter maths marks \n'))
            dict_of_students['physics'] = int(input('enter physics marks \n'))
            dict_of_students['chemistry'] = int(input('enter chemistry marks \n'))
            student_list.append(dict_of_students)
            print("data added successfuly")          

        
    except :

        print("roll number and marks should be numeric ")
        
    
                    


def display():

    for std in student_list:
        print(std)
        total_marks = std['english'] + std['hindi'] + \
            std['maths']+std['physics'] + \
            std['chemistry']
        percent = (total_marks*100)/500

        print(total_marks, percent)
        if std['english'] < 33 or std['hindi'] < 33 or std['maths'] < 33 or std['physics'] < 33 or std['chemistry'] < 33:
            print("fail")
        else:
            print('pass')

def showMarkSheet():

    roll_num = int(input("enter roll number \n "))

    for std in student_list:
        if roll_num == std["rollnum"]:
            total_marks = std['english'] + std['hindi'] + \
                std['maths']+std['physics'] + \
                std['chemistry']
            percent = (total_marks*100)/500

            if std['english'] < 33 or std['hindi'] < 33 or std['maths'] < 33 or std['physics'] < 33 or std['chemistry'] < 33:
                print(
                    "---------------------------------------------------------------------------")
                print(
                    "                                                                         ")
                print(
                    "                           MARKSHEET                                    ")
                print(
                    "---------------------------------------------------------------------------")
                print("|Roll Number  = ", std['rollnum'],
                      "                                        |")
                print("|Student Name = ", std['studname'],
                      "                                      |")
                print(
                    "--------------------------------------------------------------------")
                print(
                    "Subjects--------------------Total----------------------------Mark Obtain ")
                print(
                    "|English---------------------100------------------------------", std['english'])
                print(
                    "|Hindi-----------------------100------------------------------", std['hindi'])
                print(
                    "|Maths-----------------------100------------------------------", std['maths'])
                print(
                    "|Physics---------------------100------------------------------", std['physics'])
                print(
                    "|Chemistry-------------------100------------------------------", std['chemistry'])
                print(
                    "|----------------------------------------------------------------------------")
                print("Result     fail    Total marks ", total_marks,
                      "      Percentage ", percent, "      |")
                print(
                    "|----------------------------------------------------------------------------")

            else:

                print(
                    "---------------------------------------------------------------------------")
                print(
                    "                                                                         ")
                print(
                    "                           MARKSHEET                                    ")
                print(
                    "---------------------------------------------------------------------------")
                print("Roll Number  = ",
                      std['rollnum'], "                                         ")
                print("Student Name = ", std['studname'],
                      "                                      |")
                print(
                    "--------------------------------------------------------------------")
                print(
                    "Subjects--------------------Total----------------------------Mark Obtain ")
                print(
                    "__________________________________________________________________________")

                print(
                    "English---------------------|100|------------------------------", std['english'])
                print(
                    "Hindi-----------------------|100|------------------------------", std['hindi'])
                print(
                    "Maths-----------------------|100|------------------------------", std['maths'])
                print(
                    "Physics---------------------|100|------------------------------", std['physics'])
                print(
                    "Chemistry-------------------|100|------------------------------", std['chemistry'])
                print(
                    "----------------------------------------------------------------------------")
                print("Result     pass    Total marks ", total_marks,
                      "      Percentage ", percent, "      |")
                print(
                    "----------------------------------------------------------------------------")
        else:
            print(" Student not Found ")

def update():

    roll_num = int(input("enter roll number \n "))

    for dic in student_list:

        if dic['rollnum'] == roll_num:
            dic['english'] = int(input('enter english marks \n'))
            dic['hindi'] = int(input('enter hindi marks \n'))
            dic['maths'] = int(input('enter maths marks \n'))
            dic['physics'] = int(input('enter physics marks \n'))
            dic['chemistry'] = int(input('enter chemistry marks \n'))

    # display()

def remove():
    roll_num = int(input("enter roll number \n "))
    for dic in student_list:
        if dic['rollnum'] == roll_num:
            student_list.remove(dic)

while True:

  
    oplist=['add','upd','rem','sm' 'dl']
    option = input("what you want  For Add data use add For Update use upd For Remove user rem  Show marksheet use sm  Show list of marksheet ")
    if option in 'add':
        info()

        
        # list_of_student()
    elif option == 'upd':
        update()
    elif option == 'dl':
        display()
    elif option == 'rem':
        remove()
    elif option == 'sm':
        showMarkSheet()
        
    elif  option not in oplist:
        print("enter vaild input ")

    elif option == 'end':

        break
