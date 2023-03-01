def print_index(textFile):
    count = {}
    for i in (something := textFile.readlines()):
        for j in i.split():
            if j in count:
                count[j].add(something.index(i) + 1)
            else:
                count[j] = {something.index(i) + 1}
    for word in sorted(count):
        print(f'{word}: {count[word]}')

def compare_files(textFile1, textFile2):
    file1Words = {i for x in textFile1.readlines() for i in x.split()}
    file2Words = {i for x in textFile2.readlines() for i in x.split()}
    return file1Words.intersection(file2Words), file1Words.union(file2Words)