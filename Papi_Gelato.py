#Als je het programmaatje opstart moet de volgende welkomstzin te zien zijn: “Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.”

# Stap 1 – van het stappen plan voor de werknemer is dat hij/zij vraagd: “Hoeveel bolletjes wilt u?”.
# Aan de hand van het antwoord kunnen er een aantal dingen gebeuren:
#    A. bij een getal van 1 t/m 3 ga je naar stap 2
#    B. bij een getal van 4 t/m 8 sla je stap 2 over en krijg je de tekst te zien: “Dan krijgt u van mij een bakje met {aantal} bolletjes”
#    C. bij een getal van hoger dan 8 krijg je de tekst te zien “Sorry, zulke grote bakken hebben we niet” en wordt deze stap herhaald
#    D. anders krijg je de tekst te zien: “Sorry dat snap ik niet...” en wordt deze stap herhaald

# Stap 2 – Nu moet de volgende vraag gesteld worden: “Wilt u deze {aantal} bolletje(s) in A) een hoorntje of B) een bakje?”
#    A. bij een keuze van A of B ga je naar stap 3
#    B. anders krijg je de tekst te zien: “Sorry, dat snap ik niet...” en wordt deze stap herhaald.

# Stap 3 – Als laatste krijg je te zien “Hier is uw {hoorntje/bakje} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Y/N)”
#    A. bij Y als als antwoord ga je terug naar stap 1 en herhaalt zich het proces
#    B. bij N als als antwoord stopt het programma en krijg je de boodschap: “Bedankt en tot ziens!”
#    C. anders krijg je de tekst te zien: “Sorry, dat snap ik niet...” en wordt deze stap herhaald
# Let op: Programmeer zo DRY mogelijk en gebruik duidelijke beschrijvenende namen voor je functies en variabelen
def welkom():
    print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')

def vraagbolletjes():
    while True:
        bolletjes = int(input('Hoeveel bolletjes wilt u? '))
        if bolletjes > 8 :
            print("Zulke grote bakken hebben we niet!")
        else:
            return bolletjes

def vraagbakje(bolletjes):
    while True:
        vraagbakjes = input(f'Wilt u deze {bolletjes} bolletje(s) in A) een hoorntje of B) een bakje? ')
        if vraagbakjes.lower() == "a":
            return "Hoorntje"
        elif vraagbakjes.lower() == 'b':
            return 'Bakje'
        else:
            print("Dit is geen geldige optie!")

def resultaat():
    while True:
        verderbestellen = input('Wilt u nog meer bestellen? (Y/N) ')
        if verderbestellen.lower() == "y":
            return True
        elif verderbestellen.lower() == "n":
            return False
        else:
            print("Sorry, dat snap ik niet...")

def sorry():
    print('Sorry, dat snap ik niet...')
    return sorry()




def papi():
    process = True
    while process:
        welkom()
        bolletjes = vraagbolletjes()
        if bolletjes  <= 3:
            HoornOfBakje = vraagbakje(bolletjes)
            print(f"Hier is uw {HoornOfBakje}")
        elif bolletjes >= 4 and bolletjes <=8:
            print(f'Hier is uw bakje met {bolletjes} bolletje(s)')

 
        Doorgaan =resultaat()
        if Doorgaan:
            process = True
        else:
            process = False
            print('Bedankt en tot ziens!')
            return

papi()

    
