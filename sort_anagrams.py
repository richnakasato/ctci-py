'''
Problem: Sort an array of anagrams by anagram
Takeaways: sorting by key (itemgetter)
Issues: How to make this better than quadratic (also less than O(n) space?)

'''
from operator import itemgetter

def sort_anagrams(words):
    unsorted = list()
    for word in words:
        word_dict = dict()
        for char in word: # quadratic time!  how to get to n lg n?
            if char not in word_dict:
                word_dict[char] = 1
            else:
                word_dict[char] += 1
        unsorted.append((word_dict, word))
    sorted_anagrams = [tup[1] for tup in sorted(unsorted, key=itemgetter(0))]
    return sorted_anagrams


def main():
    words = ["abc", "a", "cbc", "b", "c", "cba", "bcc", "bac"]
    sorted_words = sort_anagrams(words)
    print(sorted_words)

if __name__ == "__main__":
    main()

