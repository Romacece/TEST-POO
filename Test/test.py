import os
import string
import random

def generate_random_string(length):
    # Générer une chaîne aléatoire de caractères de longueur spécifiée
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_test_file(total_lines=1000):
    # Création du fichier test.txt
    with open('test.txt', 'w') as f:
        for i in range(total_lines):
            # Si la ligne est impaire (index pair car on commence à 0)
            if i % 2 == 0:
                line = generate_random_string(30)
            else:
                line = ''
            f.write(line + '\n')

def split_file(filename, lines_per_file):
    # Lecture du fichier source
    with open(filename, 'r') as source:
        content = source.readlines()
    
    # Création du dossier pour les fichiers découpés s'il n'existe pas
    if not os.path.exists('split_files'):
        os.makedirs('split_files')
    
    # Découpage du fichier
    for i in range(0, len(content), lines_per_file):
        part_num = (i // lines_per_file) + 1
        with open(f'split_files/part_{part_num}.txt', 'w') as f:
            f.writelines(content[i:i + lines_per_file])

def main():
    total_lines = 1000
    lines_per_file = 100  # Chaque fichier enfant aura 100 lignes
    
    # Création du fichier test.txt
    print("Création du fichier test.txt...")
    create_test_file(total_lines)
    print("Fichier test.txt créé avec succès.")
    
    # Découpage du fichier
    print("Découpage du fichier en cours...")
    split_file('test.txt', lines_per_file)
    print(f"Découpage terminé. Les fichiers ont été créés dans le dossier 'split_files'.")
    
    # Affichage des informations
    num_files = len(os.listdir('split_files'))
    print(f"Nombre de fichiers créés : {num_files}")

if __name__ == "__main__":
    main()