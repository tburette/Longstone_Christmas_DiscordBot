import pandas as pd

d = {'Commande': ["$je_suis", "$oublie_moi", "$del"],
     'Argument': ["'Nom'", "", "#"],
     'Description': ["Enregistre le nom de l'utilisateur discord",
                     "Supprime le nom de l'utilisateur discord",
                     "Supprime les n messages precedents"]}
help = pd.DataFrame(data=d)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)