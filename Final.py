import string
import re
import sys

def Nuclo_Slicer(Neucliotide, FilePassIn):
    Slicer2 = 90
    for Char in range(0, len(Neucliotide), Slicer2):
        NeuclioString = Neucliotide[Char: Slicer2]
        Slicer2 += 90
        FilePassIn.write(NeuclioString)
        FilePassIn.write("\n")


def Find_Proteins(Item, Dict):
    ReturnAA = ""
    for AminoAcid in Dict:
        if Item in AminoAcid:
            ReturnAA += Dict[AminoAcid]
            return ReturnAA        

def tRNA_Tranlation(mRNATranscribe):
    tRNATrans = mRNATranscribe.maketrans("AUCG", "UAGC")
    tRNA = mRNATranscribe.translate(tRNATrans)
    return tRNA

def Translation_Transcription(Sequence, Codon):
    ReturnDNA = []
    SanitizeTrans = Sequence.maketrans(string.ascii_lowercase, string.ascii_uppercase)
    Sanitize = Sequence.translate(SanitizeTrans)
    ReturnDNA.append(Sanitize)
    
    if Codon == "1": #Codon translation / transcription
        AntiTrans = Sanitize.maketrans("ATCG", "TAGC")
        AntiCodon = Sanitize.translate(AntiTrans)
        ReturnDNA.append(AntiCodon)
        mRNATrans = Sanitize.maketrans("ATCG", "UAGC")
        mRNA = Sanitize.translate(mRNATrans)
        ReturnDNA.append(mRNA)
    elif Codon == "2": #Anti-Codon translation / transcription
        CodonTrans = Sanitize.maketrans("ATCG", "TAGC")
        CodonTemp = Sanitize.translate(CodonTrans)
        ReturnDNA.append(CodonTemp)
        mRNATrans = CodonTemp.maketrans("ATCG", "UAGC")
        mRNA = CodonTemp.translate(mRNATrans)
        ReturnDNA.append(mRNA)
    elif Codon == "3": #mRNA translation / transcription
        CodonTrans = Sanitize.maketrans("AUCG", "TAGC")
        CodonTemp = Sanitize.translate(CodonTrans)
        ReturnDNA.append(CodonTemp)
        AntiTrans = CodonTemp.maketrans("ATCG", "TAGC")
        AntiCodon = CodonTemp.translate(AntiTrans)
        ReturnDNA.append(AntiCodon)
    return ReturnDNA

def Determine_Sequence():
    print("Please tell me the type of sequence you the file contains")
    FullSequence = input(
        "Press 1 for Codon\nPress 2 for Anti-Codon\nPress 3 for mRNA\nPress anything else to exit.\n"
    )
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
    FinalSanSequence = SanSequence2.replace("\n", "")
    return FinalSanSequence

def Slicing(mRNASlice):
    Slicer = 3
    SlicedSequence = []
    for Characters in range(0, len(mRNASlice), 3):
        SlicedSequence.append(mRNASlice[Characters: Slicer])
        Slicer += 3
    return SlicedSequence

def Create_New_File(EndAminoAcid, EndtRNA, EndProtein, EndCodon):
    with open("Sequence.txt", "w") as EndFile:
        EndFile.write("The protein for the DNA  is:\n")
        EndFile.write(EndProtein)
        EndFile.write("\n")
        EndFile.write("The tRNA Sequence is:\n")
        EndFile.write(EndtRNA)
        EndFile.write("\n")
        if EndCodon == "1":
            EndFile.write("The Codon Sequence is:\n")
            CodonSequence = EndAminoAcid[0]
            Nuclo_Slicer(CodonSequence, EndFile)
            EndFile.write("The Anti-Codon Sequence is:\n")
            CodonSequence = EndAminoAcid[1]
            Nuclo_Slicer(CodonSequence, EndFile)
            EndFile.write("The mRNA Sequence is:\n")
            CodonSequence = EndAminoAcid[2]
            Nuclo_Slicer(CodonSequence, EndFile)
        if EndCodon == "2":
            EndFile.write("The Codon Sequence is:\n")
            CodonSequence = EndAminoAcid[1]
            Nuclo_Slicer(CodonSequence, EndFile)
            EndFile.write("The Anti-Codon Sequence is:\n")
            CodonSequence = EndAminoAcid[0]
            Nuclo_Slicer(CodonSequence, EndFile)
            EndFile.write("The mRNA Sequence is:\n")
            CodonSequence = EndAminoAcid[2]
            Nuclo_Slicer(CodonSequence, EndFile)
        if EndCodon == "3":
            EndFile.write("The Codon Sequence is:\n")
            CodonSequence = EndAminoAcid[1]
            Nuclo_Slicer(CodonSequence, EndFile)
            EndFile.write("The Anti-Codon Sequence is:\n")
            CodonSequence = EndAminoAcid[2]
            Nuclo_Slicer(CodonSequence, EndFile)
            EndFile.write("The mRNA Sequence is:\n")
            CodonSequence = EndAminoAcid[0]
            Nuclo_Slicer(CodonSequence, EndFile)
        

