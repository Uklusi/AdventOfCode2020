import re

result = 0
imageFrames = {}


with open("input.txt", "r") as input:
    allLines = input.read().strip().replace(".", " ")
    rawimageFrames = allLines.split("\n\n")
    for rawimageFrame in rawimageFrames:
        arr = rawimageFrame.split("\n")
        imageFrame = arr[1:]
        id = int(arr[0][5:-1])
        imageFrames[id] = imageFrame.copy()


def showImage(image):
    return "\n".join(image)


def extractBorders(imageFrame):
    borders = {
        imageFrame[0]: "0",
        imageFrame[-1][::-1]: "180",
        "".join([line[0] for line in imageFrame][::-1]): "270",
        "".join([line[-1] for line in imageFrame]): "90"
    }
    borders.update({b[::-1]: borders[b] + "F" for b in borders})
    return borders


def extractImage(imageFrame):
    return [line[1:-1] for line in imageFrame[1:-1]]


def intersection(l1, l2):
    return [i for j in l2 for i in l1 if i == j]


def product(l1):
    p = 1
    for i in l1:
        p *= i
    return p


def rotateImage(image, angle):
    if angle == 0:
        return image
    imagerot = [
        "".join(
            [
                line[i] for line in image
            ]
        ) for i in range(len(image) - 1, -1, -1)
    ]
    return rotateImage(imagerot, angle - 90)


def flipImage(image, isFlipped, orient1):
    if isFlipped:
        if (orient1//90) %2 == 0:
            return [
                line[::-1] for line in image
            ]
        else:
            return image[::-1]
    else:
        return image


def rotateImageFrame(borders, id1, id2, intersect, imageFrames):
    if len(intersect) == 0:
        return
    border = intersect[0]
    orient1 = borders[id1][border]
    iFrame = imageFrames[id2]

    if "F" in orient1:
        orient1 = orient1[:-1]
        border = border[::-1]
    
    orient2 = borders[id2][border[::-1]]

    orient1Int = int(orient1)
    isFlipped = False
    if "F" in orient2:
        isFlipped = True
        orient2 = orient2[:-1]
    orient2Int = int(orient2)

    r = (orient2Int - orient1Int - 180) % 360
    newIFrame = rotateImage(iFrame, r)
    newIFrame = flipImage(newIFrame, isFlipped, orient1Int)
    imageFrames[id2] = newIFrame.copy()

    borders[id2] = extractBorders(newIFrame)


# No border is symmetryc THANK GOD
borders = {
    id: extractBorders(imageFrames[id]) for id in imageFrames
}

ids = list(imageFrames.keys())
idsToCheck = [ids[0]]
idsChecked = []

neighs = {
    id: {} for id in ids
}


while len(idsToCheck) > 0:
    id1 = idsToCheck.pop()

    for id2 in ids:
        if id2 in idsChecked or id2 == id1:
            continue
        intersect = intersection(
            borders[id1],
            borders[id2]
        )
        if len(intersect) == 0:
            continue
        rotateImageFrame(
            borders,
            id1,
            id2,
            intersect,
            imageFrames
        )
        r0 = borders[id1][intersect[0]]
        if "F" in r0:
            r0 = r0[:-1]
        r = int(r0)
        neighs[id1][r] = id2
        neighs[id2][(r - 180) % 360] = id1
        if id2 not in idsToCheck:
            idsToCheck.append(id2)
    idsChecked.append(id1)

images = {
    id: extractImage(imageFrames[id]) for id in imageFrames
}

topLeftCornerId = [id for id in ids if set(neighs[id].keys()) == {90, 180}][0]
bigImage0 = images[topLeftCornerId].copy()

right = neighs[topLeftCornerId][90]
down = neighs[topLeftCornerId][180]
l = len(images[topLeftCornerId])

while right is not None or down is not None:
    if right is not None:
        for i in range(1, l + 1):
            bigImage0[-i] += images[right][-i]
        right = neighs[right].get(90)
    elif down is not None:
        bigImage0 += images[down]
        right = neighs[down].get(90)
        down = neighs[down].get(180)


pattern = [
    "..................#.",
    "#....##....##....###",
    ".#..#..#..#..#..#..."
]

l0 = len(bigImage0[0])
l1 = l0 - len(pattern[0])

compiledREs = []
for i in range(l1 + 1):
    compiledREs.append(re.compile(
        r"((?:^|\n).{" + str(i) + "})" + pattern[0] + "(.{" + str(l1 - i) + r"}\n" +
        ".{" + str(i) + "})" + pattern[1] + "(.{" + str(l1 - i) + r"}\n" +
        ".{" + str(i) + "})" + pattern[2] + "(.{" + str(l1 - i) + r"}(?:$|\n))"
    ))

s = 0
bigImageString = ""
for i in range(0, 360, 90):
    bigImage = rotateImage(bigImage0, i)
    bigImageString = "\n".join(bigImage)
    match = []
    for compiledRE in compiledREs:
        match.append(len(compiledRE.findall(bigImageString)))
    s = sum(match)
    if s > 0:
        break
    bigImage = flipImage(bigImage, True, 0)
    bigImageString = "\n".join(bigImage)
    match = []
    for compiledRE in compiledREs:
        match.append(len(compiledRE.findall(bigImageString)))
    s = sum(match)
    if s > 0:
        break


result = bigImageString.count("#")
result -= s * "\n".join(pattern).count("#")

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))
