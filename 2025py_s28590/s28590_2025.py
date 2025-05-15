# Cel programu:
# Program generuje losową sekwencję DNA, oblicza statystyki nukleotydowe,
# wstawia imię użytkownika w losowe miejsce sekwencji, a następnie zapisuje dane do pliku w formacie FASTA.

# Kontekst zastosowania:
# Program może być wykorzystywany do celów edukacyjnych, testowania narzędzi bioinformatycznych
# lub symulacji danych biologicznych. Format FASTA jest powszechnie używany w biologii molekularnej.

# Cel programu:
# Program generuje losową sekwencję DNA, oblicza statystyki nukleotydowe,
# wstawia imię użytkownika w losowe miejsce sekwencji, a następnie zapisuje dane do pliku w formacie FASTA.

# Kontekst zastosowania:
# Program może być wykorzystywany do celów edukacyjnych, testowania narzędzi bioinformatycznych
# lub symulacji danych biologicznych. Format FASTA jest powszechnie używany w biologii molekularnej.

import random  # Importuje moduł random, który umożliwia losowanie (np. liter w sekwencji DNA)

def generate_dna_sequence(length):
    """Generuje losową sekwencję DNA o podanej długości."""
    return ''.join(random.choices('ACGT', k=length))  # Losuje 'length' znaków z zestawu 'ACGT' i zwraca je jako jeden ciąg

def insert_name(sequence, name):
    """Wstawiam imię w losowe miejsce sekwencji, nie wpływając na jej skład."""
    insert_pos = random.randint(0, len(sequence))  # Wybiera losową pozycję w sekwencji
    return sequence[:insert_pos] + name + sequence[insert_pos:]  # Wstawia imię w wybraną pozycję i zwraca nową sekwencję

def calculate_statistics(sequence):
    """Obliczam procentową zawartość nukleotydów oraz stosunek CG do AT."""
    stats = {nuc: sequence.count(nuc) for nuc in 'ACGT'}  # Liczy wystąpienia każdego nukleotydu: A, C, G, T
    total = sum(stats.values())  # Oblicza łączną liczbę nukleotydów
    percentages = {nuc: round((count / total) * 100, 1) for nuc, count in stats.items()}  # Oblicza procentowy udział każdego nukleotydu
    cg = stats['C'] + stats['G']  # Liczy łączną liczbę nukleotydów C i G
    at = stats['A'] + stats['T']  # Liczy łączną liczbę nukleotydów A i T
    cg_at_ratio = round((cg / at) * 100, 1) if at > 0 else 0.0  # Oblicza stosunek CG do AT jako procent, o ile AT > 0
    return percentages, cg_at_ratio  # Zwraca słownik procentów i stosunek CG/AT

def format_fasta_sequence(seq, line_length=60):
    """Dzielę sekwencję na linie po określonej liczbie znaków (standard FASTA)."""
    return '\n'.join(seq[i:i+line_length] for i in range(0, len(seq), line_length))
    # Dzieli sekwencję na fragmenty co 60 znaków i łączy je w tekst oddzielony znakami nowej linii

def main():
    # Pobranie danych wejściowych od użytkownika
    try:
        length = int(input("Podaj długość sekwencji: "))  # Pobiera długość sekwencji jako liczbę całkowitą
    except ValueError:
        print("Długość musi być liczbą całkowitą.")  # Komunikat o błędzie w razie nieprawidłowego wejścia
        return  # Kończy działanie programu w przypadku błędu

    seq_id = input("Podaj ID sekwencji: ").strip()  # Pobiera i usuwa białe znaki z ID sekwencji
    description = input("Podaj opis sekwencji: ").strip()  # Pobiera i usuwa białe znaki z opisu sekwencji
    name = input("Podaj imię: ").strip()  # Pobiera i usuwa białe znaki z imienia

    dna_sequence = generate_dna_sequence(length)  # Generuje losową sekwencję DNA o zadanej długości

    # Obliczanie statystyk po wstawieniu imienia do sekwencji
    stats, cg_at_ratio = calculate_statistics(insert_name(dna_sequence, name))
    # Oblicza statystyki procentowe oraz stosunek CG/AT po wstawieniu imienia

    sequence_with_name = insert_name(dna_sequence, name)  # Wstawia imię do sekwencji w losowe miejsce (raz)

    formatted_sequence = format_fasta_sequence(sequence_with_name)  # Formatuje sekwencję do formatu FASTA (linie po 60 znaków)

    # Zapis do pliku FASTA
    filename = f"{seq_id}.fasta"  # Tworzy nazwę pliku na podstawie ID sekwencji

    with open(filename, 'w') as fasta_file:  # Otwiera plik FASTA do zapisu
        fasta_file.write(f">{seq_id} {description}\n")  # Zapisuje nagłówek FASTA
        fasta_file.write(formatted_sequence + "\n")  # Zapisuje sformatowaną sekwencję

    print(f"\nSekwencja została zapisana do pliku {filename}")  # Informuje o zapisaniu sekwencji
    print("Statystyki sekwencji:")  # Nagłówek dla statystyk

    for nuc in "ACGT":  # Iteruje przez nukleotydy
        print(f"{nuc}: {stats[nuc]} ({stats[nuc] / sum(stats.values()) * 100:.1f}%)")
        # Wyświetla liczbę i procentowy udział każdego nukleotydu

    print(f"%CG (stosunek CG do AT): {cg_at_ratio}")  # Wyświetla stosunek CG/AT w procentach

if __name__ == "__main__":  # Sprawdza, czy plik jest uruchamiany jako główny program
    main()  # Uruchamia funkcję główną

#Podsumowanie wprowadzonych ulepszeń:
#1. Obliczanie statystyk po wstawieniu imienia:
#na początku: statystyki były liczone na czystej sekwencji DNA.
#dodana modyfikacja: teraz są liczone po wstawieniu imienia, co lepiej odzwierciedla ostateczną zawartość pliku FASTA.

#Uzasadnienie: poprawność statystyk odzwierciedlających zawartość końcowej sekwencji.

#2. Dodanie funkcji format_fasta_sequence:
#na początku: cała sekwencja była zapisywana w jednej linii.
#dodana modyfikacja: sekwencja dzielona jest na linie po 60 znaków.

#Uzasadnienie: zgodność z konwencją formatu FASTA, ułatwia przetwarzanie danych przez narzędzia bioinformatyczne.

#3. Obsługa błędów przy wprowadzaniu długości sekwencji:
#na początku: brak walidacji wejścia.
#dodana modyfikacja: dodano try-except dla niepoprawnych danych wejściowych.

#Uzasadnienie: poprawa odporności programu na błędy użytkownika.
