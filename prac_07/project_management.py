from project import Project

import datetime

# PROJECT_NAME = ""

def main():
    project_list = []

    print("MAIN MENU\n"
          "- (L)oad projects\n"
          "- (S)ave projects\n"
          "- (D)isplay projects\n"
          "- (F)ilter projects by date\n"
          "- (A)dd new project\n"
          "- (U)pdate project\n"
          "- (Q)uit")
    choice = str(input(">>> "))
    choice = choice.upper()
    while choice != "Q":
        if choice == "L":
            load_project(project_list)
        elif choice == "S":
            save_project(project_list)
        elif choice == "D":
            display_project(project_list)
        elif choice == "F":
            filter_project(project_list)
        elif choice == "A":
            add_project(project_list)
        elif choice == "U":
            update_project(project_list)

        print("MAIN MENU\n"
              "- (L)oad projects\n"
              "- (S)ave projects\n"
              "- (D)isplay projects\n"
              "- (F)ilter projects by date\n"
              "- (A)dd new project\n"
              "- (U)pdate project\n"
              "- (Q)uit")
        choice = str(input(">>> "))
        choice = choice.upper()


def load_project(project_list):

    project_name = str(input("Enter filename to load: "))

    with open(project_name, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            project_format = line.strip().split('\t')
            project_entry = Project(project_format[0], project_format[1], project_format[2], project_format[3],
                                    project_format[4])

            project_list.append(project_entry)

    # print(project_list[1])


def save_project(project_list):

    project_name = str(input("Enter filename to save as: "))

    with open(project_name, 'w') as out_file:
        header = f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"
        print("success")
        out_file.write(header)
    with open(project_name, 'a') as out_file:
        for i in range(len(project_list)):
            date_string = project_list[i].start_date.strftime("%d/%m/%Y")
            project_entry = (f"\n{project_list[i].name}\t{date_string}\t{project_list[i].priority}\t"
                             f"{project_list[i].cost}\t{project_list[i].completion}")
            out_file.write(project_entry)


def display_project(project_list):
    completed_projects = []

    sorted_project = sorted(project_list, key=lambda project: project.priority)
    print("Incomplete projects:")
    for i in range(len(sorted_project)):
        # print(f"{project_list[i].completion == 100}")
        # print(project_list[i].is_complete())
        if sorted_project[i].is_complete():
            completed_projects.append(sorted_project[i])
            # print("test2")
        else:
            print(f"  {str(sorted_project[i])}")
            # print("test1")

    print("Complete projects:")
    for i in range(len(completed_projects)):
        print(f"  {completed_projects[i]}")


def filter_project(project_list):
    user_date = input("Show projects that start after date (dd/mm/yyyy): ")
    # user_date = "20/7/2022"

    earliest_date = datetime.datetime.strptime(user_date, "%d/%m/%Y").date()
    sorted_project = sorted(project_list, key=lambda project: project.start_date)
    for i in range(len(sorted_project)):
        if sorted_project[i].start_date <= earliest_date:
            continue
        print(sorted_project[i])


def add_project(project_list):
    print("Let's add a new project")
    project_name = input("Name: ")
    project_date = input("Start date (dd/mm/yy): ")
    project_priority = input("Priority: ")
    project_cost = input("Cost estimate: $")
    project_completion = input("Percent complete: ")

    project_entry = Project(project_name, project_date, project_priority, project_cost, project_completion)
    project_list.append(project_entry)


def update_project(project_list):
    for i in range(len(project_list)):
        print(f"{i} {project_list[i]}")

    user_choice = int(input("Project choice: "))

    print(project_list[user_choice])
    user_completion = input("New percentage: ")
    try:
        user_completion = int(user_completion)
    except ValueError:
        user_completion = -1
    user_priority = input("New priority: ")
    try:
        user_priority = int(user_priority)
    except ValueError:
        user_priority = -1

    if 0 <= user_completion <= 100:
        project_list[user_choice].completion = user_completion
    else:
        pass

    if 0 <= user_priority:
        project_list[user_choice].priority = user_priority
    else:
        pass


main()
