
OUTPUT_FILE = "name.txt"
INPUT_FILE = "numbers.txt"

def main1():
    user_name = str(input("Enter Name: "))
    out_file = open(OUTPUT_FILE,"w")
    print(user_name, file=out_file)

    out_file.close()

def main2():
    user_name = str(input("Enter Name: "))
    out_file = open(OUTPUT_FILE, "w")
    print(f"Your name is {user_name}", file=out_file)

    out_file.close()

def main3():
    in_file = open(INPUT_FILE,"r")

    text = in_file.readlines()
    file_sum = int(text[0]) + int(text[1])
    print(file_sum)

    in_file.close()

def main4():
    in_file = open(INPUT_FILE, "r")
    file_sum = 0

    for line in in_file:
        file_sum += int(line)

    print(file_sum)

    in_file.close()

main1()
#main2()
#main3()
#main4()