# dict of : gifter -> person who receives the gift from two christmases ago
penultimate_christmas_dict = {'Cricri': 'Lucine',
 'bylex0802': 'Vivianus',
 'Cinducci': 'Cricri',
 'Laurette': 'Cinducci',
 'Vivianus': 'Laurette',
 'Gabin': '_meliz_',
 'Lucine': 'bylex0802',
 '_meliz_': 'Gabin'}
 

 # dict of : gifter -> person who receives the gift from last christmas ago
previous_christmas_dict = {'Cinducci': 'Laurette',
 'Romain': 'Lucine',
 'bylex0802': '_meliz_',
 '_meliz_': 'Vivianus',
 'Laurette': 'bylex0802',
 'Vivianus': 'Cricri',
 'Cricri': 'Romain',
 'Lucine': 'Cinducci'}

# couple data
# ! two lines required for each couple:
#   'A' : 'B',
#   'B' : 'A',
# last update : 2023, added Mailys<-->Thomas
couple_dict = {'bylex0802': 'Cinducci',
 'Vivianus': 'Lucine',
 'Cinducci': 'bylex0802',
 'Lucine': 'Vivianus',
 '_meliz_': 'thomas5564',
 'thomas5564': '_meliz_',
 'Cricri' : 'LoloManzo',
 'LoloManzo' : 'Cricri'
 }

# list of users participating in the secret santa
# update : 2023, -Gabin +Thomas
users = ['bylex0802',
 'Vivianus',
 '_meliz_',
 'Cricri',
 'LoloManzo',
 'Cinducci',
 'Lucine',
 'Laurette',
 'thomas5564']

id_to_display_name = dict(
    [('thomas5564', 'ThomasB'), 
     ('bylex0802', 'ByLex'),  # alex
     ('_meliz_', 'méliz'), 
     ('Laurette', 'Laurette'),  #Laura
     #('Romain', 'Romain'),  # PAS cette année
     ('Vivianus', 'Vivianus'), 
     ('Cinducci', 'Cinducci'), 
     ('LoloManzo', 'LoloManzo'), #Loic
     ('Lucine', 'Lucine'),  # Lucie
     #('OscarBot', 'OscarBot'),
     ('Cricri', 'Cricri'), # Christelle
     #('SecretSanta', 'SecretSanta')
     ]
    )