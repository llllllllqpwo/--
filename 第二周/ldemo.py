import jieba
from collections import Counter

ts = []
#1
with open("weibo.txt", "r") as f:
    for line in f:
        #2
        for word in jieba.cut(line.split("\t")[1]):
            ts.append(word)
#3
tfreq = Counter(ts)
print(tfreq.most_common(10))
print(tfreq.most_common()[-11:-1])
#4
