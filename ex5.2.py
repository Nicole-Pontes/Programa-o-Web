phrase = input ("Type a phrase: ")
words = phrase.split()
words_with_a = [w for w in words if words in phrase]
replaced_a_by_o = [w.replace("a", "o") for w in words_with_a]
print(replaced_a_by_o)