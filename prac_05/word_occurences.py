"""
Word Occurrences
Estimate: 30 minutes
Start:    14:43
Actual:   21 minutes
End:      15:04
"""

def main():

    sentence_dict = {}
    longest_key = 0

    user_sentence = set_user_sentence()

    count_words(sentence_dict, user_sentence)

    get_sentence_dictionary(sentence_dict)


def get_sentence_dictionary(sentence_dict):
    sentence_dict = dict(sorted(sentence_dict.items()))
    longest_key = len(max(sentence_dict, key=len))
    for key, value in sentence_dict.items():
        print(f"{key:{longest_key}} : {value}")


def count_words(sentence_dict, user_sentence):
    user_sentence = user_sentence.split()
    for word in user_sentence:
        if word in sentence_dict.keys():
            sentence_dict[word] += 1
        else:
            sentence_dict[word] = 1


def set_user_sentence():
    user_sentence = input("Text: ")
    return user_sentence


main()