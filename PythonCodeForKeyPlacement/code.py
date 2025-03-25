f = open("file.txt","w")

cx = 180
cy = 170
spacing = 1
keyPadding = cy + spacing - 2
keySpread = cx + spacing
stringStart = "<&key_physical_attrs "
locations = {}
stagger = {0:0,1:0,2:8,3:5,4:-5,5:0}

currentX = 0
currentY = 0
firstY = 0
for r in range(4):
    if r == 0:
        currentX += 100
        for c in range(10):
            if c > 4 and c < 5:
                currentX = currentX + 1000
            currentY += stagger.get(c, 0)
            f.write(f'{stringStart}{cx} {cy} {currentX} {currentY} 0 0 0>\n,')
            currentX += 100
        continue
    for c in range(12):
        if c > 5 and c < 6:
            currentX += 1000
        currentY += stagger.get(c, 0)
        f.write(f'{stringStart}{cx} {cy} {currentX} {currentY} 0 0 0>\n,')
        currentX = currentX + 100
    firstY = firstY - keyPadding
    currentY = firstY
    currentX = 0
f.close()