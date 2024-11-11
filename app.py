def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def roman_to_int(s):
    roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(s.upper()):  # Convertir l'entrée en majuscules
        curr_value = roman_dict[char]
        if curr_value < prev_value:
            total -= curr_value
        else:
            total += curr_value
        prev_value = curr_value
    return total

def is_roman(s):
    roman_chars = set("IVXLCDM")
    return all(char in roman_chars for char in s.upper())

# Fonction principale pour l'interaction utilisateur
def main():
    input_value = input("Entrez un nombre entier ou un chiffre romain: ")
    
    if input_value.isdigit():
        num = int(input_value)
        print(f"Le chiffre romain pour {num} est: {int_to_roman(num)}")
    elif is_roman(input_value):
        print(f"L'entier pour {input_value} est: {roman_to_int(input_value)}")
    else:
        print("Entrée non valide. Veuillez entrer un nombre entier ou un chiffre romain.")

if __name__ == "__main__":
    main()
