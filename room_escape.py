import random
import pprint
def stampa_griglia(n, pos, uscita):
    """Stampa la griglia con G = giocatore, U = uscita, . = spazio vuoto"""
    # TODO
    griglia = []
    for i in range(n):
        griglia.append(["."] * n)
    griglia[pos[0]][pos[1]] = "G"
    griglia[uscita[0]][uscita[1]] = "U"
    return list(griglia)



def muovi(pos, mossa):
    """Aggiorna la posizione in base alla mossa"""
    # TODO
    if mossa == "n":
        new_pos = (pos[0] - 1, pos[1])
    elif mossa == "e":
        new_pos = (pos[0], pos[1] + 1)
    elif mossa == "s":
        new_pos = (pos[0] + 1, pos[1])
    elif mossa == "o":
        new_pos = (pos[0], pos[1] - 1)
    try:
        return new_pos
    except Exception:
        print("\ninput Error: Riprovare con un input corretto\n")
        return pos


def gestisci_livello(livello):
    """ Gestisce un singolo livello del gioco
    Ritorna:
    * True se il giocatore raggiunge l'uscita
    * False se il giocatore va oltre i limiti della griglia.

    NB: Le funzioni stampa_griglia() e muovi() vanno chiamate dentro questa funzione
    """

    # Inizializzazioni
    n = livello + 2
    uscita = [n - 1, n - 1]  # posizione uscita
    # TODO
    while True:
        pos = (random.randint(0, n - 1), random.randint(0, n - 1))
        if (pos[0] != uscita[0] or pos[1] != uscita[1]): break
    griglia = stampa_griglia(n,pos,uscita)

    while True:
        while True:
            for riga in griglia:
                for p in riga:
                    print(p, end=" ")
                print()
            mossa = input("- n → nord  su  \n- s → sud  giù  \n- e → est destra  \n- o → ovest  sinistra\nInserire la mossa: ")
            if mossa in "nseo":
                break
            else:
                print("\ninput Error: Riprovare con un input corretto\n")
        new_pos = muovi(pos, mossa)
        if new_pos[0] < 0 or new_pos[1] < 0: return False
        try:
            griglia[pos[0]][pos[1]] = "."
            griglia[new_pos[0]][new_pos[1]] = "G"
            pos = new_pos
            if new_pos[0] == uscita[0] and new_pos[1] == uscita[1]:
                return True
        except IndexError:
            return False




def main():
    print("=== Benvenuto in Room Escape ===")
    livello = 0
    max_livello = 5

    while livello <= max_livello:
        print(f"Livello {livello}) Griglia {livello+2}x{livello+2}")
        completato = gestisci_livello(livello)
        if completato:
            print("Livello completato\n")
            livello += 1
        else:
            print("Hai perso!")
            break


if __name__ == "__main__":
    while(True): main()
