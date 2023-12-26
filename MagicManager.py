import psycopg
import datetime
import pandas as pd
import requests
import json  
import time
import tkinter as tk
from tkinter import N,S,E,W
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

gb_user_id = -1

def FullDataReset():
    with psycopg.connect("dbname=mtgdata user=postgres password=DB1basic!") as conn:
        with conn.cursor() as cur:
            if(conn.TransactionStatus.INERROR):
                conn.rollback()
            #query = "DROP TABLE ~~~"
            #cur.execute(query)
            #conn.commit()
            print("THIS IS A LOT OF LOADING, ARE YOU SURE THIS IS A GOOD IDEA (y/n)")
            if input() != "y":
                return
            file = open('all-cards-20231204221920.json',encoding='utf8')
            fdata = json.loads(file.read())
            for i in range(len(fdata)):
                try:
                    _id = fdata[i]["oracle_id"]
                except KeyError:
                    continue
                name = fdata[i]["name"]
                name = str.replace(name,"'","''")
                mtg_set = fdata[i]["set"]
                try:
                    manaCost = fdata[i]["mana_cost"]
                except KeyError:
                    manaCost = {}
                typeline = fdata[i]["type_line"]
                typeline = str.replace(typeline,"'","''")
                rarity = fdata[i]["rarity"]
                artist = fdata[i]["artist"]
                artist = str.replace(artist,"'","''")
                try:
                    medResImg = fdata[i]["image_uris"]["normal"]
                except KeyError:
                    medResImg = "https://cards.scryfall.io/normal/front/0/0/00020b05-ecb9-4603-8cc1-8cfa7a14befc.jpg?1562633475%22,%22large%22:%22https://cards.scryfall.io/large/front/0/0/00020b05-ecb9-4603-8cc1-8cfa7a14befc.jpg?1562633475%22,%22png%22:%22https://cards.scryfall.io/png/front/0/0/00020b05-ecb9-4603-8cc1-8cfa7a14befc.png?1562633475%22,%22art_crop%22:%22https://cards.scryfall.io/art_crop/front/0/0/00020b05-ecb9-4603-8cc1-8cfa7a14befc.jpg?1562633475%22,%22border_crop%22:%22https://cards.scryfall.io/border_crop/front/0/0/00020b05-ecb9-4603-8cc1-8cfa7a14befc.jpg?1562633475%22},%22mana_cost%22:%22{X}{G}{G}%22,%22cmc%22:2.0,%22type_line%22:%22Sorcery%22,%22oracle_text%22:%22Manifest%20the%20top%20card%20of%20your%20library,%20then%20put%20X%20+1/+1%20counters%20on%20it.%20(To%20manifest%20a%20card,%20put%20it%20onto%20the%20battlefield%20face%20down%20as%20a%202/2%20creature.%20Turn%20it%20face%20up%20any%20time%20for%20its%20mana%20cost%20if%20it%27s%20a%20creature%20card.)%22,%22colors%22:[%22G%22],%22color_identity%22:[%22G%22],%22keywords%22:[%22Manifest%22],%22legalities%22:{%22standard%22:%22not_legal%22,%22future%22:%22not_legal%22,%22historic%22:%22not_legal%22,%22gladiator%22:%22not_legal%22,%22pioneer%22:%22legal%22,%22explorer%22:%22not_legal%22,%22modern%22:%22legal%22,%22legacy%22:%22legal%22,%22pauper%22:%22not_legal%22,%22vintage%22:%22legal%22,%22penny%22:%22legal%22,%22commander%22:%22legal%22,%22oathbreaker%22:%22legal%22,%22brawl%22:%22not_legal%22,%22historicbrawl%22:%22not_legal%22,%22alchemy%22:%22not_legal%22,%22paupercommander%22:%22not_legal%22,%22duel%22:%22legal%22,%22oldschool%22:%22not_legal%22,%22premodern%22:%22not_legal%22,%22predh%22:%22not_legal%22},%22games%22:[%22paper%22],%22reserved%22:false,%22foil%22:false,%22nonfoil%22:true,%22finishes%22:[%22nonfoil%22],%22oversized%22:false,%22promo%22:true,%22reprint%22:true,%22variation%22:false,%22set_id%22:%22fc7ea025-628e-45f4-9e0b-73681b1f68b7%22,%22set%22:%22ugin%22,%22set_name%22:%22Ugin%27s%20Fate%22,%22set_type%22:%22promo%22,%22set_uri%22:%22https://api.scryfall.com/sets/fc7ea025-628e-45f4-9e0b-73681b1f68b7%22,%22set_search_uri%22:%22https://api.scryfall.com/cards/search?order=set&q=e%3Augin&unique=prints%22,%22scryfall_set_uri%22:%22https://scryfall.com/sets/ugin?utm_source=api%22,%22rulings_uri%22:%22https://api.scryfall.com/cards/00020b05-ecb9-4603-8cc1-8cfa7a14befc/rulings%22,%22prints_search_uri%22:%22https://api.scryfall.com/cards/search?order=released&q=oracleid%3Ad96ac790-428b-4a64-8dbd-6baa73eb6210&unique=prints%22,%22collector_number%22:%22146%22,%22digital%22:false,%22rarity%22:%22rare%22,%22flavor_text%22:%22A%20howl%20on%20the%20wind%20hides%20many%20dangers.%22,%22card_back_id%22:%220aeebaf5-8c7d-4636-9e82-8c27447861f7%22,%22artist%22:%22Adam%20Paquette%22,%22artist_ids%22:[%2289023dad-e6c0-41e0-83fb-eb2bfbbdc3f2%22],%22illustration_id%22:%22b90c25fd-2ee1-4372-89d1-fc806d01d501%22,%22border_color%22:%22black%22,%22frame%22:%222015%22,%22security_stamp%22:%22oval%22,%22full_art%22:false,%22textless%22:false,%22booster%22:true,%22story_spotlight%22:false,%22promo_types%22:[%22setpromo%22],%22edhrec_rank%22:19146,%22penny_rank%22:11545,%22prices%22:{%22usd%22:%221.74%22,%22usd_foil%22:null,%22usd_etched%22:null,%22eur%22:%222.00%22,%22eur_foil%22:null,%22tix%22:null},%22related_uris%22:{%22gatherer%22:%22https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=394089&printed=false%22,%22tcgplayer_infinite_articles%22:%22https://tcgplayer.pxf.io/c/4931599/1830156/21018?subId1=api&trafcat=infinite&u=https%3A%2F%2Finfinite.tcgplayer.com%2Fsearch%3FcontentMode%3Darticle%26game%3Dmagic%26partner%3Dscryfall%26q%3DWildcall%22,%22tcgplayer_infinite_decks%22:%22https://tcgplayer.pxf.io/c/4931599/1830156/21018?subId1=api&trafcat=infinite&u=https%3A%2F%2Finfinite.tcgplayer.com%2Fsearch%3FcontentMode%3Ddeck%26game%3Dmagic%26partner%3Dscryfall%26q%3DWildcall%22,%22edhrec%22:%22https://edhrec.com/route/?cc=Wildcall%22},%22purchase_uris%22:{%22tcgplayer%22:%22https://tcgplayer.pxf.io/c/4931599/1830156/21018?subId1=api&u=https%3A%2F%2Fwww.tcgplayer.com%2Fproduct%2F95585%3Fpage%3D1%22,%22cardmarket%22:%22https://www.cardmarket.com/en/Magic/Products/Search?referrer=scryfall&searchString=Wildcall&utm_campaign=card_prices&utm_medium=text&utm_source=scryfall%22,%22cardhoarder%22:%22https://www.cardhoarder.com/cards?affiliate_id=scryfall&data%5Bsearch%5D=Wildcall&ref=card-profile&utm_campaign=affiliate&utm_medium=card&utm_source=scryfall"
                try:
                    textbox = fdata[i]["oracle_text"]
                except KeyError:
                    continue
                textbox = str.replace(textbox,"'","''")
                time = datetime.datetime.now()
                legalities = fdata[i]["legalities"]
                try:
                    cur.execute(f"""
                            insert into cards VALUES (
                            '{_id}',
                            '{name}',
                            '{mtg_set}',
                            '{manaCost}',
                            '{typeline}',
                            '{rarity}',
                            '{artist}',
                            '{medResImg}',
                            '{textbox}'
                            );
                            """)
                except psycopg.errors.UniqueViolation:
                    conn.rollback()
                    continue
                for l in legalities:
                    if(legalities[l] == "not_legal"):
                        try:
                            cur.execute(f"""
                                insert into banned_list VALUES (
                                '{_id}',
                                '{l}',
                                '{time}'
                                );
                                """)
                        except psycopg.errors.UniqueViolation:
                            conn.rollback()
                            continue
                conn.commit()

