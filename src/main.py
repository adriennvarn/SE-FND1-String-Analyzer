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
    
    return most_common_word["word"]


# calculate average length of word in str
# exclude punctuation and special characters
def calculate_average_word_length(str):
    # if str empty, return 0
    if not str:
        return 0
    # init sum 
    sum = 0
    # clean string of punctuation, convert to array
    words = re.sub(r"[^\w\s]", "", str).split()
    
    # loop through words, adding length to sum
    for word in words:
        sum += len(word)
    
    return sum / len(words)


# calculate number of paragraphs in str based on empty lines between paragraphs
# empty str should return 1
def count_paragraphs(str):
    pass


# return number of sentences based on periods, question marks, exclamation points
# empty str should return 1
def count_sentences(str):
    pass

# def main():
#     print(identify_most_common_word("cat cat cat cat"))
    
if __name__ == "__main__":
    main()