from django.shortcuts import render

# Create your views here.


def home(request):
    # Ein String (Zeichenkette)
    titel_der_webseite = 'Rechnen mit Python'
    # Ein Integer (Ganzzahl)
    zahl_1 = 5
    zahl_2 = 3
    # Ein Float (Kommazahl) => Im Englischen wird der Punkt verwendet!
    kommazahl_1 = 1.5
    kommazahl_2 = 3.5

    # Mit Python können wir rechnen!
    ergebnis_zahlen = zahl_1 + zahl_2
    ergebnis_kommazahlen = kommazahl_1 + kommazahl_2

    # Damit das funktioniert muss der Datentyp übereinstimmen.
    # Der Unterschied ist gut erkennbar, wenn man versucht mit
    # Strings zu rechnen:
    string_zahl_1 = '5'
    string_zahl_2 = '3'
    string_kommazahl_1 = '1.5'
    string_kommazahl_2 = '3.5'
    seltsames_ergebnis1 = string_zahl_1 + string_zahl_2
    seltsames_ergebnis2 = string_kommazahl_1 + string_kommazahl_2

    # Die Ergebnisse übertragen wir auf die Webseite
    context = {
        'titel': titel_der_webseite,
        'ergebnis_zahlen': ergebnis_zahlen,
        'ergebnis_kommazahlen': ergebnis_kommazahlen,
        'seltsames_ergebnis1': seltsames_ergebnis1,
        'seltsames_ergebnis2': seltsames_ergebnis2
    }

    return render(request, 'playground/home.html', context)
