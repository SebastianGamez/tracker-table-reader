import  csv

def read_data(file):

    # Listas de datos a obtener del archivo

    x: list = []
    t: list = []

    # Se obtienen los datos y se transforman en su tipopara ser manipulados
    with open(file, "r") as document:
        lines = [line for line in document][2:]

        for line in lines:
            values = line.split("\t")
            t.append(float(values[0].replace(",", ".").replace("\t", "")))
            x.append(float(values[1].replace(",", ".").replace("\n", "").replace("E", "e")))

    # Se calculan nuevas medidas indirectas
    # Velocidad y su instánte de tiempo
    v: list = [(x[i] - x[i - 1]) / (t[i] - t[i - 1]) for i in range(1, len(t))]
    tv = [(t[i] + t[i - 1]) / 2 for i in range(1, len(t))]

    # Aceleración y su instánte de tiempo
    a: list = [(v[i] - v[i - 1]) / (tv[i] - tv[i - 1]) for i in range(1, len(tv))]
    ta = [(tv[i] + tv[i - 1]) / 2 for i in range(1, len(tv))]

    # Promedio de los datos obtenidos
    x_average = sum(x) / len(x)
    v_average = sum(v) / len(v)
    a_average = sum(a) / len(a)

    # Cambio de notación científica a decimal
    x = ["{:f}".format(i) for i in x]
    t = ["{:f}".format(i) for i in t]

    v = ["{:f}".format(i) for i in v]
    tv = ["{:f}".format(i) for i in tv]

    a = ["{:f}".format(i) for i in a]
    ta = ["{:f}".format(i) for i in ta]

    # Se escribe la información en un nuevo archivo
    with open(f"{file.replace('.txt', '')}_result.csv", "w") as document:
        writer = csv.writer(document)
        writer.writerow(["xPromedio", "vPromedio", "aPromedio"])
        writer.writerow([x_average, v_average, a_average])
        writer.writerow([])
        writer.writerow(["t", "x", "", "t", "v", "", "t", "a"])
        for i in range(len(t)):

            row = []

            row.append(t[i])
            row.append(x[i])
            row.append("")

            if i < len(tv):
                row.append(tv[i])
                row.append(v[i])
            else:
                row.append("")
                row.append("")

            row.append("")

            if i < len(ta):
                row.append(ta[i])
                row.append(a[i])
            else:
                row.append("")
                row.append("")

            row.append("")

            writer.writerow(row)


for i in range(1, 7):
    read_data(f"./{i}.txt")

