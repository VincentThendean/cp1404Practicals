import wikipedia


def main():
    search_entry = str(input("Enter search:"))

    while search_entry != "":
        wikipedia.search(search_entry)
        # wikipedia.summary(search_entry)

        try:
            wikipedia.page(title=search_entry, auto_suggest=False)
            if wikipedia.page(search_entry):
                print(wikipedia.page(search_entry).title)
                print(wikipedia.page(search_entry).summary)
                print(wikipedia.page(search_entry).url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)


        search_entry = input("Enter search:")

main()