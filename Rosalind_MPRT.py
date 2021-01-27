# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Parse input, request the FASTA for each ID, without header or any newlines. Replace entry with [ID, sequence] pair

# Then iterate over each letter in protein representation and check if all the 4 letters are correct

import urllib.request

def main():
    file = open("./rosalind_mprt.txt", "r")
    params = file.readlines()
    file.close()
    for i in range(len(params)):
        params[i] = params[i].replace('\n', '')

    for j in range(len(params)):
        prefix = "https://www.uniprot.org/uniprot/"
        suffix = ".fasta"
        url = prefix + params[j] + suffix
        fasta = urllib.request.urlopen(url).read()
        fasta = fasta.decode("utf-8")
        fasta = fasta[fasta.find('\n') + 1:]
        fasta = fasta.replace('\n', '')
        params[j] = [params[j], fasta]

    for k in range(len(params)):
        sequence = params[k][1]
        indices = []
        for idx in range(len(sequence) - 4):
            flag1 = sequence[idx] == 'N'
            flag2 = sequence[idx + 1] != 'P'
            flag3 = sequence[idx + 2] == 'S' or sequence[idx + 2] == 'T'
            flag4 = sequence[idx + 3] != 'P'
            if flag1 and flag2 and flag3 and flag4:
                indices.append(idx + 1)
        params[k][1] = indices

    for item in params:
        if item[1]:
            print(item[0])
            for num in item[1]:
                print(num, end=' ')
            print()
    return
