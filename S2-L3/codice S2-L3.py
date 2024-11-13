nome_citta = input("Inserisci il nome della tua città: ")
nome_animale = input("Inserisci il nome del tuo animale domestico: ")
print(f"Il nome della tua band potrebbe essere: {nome_citta} {nome_animale}")

risposta = input("Ti piace questo nome? Rispondi SI o NO: ")
if risposta == "SI":
    print("Sono contento ti piaccia!!!")
elif risposta == "NO":
    print(f"mmm forse può piacerti: {nome_animale} {nome_citta}")
    risposta = input("Ti piace questo nome? Rispondi SI o NO: ")
    if risposta == "SI":
        print("Sono contento ti piaccia!!!")
    elif risposta == "NO":
        print("Ti ci hanno mai mandato in quel posto...")

