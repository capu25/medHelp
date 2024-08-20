import pandas as pd


def convert_csv_to_readable_format(csv_file, output_file):
    # Legge il file CSV
    df = pd.read_csv(csv_file)

    # Crea un contenuto formattato
    formatted_text = ""
    for index, row in df.iterrows():
        formatted_text += f"Codice: {row['Codice']}, Codice: {row['Codice']}\n"

    # Salva il contenuto formattato in un file di testo
    with open(output_file, 'w') as file:
        file.write(formatted_text)

    print(f"I dati sono stati salvati in formato leggibile in {output_file}")


# Esempio di utilizzo
csv_file = "punteggi_maggiori_70.csv"
output_file = "punteggi_maggiori_70.txt"

convert_csv_to_readable_format(csv_file, output_file)
