from tasks import task_menu
from subject import subject_menu
from book import book_menu
from curriculum import curriculum_menu
while True:
    print('''
    1. To-Do List
    2. Subject Performance
    3. Book Tracker
    4. Personal Curriculum
    5. Exit
    ''')

    opt=int(input("Enter your choice: "))

    if opt==1:
        task_menu()
    elif opt==2:
        subject_menu()
    elif opt==3:
        book_menu()
    elif opt==4:
        curriculum_menu()
    elif opt==5:
        print("Have a nice day.")
        break
    else:
        print("Invalid choice.")