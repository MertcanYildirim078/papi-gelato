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

#a het kiezen van een aantal bolletjes komt voor ieder bolletje de vraag: “Welke smaak wilt u voor bolletje nummer {X}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?”

#Bij een andere keuze dan A, C, M of V krijg je de tekst te zien: “Sorry dat snap ik niet...” en wordt deze stap herhaald.
#Bolletjes (ongeacht de smaak) zijn €1,10 per stuk
# Horrentjes zijn €1,25 per stuk
# Bakjes zijn €0,75 per stuk


# “Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?”.

# Iedere topping heeft zo zijn eigen prijs, maar alle toppings staan als 1 regel op het bonnetje.

# Geen: geen extra kosten
# Slagroom: €0,50 extra kosten
# Sprinkels: voor ieder bolletje €0,30 extra kosten
# Caramel Saus: als de bestelling in een horrentje zit dan €0,60 extra kosten, als het in een bakje zit dan €0,90 extra kosten.

# Bij een andere keuze dan A, B, C of D krijg je de tekst te zien: “Sorry dat snap ik niet...” en wordt deze stap herhaald

# Als er geen toppings zijn gekozen komt de regel met toppings niet op het bonnetje.

# Aan het begin (voor stap 1) word de vraag gesteld: “Bent u 1) particulier of 2) zakelijk?”
#    A. Als er particulier gekozen wordt dan ga je naar stap 1 (met de bolletjes)
#    B. Als er zakelijk gekozen wordt:

# is stap 1 anders dan wordt er niet gevraagd hoeveel bolletjes de klant wilt, maar hoeveel liter.
# Daarna wordt er per liter gevraagd welke smaak de klant wil.
# Toppings worden niet om gevraagd en ook niet of de klant meer wil bestellen. 
# De prijs van ijs per liter is voor iedere smaak €9,80 inclusief BTW
# Op het bonnetje moet bij een zakelijke klant BTW komen onder het totaal 



def welkom():
    print('Welkom bij Papi Gelato')

def vraagbolletjes():
    while True:
        bolletjes = int(input('Hoeveel bolletjes wilt u? '))
        if bolletjes > 8 :
            print("Zulke grote bakken hebben we niet!")
        else:
            return bolletjes

TotaalBolletjes = 0
toppingprijs = 0
hoorntje = 0
bakje = 0
def vraagbakje(bolletjes):
    while True:
        vraagbakjes = input(f'Wilt u deze {bolletjes} bolletje(s) in A) een hoorntje of B) een bakje? ')
        if vraagbakjes.lower() == "a":
            global hoorntje
            hoorntje += 1
            return "Hoorntje"
        elif vraagbakjes.lower() == 'b':
            global bakje
            bakje += 1
            return 'Bakje'
        else:
            print("Sorry dat snap ik niet...")

def resultaat():
    while True:
        verderbestellen = input('Wilt u nog meer bestellen? (Y/N) ')
        if verderbestellen.lower() == "y":
            return True
        elif verderbestellen.lower() == "n":
            return False
        else:
             print("Sorry dat snap ik niet...")

def smaken(bolletjes):
        smaaken = ""
        for x in range(bolletjes):
            x += 1
            while True:
                smaak = input(f'Welke smaak wilt u voor bolletje nummer {x}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ')
                if smaak.lower() == 'a':
                    smaaken = smaaken + f"Bolletje {x}: Aardbei \n"
                    break
                elif smaak.lower() == 'c':
                    smaaken = smaaken + f"Bolletje {x}: Chocolade \n"
                    break
                elif smaak.lower() == 'm':
                    smaaken = smaaken + f"Bolletje {x}: Munt \n"
                    break
                elif smaak.lower() == 'v':
                    smaaken = smaaken + f"Bolletje {x}: Vanille \n"
                    break
                else:
                    print("Sorry dat snap ik niet...")
        return smaaken

def topping(bolletjes, hoorntje, bakje):
    while True:
        inputTopping = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ')
        if inputTopping.lower() == 'a':
            return 0
        elif inputTopping.lower() == 'b':
            return 0.50
            
        elif inputTopping.lower() == 'c':
            return bolletjes * 0.30
        elif inputTopping.lower() == 'd':
            if hoorntje >= 1:
                return hoorntje * 0.60
            elif bakje >= 1:
                return bakje * 0.90

        else:
            print('Sorry ik snap het niet...')


               
def bonnetje(bolletjes, hoorntje, bakje, toppingprijs):
    if bolletjes in range(4,9):
        bakje += 1 
    bolletjesprijs = bolletjes * 1.10 
    hoorentjeprijs = hoorntje * 1.25
    bakjesprijs = bakje * 0.75
    totaal = float(bolletjesprijs) + float(hoorentjeprijs) + float(bakjesprijs) + float(toppingprijs)
    print('--------------------papi gelato------------------------ \n'
          '                                                        \n'
         f'Bolletjes:     {bolletjes} x €1.10    = €{bolletjesprijs}\n'
         f'Hoorntjes:     {hoorntje} x €1.25     = €{hoorentjeprijs}\n' 
         f'Bakjes:        {bakje} x €0.75        = €{bakjesprijs}   \n')
    if toppingprijs > 0:
        print(f'Toppings:                             = €{toppingprijs}  \n')
    print(f'                                  --------------- +\n'
    f'Totaal:                               = €{round(totaal,2)}          ')                           



