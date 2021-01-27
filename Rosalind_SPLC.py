# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Codon table (copied from previous problem)

# Open data, loop for every intron, find start of intron and then, length. 

# Slice and get exons and swap T for U to make RNA.

# Translate using table, then print.

def main():
    table = {
        "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
        "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
        "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
        "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
        "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
        "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
        "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
        "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
        "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
        "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
        "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
        "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
        "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
        "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
        "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
        "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }
    file = open("rosalind_splc.txt", "r")
    lines = file.readlines()
    file.close()
    introns = []
    buffer = ''

    for line in lines:
        if line[0] == '>':
            if buffer:
                introns.append(buffer)
                buffer = ''
        else:
            buffer += line.replace('\n', '')
    introns.append(buffer)
    seq = introns.pop(0)

    for intron in introns:
        while intron in seq:
            start_idx = seq.find(intron)
            prefix = seq[:start_idx]
            suffix = seq[start_idx + len(intron):]
            seq = prefix + suffix

    seq = seq.replace('T', 'U')
    protein = ''
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i + 3]
        amino_acid = table[codon]
        if amino_acid == 'STOP':
            break
        else:
            protein += amino_acid
    print(protein)
    return

