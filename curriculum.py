curriculum = []
def curriculum_menu():
    while True:
        print("PERSONAL CURRICULUM")
        print('''
        1. Add Learning Topic
        2. View Curriculum
        3. Add Learning Objective
        4. Mark Objective Complete
        5. View Progress
        6. Delete Learning Topic
        7. Exit ''')

        opt_4=int(input("Enter your choice: "))

        if opt_4==1:
            topic=input("Learning topic: ")
            field=input("Field: ")
            reason=input("Why do you want to study it? ")
            new_topic={
                "Topic": topic,
                "Field": field,
                "Reason": reason,
                "Objectives": []
            }
            curriculum.append(new_topic)
            print("Learning topic has been added.")

        elif opt_4==2:
            if len(curriculum)==0:
                print("No learning topics available.")

            else:
                for i, topic in enumerate(curriculum, start=1):
                    print("Topic Number:", i)
                    print("Topic: ", topic["Topic"])
                    print("Field: ", topic["Field"])
                    print("Reason: ", topic["Reason"])

                    if len(topic["Objectives"])==0:
                        print("No objectives available.")

                    else:
                        print("Objectives: ")
                        for obj in topic["Objectives"]:
                            if obj["Completed"]:
                                print("Completed:", obj["Name"])

                            else:
                                print("Pending:", obj["Name"])

        elif opt_4==3:
            if len(curriculum)==0:
                print("No learning topics available.")

            else:
                for i, topic in enumerate(curriculum, start=1):
                    print(i, topic["Topic"])

                num=int(input("Enter topic number: "))

                if 1<=num<=len(curriculum):
                    obj_name=input("Learning objective: ")
                    objective={
                        "Name": obj_name,
                        "Completed": False
                    }
                    curriculum[num-1]["Objectives"].append(objective)
                    print("Learning objective has been added.")

                else:
                    print("Invalid Topic Number.")

        elif opt_4==4:
            if len(curriculum)==0:
                print("No learning topics available.")

            else:
                for i, topic in enumerate(curriculum, start=1):
                    print(i, topic["Topic"])

                topic_num=int(input("Enter topic number: "))

                if 1<=topic_num<=len(curriculum):
                    topic=curriculum[topic_num-1]
                    if len(topic["Objectives"])==0:
                        print("No objectives available.")

                    else:
                        for i, objective in enumerate(topic["Objectives"], start=1):
                            print(i, objective["Name"])

                        objective_num=int(input("Enter objective number: "))

                        if 1<=objective_num<=len(topic["Objectives"]):
                            topic["Objectives"][objective_num-1]["Completed"]=True
                            print("Objective has been completed.")

                        else:
                            print("Invalid Objective Number.")

                else:
                    print("Invalid Topic Number.")

        elif opt_4==5:
            total=0
            comp=0
            for topic in curriculum:
                for objective in topic["Objectives"]:
                    total+=1
                    if objective["Completed"]:
                        comp+=1
            if total==0:
                prog=0
            else:
                prog=comp/total*100

            print("Total Objectives: ", total)
            print("Completed Objectives: ", comp)
            print("Progress: ", prog, "%")

        elif opt_4==6:
            if len(curriculum)==0:
                print("No learning topics available.")

            else:
                for i, topic in enumerate(curriculum, start=1):
                    print(i, topic["Topic"])

                num=int(input("Enter topic number to delete: "))

                if 1<=num<=len(curriculum):
                    dele=curriculum.pop(num-1)
                    print(dele["Topic"], "has been deleted.")

                else:
                    print("Invalid Topic Number.")

        elif opt_4==7:
            break

        else:
            print("Invalid choice.")