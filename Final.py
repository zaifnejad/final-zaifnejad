def Find_Proteins(String)
    fMET = "AUG"
    STOP = ["UAA", "UAG", "UGA"]
    PHE = ["UUU", "UUC"]
    LEU = ["UUA", "UUG", "CUA", "CUU", "CUC", "CUG"]
    SER = ["UCU", "UCA", "UCG", "UCC", "AGU", "AGC"]
    TYR = ["UAC", "UAU"]
    CYS = ["UGU", "UGC"]
    TRP = ["UGG"]
    PRO = ["CCG", "CCA", "CCC", "CCU"]
    HIS = ["CAU", "CAC"]
    GLN = ["CAA", "CAG"]
    ARG = ["CGG", "CGC", "CGA", "CGU", "AGA", "AGG"]
    ILE = ["AUC", "AUA", "AUU"]
    THR = ["ACC", "ACU", "ACA", "ACG"]
    ASN = ["AAC", "AAU"]
    LYS = ["AAA", "AAG"]
    VAL = ["GUU", "GUA", "GUC", "GUG"]
    ALA = ["GCU", "GCA", "GCC", "GCG"]
    ASP = ["GAU", "GAC"]
    GLU = ["GAA", "GAG"]
    GLY = ["GGA", "GGC", "GGU", "GGG"]

    ProteinsList = [fMET, STOP, PHE, LEU, SER, TYR, CYS, TRP, PRO, HIS, GLN, ARG, ILE, THR, ASN, LYS,, VAL, ALA, ASP, GLU, GLY]
    
    ReturnProtein = ""

    for Proteins in ProteinsList:
        for Protein in Proteins:
            if Protein == String:
                ReturnProtein += Protein
                return ReturnProtein
    

if __name__ = "__main__":
    Main()