def send_query(my_query):
    with psycopg.connect("dbname=mtgdata user=postgres password=DB1basic!") as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(my_query)
            except Exception as exept:
                print("FAILURE ON SEND: "+str(exept))
                conn.rollback()
            conn.commit()

def recive_query(my_query):
    with psycopg.connect("dbname=mtgdata user=postgres password=DB1basic!") as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(my_query)
                return cur.fetchall()
            except Exception as exept:
                print("FAILURE ON RECIVE: "+str(exept))
                conn.rollback()
                return NONE


                
def login():
    root = tk.Tk()
    root.title("Login")
    mainframe = ttk.Frame(root, padding="20 20 25 25")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    username = tk.StringVar()
    pw = tk.StringVar()

    def check_creds():
        output = recive_query(f"""
                        select user_id from user_table 
                        where username='{username.get()}' AND password='{pw.get()}'
                         """)
        if(len(output)>0 and len(output[0])>0):
            global gb_user_id
            gb_user_id=output[0][0]
            gb_user_id=int(gb_user_id)
            print(gb_user_id)
            mainmenu()
            root.destroy()
        

    username = ttk.Entry(mainframe, width=25, textvariable=username)
    pw = ttk.Entry(mainframe, width=25, textvariable=pw)

    ttk.Label(mainframe, text="Username").grid(column=0, row=1, sticky=(W,E))
    username.grid(column=0, row=2, sticky=(W, E))
    ttk.Label(mainframe, text="Password").grid(column=0, row=3, sticky=(W,E))
    pw.grid(column=0, row=4, sticky=(W, E))

    ttk.Button(mainframe, text="Login", command=check_creds).grid(column=0, row=5, sticky=(W,E))
                    
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    root.bind("<Return>", check_creds)

    

