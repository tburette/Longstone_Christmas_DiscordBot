import pandas as pd

d = {'Commande': ["$je_suis","$qui_je_suis", "$qui_est_qui", "$oublie_moi", "$del"],
     'Argument': ["'Nom'", "", "", "", "#"],
     'Description': ["Enregistre le nom de l'utilisateur discord",
                     "Affiche le nom connu avec ton pseudo",
                     "Affiche la liste des utilisateurs connu",
                     "Supprime le nom de l'utilisateur discord",
                     "Supprime les n messages precedents"]}
help = pd.DataFrame(data=d)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)