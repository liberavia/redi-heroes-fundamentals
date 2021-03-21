from django.shortcuts import render

# Create your views here.


def home(request):
    # Variablen sind Platzhalter-Namen, die einen Wert enthalten
    titel_der_webseite = 'Meine Lieblingsserie'
    lieblingsserie = 'Die Simpsons'
    # z. B. ist "titel_der_webseite" der Platzhalter-Name (kurz: die Variable) und
    # "'Meine Lieblingsserie'" der Wert der in die Variable (den Platzhalter-Namen)
    # gespeichert wird. Der Name steht links vom Gleichheitszeichen, der Wert rechts.

    # Jetzt müssen wir die Variablen noch an unsere HTML-Seite übergeben
    # Dies geschieht ebenfalls über eine Variable. Der Datentyp ist dabei
    # ein Dictionary (Wörterbuch). Dieser Typ sieht so aus:
    context = {
        'titel': titel_der_webseite,
        'serie': lieblingsserie
    }
    # Der Name (hier: "context") ist frei wählbar, "context" ist jedoch am gebräuchlichsten.
    # Ein Dictionary ist von geschweiften Klammern ("{}") umgeben und funktioniert eben so, wie man es
    # von einem Wörterbuch erwartet. In unserer Variable "context" kann man nach "titel" nachschlagen und
    # bekommt den Wert der Variablen "titel_der_webseite". Der Inhalt dieser Variablen ist "Meine Lieblingsserie".
    # Diese Nachschlagewörter (Index genannt) können wir auf unserer Webseite verwenden.
    # Damit das funktioniert müssen wir die Variable "context" an die HTML-Seite übergeben
    return render(request, 'playground/home.html', context)
