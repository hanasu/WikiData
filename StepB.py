import bs4
import re
import codecs

f = codecs.open("small-corpus.xml", encoding="UTF-8")
contents = f.read()
soup = bs4.BeautifulSoup(contents, "html.parser")
cleaned = soup.get_text()
cleaned = re.sub(r'==+', "", cleaned)
pre = codecs.open('pre.txt', 'w', 'utf8')
pre.write(cleaned)
pre.close()
cleaned = re.sub(r'\*', "", cleaned)
post = codecs.open('post.txt', 'w', 'utf8')
post.write(cleaned)
post.close()
