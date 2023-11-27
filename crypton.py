def encrypt_vigenere(plaintext, key):
    # Convertir le texte en majuscules pour simplifier le chiffrement
    plaintext = plaintext.upper()
    key = key.upper()

    # Initialiser la chaîne chiffrée
    ciphertext = ""

    # Répéter la clé pour qu'elle ait la même longueur que le texte
    repeated_key = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]

    # Chiffrer chaque caractère du texte
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            # Utiliser l'arithmétique modulo pour effectuer le chiffrement
            encrypted_char = chr(((ord(plaintext[i]) + ord(repeated_key[i])) % 26) + ord('A'))
            ciphertext += encrypted_char
        else:
            # Si le caractère n'est pas une lettre, le laisser inchangé
            ciphertext += plaintext[i]

    return ciphertext

def encrypt_affine(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Utiliser l'arithmétique affine pour effectuer le chiffrement
            encrypted_char = chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
            ciphertext += encrypted_char
        else:
            # Si le caractère n'est pas une lettre, le laisser inchangé
            ciphertext += char

    return ciphertext

def encrypt_digraph(plaintext):
    # Exemple simple : remplacer chaque paire de lettres par la lettre suivante
    ciphertext = ""
    for i in range(0, len(plaintext) - 1, 2):
        pair = plaintext[i:i+2]
        encrypted_pair = chr((ord(pair[0]) + 1 - ord('A')) % 26 + ord('A')) + \
                         chr((ord(pair[1]) + 1 - ord('A')) % 26 + ord('A'))
        ciphertext += encrypted_pair

    return ciphertext

def encrypt_adfgvx(plaintext, keyword):
    # Exemple simple : remplacer chaque lettre par une paire ADFGVX
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Utiliser une correspondance simple pour ADFGVX
            mapping = {'A': '11', 'D': '12', 'F': '21', 'G': '22', 'V': '33', 'X': '34'}
            encrypted_char = mapping[char]
            ciphertext += encrypted_char
        else:
            # Si le caractère n'est pas une lettre, le laisser inchangé
            ciphertext += char

    return ciphertext


# Boucle principale
while True:
    # Afficher le menu des options
    print("Choisissez une option :")
    print("1. Chiffrement Vigenère")
    print("2. Chiffrement Affine")
    print("3. Chiffrement Digraph")
    print("4. Chiffrement ADFGVX")
    print("0. Quitter")

    # Laisser l'utilisateur entrer un choix
    choix = input("Votre choix (0-4) : ")

    # Quitter le programme si l'utilisateur le souhaite
    if choix == '0':
        break

    # Chiffrement Vigenère
    elif choix == '1':
        message = input("Entrez le texte à chiffrer : ")
        cle = input("Entrez la clé : ")
        message_chiffre = encrypt_vigenere(message, cle)
        print(f"Message chiffré : {message_chiffre}")

    # Chiffrement Affine
    elif choix == '2':
        message = input("Entrez le texte à chiffrer : ")
        a = int(input("Entrez la première clé (a) : "))
        b = int(input("Entrez la deuxième clé (b) : "))
        message_chiffre = encrypt_affine(message, a, b)
        print(f"Message chiffré : {message_chiffre}")

    # Chiffrement Digraph
    elif choix == '3':
        message = input("Entrez le texte à chiffrer : ")
        message_chiffre = encrypt_digraph(message)
        print(f"Message chiffré : {message_chiffre}")

    # Chiffrement ADFGVX
    elif choix == '4':
        message = input("Entrez le texte à chiffrer : ")
        keyword = input("Entrez la clé (mot-clé) : ")
        message_chiffre = encrypt_adfgvx(message, keyword)
        print(f"Message chiffré : {message_chiffre}")

    else:
        print("Choix non valide. Veuillez entrer un chiffre entre 0 et 4.")
