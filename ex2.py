from pathlib import Path 
def sortfun(x):
    return x[1], x[0]

p = Path.cwd()
p = p.joinpath("gray.txt")
line_count = 0
char_count = {}
words = []

with p.open("rt") as f:
    for line in f:
        line_count +=1
        split_line = line.split()
        for word in split_line:
            words.append(word.lower().strip(".,?!\n"))
        #print(line)
        for char in line.lower():
            char = char.lower()
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

char_total = sum(char_count.values())

print("Total lines:", line_count)
print("Total words:", len(words))
print("Total characters", char_total)
print("Character %:")
char_perc = {key : round(value/char_total*100, 2) for key, value in sorted(char_count.items(), reverse=True, key=sortfun)}
for key, value in char_perc.items():
    if value > 0:
        print(f"{key} : {value}%")

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

top_words = []
top_word_count = 0
#top_word_count = sorted(word_count.items(), key = sortfun)[-10:]
word_count = sorted(word_count.items(), reverse = True, key = sortfun)
for pair in word_count:
    if len(pair[0]) > 5 and top_word_count < 11:
        top_words.append(pair)
        top_word_count += 1
#print(top_words)

print("Top 10 words longer than 5 letters:")
for pair in top_words:
    print(f"{pair[0].capitalize()}: {pair[1]}")