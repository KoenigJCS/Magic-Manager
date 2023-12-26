# Starting the MTG Manager
1.	Load the pg schema dump to initialize the database
    a.	If you load the pg data dump skip steps 2-9, admin username = Admin, password = pw
2.	Download “All Cards” from https://scryfall.com/docs/api/bulk-data
3.	Place the json into the same folder as JKoenig_MagicManager.py
4.	Run the python file (installing all needed libraries)
5.	Start the program
6.	Create a user
    a.	The first user created in the db will be the admin user
7.	Login as the admin user
8.	Click “FULL DB RELOAD”
    a.	Type y in terminal to load
    b.	This may take a while and 8+ gb of ram
9.	Close and reopen the program
10.	Make sure your connected to the internet for the API
11.	You should be ready to go. Use the menu to navigate
