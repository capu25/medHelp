import os
import re
import PyPDF2
import pandas as pd


def extract_data_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    # Regex per trovare righe che contengono un codice seguito da un punteggio totale
    matches = re.findall(r'(\d{13,14})\s+([-+]?\d*\.\d+|\d+)', text)

    # Dividi i dati in due liste: punteggi > 70 e punteggi <= 70
    data_above_70 = [(code, float(score)) for code, score in matches if float(score) > 70]
    data_below_or_equal_70 = [(code, float(score)) for code, score in matches if float(score) <= 70]

    return data_above_70, data_below_or_equal_70


def process_pdfs(directory):
    all_data_above_70 = []
    all_data_below_or_equal_70 = []

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            data_above_70, data_below_or_equal_70 = extract_data_from_pdf(pdf_path)
            all_data_above_70.extend(data_above_70)
            all_data_below_or_equal_70.extend(data_below_or_equal_70)

    return all_data_above_70, all_data_below_or_equal_70


def save_data_to_csv(data, output_file):
    df = pd.DataFrame(data, columns=["Codice", "Punti TOT"])
    df.to_csv(output_file, index=False)


# Directory dove si trovano i file PDF
directory = "./PDFs"
output_file_above_70 = "punteggi_maggiori_70.csv"
output_file_below_or_equal_70 = "punteggi_minori_o_uguali_70.csv"

# Processa i PDF e separa i dati
data_above_70, data_below_or_equal_70 = process_pdfs(directory)

# Salva i dati nei rispettivi file CSV
save_data_to_csv(data_above_70, output_file_above_70)
save_data_to_csv(data_below_or_equal_70, output_file_below_or_equal_70)

print(f"I punteggi maggiori di 70 sono stati salvati in {output_file_above_70}")
print(f"I punteggi minori o uguali a 70 sono stati salvati in {output_file_below_or_equal_70}")
