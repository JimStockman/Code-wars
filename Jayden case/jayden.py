
"""
  First the split will seperate each word contained in the quote.
  Then for each word, it's going to capitalize it.
  Finally it will join them back into a quote and return it
"""

quote = "How can mirrors be real if our eyes aren't real"

# Personnal code
def ToJaydenCase(string):
  charList = list(string)

  charList[0] = charList[0].upper()

  for i in range(len(charList)):
    if charList[i] == " ":
      charList[i + 1] = charList[i + 1].upper()

  return "".join(charList)

# Best solution
def BestToJaydenCase(string):
  return " ".join(w.capitalize() for w in string.split())


print(BestToJaydenCase(quote))
