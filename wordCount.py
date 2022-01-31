def wordCount(inpt, outpt):
    with open(inpt) as f:
        lines = f.readlines()

    words = dict()

    for line in line:
        line = line.replace(",", "")
        line = line.replace(".", "")
        line = line.replace(":", "")
        line = line.replace(";", "")

        for word in line.split():
            word = word.lower()
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1

    f = open(outpt, "w")
    for i in sorted (words.keys()):
        f.write(i+ " " + str(words[i]) + "\n")
    f.close()

