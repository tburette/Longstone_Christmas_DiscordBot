# Longstone Secret Santa Discord Bot

## Structure

### Directories
- pre_2023 : Alex's code
- 2023 : Thomas's code for the 2023 longstone (the event actually occured early 2024)
- In the root directory : the up-to-date code

### Code
- generate_pairs.py : algorithm to generate pairs of gifter -> giftee
- secret_santa_bot.py : Discord bot to generate pairs and announce the results on Discord
- data_20xx.py : data needed to run a secret santa draw

*Not* included in the repository : the Discord bot (application) token file (tokenSecretSanta).

## How to run a secret santa

It's a simple 10 steps process. *Hurrah!*

1) Download the code
2) Install the [discord.py dependency ](https://pypi.org/project/discord.py/)  
`pip install discord.py`  
(todo : add a `requirements.txt` file)
3) Start the discord bot  
`cd Longstone_Christmas_DiscordBot; python secret_santa_bot.py`  
tokenSecretSanta must be in the parent directory and contain the Discord application token.
4) Test that the bot works with discord.  
Eg. send it the !dm command in a DM message to ask it to send a message to someone : *!dm \<userID\> Bonjour mon enfant!*
5) Create a new data_20xx.py from the previous year and update it.  
Discord ID and display names can be retrieved by sending a DM to the bot : !members  
The previous year draw should be available in a*secretsanta.bin* file which can be read with `python printsecretsantabin.py secretsanta.bin`  
Be careful, the code doesn't check that the data is correct. Make sure :
   - every user_id exists in the discord (*!members*), 
   - in the data, the strings are the discord ids and not the display name (except for *id_to_display_name* value)
   - *users* are the people actually participating in the secret santa (no one is missing, no extra)
   - the id of an user can change! (check with *!members*)
   - every id in *user* is also in *id_to_display_name*
1) Update the `from data_2023 import penultimate_christmas_dict, ..` at the top of secret_santa_bot.py with the new data file
2) Test that the draw works. You can use *!testsecretsanta* to help testing. Make sure to test the draw several times to make sure it works every time! It is posible for it to sometimes work and sometimes not.
If it doesn't work : check the data is correct in *data_20xx.py*, remove contraints (remove data from xxx_christmas_dict, couple_dict)
1) Run the draw using !runsecretsanta. Make sure to have access to the (command line) stdout/stderr output of the bot 
2) check that the draw and the sending of messages worked (look at the stdout of the bot)
3)  Back up the the secretsanta.bin created by the bot during the draw (*secretsanta.bin*, can be read with *printsecretsantabin.py*).  
Push it to github!

## Bot commands
Commands to make the bot perform an action. Send a DM to the bot.  
This is not protected, anybody can make the bot perform an action!

- !members : list of members on the discord group
- !dm from_user_id message : make the bot send a message to someone
- !speak message : send a message to the general chat
- !data : print all the data used to make a draw
- !testsecretsanta : make a draw but do not send the messages to users, do not save it to secretsanta.bin either
- !runsecretsanta : make a draw and send a message to each member with the person the member must send a gift to. Careful!