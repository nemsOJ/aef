def rendreTousLesEtatsReconnaissants(automate):
    etats = set(automate["etats"])
    alphabet = set(automate["alphabet"])
    transitions = dict(automate["transitions"])
    etat_initial = automate["etat_initial"]
    etats_finaux = set(automate["etats_finaux"])

    # Crée un nouvel état initial
    nouvel_etat_initial = "new_initial_state"

    # Ajoute des transitions depuis le nouvel état initial vers les anciens états initiaux
    for symbole in alphabet:
        transitions[(nouvel_etat_initial, symbole)] = [etat_initial]

    # Met à jour l'automate
    etats.add(nouvel_etat_initial)
    etat_initial = nouvel_etat_initial

    # Retourne le nouvel automate
    nouvel_automate = {
        "etats": etats,
        "alphabet": alphabet,
        "transitions": transitions,
        "etat_initial": etat_initial,
        "etats_finaux": etats_finaux
    }

    return nouvel_automate

'''# Exemple d'utilisation
automate = {
    "etats": {"q0", "q1"},
    "alphabet": {"0", "1"},
    "transitions": {("q0", "0"): ["q1"], ("q0", "1"): ["q0"], ("q1", "0"): ["q0"], ("q1", "1"): ["q1"]},
    "etat_initial": "q0",
    "etats_finaux": {"q0"}
}

nouvel_automate = rendreTousLesEtatsReconnaissants(automate)
print(nouvel_automate)'''