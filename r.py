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

new = []
for line in c:
	if len(line) < 100:
		new.append(line)
print('一共有', len(new), '筆資料長度小於100')		
print(new[0])
print(new[1])

good =[]
for line in c:
	if 'good' in line:
		good.append(line)
print('一共有', len(good), '筆資料提到good')
print(good[0])		



            


