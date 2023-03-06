import jieba
import jieba.posseg as pseg
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

doc = '经历台前幕后的多次打磨，这个作品终于呈现在大家面前，你们喜欢吗'
#C:\Windows\Fonts\simfang.ttf
fpath = '/Users/zhaojichang/Library/Fonts/Microsoft-YaHei.ttf'

terms = jieba.cut(doc)
terms = list(terms)
tfreq = Counter(terms)
for term in tfreq:
	print(f'{term}\t{tfreq[term]}')

wd = WordCloud(font_path=fpath)
wd.fit_words(tfreq)
#wd.to_file('./wd.png')
plt.imshow(wd)
plt.axis('off')
plt.show()

#words = pseg.cut(doc)
#for w, p in words:
#	print(f'{w}\t{p}')

ts=[]
with open('weibo.txt','r') as f:
	for line in f:
		for word, flag in pseg.cut(line.strip().split('\t')[1]):
			if flag == 'n':
				ts.append(word)
tfreq = Counter(ts)
wd = WordCloud(font_path=fpath, max_words=1000)
wd.fit_words(tfreq)
plt.imshow(wd, interpolation="bilinear")
plt.axis('off')
plt.show()
