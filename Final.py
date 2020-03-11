import string
import re

def Find_Proteins(Item, Dict):
    ReturnAA = ""
    for AminoAcid in Dict:
        if Item in AminoAcid:
            ReturnAA += Dict[AminoAcid]
            return ReturnAA
    return "Stop"

def tRNA_Tranlation(mRNATranscribe):
    tRNATrans = mRNATranscribe.maketrans("AUCG", "UAGC")
    tRNA = mRNATranscribe.translate(tRNATrans)
    return tRNA

def Translation_Transcription(Sequence, Codon):
    ReturnDNA = []
    SanitizeTrans = Sequence.maketrans(string.ascii_lowercase, string.ascii_uppercase)
    Sanitize = Sequence.translate(SanitizeTrans)
    ReturnDNA.append(Sanitize)
    
    if Codon == 1: #Codon translation / transcription
        TemplateTrans = Sanitize.maketrans("ATCG", "TAGC")
        Template = Sanitize.translate(TemplateTrans)
        ReturnDNA.append(Template)
        mRNATrans = Sanitize.maketrans("ATCG", "UAGC")
        mRNA = Sanitize.translate(mRNATrans)
        ReturnDNA.append(mRNA)
    elif Codon == 2: #Template translation / transcription
        CodonTrans = Sanitize.maketrans("ATCG", "TAGC")
        CodonTemp = Sanitize.translate(CodonTrans)
        ReturnDNA.append(CodonTemp)
        mRNATrans = CodonTemp.maketrans("ATCG", "UAGC")
        mRNA = CodonTemp.translate(mRNATrans)
        ReturnDNA.append(mRNA)
    elif Codon == 3: #mRNA translation / transcription
        CodonTrans = Sanitize.maketrans("AUCG", "TAGC")
        CodonTemp = Sanitize.translate(CodonTrans)
        ReturnDNA.append(CodonTemp)
        TemplateTrans = CodonTemp.maketrans("ATCG", "TAGC")
        Template = CodonTemp.translate(TemplateTrans)
        ReturnDNA.append(Template)
    elif Codon == 4: #tRNA translation / transcription
        CodonTrans = Sanitize.maketrans("AUCG", "TAGC")
        CodonTemp = Sanitize.translate(CodonTrans)
        ReturnDNA.append(CodonTemp)
        TemplateTrans = CodonTemp.maketrans("ATCG", "TAGC")
        Template = CodonTemp.translate(TemplateTrans)
        ReturnDNA.append(Template)
        mRNATrans = Sanitize.maketrans("AUCG", "UAGC")
        mRNA = Sanitize.translate(mRNATrans)
        ReturnDNA.append(mRNA)
    return ReturnDNA

def Determine_Sequence():
    print("Please tell me the type of sequence you the file contains")
    FullSequence = input(
        "Press 1 for Codon\nPress 2 for Anti-Codon\nPress 3 for mRNA\nPress 4 for tRNA\nPress anything else to exit."
    )
    #if FullSequence != 1 or 2 or 3 or 4:
    #    print("Have a nice day.")
    return FullSequence

def Find_Start(SearchSequence):
    StartSequence = ""
    CutSequence = re.findall(r'AUG\w+', SearchSequence)
    StartSequence += CutSequence[0]
    return StartSequence

def Get_Sequence(File):
    with open(File, "r") as SequenceFile:
        ReturnFile = SequenceFile.readlines()
    return ReturnFile

def Sanitation(UnsanSequence):
    SanSequence1 = ""
    SanSequence1 = SanSequence1.join(UnsanSequence)
    SanSequence2 = SanSequence1.strip()
    FinalSanSequence = SanSequence2.replace(" ", "")
    return FinalSanSequence

def Slicing(mRNASlice):
    Slicer = 3
    SlicedSequence = []
    for Characters in range(0, len(mRNASlice), 3):
        SlicedSequence.append(mRNASlice[Characters: Slicer])
        Slicer += 3
    return SlicedSequence

