import random


subjects = []
study_hours = []
priorities = []


quotes = [
    "Stay consistent and success will follow.",
    "Small progress every day adds up.",
    "Discipline is the key to success.",
    "Focus on improvement, not perfection.",
    "Work hard and trust the process."
]

print("===== Smart Study Planner =====")


number_of_subjects = int(input("How many subjects do you have? "))


for i in range(number_of_subjects):

    subject_name = input("\nEnter subject name: ")

    hours = int(input("Enter study hours: "))

    print("\nPriority Levels")
    print("1 - High")
    print("2 - Medium")
    print("3 - Low")

    priority = int(input("Enter priority level: "))

    subjects.append(subject_name)
    study_hours.append(hours)
    priorities.append(priority)

print("===== Your Study Timetable =====")

start_time =int(input("Enter your preferred timing to start studying:-"))


for i in range(number_of_subjects):

    if priorities[i] == 1:

        end_time = start_time + study_hours[i]

        print("Subject :", subjects[i])
        print("Priority : High")
        print("Study Time :", start_time, "to", end_time)

        break_time = random.randint(10, 20)

        print("Break Time :", break_time, "minutes")
        print("-" * 35)

        start_time = end_time


for i in range(number_of_subjects):

    if priorities[i] == 2:

        end_time = start_time + study_hours[i]

        print("Subject :", subjects[i])
        print("Priority : Medium")
        print("Study Time :", start_time, "to", end_time)

        break_time = random.randint(10, 20)

        print("Break Time :", break_time, "minutes")
        print("-" * 35)

        start_time = end_time


for i in range(number_of_subjects):

    if priorities[i] == 3:

        end_time = start_time + study_hours[i]

        print("Subject :", subjects[i])
        print("Priority : Low")
        print("Study Time :", start_time, "to", end_time)

        break_time = random.randint(10, 20)

        print("Break Time :", break_time, "minutes")
        print("-" * 35)

        start_time = end_time


quote = random.choice(quotes)

print("\nMotivational Quote of the Day:")
print(f'"{quote}"')


file = open("study_plan.txt", "w")

file.write("===== Smart Study Timetable =====\n\n")

for i in range(number_of_subjects):

    file.write("Subject : " + subjects[i] + "\n")
    file.write("Study Hours : " + str(study_hours[i]) + "\n")

    if priorities[i] == 1:
        file.write("Priority : High\n")
    elif priorities[i] == 2:
        file.write("Priority : Medium\n")
    else:
        file.write("Priority : Low\n")

    file.write("-" * 35 + "\n")

file.write("\nMotivational Quote:\n")
file.write(quote)

file.close()

print("\nStudy plan saved successfully!")