def comp(seq):  #상보적 방식 함수
    comp_dict={'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    seq_comp=""
    for char in seq:
        if char in comp_dict:
            seq_comp = seq_comp + comp_dict[char]
        else:
            seq_comp = seq_comp + '?'
    return seq_comp
 
def rev(seq): #역순 방식 함수
    comp_dict={'A':'A', 'T':'T', 'C':'C', 'G':'G'}
    rev_str = "".join(reversed(seq))
    seq_rev = ""
    for char in rev_str:
        if char in comp_dict:
            seq_rev = seq_rev + comp_dict[char]
        else:
            seq_rev = seq_rev + '?'
    return seq_rev
 
def rev_comp(seq): #상보적 역순 방식 함수
    return (rev(comp(seq)))
 

option = int(input("1(DNA) 2(RNA)")) #DNA RNA 선택
src = input("seq: ")
cnvt = int(input("1(Comp) 2(Rev) 3(Rev_Comp)"))

if option == 2:
    src = src.replace("U", "T")

if cnvt == 1:
    rslt = comp(src)
elif cnvt == 2:
    rslt = rev(src)
else:
    rslt = rev_comp(src)

def translate(): 
    table = { 
        'ATA':'ILEU-', 'ATC':'ILEU-', 'ATT':'ILEU-', 'ATG':'MET-', 
        'ACA':'THR-', 'ACC':'THR-', 'ACG':'THR-', 'ACT':'THR-', 
        'AAC':'ASN-', 'AAT':'ASN-', 'AAA':'LYS-', 'AAG':'LYS-', 
        'AGC':'SER-', 'AGT':'SER-', 'AGA':'ARG-', 'AGG':'ARG-',                  
        'CTA':'LEU-', 'CTC':'LEU-', 'CTG':'LEU-', 'CTT':'LEU-', 
        'CCA':'PRO-', 'CCC':'PRO-', 'CCG':'PRO-', 'CCT':'PRO-', 
        'CAC':'HIS-', 'CAT':'HIS-', 'CAA':'GLN-', 'CAG':'GLN-', 
        'CGA':'ARG-', 'CGC':'ARG-', 'CGG':'ARG-', 'CGT':'ARG-', 
        'GTA':'VAL-', 'GTC':'VAL-', 'GTG':'VAL-', 'GTT':'VAL-', 
        'GCA':'ALA-', 'GCC':'ALA-', 'GCG':'ALA-', 'GCT':'ALA-', 
        'GAC':'ASP-', 'GAT':'ASP-', 'GAA':'GLU-', 'GAG':'GLU-', 
        'GGA':'GLY-', 'GGC':'GLY-', 'GGG':'GLY-', 'GGT':'GLY-', 
        'TCA':'SER-', 'TCC':'SER-', 'TCG':'SER-', 'TCT':'SER-', 
        'TTC':'PHE-', 'TTT':'PHE-', 'TTA':'LEU-', 'TTG':'LEU-', 
        'TAC':'TYR-', 'TAT':'TYR-', 'TAA':'_', 'TAG':'_', 
        'TGC':'CYS-', 'TGT':'CYS-', 'TGA':'_', 'TGG':'TRY-', 
    } 
    protein = "" 
    sm = False
    if len(rslt)%3 == 0: 
        for i in range(0, len(rslt), 3):
            codon = rslt[i:i + 3]
            if codon == 'ATG':
                sm = True
            if sm == True:
                if codon == ('TAA' or 'TAG' or 'TGA'):
                    return protein
                else: 
                    protein += table[codon]                  
    return False
print(translate())
