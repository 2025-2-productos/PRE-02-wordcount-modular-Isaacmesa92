import os

def write_count_words(counter):
    # Verifica si el directorio 'data/output' existe, si no, lo crea.
    if not os.path.exists("data/output"):
        os.makedirs("data/output")

    # save the results using tsv format
    # Abre el archivo 'data/output/results.tsv' en modo escritura ('w') con codificación UTF-8
    with open("data/output/results.tsv", "w", encoding="utf-8") as f:
        # Itera sobre los pares clave-valor (palabra y conteo) en el objeto 'counter'
        for key, value in counter.items():
            # write the key and value to the file
            # Escribe la clave, un tabulador ('\t'), el valor y un salto de línea ('\n')
            # Esto crea un formato TSV (Valores Separados por Tabuladores)
            f.write(f"{key}\t{value}\n")