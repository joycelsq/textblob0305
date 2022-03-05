from textblob import TextBlob

f = open("news.txt")

d = f.read()

print(d)

TextBlob(d).sentiment