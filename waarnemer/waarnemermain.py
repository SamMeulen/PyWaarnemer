from waarnemer.waarnemer import waarnemer
from decimal import Decimal

"""Maak een class Waarnemer. Deze class kan gegevens van temperaturen bijhouden. Na het
registreren van een temperatuur (of meerdere temperaturen), kan de minimumtemperatuur, de
maximumtemperatuur, het aantal waarnemingen en een gemiddelde temperatuur opgevraagd
worden.
Denk zelf na over de membervariabelen en hun types en de methods die hiervoor nodig zijn.
Maak vervolgens een main-class aan, nl. WaarnemerMain. De bedoeling is om meerdere
temperaturen in te geven en deze te laten registreren door de class Waarnemer. Bij ingave van
temperatuur 999 stopt de invoer en worden volgende gegevens getoond:
- het aantal ingegeven temperaturen
- de hoogste temperatuur
- de laagste temperatuur
- de gemiddelde temperatuur"""

waar = waarnemer()

temp = Decimal(0)

while temp != 999:
    try:
        temp = Decimal(input("Geef een temperatuur. Druk 999 om de eindigen. \n")) 
    except:
        print("Geef een getal in.")
    else:
        if temp == 999:
            break
        waar.tempList.append(temp)

waar.tempList.sort()
print("aantal ingegeven temperaturen: ") 
print(len(waar.tempList))
print("hoogste temperatuur: ")
print(waar.tempList[-1])
print("laagste temperatuur: ") 
print(waar.tempList[0])
print("gemiddelde temperatuur: ") 
print(sum(waar.tempList) / len(waar.tempList))