import pytest
from src.pythonAssessment import *


# count number of "search" in "str"
# if no match found, return 0
def test_count_specific_word():
    assert count_specific_word("ACME ACME ACME Wile E. Coyote", "ACME") == 3
    assert count_specific_word("No match found!", "zzz") == 0
    assert count_specific_word("Search with an empty string.", "") == 0


# identify most common word in str
# empty str should return None
def test_identify_most_common_word():
    assert identify_most_common_word("") == None
    assert identify_most_common_word("cat cat cat dog dog snake") == "cat"


# calculate average length of word in str
# exclude punctuation and special characters
# empty str should return 0
def test_calculate_average_word_length():
    assert calculate_average_word_length("bat cat hat mat fat pat") == 3
    assert calculate_average_word_length("main immense in roundabout") == 5.75
    assert calculate_average_word_length("") == 0


# calculate number of paragraphs in str based on empty lines between paragraphs
# empty str should return 1
def test_count_paragraphs():
    assert count_paragraphs("") == 1
    assert count_paragraphs("This is \n\n an example \n\n of 3 paragraphs.") == 3


# return number of sentences based on periods, question marks, exclamation points
# empty str should return 1
def test_count_sentences():
    assert count_sentences("") == 1
    assert count_sentences("There are technically. Three sentences? In this string!") == 3
