HEX_COLOR_CODE = {"alizarin crimson": "#e32636", "cadmium orange": "#ed872d", "daffodil": "#ffff31",
                      "forest green": "#228b22", "han blue": "#446ccf",
                      "lightpink": "#ffb6c1", "magenta": "#ff00ff", "melon": "#febaad", "nickel": "#727472",
                      "oldlace": "#fdf5e6"}

def main():
    print(HEX_COLOR_CODE)
    for key, value in HEX_COLOR_CODE.items():
        print(f"{key} is {value}")

    color_name = ""
    color_name = set_color_name()

    get_color_name(color_name)


def get_color_name(color_name):
    while color_name != "":
        try:
            HEX_COLOR_CODE[color_name]
        except KeyError:
            print("Not a valid color name.")
            color_name = set_color_name()
        finally:
            print(HEX_COLOR_CODE[color_name])
            color_name = set_color_name()


def set_color_name():
    color_name = input("Type a color to get its hex code: ")
    color_name = color_name.lower()
    return color_name


main()