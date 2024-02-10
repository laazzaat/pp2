def reversing(stroka):
    words = stroka.split()
    reversed_words = words[::-1]
    reversed_sent = " ".join(reversed_words)

    return reversed_sent

stroka = input("Enter a sentence: ")
reverse = reversing(stroka)
print("Reversed sentence:", reverse)