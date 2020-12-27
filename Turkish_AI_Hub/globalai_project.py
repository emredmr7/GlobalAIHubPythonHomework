print("------ WELCOME TO THE STUDENT MANAGEMENT SYSTEM ------")
name = "Emre"
surname = "Demir"

courses = ["Mathematics", "Science", "History", "Art", "Music"]
taken_courses = []
grades = {}

chance = 3

while True:
    user_name = input("Enter your name : ").capitalize()
    user_surname = input("Enter your surname : ").capitalize()
    
    if (name == user_name) and (surname == user_surname):
        print(f"----- Welcome {name} {surname}-----\n---------------")

        print("You Have to Minimum 3 and Maximum 5")
        pick_number = int(input("How many courses will you choose? : "))
        
        if (pick_number >= 3) and (pick_number <= 5):
            print(f"----------------\nThat's the courses will you take = {courses}\n-------------------")
            while pick_number > 0:
                lessons_name = input("Pick the lessons : ").capitalize()
                if lessons_name not in courses:
                    print("There is no this lesson. Try again.")
                    pick_number += 1
                else:
                    if lessons_name in taken_courses:
                        print("This lesson already entered. Please try another lessons.")
                        continue
                    taken_courses.append(lessons_name)
                    print("----",taken_courses,"----")
                    print("Courses saved.")
                pick_number -= 1
            print(f"Selected courses is = {taken_courses}\n---------------")

            forexam = input("Write the course you want to take an exam :").capitalize()
            print("---------------")
            midterm = int(input("Enter your midterm grade : "))
            final = int(input("Enter your final grade : "))
            project = int(input("Enter your project grade : "))

            grades["midterm"] = midterm
            grades["final"] = final
            grades["project"] = project

            averages = (midterm*(30/100)) + (final*(50/100)) + (project*(20/100))

            if averages >= 90:
                print(f"---------------\nYour average is {averages} Congrats ! Your grade AA")
            elif averages < 90 and averages >= 70:
                print(f"---------------\nYour average is {averages} Congrats ! Your grade BB")
            elif averages < 70 and averages >= 50:
                print(f"---------------\nYour average is {averages} Congrats ! Your grade CC")
            elif averages < 50 and averages >= 30:
                print(f"---------------\nYour average is {averages} . Your grade DD")
            else:
                print(f"---------------\nYour average is {averages}. Your grade FF.")
                print("GRADE REPEAT")
            break
        else:
            print("You must enter 3 to 5 courses.")
            break
    
    elif  (name != user_name) or (surname != user_surname) and chance != 0:
        print("---------------\nIncorrect name or surname. Please try again")
        chance -= 1
        print(f"You can try more {chance}\n---------------")
        if chance == 0:
            print("Try Later... You have no chance anymore.")
            break