def new_user():
    root = tk.Tk()
    root.title("New User")
    username = tk.StringVar()
    pw = tk.StringVar()
    confirm_pw = tk.StringVar()

    def save():
        if(pw.get()==confirm_pw.get()):
            send_query(f"""
                       insert into user_table
                       values (default,'{username.get()}','{pw.get()}');
                       """)
            root.destroy()
        else:
            print(pw.get()+"!="+confirm_pw.get())
    
    mainframe = ttk.Frame(root, padding="20 20 25 25")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    username = ttk.Entry(mainframe, width=25, textvariable=username)
    pw = ttk.Entry(mainframe, width=25, textvariable=pw)
    confirm_pw = ttk.Entry(mainframe, width=25, textvariable=confirm_pw)
    
    ttk.Label(mainframe, text="Username").grid(column=0, row=1, sticky=(W,E))
    username.grid(column=0, row=2, sticky=(W, E))
    ttk.Label(mainframe, text="Password").grid(column=0, row=3, sticky=(W,E))
    pw.grid(column=0, row=4, sticky=(W, E))
    ttk.Label(mainframe, text="Confirm Password").grid(column=0, row=5, sticky=(W,E))
    confirm_pw.grid(column=0, row=6, sticky=(W, E))
                    
    ttk.Button(mainframe, text="Save User!", command=save).grid(column=0, row=7, sticky=(W,E))
                    
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

mm_root = tk.Tk()
    

def main():
    mm_root.title("MTG Manager")

    mainframe = ttk.Frame(mm_root, padding="20 20 25 25")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mm_root.columnconfigure(0, weight=1)
    mm_root.rowconfigure(0, weight=1)

    ttk.Button(mainframe, text="Make New User", command=new_user).grid(column=2, row=2, sticky=N,ipadx=30)
    ttk.Button(mainframe, text="Login", command=login).grid(column=2, row=3, sticky=N,ipadx=30)

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    mm_root.mainloop()

