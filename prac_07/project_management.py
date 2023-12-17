from project import Project

import datetime


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
    # project_name = str(input("Enter filename to load: "))
    project_name = "project.txt"

    get_project_file(project_list, project_name)


def get_project_file(project_list, project_name):
    try:
        with open(project_name, 'r') as in_file:
            in_file.readline()
            for line in in_file:
                project_format = line.strip().split('\t')
                project_entry = Project(project_format[0], project_format[1], project_format[2], project_format[3],
                                        project_format[4])

                project_list.append(project_entry)
    except FileNotFoundError:
        print("File does not exist.")


def save_project(project_list):
    project_name = str(input("Enter filename to save as: "))

    set_project_file(project_list, project_name)


def set_project_file(project_list, project_name):
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

    get_incomplete_projects(completed_projects, sorted_project)

    get_complete_projects(completed_projects)


def get_complete_projects(completed_projects):
    print("Complete projects:")
    for i in range(len(completed_projects)):
        print(f"  {completed_projects[i]}")


def get_incomplete_projects(completed_projects, sorted_project):
    print("Incomplete projects:")
    for i in range(len(sorted_project)):
        if sorted_project[i].is_complete():
            completed_projects.append(sorted_project[i])
        else:
            print(f"  {str(sorted_project[i])}")


def filter_project(project_list):
    try:
        user_date = input("Show projects that start after date (dd/mm/yyyy): ")  # user_date = "20/7/2022"
        earliest_date = datetime.datetime.strptime(user_date, "%d/%m/%Y").date()

        sorted_project = sorted(project_list, key=lambda project: project.start_date)

        get_projects_after_date(earliest_date, sorted_project)
    except ValueError:
        print("Incorrect date format. Date must be written as dd/mm/yyyy")


def get_projects_after_date(earliest_date, sorted_project):
    for i in range(len(sorted_project)):
        if sorted_project[i].start_date >= earliest_date:
            print(sorted_project[i])


def add_project(project_list):
    print("Let's add a new project")
    project_name = input("Name: ")
    project_date = set_project_date()
    if project_date is not None:
        project_priority = set_project_priority()
        if project_priority is not None:
            project_cost = set_project_cost()
            if project_cost is not None:
                project_completion = set_project_completion()
                if project_completion is not None:
                    project_entry = Project(project_name, project_date, project_priority, project_cost,
                                            project_completion)
                    project_list.append(project_entry)


def set_project_completion():
    try:
        project_completion = int(input("Percent complete: "))
        return project_completion
    except ValueError:
        print("Completion must be integer")
        return None


def set_project_cost():
    try:
        project_cost = float(input("Cost estimate: $"))
        return project_cost
    except ValueError:
        print("Cost must be float or integer")
        return None


def set_project_priority():
    try:
        project_priority = int(input("Priority: "))
        return project_priority
    except ValueError:
        print("Priority must be an integer")
        return None


def set_project_date():
    try:
        project_date = input("Start date (dd/mm/yy): ")
        date_check(project_date)
        return project_date
    except ValueError:
        print("Incorrect date format. Date must be written as dd/mm/yyyy")
        return None


def date_check(input_date):
    date_entry = datetime.datetime.strptime(input_date, "%d/%m/%Y").date()
    return date_entry


def update_project(project_list):
    for i in range(len(project_list)):
        print(f"{i} {project_list[i]}")

    user_choice = int(input("Project choice: "))

    print(project_list[user_choice])
    project_list[user_choice].set_completion()
    project_list[user_choice].set_priority()


main()