def Create_New_File(EndAminoAcid, EndtRNA, EndProtein, EndCodon):
    with open("Sequence.txt", "a") as EndFile:
        # EndFile.append("The protein for the DNA  is:")
        # EndFile.append(EndProtein)
        # if EndCodon == 1:
        #     EndFile.append("The Codon Sequence is:")
        #     EndFile.append(EndAminoAcid[0])
        #     EndFile.append("The Template Sequence is:")
        #     EndFile.append(EndAminoAcid[1])
        #     EndFile.append("The mRNA Sequence is:")
        #     EndFile.append(EndAminoAcid[2])
        # if EndCodon == 2:
        #     EndFile.append("The Codon Sequence is:")
        #     EndFile.append(EndAminoAcid[1])
        #     EndFile.append("The Template Sequence is:")
        #     EndFile.append(EndAminoAcid[0])
        #     EndFile.append("The mRNA Sequence is:")
        #     EndFile.append(EndAminoAcid[2])
        # if EndCodon == 3:
        #     EndFile.append("The Codon Sequence is:")
        #     EndFile.append(EndAminoAcid[1])
        #     EndFile.append("The Template Sequence is:")
        #     EndFile.append(EndAminoAcid[2])
        #     EndFile.append("The mRNA Sequence is:")
        #     EndFile.append(EndAminoAcid[0])
        # if EndCodon == 4:
        #     EndFile.append("The Codon Sequence is:")
        #     EndFile.append(EndAminoAcid[1])
        #     EndFile.append("The Template Sequence is:")
        #     EndFile.append(EndAminoAcid[2])
        #     EndFile.append("The mRNA Sequence is:")
        #     EndFile.append(EndAminoAcid[3])
        # EndFile.append("The tRNA Sequence is:")
        # EndFile.append(EndtRNA)
        print(EndProtein, EndtRNA)

def Main():
    fMET = "AUG"
    STOP = ("UAA", "UAG", "UGA")
    PHE = ("UUU", "UUC")
    LEU = ("UUA", "UUG", "CUA", "CUU", "CUC", "CUG")
    SER = ("UCU", "UCA", "UCG", "UCC", "AGU", "AGC")
    TYR = ("UAC", "UAU")
    CYS = ("UGU", "UGC")
    TRP = ("UGG")
    PRO = ("CCG", "CCA", "CCC", "CCU")
    HIS = ("CAU", "CAC")
    GLN = ("CAA", "CAG")
    ARG = ("CGG", "CGC", "CGA", "CGU", "AGA", "AGG")
    ILE = ("AUC", "AUA", "AUU")
    THR = ("ACC", "ACU", "ACA", "ACG")
    ASN = ("AAC", "AAU")
    LYS = ("AAA", "AAG")
    VAL = ("GUU", "GUA", "GUC", "GUG")
    ALA = ("GCU", "GCA", "GCC", "GCG")
    ASP = ("GAU", "GAC")
    GLU = ("GAA", "GAG")
    GLY = ("GGA", "GGC", "GGU", "GGG")

    AminoAcidDict = {
        fMET: "MET",
        STOP: "Stop",
        PHE: "PHE",
        LEU: "LEU",
        SER: "SER",
        TYR: "TYR",
        CYS: "CYS",
        TRP: "TRP",
        PRO: "PRO",
        HIS: "HIS",
        GLN: "GLN",
        ARG: "ARG",
        ILE: "ILE",
        THR: "THR",
        ASN: "ASN",
        LYS: "LYS",
        VAL: "VAL",
        ALA: "ALA",
        ASP: "ASP",
        GLU: "GLU",
        GLY: "GLY"
    }
    while True:
        FileOpen = input("Please give me the name the .txt file with the DNA sequence:\n")
        try:
            MainSequence = Get_Sequence(FileOpen)
        except FileNotFoundError:
            print("The file name given can not be found.")
            continue
        break
    DNAType = Determine_Sequence()
    #if DNAType != 1 or 2 or 3 or 4:
    #    quit()
    MainSequence = Sanitation(MainSequence)
    DNATranslations = Translation_Transcription(MainSequence, DNAType)
    mRNASequence = ""
    if DNAType == 1 or 2:
        mRNASequence += DNATranslations[2]
    if DNAType == 3:
        mRNASequence += DNATranslations[0]
    if DNAType == 4:
        mRNASequence += DNATranslations[3]
    DNAStart = Find_Start(mRNASequence)
    SlicedDNAList = Slicing(DNAStart)
    ProteinStrand = []
    for AminoAcids in SlicedDNAList:
        ProteinStrand.append(Find_Proteins(AminoAcids, AminoAcidDict))
        if Find_Proteins(AminoAcids, AminoAcidDict) == "Stop":
            break
    tRNAList = []
    for tRNAAminos in SlicedDNAList:
        if Find_Proteins(AminoAcids, AminoAcidDict) != "Stop":
            tRNAList.append(tRNA_Tranlation(tRNAAminos))
        else:
            break
    AminoAcidChain = ""
    for AA in ProteinStrand:
        AminoAcidChain += AA
        AminoAcidChain += " "
    Create_New_File(DNATranslations, tRNAList, AminoAcidChain, DNAType)

if __name__ == "__main__":
    Main()