def add_deck():
    mm_root.title("Add Deck")

    mainframe = ttk.Frame(mm_root, padding="20 20 25 25")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mm_root.columnconfigure(0, weight=1)
    mm_root.rowconfigure(0, weight=1)
    global gb_user_id

    decklist = ScrolledText(mainframe,wrap=tk.WORD,height=55,width=100)
    decklist.grid(column=0, row=2, sticky=N,ipadx=30)

    def save_deck():
        line_count = int(decklist.index('end-1c').split('.')[0])
        if(line_count>0 and len(deck_name.get())>0 and len(format_name.get())>0):
            send_query(f"""
                       INSERT INTO deck_storage VALUES ('{gb_user_id}',DEFAULT,'{deck_name.get()}','{format_name.get().lower()}');
                       """)
            deck_id = recive_query(f"""
                        SELECT deck_id FROM deck_storage
                        WHERE deck_name = '{deck_name.get()}'; 
                        """)[0][0]
        for i in range(1,line_count+1):
            text = decklist.get(float(i),float(i+1))
            text = str.replace(text,"'","''")
            text = text.split('\n')
            text = text[0].partition(' ')
            try:
                oracle_id = str(recive_query(f" SELECT oracle_id as id FROM cards WHERE card_name='{text[2]}' GROUP BY oracle_id LIMIT 1;")[0][0])
            except Exception:
                continue
            send_query(f"""
                       INSERT INTO library_storage VALUES ('{oracle_id}',{deck_id},FALSE,{text[0]},'{text[2]}');
                       """)
        mainmenu()


    ttk.Label(mainframe, text="Decklist:").grid(column=0, row=1, sticky=(W,E))
    decklist.grid(column=0, row=2, sticky=(W, E))
    ttk.Button(mainframe, text="Save Deck", command=save_deck).grid(column=0, row=3, sticky=N,ipadx=30)

    deck_name = tk.StringVar()
    deck_name = ttk.Entry(mainframe, width=25, textvariable=deck_name)
    ttk.Label(mainframe, text="Deck Name").grid(column=0, row=4, sticky=(W,E))
    deck_name.grid(column=0, row=5, sticky=(W, E))

    format_name = tk.StringVar()
    format_name = ttk.Entry(mainframe, width=25, textvariable=format_name)
    ttk.Label(mainframe, text="Format Name").grid(column=0, row=6, sticky=(W,E))
    format_name.grid(column=0, row=7, sticky=(W, E))

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    ttk.Button(mainframe, text="Return", command=mainmenu).grid(column=0, row=0, sticky=W,ipadx=30,ipady=10)


def load_deck():
    mm_root.title("Load Deck")

    mainframe = ttk.Frame(mm_root, padding="20 20 25 25")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mm_root.columnconfigure(0, weight=1)
    mm_root.rowconfigure(0, weight=1)
    global gb_user_id

    display_list = ScrolledText(mainframe,wrap=tk.WORD,height=55,width=50)
    display_list.grid(column=0, row=99, sticky=N,ipadx=30)
    global cur_deck_id
    cur_deck_id = 0
    def remove_deck():
        global cur_deck_id
        send_query(f"""
                   DELETE from library_storage
                    WHERE deck_id={cur_deck_id};
                   """)
        send_query(f"""
                   DELETE from deck_storage
                    where deck_id={cur_deck_id};
                   """)
        load_deck()

    def load_deck_data(deck_id):
        global cur_deck_id
        box_text = ""
        display_list.delete("1.0",'end-1c')
        cur_deck_id=deck_id
        card_data = recive_query(f"""
                    SELECT oracle_id,quantity,card_name from library_storage
                    WHERE deck_id={deck_id};
                    """)
        for o in range(0,len(card_data)):
            box_text+=str(card_data[o][1])+" "+str(card_data[o][2])+"\n"
        display_list.insert(tk.INSERT,box_text)

    ttk.Label(mainframe, text="Load Decks:").grid(column=0, row=2, sticky=(W,E))
    decks = recive_query(f"""
                    SELECT deck_id,deck_name from deck_storage
                    WHERE user_id={gb_user_id};
                 """)
    for i in range(0,len(decks)):
        ttk.Button(mainframe, text=str(decks[i][1]), command=lambda arg1 = decks[i][0]:load_deck_data(arg1)).grid(column=0, row=i+3, sticky=(W,E),ipadx=30)

    ttk.Button(mainframe, text="Return", command=mainmenu).grid(column=0, row=1, sticky=(W,E),ipadx=30,ipady=10)
    ttk.Button(mainframe, text="Remove Deck", command=remove_deck).grid(column=0, row=2, sticky=(W,E),ipadx=30,ipady=10)

