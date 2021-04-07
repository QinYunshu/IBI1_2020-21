#from task1
genecode={'ATA':'I', 'ATC':'I','ATT':'I','ATG':'M','ACA':'T','ACC':'T','ACG':'T','ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R','CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P','CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q','CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R','GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A','GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G','TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L','TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_','TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
#from task 2
import os
import re
os.chdir("C:/Users/Lenovo/IBI1_2020-21/Practical8")
file1=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
file2=open('task3_protein_sequence.fa','w')
genes=file1.read()#read all the gene sequences
sequence=genes.split('>')#split sequences
gene_name=[]
gene_len=[]
protein_seq=[]
n=0
for aim in sequence:
    if 'unknown function' in aim:
        n=n+1
        name=re.findall(r'(\S+?)_',aim)[0]
        aim_=re.sub("\n", r"",aim)
        seq=re.findall(r']([^ ]+)',aim_)[0]
        a=len(seq)
        length=(a/3)
        gene_name.append(name)
        gene_len.append(length)
        amino_acid = ' '
        for i in range(0,a+1,3):
            condon = seq[i - 3:i]
            if condon in genecode:
                amino_acid = amino_acid + genecode[condon] + ' '
        protein_seq.append(amino_acid)

for i in range(0,n):
    file2.write(str(gene_name[i])+'\t'+str(gene_len[i])+'\n'+str(protein_seq[i])+'\n')
file1.close()
file2.close()
file2=open('task3_protein_sequence.fa','r')
read_=file2.read()
print(read_)