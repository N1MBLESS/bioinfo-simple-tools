"""Zacharie Blanchard"""

from donnes import GENETIC_CODE
import sys

def main():
    """ Cette fonction sert a lire une sequence ADN Codant et la convertie 
    en ARNm ensuite elle traduit cette sequence en nucleotides """
    #variables pour la foncion main
    sequence = input("mettre la sequence d'ADN ici: ").upper()

    valid_nucleotide = set("ACGT")
    position = 0
    amino_acid = ""
    rna_sequence = ""

    valid_dna_seq = True
    for nucleotide in sequence:
        # verifier que la sequence est valide
        if nucleotide not in valid_nucleotide:
            sys.exit(nucleotide + " is not a valid nucleotide...")
            valid_dna_seq = False
        # Transcription ADN vers ARN
        if nucleotide == "T":
            rna_sequence += "U"
        else:
            rna_sequence += nucleotide

    #verifier que la sequence d'ARN est valide
    valid_rna_seq = True
    nuc_start = ["AUG"]
    nuc_end = ["UAA","UGA","UAG"]
    if valid_dna_seq:
        if len(rna_sequence) % 3 != 0:
            sys.exit("RNA sequence not valid:",len(rna_sequence),
                "is not a multiple of 3")
            valid_rna_seq = False

        if rna_sequence[:3] not in nuc_start:
            sys.exit("RNA sequence not valid:",
                rna_sequence[:3], "is not a start codon")
            valid_rna_seq = False

        if rna_sequence[-3:] not in nuc_end:
            sys.exit("RNA sequence not valid:",
                rna_sequence[-3:],"is not an stop codon")
            valid_rna_seq = False

    #traduction seqence ARN vers Peptides
    if valid_rna_seq and valid_dna_seq:
        while position < len(rna_sequence):
            amino_acid += GENETIC_CODE[rna_sequence[position: position + 3]]
            position += 3
        print("proteine: ", amino_acid)

if __name__ == "__main__":
    main()
