
# May Trinh 
# CMPS 4553 - Computational Methods
# This program searches through mycoplasma dna sequence and its reverse complement in genbank format and finds all open reading frames (ORFs) with start
# codon ATG and stop codon TAA, TAG , TGA. It only print genes that has more than 1000 nucleotides. Additionally, it translates the ORFs 
# to its corresponding amino acid sequence.

from Bio import SeqIO
from Bio.Seq import translate
import re

# Find ORF in Sequence
def find_orf(sequence):      
    # Find all ATG indexs
    start_indexs = []
    index = []
    stops =["TAA", "TAG", "TGA"]
    mark = 0

    # find start codon index
    for i in range(1, len(sequence)): # ORF 1, 2, 3
        if sequence[i:i+3] == "ATG": #group of 3 nucleotides
            start_indexs.append(i)


    for i in range(0, len(start_indexs)):
        if start_indexs[i] > mark: #start from the end of the previous ORF found
            for j in range (start_indexs[i], len(sequence),3):
                if sequence[j:j+3] in stops: #found stop codons
                    index.append((start_indexs[i], j+3)) #save the start and stop index of ORF found
                    mark = j + 3 #mark the end of the ORF just found. If another ATG is within the ORF, we ignore it
                    break #break out of for loop once ORF is found for a start index
    return index


with open("orfs.txt","w") as outf:
    outf.write("""
    May Trinh 
    CMPS 4553 - Computational Methods
    This program searches through mycoplasma dna sequence and its reverse complement and finds all open reading frames (ORFs) with start
    codon ATG and stop codon TAA, TAG , TGA. It only print genes that has more than 1000 nucleotides. Additionally, it translates the ORFs 
    to its corresponding amino acid sequence. \n\n""")

    outf.write("ORFs of original strand \n\n")
    outf.write("Length \t\tStart \t Stop  \t Sequence \n")
    # find ORFs in the sequence
    for seq_record in SeqIO.parse("mycoplasma.gb", "genbank"):
        record = seq_record.seq
        orfs = find_orf(record)

        # the normal way
        for s in orfs:
            length = s[1] - s[0]
            if length >= 1000: #only get gene with more than 1000 nucleotide in it
                orf = record[s[0]:s[1]]
                aa =  orf.translate(cds=True, table = "Bacterial") #translate ORF to amino acid
                outf.write(str(length) + "\t\t "  + str(s[0]) + "\t " + str(s[1]) + "\t " + str(orf)+  "\n")
                outf.write("Amino Acid: \t  \t\t  \t " + str(aa) + "\n")
            

        outf.write("\nORFs of reverse complement strand \n\n")
        outf.write("Length \t\tStart \t Stop  \t Sequence \n")

        # find orfs of reverse complement strand
        reverse = record.reverse_complement()
        orfReverse = find_orf(reverse)

        for s in orfReverse:
            length = s[1] - s[0]
            start = len(record) - s[1]
            stop = len(record) - s[0]
            if length >= 1000:
                orfR = reverse[s[0]:s[1]]
                orf = record[start:stop]
                # origin = orfR.reverse_complement()

                # this translation also works as well
                # aa =  orfR.translate(to_stop=True, table = 4) 
                aa =  orfR.translate(cds=True, table = "Bacterial")
                outf.write(str(length) + "\t\t "  + str(start) + "\t " + str(stop) + "\t " + str(orfR)+  "\n")
                outf.write("Orginal strand: \t \t\t " + str(orf)+"\n")
                outf.write("Amino Acid: \t  \t\t  \t " + str(aa) + "\n")


    




    
