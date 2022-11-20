kuvert_vikt = int(input("Kuvert ? "))
affisch_vikt = int(input("Affisch ? "))
blad_vikt = int(input("Blad ? "))

kuvert_area = (2*229*324)*1e-6
affisch_area = (2*297*420)*1e-6
blad_area = (210*297)*1e-6

total_vikt = kuvert_area*kuvert_vikt + \
    affisch_area*affisch_vikt + blad_area*blad_vikt

print("Svar:", "{0:.4f}".format(total_vikt))
