import re
DNA_strand=str(input('The DNA complement is: '))
def reverse_complement(DNA_strand):
    RNA={'A':'U','T':'A','C':'G','G':'C'}
    reverse=''#define reverse
    i=0
    for i in range(len(DNA_strand)):
        reverse = reverse+RNA[DNA_strand[i]]#run function in DNA sequence input
        i+=1
    print('The reverse complement is: '+reverse)
    return DNA_strand,i
z=reverse_complement(DNA_strand)