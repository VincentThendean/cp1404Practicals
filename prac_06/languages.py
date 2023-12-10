from prac_06.programming_languages import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    language_list = [python, ruby, visual_basic]

    get_dynamic_languages(language_list)


def get_dynamic_languages(language_list):
    dynamic_languages = []

    for language in language_list:
        if language.is_dynamic():
            dynamic_languages.append(language)

    print("The dynamically typed languages are:")
    for i in range(len(dynamic_languages)):
        print(dynamic_languages[i].name)


main()
