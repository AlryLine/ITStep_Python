# Функція для додавання студента:
def add_student():
    try:
        with open('Students.txt', 'a') as students:
            surname = input('Input surname: ')
            if not surname:
                raise Exception ('Can\'t be empty!')
            elif not surname.isalpha ():
                raise ValueError ('Surname can contains only letters!')
            
            name = input ('Input name: ')
            if not name:
                raise Exception ('Can\'t be empty!')
            elif not name.isalpha ():
                raise ValueError ('Name can contains only letters!')
            
            mark = float (input ('Input mark (1 - 12): '))
            if not mark:
                raise Exception ('Can\'t be empty!')
            elif not isinstance (mark, float):
                raise ValueError 
            elif mark < 1 or mark > 12:
                raise Exception (f'Mark can\'t be {mark}! Please, input mark 1 - 12!')
            
            student = (f"{surname} {name} {mark} \n")
            students.write (student)
            print () 
            print (f'Student {surname} {name} successfully added!')
    except ValueError as val:
        print ('Error: ',val)
    except Exception as ex:
        print ('Error: ',ex)
    except:
        print('File handling error.')      

# Функція для видалення студента:
def remove_student():
    try:
        with open('Students.txt', 'r+') as students:
            lines = students.readlines()
            num = int(input('Input student number to delete: '))
            if num < 1 or num > len(lines):
                raise Exception (f'Invalid input. Enter a student number from 1 to {len(lines)}')
            
            del lines[num-1]
        with open('Students.txt', 'w') as students:
            students.writelines (lines) 
            print ()   
            print('Student successfully removed!')
    except ValueError:
        print ('Error: Number of student can contains only numbers!')         
    except Exception as ex:
        print ('Error: ',ex)
    except:
        print('File handling error.')

# Функція для зміни інформації про студента:
def edit_student():
    try:
        with open('Students.txt', 'r+') as students:
            lines = students.readlines()
            num = int(input('Input student number to edit: '))
            if num < 1 or num > len(lines):
                raise Exception (f'Invalid input. Enter a student number from 1 to {len(lines)}')
            
            surname = input('Input surname: ')
            if not surname:
                raise Exception ('Can\'t be empty!')
            elif not surname.isalpha ():
                raise ValueError ('Surname can contains only letters!')
            
            name = input('Input name: ')
            if not name:
                raise Exception ('Can\'t be empty!')
            elif not name.isalpha ():
                raise ValueError ('Name can contains only letters!')
            
            mark = float(input('Input mark: '))
            if not mark:
                raise Exception ('Can\'t be empty!')
            elif not isinstance (mark, float):
                raise ValueError 
            elif mark < 1 or mark > 12:
                raise Exception (f'Mark can\'t be {mark}! Please, input mark 1 - 12!')
            
            student = f'{surname} {name} {mark}\n'
            lines [num-1] = student
        with open('Students.txt', 'w') as students:
            students.writelines (lines)
            print ()
            print (f'Student information has been successfully changed!')
    
    except ValueError as val:
        print ('Error: ',val)  
    except Exception as ex:
        print ('Error: ',ex)
    except:
        print('File handling error.')    

# Функція для виведення списку студентів:
def show_students():
    try:
        with open('Students.txt', 'r') as students:
            print ()
            print('Sudents list:')
            num = 1
            for student in students:
                print(num,'. ',student.strip(), sep='')
                num += 1     
    except Exception:
        print('Error: Something went wrong...')