def check_deck_legal():
    mm_root.title("Check Decks")

    mainframe = ttk.Frame(mm_root, padding="20 20 25 25")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mm_root.columnconfigure(0, weight=1)
    mm_root.rowconfigure(0, weight=1)
    global gb_user_id

    global output
    output = ttk.Label(mainframe, text="Is It Legal?")
    output.grid(column=0, row=2, sticky=W,ipadx=30)

    def check_deck_data(deck_id):
        global output
        mtg_format = str(recive_query(f"""
                                    SELECT mtg_format from deck_storage
                                    where deck_id = {deck_id};
                                      """)[0][0])
        card_data = recive_query(f"""
                    SELECT oracle_id from library_storage
                    WHERE deck_id={deck_id};
                    """)
        for o in range(0,len(card_data)):
            legal_data = recive_query(f"""
                        SELECT oracle_id from banned_list
                        WHERE oracle_id = '{card_data[o][0]}' and mtg_format='{mtg_format}';
                        """)
            if(len(legal_data)>0):
                print("False")
                output.config(text = "False")
                return
        print("True")
        output.config(text = "True")

    decks = recive_query(f"""
                    SELECT deck_id,deck_name from deck_storage
                    WHERE user_id={gb_user_id};
                 """)
    for i in range(0,len(decks)):
        ttk.Button(mainframe, text=str(decks[i][1]), command=lambda arg1 = decks[i][0]:check_deck_data(arg1)).grid(column=0, row=i+3, sticky=(W,E),ipadx=30)

    ttk.Button(mainframe, text="Return", command=mainmenu).grid(column=0, row=1, sticky=(W,E),ipadx=30,ipady=10)

