result = 0
images = {}

with open("input.txt", "r") as input:
    allLines = input.read().strip()
    rawImages = allLines.split("\n\n")
    # print(rawImages[0])
    for rawImage in rawImages:
        arr = rawImage.split("\n")
        image = arr[1:]
        id = int(arr[0][5:-1])
        images[id] = image.copy()


def showImage(image):
    return "\n".join(image)


def extractBorders(image):
    borders = [
        image[0],
        image[-1],
        "".join([line[0] for line in image]),
        "".join([line[-1] for line in image])
    ]
    return borders + [b[::-1] for b in borders]


def intersection(l1, l2):
    return [i for j in l2 for i in l1 if i == j]


def product(l1):
    p = 1
    for i in l1:
        p *= i
    return p


borders = {
    id: extractBorders(images[id]) for id in images
}

numShared = {
    id1: sum(
        [
            len(
                intersection(
                    borders[id1],
                    borders[id2]
                )
            ) for id2 in images if id2 != id1
        ]
    ) // 2 for id1 in borders
}


corners = [id for id in images if numShared[id] == 2]

# print(corners)

result = product(corners)

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))
