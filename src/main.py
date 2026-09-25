import re


# count number of "search" in "str"
# if no match found, return 0
def count_specific_word(str, search):
    # init count to 0
    count = 0
    # clean out punctuation before splitting words into array
    words = re.sub(r"[^\w\s]", "", str).split()
    # loop through words to look for search
    for word in words:
        if word == search:
            count += 1

    return count


# identify most common word in str
# empty str should return None
def identify_most_common_word(str):
    # if empty string, return None
    if not str:
        return None

    # array of words already checked for
    checked_words = []
    # current most common word and its number of appearances
    most_common_word = {"word": None, "count": 0}
    # clean out punctuation before splitting words into array
    words = re.sub(r"[^\w\s]", "", str).split()
    
    # loop through words
    for word in words:
        # if word already checked for, skip
        if word in checked_words:
            continue
        # compare count of current word to count of existing most common word
        if str.count(word) > most_common_word["count"]:
            most_common_word["word"] = word
            most_common_word["count"] = str.count(word)


# calculate average length of word in str
# exclude punctuation and special characters
# empty str should return 0
def calculate_average_word_length(str):
    pass


# calculate number of paragraphs in str based on empty lines between paragraphs
# empty str should return 1
def count_paragraphs(str):
    pass


# return number of sentences based on periods, question marks, exclamation points
# empty str should return 1
def count_sentences(str):
    pass
