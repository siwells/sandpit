from textblob import TextBlob, Word

text = '''
The quick brown fox jumped over the lazy dog. Pack my box with five dozen liquor jugs
'''

blob = TextBlob(text)
print blob.tags

for sentence in blob.sentences:
    print sentence

for word in blob.sentences[1].words:
    print Word(word).lemmatize()
#    print Word(word).pluralize()

#for np in blob.noun_phrases:
#    print np

#for word, pos in blob.tags:
#    print word, pos


