sp = ['text2.txt', 'text1.txt', 'text3.txt']
files = {}
for i in sp:
    with open(i, 'r', encoding='UTF-8') as f:
        s = [i.rstrip('\n') for i in f.readlines()]
        files[i] = [len(s), s]
files = {k: v for k, v in sorted(files.items(), key=lambda item: item[0])}
with open('res.txt', 'w', encoding='UTF-8') as f:
    for i in files:
        f.write(i + '\n')
        f.write(str(files[i][0]) + '\n')
        for j in files[i][1]:
            f.write(j + '\n')
    f.close()

