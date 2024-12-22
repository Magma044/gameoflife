from tkinter import *

def clicked(bottone):
    bottone.config(text="⬤") # Configura le celle vive scelte dall'utente

def testoBottone(j, y): # Ottieni il testo del bottone alle coordinate j, y
    if 0 <= j < len(bottoni) and 0 <= y < len(bottoni[0]): # Evita di uscire dall'index per i bottoni con meno di 8 celle adiancenti (bordi)
        return bottoni[j][y].cget("text") # Restituisce il testo del bottone
    return "" # Restituisce stringa vuota se la cella è morta

def run():
    #Griglia temporanea della prossima iterazione
    prossimoStato = [[testoBottone(j, y) for y in range(len(bottoni[0]))] for j in range(len(bottoni))]
    #Prossimo stato crea una lista di liste che esegue un'iterazione tra ogni riga e ogni cella della riga prima di
    #passare a quella successiva chiamando la funzione testoBottone con i parametri j e y aggiornati per ottenere il testo di ogni cella
    #Questo crea una lista di liste che rappresenta la situazione attuale della griglia, questa lista viene poi usata per
    #aggiornare lo stato di ogni cella seguendo le regole di game of life, in modo che non venga fatto durante l'iterazione andando
    #a causare problemi alle celle successive, il risultato viene poi applicato alla griglia

    for j in range(len(bottoni)): # Iterazione tra le righe
        for y in range(len(bottoni[j])): # Iterazione su ogni bottone della riga attuale
            testo = testoBottone(j, y) # Controlla il testo del bottone
            adiacenti = 0 # Counter di celle vive adiacenti
            
            # Controlla le celle adiacenti (offset dalla cella attuale)
            #oj = offset j, oy = offset y
            for oj, oy in [(-1, -1), (1, 1), (-1, 1), (1, -1), (0, -1), (0, 1), (-1, 0), (1, 0)]:
                #j/y + oj/oy = posizione cella attuale + offset cella adiacente
                if testoBottone(j + oj, y + oy) == "⬤": # Se una cella adiacente è viva incrementa il counter
                    adiacenti += 1
            if testo == "⬤": # Regole che fanno morire una cella
                if adiacenti < 2 or adiacenti > 3:
                    prossimoStato[j][y] = "" #Aggiorna la lista prossimo stato
            else: # Regole che fanno tornare in vita una cella
                if adiacenti == 3:
                    prossimoStato[j][y] = "⬤" #Aggiorna la lista prossimo stato

    #Aggiorna la griglia allo stato successivo
    for j in range(len(bottoni)): #Iterazione tra le righe
        for y in range(len(bottoni[j])): #Iterazione tra le colonne presenti in ogni riga
            bottoni[j][y].config(text=prossimoStato[j][y]) #Testo della cella uguale al testo del prossimo stato della
    
    #Aggiorna ogni secondo
    root.after(1000, run)

root = Tk()
root.title("Game of Life")

bottoni = [] # Crea una lista dei bottoni

for i in range(10):
    row = [] # Lista dei bottoni sulla riga attuale
    for k in range(5):
        button = Button(root, width=10, height=5)
        button.config(command=lambda b=button: clicked(b)) # Rende viva la cella selezionata
        button.grid(column=i, row=k)
        row.append(button) # Aggiunge i bottoni alla riga
    bottoni.append(row) # Aggiunge la riga alla lista dei bottoni

start = Button(root, width=20, height=5, text="AVVIA", command=run) # Avvia la simulazione
start.grid(column=4, row=6, columnspan=2)

root.mainloop()
