subjects={}
def subject_menu():
    while True:
        print("SUBJECT PERFORMANCE")
        print('''
        1. Add Subject
        2. View Subjects
        3. Enter Exam Result
        4. View Performance
        5. Delete Subject
        6. Exit ''')

        opt_2=int(input("Enter your choice: "))

        if opt_2==1:
            name=input("Subject name: ")
            subjects[name]=[]
            print("Subject has been added.")

        elif opt_2==2:
            if len(subjects)==0:
                print("No subjects available.")

            else:
                print("Subjects: ")
                for subject in subjects:
                    print(subject)

        elif opt_2==3:
            if len(subjects)==0:
                print("No subjects available.")

            else:
                for subject in subjects:
                    print(subject)

                name=input("Enter subject name: ")

                if name in subjects:
                    marks=float(input("Enter marks: "))
                    subjects[name].append(marks)
                    print("Result has been added.")

                else:
                    print("Subject not found.")

        elif opt_2==4:
            if len(subjects)==0:
                print("No subjects available.")

            else:
                for subject in subjects:
                    print("Subject:", subject)
                    if len(subjects[subject])==0:
                        print("No exam results available.")

                    else:
                        sum=0
                        for marks in subjects[subject]:
                            sum=sum+marks
                        avg=sum/len(subjects[subject])
                        print("Exam Results:", subjects[subject])
                        print("Average Marks:", avg)

        elif opt_2==5:
            if len(subjects)==0:
                print("No subjects available.")

            else:
                for subject in subjects:
                    print(subject)

                name=input("Enter subject name to delete: ")
                if name in subjects:
                    del subjects[name]
                    print("Subject has been deleted.")

                else:
                    print("Subject not found.")

        elif opt_2==6:
            break

        else:
            print("Invalid choice.")