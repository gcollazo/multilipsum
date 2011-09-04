import string
import codecs
import json

f = codecs.open('text/design.txt', encoding='utf-8')
text = f.read()
f.close()

exclude = set(string.punctuation)
text = ''.join(ch for ch in text if ch not in exclude)
text = text.lower()
text = text.replace('\n', '')

text = text.split(' ')

distinct = set()
for w in text:
  if w not in distinct:
    distinct.add(w)

words = list(distinct)

print json.dumps(words)