def check_deck_price():
    mm_root.title("Check Decks")
    mainframe = ttk.Frame(mm_root, padding="20 20 25 25")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mm_root.columnconfigure(0, weight=1)
    mm_root.rowconfigure(0, weight=1)
    global gb_user_id
    global total_output
    global total_foil_output
    global canvas
    global bbox

    decks = recive_query(f"""
                    SELECT deck_id,deck_name from deck_storage
                    WHERE user_id={gb_user_id};
                 """)
    global deckcount
    deckcount = len(decks)+3

    subframe = ttk.Frame(mainframe)
    subframe.grid(row=deckcount,column=0)

    scroll_bar = tk.Scrollbar(subframe, orient=tk.VERTICAL)
    scroll_bar.grid(row=0, column=1, sticky=tk.NS)

    canvas = tk.Canvas(subframe,yscrollcommand=scroll_bar.set)
    canvas.grid(row=0,column=0)

    scroll_bar.configure(command=canvas.yview)

    table_frame = ttk.Frame(canvas)
    table_frame.grid(row=0, column=0,sticky=(N, W, E, S))

    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.configure(yscrollcommand=scroll_bar.set)

    ttk.Label(table_frame, text="Total:").grid(column=0, row=0, sticky=(W,E),ipadx=10)
    ttk.Label(table_frame, text="Total Foil:").grid(column=1, row=0, sticky=(W,E),ipadx=10)
    total_output = ttk.Label(table_frame, text="$0.00")
    total_output.grid(column=0, row=1, sticky=(W,E),ipadx=10)
    total_foil_output = ttk.Label(table_frame, text="$0.00")
    total_foil_output.grid(column=1, row=1, sticky=(W,E),ipadx=10)
    ttk.Label(table_frame, text="Amount:").grid(column=0, row=2, sticky=(W,E),ipadx=10)
    ttk.Label(table_frame, text="Name:").grid(column=1, row=2, sticky=(W,E),ipadx=10)
    ttk.Label(table_frame, text="USD Price:").grid(column=2, row=2, sticky=(W,E),ipadx=10)
    ttk.Label(table_frame, text="Foil USD Price:").grid(column=3, row=2, sticky=(W,E),ipadx=10)

    table_labels = [] 

    def check_price_data(deck_id):
        for cell in table_labels:
            cell.destroy()
        table_labels.clear()

        global total_output
        global total_foil_output
        global deckcount
        global canvas
        price=0.0
        foil_price=0.0
        total = 0.0
        total_foil = 0.0
        card_data = recive_query(f"""
                    SELECT oracle_id,card_name,quantity from library_storage
                    WHERE deck_id={deck_id};
                    """)
        
        date = datetime.datetime.now()
        for o in range(0,len(card_data)):
            cost_data = recive_query(f"""
                        SELECT usd_price,usd_foil_price from card_cost
                        WHERE oracle_id = '{card_data[o][0]}'
                            AND card_cost.cash_time >= '{str(date)}'::date and card_cost.cash_time < '{str(date)}'::date + '1 day'::interval;
                        """)
            if(len(cost_data)>0):
                price= cost_data[0][0]
                foil_price = cost_data[0][1]
            else:
                send_query(f"""
                        DELETE from card_cost
                        where oracle_id='{card_data[o][0]}';
                        """)
                api_url = f"https://api.scryfall.com/cards/named?exact='{card_data[o][1]}'"
                response = requests.get(api_url)
                json = response.json()
                try:
                    price = float(json["prices"]["usd"])*float(card_data[o][2])
                except Exception:
                    json["prices"]["usd"]=0.0
                price=float(json["prices"]["usd"])

                try:
                    foil_price = float(json["prices"]["usd_foil"])*float(card_data[o][2])
                except Exception:
                    json["prices"]["usd_foil"]=0.0
                foil_price=float(json["prices"]["usd_foil"])

                send_query(f"""
                           INSERT INTO card_cost VALUES ('{card_data[o][0]}',{json["prices"]["usd"]},{json["prices"]["usd_foil"]},'{date}')
                           """)
                time.sleep(0.1)
            total += price*float(card_data[o][2])
            total_foil += foil_price*float(card_data[o][2])
            a = ttk.Label(table_frame, text=str(card_data[o][2]))
            a.grid(column=0, row=o+3+deckcount, sticky=(W,E),ipadx=10)
            table_labels.append(a)

            a = ttk.Label(table_frame, text=str(card_data[o][1]))
            a.grid(column=1, row=o+3+deckcount, sticky=(W,E),ipadx=10)
            table_labels.append(a)

            a = ttk.Label(table_frame, text=str(round(price*card_data[o][2],2)))
            a.grid(column=2, row=o+3+deckcount, sticky=(W,E),ipadx=10)
            table_labels.append(a)

            a = ttk.Label(table_frame, text=str(round(foil_price*card_data[o][2],2)))
            a.grid(column=3, row=o+3+deckcount, sticky=(W,E),ipadx=10)
            table_labels.append(a)                        

            total_output.config(text = "$"+str(round(total,2)))
            total_foil_output.config(text = "$"+str(round(total_foil,2)))

        table_frame.update_idletasks()
        
        bbox = canvas.bbox("all")
        if(bbox):
            w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
            dw, dh = int((w/4) * 4), int((h/len(card_data)) * 20)
            canvas.configure(scrollregion=bbox, width=dw, height=dh)
    

    for i in range(0,len(decks)):
        ttk.Button(mainframe, text=str(decks[i][1]), command=lambda arg1 = decks[i][0]:check_price_data(arg1)).grid(column=0, row=i+2, sticky=(W,E),ipadx=30)

    ttk.Button(mainframe, text="Return", command=mainmenu).grid(column=0, row=1, sticky=W,ipadx=30,ipady=10)

def mainmenu():
    mm_root.title("Main Menu")

    mainframe = ttk.Frame(mm_root, padding="20 20 25 25")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mm_root.columnconfigure(0, weight=1)
    mm_root.rowconfigure(0, weight=1)

    ttk.Button(mainframe, text="Add Deck", command=add_deck).grid(column=0, row=1, sticky=N,ipadx=30,ipady=20)
    ttk.Button(mainframe, text="Load Deck", command=load_deck).grid(column=0, row=2, sticky=N,ipadx=30,ipady=20)
    ttk.Button(mainframe, text="Check Deck Legality", command=check_deck_legal).grid(column=0, row=3, sticky=N,ipadx=30,ipady=20)
    ttk.Button(mainframe, text="Check Deck Price", command=check_deck_price).grid(column=0, row=4, sticky=N,ipadx=30,ipady=20)
    if(gb_user_id==1):
        ttk.Button(mainframe, text="FULL DB RELOAD", command=FullDataReset).grid(column=0, row=5, sticky=N,ipadx=30,ipady=20)

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=30, pady=10)


main()