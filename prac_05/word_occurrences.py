def main():
    text = input("Text: ")
    words = text.split()

    word_and_counts = {}

    for word in words:
        if word in word_and_counts:
            word_and_counts[word] += 1
        else:
            word_and_counts[word] = 1

    for word in sorted(word_and_counts):
        print(f"{word:{len(max(word))}} = {word_and_counts[word]}")



main()