"""BCM2550 - TP2 - VOTRE NOM"""

def main():
    """BCM2550 - TP2"""
    
    nb_biallelique = 0
    with open ("NA12878.vcf") as f, \
         open ("results.csv", "w") as out_f:
        
        for line in f:
        
            if line.startswith("#"):
                continue
            
            row = line.rstrip().split("\t")

            chromosome = row[0]
            position = row[1]
            allele_ref = row[3]
            allele_alt = row[4]

            variant_id = f"{chromosome}:{position}:{allele_ref}"

            liste_alternatif = allele_alt.split(",")
            nb_allele = 1 + len(liste_alternatif)

            if nb_allele == 2:
                nb_biallelique += 1
                
            alt_format = "/".join(liste_alternatif)
            print(f"{variant_id},{nb_allele},{allele_ref},{alt_format}",file=out_f)

    print(f"le nombre de variation ballelique est: {nb_biallelique:,d}")

if __name__ == "__main__":
    main()