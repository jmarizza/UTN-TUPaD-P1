compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")

if "fideos" in compras[1]:
    indice_fideos = compras[1].index("fideos")
    compras[1][indice_fideos] = "tallarines"

if "pan" in compras[0]:
    compras[0].remove("pan")

print(compras)