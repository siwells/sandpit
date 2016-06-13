from goose import Goose

#url = 'http://www.simonwells.org/teaching.html'
url = 'https://games.slashdot.org/story/16/06/13/1518207/microsoft-announces-the-xbox-one-s-its-smallest-xbox-yet'
g = Goose()
article = g.extract(url=url)
print article.title
print article.meta_description
print article.cleaned_text
