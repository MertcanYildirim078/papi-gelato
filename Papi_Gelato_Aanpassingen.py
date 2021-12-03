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
            print("Sorry dat is geen optie die we aanbieden...")

def resultaat():
    while True:
        verderbestellen = input('Wilt u nog meer bestellen? (Y/N) ')
        if verderbestellen.lower() == "y":
            return True
        elif verderbestellen.lower() == "n":
            return False
        else:
             print("Sorry dat is geen optie die we aanbieden...")

def smaken(bolletjes):
        smaaken = ""
        for x in range(bolletjes):
            x += 1
            while True:
                smaak = input(f'Welke smaak wilt u voor bolletje nummer {x}? A) Aardbei, C) Chocolade of V) Vanille?: ')
                if smaak.lower() == 'a':
                    smaaken = smaaken + f"Bolletje {x}: Aardbei \n"
                    break
                elif smaak.lower() == 'c':
                    smaaken = smaaken + f"Bolletje {x}: Chocolade \n"
                    break
                elif smaak.lower() == 'v':
                    smaaken = smaaken + f"Bolletje {x}: Vanille \n"
                    break
                else:
                    print("Sorry dat is geen optie die we aanbieden...")
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
            print('Sorry dat is geen optie die we aanbieden...')


               
def bonnetje(bolletjes, hoorntje, bakje, toppingprijs):
    if bolletjes in range(4,9):
        bakje += 1 
    bolletjesprijs = bolletjes * 0.95 
    hoorentjeprijs = hoorntje * 1.25
    bakjesprijs = bakje * 0.75
    totaal = float(bolletjesprijs) + float(hoorentjeprijs) + float(bakjesprijs) + float(toppingprijs)
    print('--------------------papi gelato------------------------ \n'
          '                                                        \n'
         f'Bolletjes:     {bolletjes} x €0.95    = €{bolletjesprijs}\n'
         f'Hoorntjes:     {hoorntje} x €1.25     = €{hoorentjeprijs}\n' 
         f'Bakjes:        {bakje} x €0.75        = €{bakjesprijs}   \n')
    if toppingprijs > 0:
        print(f'Toppings:                             = €{toppingprijs}  \n')
    print(f'                                  --------------- +\n'
    f'Totaal:                               = €{round(totaal,2)}          ')                           



def sorry():
    print('Sorry dat is geen optie die we aanbieden...')
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
                    print('Sorry dat is geen optie die we aanbieden...')

            for l in range(liter):
                l += 1
                smaakliter = input(f'Welke smaak wilt u voor liter nummer {l}? A) Aardbei, C) Chocolade of V) Vanille?: ')
                if smaakliter.lower() == 'a':
                    smaakenliter = smaakenliter + f"liter(s) {l}: Aardbei \n"
                elif smaakliter.lower() == 'c':
                    smaakenliter = smaakenliter + f"liter(s) {l}: Chocolade \n"
                elif smaakliter.lower() == 'v':
                    smaakenliter = smaakenliter + f"liter(s) {l}: Vanille \n"
                else:
                    print("Sorry dat is geen optie die we aanbieden...")
                
                print(smaakenliter)
            prijsliter = liter * 9.80
            Btwprijsliter = prijsliter * 0.06
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
                    print('Sorry dat is geen optie die we aanbieden...')
            totaalliter = prijsliter + totaalbakje + totaalhoorntje
            TotaalinclusiefBTW = totaalliter + Btwprijsliter
            print('--------------------papi gelato------------------------ \n'
            '                                                        \n'
            f'liters:     {liter} x €9.80    = €{prijsliter}           \n'
            f'Hoorntjes:     {hoorntje} x €1.25     = €{totaalhoorntje}\n' 
            f'Bakjes:        {bakje} x €0.75        = €{totaalbakje}   \n'
            f'                                  --------------- +\n'
            f'Totaal:                               = €{round(totaalliter,2)}\n'
            f'BTW (6%):                             = €{round(Btwprijsliter,2)}\n'
            f'Totaal inclusief BTW:                   = €{round(TotaalinclusiefBTW,2)}')
            break
        else:
            print('Sorry dat is geen optie die we aanbieden...')         

        


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
