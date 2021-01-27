# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Define codon table

# Parse sequence and get reverse complementary

# Then, check for start codon ATG, when found, create prot and start adding aminoacids (3mer DNA)

# End protein when finding a stop codon and print

from Bio import SeqIO

table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

proteins = []
with open("rosalind_orf.txt", "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        s_frame = str(record.seq.strip())
        c_frame = s_frame.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c").upper()[::-1]
        frames = [s_frame, c_frame]
        for frame in frames:
            for i in range(len(frame)-2):
                codon = frame[i:i+3]
                if codon == 'ATG':
                    prot = ''
                    f=frame[i:]
                    start = 0
                    for c in range(len(f)//3):
                        cod = f[start:start+3]
                        start+=3
                        prot += table[cod]
                        if '_' in prot:
                            proteins.append(prot.split('_')[0])
for prot in set(proteins):
    print(prot)