# Функція для пошуку студента:
def search_student():
    print ('You can find a student by these parameters:')
    print ()
    print ('1. Students number;')
    print ('2. Surname;')
    print ('3. Name;')
    print ('4. Mark.')
    print ()
    try:
        with open('Students.txt', "r") as students:
            search_param = int(input('Input search parameter: '))
            if search_param < 1 or search_param > 4:
                raise Exception ('\nYou must to input number only 1 - 4!')
            
            if search_param == 1:
                num = int(input("Input students number to search: "))
                lines = students.readlines()
                if num < 1 or num > len(lines):
                    raise Exception (f'Invalid input. Enter a student number from 1 to {len(lines)}')
                student = lines[num-1]
                print()
                print(f"{num}. {student}")
            
            elif search_param == 2:
                surname = input('Input student surname: ')
                lines = students.readlines()
                found = False
                if not surname:
                    raise Exception ('Can\'t be empty!')
                elif not surname.isalpha ():
                    raise ValueError ('Surname can contains only letters!')
                for line in lines:
                    if line.split()[0] == surname:
                        print ()
                        print(line.strip())
                        found = True
                if not found:
                    print(f'Student {surname} not found!')
                    return
                
            elif search_param == 3:
                name=input('Input student name: ')
                lines = students.readlines()
                found = False
                if not name:
                    raise Exception ('Can\'t be empty!')
                elif not name.isalpha ():
                    raise ValueError ('Name can contains only letters!')
                for line in lines:
                    if line.split()[1] == name:
                        print ()
                        print(line.strip())
                        found = True
                if not found:
                    print(f'Student {name} not found!')
                    return
            
            elif search_param == 4:
                mark = float(input('Input student mark: '))
                lines = students.readlines()
                found = False
                if not mark:
                    raise Exception ('Can\'t be empty!')
                elif not isinstance (mark, float):
                    raise ValueError 
                elif mark < 1 or mark > 12:
                    raise Exception (f'Mark can\'t be {mark}! Please, input mark 1 - 12!')
                for line in lines:
                    if float(line.split()[2]) == mark:
                        print ()
                        print(line.strip())
                        found = True
                if not found:
                    print(f'Student with mark {mark} not found!')
                    return
    except ValueError as val:
        print ('Error: Can contains only numbers!',val)  
    except Exception as ex:
        print ('Error: ',ex)
    except:
        print('File handling error.')     
        
# Функція для сортування студентів:
def sort_students():
    print ('You can sort a student by these parameters:')
    print ()
    print ('1. By alphabet;')
    print ('2. By mark.')
    print ()
    try:
        with open('Students.txt', 'r') as f:
            students = [line.strip() for line in f.readlines()]
            sort_param = int(input('Input sort parameter: '))
            students = [student.split() for student in students]
            students = [(surname, name, float(mark)) for surname, name, mark in students]
            if sort_param < 1 or sort_param > 2:
                raise Exception ('Invalid input. Please, enter search parameter 1 - 2!')
            
            if sort_param == 1:
                students.sort(key=lambda x: x[0]) 
            
            elif sort_param == 2:
                students.sort(key=lambda x: x[2]) 
            
            for student in students:
                print(f"{student[0]} {student[1]} {student[2]}")
            return students
    except ValueError:
        print ('Error: Can contains only numbers!')             
    except Exception as ex:
        print ('Error: ',ex)
    except:
        print('File handling error.')    

# Функція для виведення відмінників:
def show_excellent_students():
    try:
        with open('Students.txt', "r") as students:
            print("Excellents list:")
            num = 1
            for line in students:
                if float(line.split()[2]) >= 10:
                    print(num,'. ',line.strip(), sep='')
                    num += 1  
    except:
        print('File handling error.')       

# Головна функція
def main():
    print ('Hello!')
    print ('I have the list with students for you.')
    print ('You can: ')
    while True:
        print ()
        print ('1: Add student.')
        print ('2: Delete student.')
        print ('3: Change student information.')
        print ('4: Show on screen all students.')
        print ('5: Search student.')
        print ('6: Show the students out in a certain order.')
        print ('7: Show "excellents" (with an mark of 10+).')
        print ('0: Exit.')
        try:
                choice = int(input ('\nPlease, choose (0 - 7): '))
                if choice < 0 or choice > 7:
                        raise Exception ('\nYou must to input number only 0 - 7!')
        except ValueError:
                print ('\nError: You must to input only numbers!')
                continue
        except Exception as ex:
                print (ex)
                continue  
        if choice == 1:
            add_student()
        elif choice == 2:
            remove_student()
        elif choice == 3:
            edit_student()
        elif choice == 4:
            show_students()
        elif choice == 5:
            search_student()
        elif choice == 6:
            sort_students()
        elif choice == 7:
            show_excellent_students()
        elif choice == 0:
            print ('\nThank you! Bye!')
            print ()
            break

main ()