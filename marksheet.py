student_list = []
dict_of_students = {'rollnum':111,'studname':'abcd','english':56,
'hindi':45,'maths':35,
'physics':85,'chemistry':75}
student_list.append(dict_of_students)

list_rollnum=[111]
def info():
    

    
    # if ro_input is not int:
    #     print("roll number should be numric ")
    # else:
    
    try:
        dict_of_students = {} 
        ro_input=int(input("enter roll number \n"))
        stdname=input("enter student name \n")
        eng=int(input('enter english marks \n'))
        hindi= int(input('enter hindi marks \n'))
        maths=int(input('enter maths marks \n'))
        physics=int(input('enter physics marks \n'))
        chemistry=int(input('enter chemistry marks \n'))

       
        if  ro_input not in list_rollnum:

            dict_of_students['rollnum'] = ro_input
            dict_of_students['studname'] = stdname
            if eng >100 or hindi >100 or maths >100 or physics >100 or chemistry > 100:
                print("marks not greater than 100 ")
            else:
                dict_of_students['english'] = eng
                dict_of_students['hindi'] =hindi
                dict_of_students['maths'] = maths
                dict_of_students['physics'] = physics
                dict_of_students['chemistry'] = chemistry
                print("data added successfuly")          

            student_list.append(dict_of_students)
            list_rollnum.append(ro_input)

        else:
            print("roll num already exist  ")

            

        
    except:

        print("roll number and marks should be numeric ")
        # print(e)
        
    
                    


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
            print(dic['studname'], "is update ")
        else:
            print(roll_num," is not  avialable ")



    # display()

def remove():
    try:
        roll_num = int(input("enter roll number \n "))
        list_rollnum.remove(roll_num)
        for dic in student_list:
            if dic['rollnum'] == roll_num:
                student_list.remove(dic)
                print(dic['studname'], "is removed")
    except:
        print(roll_num," is not  avialable ")
        
    

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
