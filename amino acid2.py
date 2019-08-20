
def translate(rslt): 
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
    protein ="" 
    sm = False

    for i in range(0, len(rslt)):

        codon = rslt[i:i + 3]

        if codon == 'ATG':
            sm = True
            pos = i
            break
    
    if sm == True :
        
        for i in range(pos, len(rslt),3) :
            
            codon = rslt[i:i + 3]
            
            if codon in ['TAA', 'TAG', 'TGA']:
                return protein
            else: 
                protein += table[codon] 
                 
    return False
             

print(translate("ATGTCGTAA"))
