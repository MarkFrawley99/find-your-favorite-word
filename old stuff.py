documentName = ('/Users/markfrawley/Downloads/64b0b814293c09999f765e265aaa2ba1'
                   '-79f24f9f87654d7ec7c2f6ba83e927852cdbf9a5/gistfile1.txt')
with open(documentName, "r") as f:
    words = f.read().split()

# type the word you want to find and make lowercase to avoid capitalization dupes

find_words = input("Which word or words do you want to find? ").split(',')
find_words = [word.strip().lower() for word in find_words]
#print(find_words)
search_counts = dict.fromkeys(find_words, 0)

# make a counter for input word
print('\n******finding words*******')
for word in words:
    word = word.rstrip(",.").lower()
    if word in search_counts:
        search_counts[word] += 1
# print the frequency
print('\nNumber of times your word is used within', documentName + ":")
for word in find_words:
    print("   {:<20s} / {} occurrences".format(word, search_counts[word]))

