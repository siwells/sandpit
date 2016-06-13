from textblob import TextBlob

text = '''
The quick brown fox jumped over the lazy dog
'''

blob = TextBlob(text)
print blob.tags

