# list of users participating in the secret santa
# update 2023, -Gabin +Thomas
# update 2024, -LoloManzo
users = ['bylex0802',
 'Vivianus',
 '_meliz_',
 'cricri7570',
 'Cinducci',
 'lucine2884',
 'barbieguuurl',
 'thomas5564']

# use the bot !members command to update if needed
# if an id changed : must change in all the other variables!
id_to_display_name = dict(
    [('thomas5564', 'ThomasB'), 
     ('bylex0802', 'ByLex'),  # alex
     ('_meliz_', 'méliz'), 
     ('barbieguuurl', 'Laurette'),  #Laura
     ('Romain', 'Romain'),  # PAS cette année
     ('Vivianus', 'Vivianus'), 
     ('Cinducci', 'Cinducci'), 
     ('LoloManzo', 'Lolomanzo'), #Loic
     ('lucine2884', 'Lucine'),  # Lucie
     #('OscarBot', 'OscarBot'),
     ('cricri7570', 'Cricri'), # Christelle
     #('SecretSanta', 'SecretSanta')
     ]
    )



# dict of : gifter -> person who receives the gift from two christmases ago
# christmas_2022_dict = {'cricri7570': 'lucine2884',
#  'bylex0802': 'Vivianus',
#  'Cinducci': 'cricri7570',
#  'barbieguuurl': 'Cinducci',
#  'Vivianus': 'barbieguuurl',
#  'Gabin': '_meliz_',
#  'lucine2884': 'bylex0802',
#  '_meliz_': 'Gabin'}

 # dict of : gifter -> person who receives the gift from last christmas ago
penultimate_christmas_dict = {'Cinducci': 'barbieguuurl',
 'Romain': 'lucine2884',
 'bylex0802': '_meliz_',
 '_meliz_': 'Vivianus',
 'barbieguuurl': 'bylex0802',
 'Vivianus': 'cricri7570',
 'cricri7570': 'Romain',
 'lucine2884': 'Cinducci'}

# dict of : gifter -> person who receives the gift from two christmases ago
# retrieved from secretsanta.bin
previous_christmas_dict = {
    'bylex0802': 'LoloManzo', 
    'Vivianus': 'Cinducci', 
    '_meliz_': 'barbieguuurl', 
    'cricri7570': 'Vivianus',
    'LoloManzo': 'lucine2884',
    'Cinducci': '_meliz_',
    'lucine2884': 'cricri7570',
    'barbieguuurl': 'thomas5564',
    'thomas5564': 'bylex0802'
}

# couple data
# ! two lines required for each couple:
#   'Him' : 'Her',
#   'Her' : 'Him',
# last update : 2023, added Mailys<-->Thomas
couple_dict = {'bylex0802': 'Cinducci',
 'Vivianus': 'lucine2884',
 'Cinducci': 'bylex0802',
 'lucine2884': 'Vivianus',
 '_meliz_': 'thomas5564',
 'thomas5564': '_meliz_',
 'cricri7570' : 'LoloManzo',
 'LoloManzo' : 'cricri7570'
 }
