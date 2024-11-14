from flask import Flask, request, render_template

app = Flask(__name__)

valeurs = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symboles_romains = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def convertir_entier_en_romain(nombre):
    resultat = []
    for i in range(len(valeurs)):
        while nombre >= valeurs[i]:
            resultat.append(symboles_romains[i])
            nombre -= valeurs[i]
    return ''.join(resultat)

def convertir_romain_en_entier(chaine):
    roman_vers_entier = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultat, valeur_precedente = 0, 0
    for caractere in reversed(chaine):
        valeur = roman_vers_entier[caractere]
        if valeur >= valeur_precedente:
            resultat += valeur
        else:
            resultat -= valeur
        valeur_precedente = valeur
    return resultat

@app.route('/', methods=['GET', 'POST'])
def index():
    resultat = ''
    if request.method == 'POST':
        entree_utilisateur = request.form['input']
        try:
            nombre = int(entree_utilisateur)
            resultat = f"{nombre} en chiffres romains: {convertir_entier_en_romain(nombre)}"
        except ValueError:
            resultat = f"{entree_utilisateur} en entier: {convertir_romain_en_entier(entree_utilisateur)}"
    return render_template('index.html', resultat=resultat)

if __name__ == "__main__":
    app.run(debug=True)
