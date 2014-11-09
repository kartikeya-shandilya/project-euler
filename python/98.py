
import string

f = open("words.txt")
words = f.readlines()[0].replace('"','').split(",")
letter = string.ascii_lowercase
wordLabel = {}; numbLabel = {}; wordAngrm = {}

def getLabel(word):
  temp = {}; i = 0; label = ""
  for char in word:
    if char not in temp:
      temp[char] = letter[i]
      i = i + 1
    label = label + temp[char]
  return label

for word in words:
  label = getLabel(word)
  angrm = "".join(sorted(list(word)))
  wordLabel[word] = label
  if angrm not in wordAngrm:
    wordAngrm[angrm] = []
  wordAngrm[angrm].append(word)

for numb in xrange(1,40000):
  label = getLabel(str(numb**2))
  if label not in numbLabel:
    numbLabel[label] = []
  numbLabel[label].append(str(numb**2))

for angrm in wordAngrm.keys():
  if len(wordAngrm[angrm])>1:
    word0 = wordAngrm[angrm][0]
    word1 = wordAngrm[angrm][1]
    label0 = wordLabel[word0]
    label1 = wordLabel[word1]
    if label0 in numbLabel.keys() and label1 in numbLabel.keys():
      numb0 = numbLabel[label0]
      numb1 = numbLabel[label1]
      for numb in numb0:
        assign = {}; angrm = ""
        for i in xrange(len(word0)):
          assign[word0[i]] = numb[i]
        for i in xrange(len(word1)):
          angrm = angrm + assign[word1[i]]
        if angrm in numb1:
          print word0, "=", numb, word1, "=", angrm


