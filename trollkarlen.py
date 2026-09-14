"""
trollkarlen_kattis.py

Uppgift 8: Version att skicka in till Kattis (problemet Trollkarlen,
under E-labbar). Ingen prompt-text, bara exakt indata/utdata.

Enligt problemtexten:
  Input:  En rad kort (heltal eller strängar), åtskilda av mellanslag.
          Ingen ledtext!
  Output: En rad med samma kort, i den ordning trollkarlen lägger ut dem.

Sample Input 1:  3 1 4 2 5      -> Sample Output 1: 1 2 3 5 4
Sample Input 2:  E Kn K D       -> Sample Output 2: Kn D K E

Andra testfallet innehåller kortkoder (E, Kn, K, D, ...) istället
för heltal. Eftersom LinkedQ inte bryr sig om vilken TYP av objekt
den lagrar kan vi lägga in alla tokens som strängar rakt av - det
fungerar för båda testfallen.

Skicka in TILLSAMMANS med linkedQFile.py, och ange den här filen
(trollkarlen_kattis.py) som "Entry point".
"""

import sys  # för att kunna läsa direkt från standard in (stdin)
from linkedQFile import LinkedQ  # importerar länkade-lista-versionen av kön


def trolla(ordning):  # funktion som simulerar hela korttricket
    kortlek = LinkedQ()  # skapar en ny, tom kö
    for kort in ordning:  # går igenom alla kort i den givna ordningen
        kortlek.enqueue(kort)  # lägger varje kort sist i kön

    resultat = []  # lista där vi samlar korten i den ordning de kommer upp
    while not kortlek.isEmpty():  # fortsätt tills alla kort är upplagda
        x = kortlek.dequeue()  # plockar ut det främsta kortet
        kortlek.enqueue(x)     # lägger tillbaka det sist i kön
        y = kortlek.dequeue()  # plockar ut nästa kort, det som läggs upp
        resultat.append(y)     # sparar det uppelagda kortet i resultatlistan

    return resultat  # returnerar hela listan med kort i den ordning de kom ut


def main():  # huvudfunktionen som sköter in- och utmatning enligt Kattis-formatet
    rad = sys.stdin.readline()  # läser exakt en rad från indata
    tokens = rad.split()  # delar upp raden i separata kort (strängar)
    resultat = trolla(tokens)  # kör själva korttricket på inmatningen
    print(" ".join(resultat))  # skriver ut korten i rätt ordning på en rad


if __name__ == "__main__":  # körs bara om filen körs direkt
    main()  # startar programmet
