c = []
count = 0
with open('reviews.txt', 'r') as a:
    for b in a:
        c.append(b)
        count += 1
        if count % 1000 == 0:
            print(len(c))
print('共有', len(c), '筆資料')
d = 0
for line in c:
    d = d + len(line)
print('平均留言長度', d/len(c))


            


