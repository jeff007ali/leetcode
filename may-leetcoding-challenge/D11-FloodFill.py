def floodFill(image, sr, sc, newColor):
    lr = len(image)
    lc = len(image[0])
    oldColor = image[sr][sc]

    def recurr(r, c):
        if (not (0 <= r < lr and 0 <= c < lc)) or image[r][c] != oldColor:
            return

        image[r][c] = newColor
        recurr(r - 1, c)
        recurr(r + 1, c)
        recurr(r, c - 1)
        recurr(r, c + 1)

    if newColor != oldColor:
        recurr(sr, sc)

    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))