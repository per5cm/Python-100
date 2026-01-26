# age = int(input("Wie alt sind Sie?: "))
# if age < 18:
#     print("Zu jung!")
# else:
#     print("Passt")

# direction = input("Welche wärung möchten wechseln? e = EUR zu dollar, d = Dollar zu euro: ").lower()
# total_sum = float(input("Wie viel geld möchten Sie wechseln?: "))

# euro_to_dollar = 1.19
# dollar_to_euro = 0.84


# if direction == "e":
#     final_sum = round(euro_to_dollar * total_sum)
# elif direction == "d":
#     final_sum = round(dollar_to_euro * total_sum)

# print(f"Die wechsell summe ist: €{final_sum:.2f}")

# print("Willkommen zu Badenoase")
# print("Preise:")
# print("- Kinder bis 17 Jahre:     5,00 €")
# print("- Erwachsene 18 - 64 Jahre: 10,00 €")
# print("- Rentner ab 65 Jahre:     7,50 €\n")

# age = int(input("Wie alt sind Sie?:  "))
# tickets = int(input("Wieviele Tickets?: "))


# if age < 18:
#     print("Kinderpreis pro ticket 5€. Insgesamt Sie müssen: ", tickets * 5,"€ zahlen")
# elif age < 65:
#     print("Erwachsenenpreis pro ticket 10€. Insgesamt Sie müssen: ", tickets * 10,"€ zahlen")
# else:
#     print("Rentnerpreis pro ticket 7.50€. Insgesamt Sie müssen:", tickets * 7.50,"€ zahlen")

# einkaufsliste = []

# entscheidung = "y"

# while entscheidung == "y":
#     einkaufsliste.append(input("was möchtest du deiner liste hinzufügen? "))
#     entscheidung = input("motest du weitere Artikel hinzufügen? (y/n): ")
    
#     print(einkaufsliste)

einkaufsliste = []

while True:
    aktion = input("möchtest du einen Artikel hinzufügen, entfernen oder die liste anzeigen?: hinzufügen / entfernen / anzeigen / beenden").lower().strip()
    
    if aktion == "hinzufügen":
        artikel = input("welchen Artikel möchtest du hinzufügen?: ").lower().strip()
        einkaufsliste.append(artikel)
        print("Artikel wurde hinzugefügt.")
    elif aktion == "entfernen":
        artikel = input("welches artikel möchtest du entfernen?: ").lower().strip()
        if artikel in einkaufsliste:
            einkaufsliste.remove(artikel)
            print("artikel wurde entfernt.")
        else:
            print("Artikel nicht in der liste.")
    elif aktion == "anzeigen":
        print("Deine einkaufs list: ", einkaufsliste)
        #print(einkaufsliste)
    elif aktion == "beenden":
        print("einkaufliste wird beendet")
        break