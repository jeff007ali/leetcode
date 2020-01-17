def lenof(s):
    scanned = ""
    maxstr = ""
    for c in s:
        if c in scanned:
            if len(scanned) > len(maxstr):
                maxstr = scanned
            scanned = scanned.split(c)[1] + c
        else:
            scanned += c

    if len(scanned) > len(maxstr):
        maxstr = scanned
    print(maxstr)
    return len(maxstr)


print(lenof("dvdf"))
