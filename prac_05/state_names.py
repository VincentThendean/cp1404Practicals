"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

for key, value in CODE_TO_NAME.items():
    print(f"{key:3} is {value}")

state_code = input("Enter short state: ")
state_code = state_code.upper()

# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(state_code, "is", CODE_TO_NAME[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ")
#     state_code = state_code.upper()

while state_code != "":
    try:
        CODE_TO_NAME[state_code]
    except KeyError:
        print("Input does not exist in CODE_TO_NAME")
        state_code = input("Enter short state: ")
        state_code = state_code.upper()
    finally:
        print(state_code, "is", CODE_TO_NAME[state_code])
        break
