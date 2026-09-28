tasks=[]
def task_menu():
    while True:
        print("TO-DO LIST")
        print(''' 
        1. Add Tasks
        2. View Tasks
        3. Mark Task Complete
        4. Delete Task
        5. View Task Completion Progress
        6. Exit ''')

        opt_1=int(input("Enter your choice: "))

        if opt_1==1:
            name=input("Task name: ")
            subject=input("Subject: ")
            deadline=input("Deadline: ")

            task = {
                "Task Name": name,
                "Subject": subject,
                "Deadline": deadline,
                "Completed": False
            }

            tasks.append(task)
            print("Task has been added.")

        elif opt_1==2:

            if len(tasks) == 0:
                print("No tasks available.")

            else:
                for i, task in enumerate(tasks, start=1):
                    print("Number of Task:", i)
                    print("Name: ", task["Task Name"])
                    print("Subject: ", task["Subject"])
                    print("Deadline: ", task["Deadline"])
                    if task["Completed"]:
                        print("Status: ", "Completed")

                    else:
                        print("Status: ", "Pending")

        elif opt_1==3:

            if len(tasks)==0:
                print("No tasks available.")

            else:
                for i, task in enumerate(tasks, start=1):
                    print(i, task["Task Name"])

                num = int(input("Enter task number: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["Completed"] = True
                    print("Task Completed.")
                else:
                    print("Invalid Task Number.")

        elif opt_1==4:

            if len(tasks)==0:
               print("No tasks available.")

            else:
                for i, task in enumerate(tasks, start=1):
                    print(i, task["Task Name"])

                num=int(input("Enter Task Number to delete: "))

                if 1<=num<=len(tasks):
                   dele=tasks.pop(num-1)
                   print("Task ", dele["Task Name"], " has been deleted.")

                else:
                    print("Invalid Task Number.")

        elif opt_1==5:
            comp=0
            for task in tasks:
                if task["Completed"]:
                    comp=comp+1
                
            if len(tasks)==0:
                progress=0

            else:
                progress=comp/len(tasks)*100

            print("Total tasks: ", len(tasks))
            print("Completed: ", comp)
            print("Progress: ", progress, "%")

        elif opt_1==6:
            break

        else:
            print("Invalid choice.")
            