def sorry():
    print('Sorry, dat snap ik niet...')
    return sorry()

ZakelijkDoorgaan = 0
def zakelijk():
    global ZakelijkDoorgaan
    zakelijkprocess = True
    while zakelijkprocess:
        zakelijkofpart = int(input('Bent u 1) particulier of 2) zakelijk? '))
        if zakelijkofpart == 1:
            ZakelijkDoorgaan = 1
            break
        elif zakelijkofpart == 2:
            ZakelijkDoorgaan = 2
            hoorntje = 0
            bakje = 0
            totaalbakje = 0
            totaalhoorntje = 0
            smaakenliter = ''
            vraagliter = True
            while vraagliter:
                liter = int(input('Hoeveel liter wilt u? '))
                if liter in range(1,9):
                    break
                elif liter >8:
                    print('Zulke grote bakken hebben we niet!')
                else:
                    print('Sorry ik snap het niet!')

            for l in range(liter):
                l += 1
                smaakliter = input(f'Welke smaak wilt u voor liter nummer {l}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ')
                if smaakliter.lower() == 'a':
                    smaakenliter = smaakenliter + f"liter(s) {l}: Aardbei \n"
                elif smaakliter.lower() == 'c':
                    smaakenliter = smaakenliter + f"liter(s) {l}: Chocolade \n"
                elif smaakliter.lower() == 'm':
                    smaakenliter = smaakenliter + f"liter(s) {l}: Munt \n"
                elif smaakliter.lower() == 'v':
                    smaakenliter = smaakenliter + f"liter(s) {l}: Vanille \n"
                else:
                    print("Sorry dat snap ik niet...")
                
                print(smaakenliter)
            prijsliter = liter * 9.80
            Btwprijsliter = prijsliter * 0.09
            vraaghoorntjesbakjes = True
            while vraaghoorntjesbakjes:
                vraaghoorntjebakje = input(f'Wilt u deze {liter} smaken in A) een hoorntje of B) een bakje? ')
                prijsliter = liter * 9.80
                Btwprijsliter = prijsliter * 0.09
                if vraaghoorntjebakje.lower() == 'a':
                    vraaghoorntjebakje = 1.25
                    hoorntje += 1
                    totaalhoorntje = hoorntje * vraaghoorntjebakje
                    break
                elif vraaghoorntjebakje.lower() == 'b':
                    vraaghoorntjebakje = 0.75
                    bakje += 1
                    totaalbakje = bakje * vraaghoorntjebakje
                    break
                else:
                    print('Sorry ik snap het niet...')
            totaalliter = prijsliter + totaalbakje + totaalhoorntje
            TotaalinclusiefBTW = totaalliter + Btwprijsliter
            print('--------------------papi gelato------------------------ \n'
            '                                                        \n'
            f'liters:     {liter} x €9.80    = €{prijsliter}           \n'
            f'Hoorntjes:     {hoorntje} x €1.25     = €{totaalhoorntje}\n' 
            f'Bakjes:        {bakje} x €0.75        = €{totaalbakje}   \n'
            f'                                  --------------- +\n'
            f'Totaal:                               = €{round(totaalliter,2)}\n'
            f'BTW (9%):                             = €{round(Btwprijsliter,2)}\n'
            f'Totaal inclusief BTW:                   = €{round(TotaalinclusiefBTW,2)}')
            break
        else:
            print('Sorry ik snap het niet...')         

        


def papi():
    global ZakelijkDoorgaan
    TotaalBolletjes = 0
    toppingprijs = 0
    process = True
    while process:
        welkom()
        zakelijks = zakelijk()
        if ZakelijkDoorgaan == 2:
            print('Bedankt en tot ziens!')
            break
        bolletjes = vraagbolletjes()
        smaaken = smaken(bolletjes)
        print (smaaken)
        if bolletjes  <= 3:
            HoornOfBakje = vraagbakje(bolletjes)
            print(f"Hier is uw {HoornOfBakje} met {bolletjes} bolletjes")
        elif bolletjes >= 4 and bolletjes <=8:
            print(f'Hier is uw bakje met {bolletjes} bolletje(s)')

        if bolletjes <= 0:
            print('Sorry u heeft geen bolletjes besteld')
            process = True
        toppingprijs = topping(bolletjes, hoorntje, bakje,)

        TotaalBolletjes += bolletjes
        Doorgaan = resultaat()
        if Doorgaan:
            process = True
        else:
            process = False
            bonnetje(TotaalBolletjes, hoorntje, bakje, toppingprijs)
            print('Bedankt en tot ziens!')
            return
            

papi()

    

