import os
import re
os.chdir("C:/Users/Lenovo/IBI1_2020-21/Practical8")
file1=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
file2=open('unkown_function.fa','w')
genes=file1.read()#read all the gene sequences
sequence=genes.split('>')#split sequences
gene_name=[]
gene_len=[]
gene_seq=[]
n=0

for aim in sequence:
    if 'unknown function' in aim:
        n=n+1
        name=re.findall(r'(\S+?)_',aim)[0]
        aim_=re.sub("\n", r"",aim)
        seq=re.findall(r']([^ ]+)',aim_)[0]
        length=len(seq)
        gene_name.append(name)
        gene_len.append(length)
        gene_seq.append(seq)

for i in range(0,n):
    file2.write(str(gene_name[i])+'\t'+str(gene_len[i])+'\n'+str(gene_seq[i])+'\n')
file1.close()
file2.close()
file2=open('unkown_function.fa','r')
read_=file2.read()
print(read_)