def Main():
    # fMET = ("AUG")
    # STOP = ("UAA", "UAG", "UGA")
    # PHE = ("UUU", "UUC")
    # LEU = ("UUA", "UUG", "CUA", "CUU", "CUC", "CUG")
    # SER = ("UCU", "UCA", "UCG", "UCC", "AGU", "AGC")
    # TYR = ("UAC", "UAU")
    # CYS = ("UGU", "UGC")
    # TRP = ("UGG")
    # PRO = ("CCG", "CCA", "CCC", "CCU")
    # HIS = ("CAU", "CAC")
    # GLN = ("CAA", "CAG")
    # ARG = ("CGG", "CGC", "CGA", "CGU", "AGA", "AGG")
    # ILE = ("AUC", "AUA", "AUU")
    # THR = ("ACC", "ACU", "ACA", "ACG")
    # ASN = ("AAC", "AAU")
    # LYS = ("AAA", "AAG")
    # VAL = ("GUU", "GUA", "GUC", "GUG")
    # ALA = ("GCU", "GCA", "GCC", "GCG")
    # ASP = ("GAU", "GAC")
    # GLU = ("GAA", "GAG")
    # GLY = ("GGA", "GGC", "GGU", "GGG")

    AminoAcidDict = {
        ("AUG"): "MET",
        ("UAA", "UAG", "UGA"): "Stop",
        ("UUU", "UUC"): "PHE",
        ("UUA", "UUG", "CUA", "CUU", "CUC", "CUG"): "LEU",
        ("UCU", "UCA", "UCG", "UCC", "AGU", "AGC"): "SER",
        ("UAC", "UAU"): "TYR",
        ("UGU", "UGC"): "CYS",
        ("UGG"): "TRP",
        ("CCG", "CCA", "CCC", "CCU"): "PRO",
        ("CAU", "CAC"): "HIS",
        ("CAA", "CAG"): "GLN",
        ("CGG", "CGC", "CGA", "CGU", "AGA", "AGG"): "ARG",
        ("AUC", "AUA", "AUU"): "ILE",
        ("ACC", "ACU", "ACA", "ACG"): "THR",
        ("AAC", "AAU"): "ASN",
        ("AAA", "AAG"): "LYS",
        ("GUU", "GUA", "GUC", "GUG"): "VAL",
        ("GCU", "GCA", "GCC", "GCG"): "ALA",
        ("GAU", "GAC"): "ASP",
        ("GAA", "GAG"): "GLU",
        ("GGA", "GGC", "GGU", "GGG"): "GLY"
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
    if DNAType not in ["1","2","3","4"]:
        print("Have a nice day.")
        sys.exit()
    MainSequence = Sanitation(MainSequence)
    DNATranslations = Translation_Transcription(MainSequence, DNAType)
    mRNASequence = ""
    if DNAType == 1 or 2:
        mRNASequence += DNATranslations[2]
    if DNAType == 3:
        mRNASequence += DNATranslations[0]
    DNAStart = Find_Start(mRNASequence)
    SlicedDNAList = Slicing(DNAStart)
    ProteinStrand = []
    for AminoAcids in SlicedDNAList:
        ProteinStrand.append(Find_Proteins(AminoAcids, AminoAcidDict))
        if Find_Proteins(AminoAcids, AminoAcidDict) == "Stop":
            break
    tRNAList = []
    for tRNAAminos in SlicedDNAList:
        if Find_Proteins(tRNAAminos, AminoAcidDict) != "Stop":
            tRNAList.append(tRNA_Tranlation(tRNAAminos))
        else:
            break
    AminoAcidChain = " ".join(ProteinStrand)
    tRNAString = " ".join(tRNAList)
    Create_New_File(DNATranslations, tRNAString, AminoAcidChain, DNAType)

if __name__ == "__main__":
    Main()
