"""
trollkarlen_kattis.py

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

import sys
from linkedQFile import LinkedQ


def trolla(ordning):
    kortlek = LinkedQ()
    for kort in ordning:
        kortlek.enqueue(kort)

    resultat = []
    while not kortlek.isEmpty():
        x = kortlek.dequeue()
        kortlek.enqueue(x)
        y = kortlek.dequeue()
        resultat.append(y)

    return resultat


def main():
    rad = sys.stdin.readline()
    tokens = rad.split()
    resultat = trolla(tokens)
    print(" ".join(resultat))


if __name__ == "__main__":
    main()
