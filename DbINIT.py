import sqlite3

connection = sqlite3.connect('shopping.db')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        Preço REAL NOT NULL,
        description TEXT,
        imageURL TEXT
    )
''')

products = [
    ('Dipirona', 8.00, 'Remédio de rápida ação para tratar dores leves e dores de cabeça, cartela com 8 comprimidos.', 'images/image1.jpg',),
    ('Estomazil', 15.00, 'Remédio para tratar azia de rápida ação, tablete com dois comprimidos solúveis na água.', 'images/image2.jpg',),
    ('Benegripe', 20.00, 'Remédio para tratar os sintomas da gripe, cartela com 10 comprimidos.', 'images/image3.jpg',),
    ('Paracetamol', 15.00, 'Analgésico e antipirético usado para alívio de dores leves e febre.', 'images/image4.jpg',),
    ('Ibuprofeno', 10.00, 'Anti-inflamatório, analgésico e antipirético para dores moderadas e inflamações.', 'images/image5.jpg',),
    ('Amoxicilina', 25.00, 'Antibiótico para infecções bacterianas, como infecções respiratórias e urinárias.', 'images/image6.jpg',),
    ('Omeprazol', 30.00, 'Reduz a produção de ácido no estômago, usado no tratamento de úlceras e refluxo.', 'images/image7.jpg',),
    ('Clonazepam', 20.00, 'Benzodiazepínico usado para tratar crises de ansiedade e epilepsia.', 'images/image8.jpg',),
    ('Loratadina', 14.00, 'Antialérgico para alívio de sintomas de alergias, como coceira e espirros.', 'images/image9.jpg',),
    ('Fluoxetina', 25.00, 'Antidepressivo usado para tratar depressão, ansiedade e outros transtornos.', 'images/image10.jpg',),
    ('Azitromicina', 12.00, 'Antibiótico de amplo espectro para infecções bacterianas como infecções de garganta.', 'images/image11.jpg',),
    ('Cetoconazol', 26.00, 'Antifúngico usado no tratamento de infecções por fungos, como micoses e candidíase.', 'images/image12.jpg',),
    ('Metformina', 70.00, 'Antidiabético que ajuda a controlar os níveis de glicose no sangue.', 'images/image13.jpg',),
    ('Whey Protein', 80.00, 'Suplemento para quem faz musculação.', 'images/image14.jpg',),
    ('Sabonete', 4.00, 'Sabonete com hidratante adicionado.', 'images/image15.jpg',),
    ('Batom', 8.00, 'Para os lábios.', 'images/image16.jpg',),
    ('Protetor labial', 10.00,'Para ajudar a não ressecar os lábios.', 'images/image17.jpg',),
    ('Protetor solar', 20.00,'Para proteção solar.', 'images/image18.jpg',),
    ('Condicionador', 30.00,'Hidrata o cabelo.', 'images/image19.jpg',),
    ('shampoo', 25.00, 'Lava a cabeça.', 'images/image20.jpg',),
    ('Escova de cabelo ricca', 30.00, 'Escova desembaraçadora de cabelo', 'images/image21.jpg',),
    ('Escova de cabelo Hello kitty', 25.00, 'Escova desembaraçadora de cabelo com tema da hello kitty', 'images/image22.jpg',),
    ('queijo da meio qualidarde', 999.00, '"É um queijo"', 'images/image23.jpg',),
    ('Ï̷̧̡̡̡̛͈̹̰͍̖̫̜̗̘̘̖̗̺̙͈̪̩͇̪͓͛́́͌͂͒͑̉̈́̔̂͗̌̈̿͋͗̃̂̆̾̐̓̋͒͘̕̕͝͠͝š̵̖͈̙̱͇̯̂̉̈́̓̓̌̎̏͐͆̓̊͐̊͌̌̔̿̀́̚͘̕͝͝͠ ̵̧̨̡͈̘̞̯͎̝͔͎͍̟̼̦͎̠̹͓̰̙̻̫̪̖̬̟͚̗͉̠̻͉̹͍̥̰͕̳̩͔͎͔͙̓̕̚͜t̷̛̛̝̫͍̭͋͂̔͂́̈́̓̄̉̑̽̌͑͌́͂̐̈́̊͐̄̌͊̽́̓͛̋͒̍̆̍͛̽̚̚̚̚͘̚͠͠͝͝͝ĥ̶̡̛͓͓̥̜̰̮͓̰̞͙̪͚͚̠̯̝̱͖̞̭̝̙͉̖̝̰͈̗̥͚̙̮̘̪͙̞̣̞̱̭̻̦̮́͆́̈́̀̂̓͆̍͂̿̄̉͗̃͛͒̀͛́̄̍̀̀̓̃̄͂̿͊̄̂̽̍̒̍̌͊̕͘̚͝͠͠ͅͅï̶̧̪̝̥̪̞͔̼̩̩͓̳̮̱͈̬͖̮̥̠̝͈͓̞̝̮̦͎̖̣̻̦͕̤̗̫̲͓͖̝͓̲͑́̂̎͆̇̉̀̓̃͗͆̔͗̄͂͊̑̚̚͜͜s̷̢̧̡̧̨̨̨͙͔̪̲̺̩̗͚̻͕̺̖̣̹͍̯̭̺͉̱̜̟̞̰̖̩̳̠̻̫͍̙͇̼̾̑͌̂̇̀̓̑́̓̂͋͛̋̓̈́̊̉́́̃̈́̑͊͋͗͆̉͘͘̕͜͝͠ͅͅͅ ̸̧̡̨̛̖̠̝̳̲̬̞̥̝̼̥̗̻̹͈̙̝̦̩̗̝̗̦̟̪̙͎̝̳͍̤̹͕̰̻͍͚͈͖̩̱̳̐̄̄̿̉̎̒̃̀̎̓̋̔̉̿͊̎̎͒̽̒̊̾̀̍͌̿̆̇̀̆̾͒̕̕͘͘͜͠ͅr̵̡̨̡̧̝̫̼̠̙̩̠͕̩͓̳̬̤̙͕͎̦̬̯͍̥̤͈͙̲̪̪͌̊̿̅͌͒͆̍̂͋͌͗́͜͠͝ę̷̛̛́͑̈́̇͊̈́̆̽͂̉̑́͗́̅́͐͆̓̿̆̓͋̅̾́̏́̏͆̀̀̕͝͠͝͝ằ̶̛̙͚̲͉̘̮̙̮̜̘̭̦̫͇̖̺̞̩̬̣̳̻̬̞͔͠͝ļ̸̨̢̛̛̹̬̫̝̦̘̪͔̗̳̤̔̈̽́̏̏̂̓̈́͐͌̿̓̈̉̋̀̌̆͒̃̓̊̌̍̚̚͠͝i̴̧̡̨̘̣̬̝̤̘͙̫̭̗̝͉͖͇͍̹̣̹̜͖̲̟͎̦͂̔̇̄́̋̎̔͋̓̈̌̋͂̀͛̔̇̔̈̃͌͐͋̒̈́̚̚̕̚͜͝͝t̶̡̡̨͔̙̥̼̖̞̫̤͚͈͕͊́̀́̿̀̐͗͜ͅy̴̢̡̛̪̰̱̭̪̹͕̘̝̥̻͍͎̤̎͗̀̓̏̍̈́̐͐͆͆̆̎͌̚͠?̵̡̧̢̨̭̳̲̮̰͖̩̪̗̫̪͔̘̬̞̮̦͖̰̗̮͕̝͕̉͊͊̏̿͌̓̓̈́̆̉̈̎̿͗̓̓̑̀͒͐̕̚͜͜͝͠ͅ', 00.00, 'P̷̨̡͉̪̫̣̮͉̘͕̖̞͔̣̼̱͚̯̲̐͊͋̽͛͛͆͗͆͒̿̒̓́̈̂̆̾̀̅͋̈̄̋̽́̏̉̈́͂͜ͅl̶̨̨̡̧̧̺̰̻̯̯̳͇͈̫̳̮̰̓͜͜ͅ ̴̛̮̦̓̆̿͌̊̍͑͌͌̈͂͐̓͗̒̔̾͆̂̀͌̔̍͛̚̕͜͝͝͠͝ě̴̢̧̲̘͔̹͈̦͕̝̜̪̱̼͓̲͕̩̠̗̭̙̪̪̗̭̦̲̦͙̳͕̌̊͂̾̀͊͒͐̕͜ ̸̭͓̠̬̭͉̥̝̯̯̳̟̤͍̱̟̫̱̝͎̦̙̠͇̮̳̑̈́ͅą̷̛̥͉̭̣̱̭̱̱̪̫͕̙̙͈͚̙̥͎̞͉͚͔̟̱̝̬̮͚̩͈̈́̓̏̄̂̉̈̽̀͗͋͆̊̌̇̇̾̏̾͌̆̈́̍̌̏̉͛͗̈́̓̂̽̐̍͆͘͘̕̕͜͠͠s̵̨̢̢̡̡̛̛̱̦̞̺͔̝͓̖̩͕͔͓̭̠̲͈̻͇͉̙̠͉̹̦͖̫͓͚̱̍̌͑̏͐̏̒̅̊̄̏̈́̾̽̌͊̋͛̐̌͌̇̏̎͝ͅ ̸̨̛̹̝̙͙̦̥̥̳̹͎̮̮̰̘͈͉͓͉̳̥̟̖̤̥͕̾̉͆͋̇̆͆̃̀̌͋̿̾͒̔̆̅̿̊̇́͒̆̆͊̍́̉̊͌̅̓̈̾̔̎͂͊̀̚͘̕͠͝ė̷̢̢̧̢̨̗̼̟̥̟͙̪̣͎̳͕̫͙̬̜͎͎̲͓̼̫̺͚̠͙̖̹̞̣̩͕̺̼͉̙̝̥̩̲̌̈̏̍̀̿̌͛̎̈́̈͋̃̿̋͂̀͗͊͋́͛͐͂̀̆͊͗̄́͊͐̓͛̓͘̕̚͜͝͠͝ ̶͕͚͇͙͚̮̖̻̙̮̄̄̂̌͗̈́̽̑͌́̂̅͊̉͐̓̃͛̐̏͂̋̋̋͊̔̃͊̉̈́́̓͆̈͆͘̕͝e̷̡̧̩͓̜̙̩̫̠͉͈̬̣͔̝͕̣̞̻͍̭̯̲̦͊̅̽̔̿͋̄͑͜͠ ̶̨̢̛̦͕͚̺͓͖̟̪̦̹̦̻̘̻̼̥͔̫͇̙̌̓̈́̏̌̒̈̒̐̓̓̉̿̎̉̍̿͋̌̌́̍̌̉̉́͊̍̌͛̐̌̋͌̔̕͝͝͠n̸̗̲̬̬͂́̄̓̀̓̽̈́̍̍̂͛̋̊͗͌͒͊̑̐͆̅̑́̅̐̋̋̔͊̿͗̾̚̚͘͘͝͠͝͝d̴̡̨̨̨̡̛̤͔͇̺͙̹̘̯̖̭̝̯͇̯̫̙̗̺̟̳̗͎̞̓̊͐̇̏͗̑͆̇̌̀̀̂͌́̄̏̈́͆͆̄̌̏̑̋͒͒̈́̒̀̇̓̀̆̃̅̾͐͘̚͝͝ ̷̢͖͇̺̯̲͔̝̼̋̿͊͐͐̿̍͌̽͝͠ͅm̷̨̛̤̼̠͇̘͖̋̾̓́̈́̾̌͗́̍͝y̷̡͖̫̮̼͈̩̘͉͍͕͙̟̍̆̀͂́̀̾͛̊͗̿̋́̓͘̚̚ͅͅ ̶̧̢̡̨̧͎͎̫̻͓͓̝͚͇͔̦̼͓̲̬̳̘͇̻͎͍̭̙͇̙̤̯̯̫̎̆͐̑̕ͅ ̴̧̛̮̲̣̥͖̻̮̯̩̟͎̟̝̓̆̆̆͂͂̓͂͗͒͂̅̃̓̇͐̀̊̀̑̐̿́̋͋́̿͒̚͘̚̕͠͠͝͝͠͝ͅm̷̫̝͈̣͖͔̲̩̭̣̣̺̮̘͋͌̇̂̍͌̃͌͐̈́̓̿̾́̈̆̊́̍̉̓̊͋̐̿͗̎̓̔̋̅̈̃̕̚̕͠͝͠ͅì̴̧̝̮̬̼̉̈́ ̶̧̡̢̛̣̩̯̠̠̹̗̘̥̠̮͙͚͕̖͔̥̺̳̞̻͈̲̱̈́͛̆͌̏̀̚͜͝ͅs̶̨̨̨̧̧̛̬̬̤̙̼͎̜͎̳̠͕̟̭̬̲͈̺͍͔̦̭̥͍͓̔͒̅́̃̓̐̀̎̊̇́̆̅̏̃͛̃͗̐̈́̿̿̅͊͐̀̌̈́̋̇̈͋̿͘̚͜͠ͅͅe̵̢̛̛̥͐̓̽̅̈́̿̏̏̓́̇́̍̈́̈́̓̎̈̃̄̓̈́͛͐͂̋͂͗̈́͆̓̔̋̀͋̀̒̓̓̀̌̕͝͝ ̷̨̡̨̛͎̥̜̤̻̬̼̩̰̯̩̝̞̬̼̙̙̹̏̀̆̎͆̾̈́̍̇̊͑͂̅̂̀̅̉̾̊̉́̅̑̒͆̊̓̀̑̈́̈̑͆̓̈͐̈͑͌̕̕̕͠͠͠͠͝ ̶̧̢̡̛͓͔̦͚̤̞̹̲̱͎͔̃̈́̄̏͂̀̄̋̄̇͛̆͆̍̋̀̂̄̏̀͋̓̓̈́͋͘̕̕͜͜͝͝ͅ ̷̝͇̳͕͕̤̻͔̠̱̙̠̩̜̟̬͇̼͙͚͕͖̘͎͎͓̐́͛́́́̆͘͝͠r̸̨̛̦͔̻̘̭̫̣̟͈̼͉̟̗̮͓͕̽̅̐̐̒̋͌̒͐̌͊̃̏̈́̇̀̓̑̌̎̋̈́̐̈́̒͐̑̈́̈́̒̏̍̈́̾͌͌̀̔̅̉͘̕͜͠͝͝͠y̷̧̧̢̡̧̧̛̙̣̬̩͍͔̟̱̼̰̪̻͕̱̣̰͚͖͍̞̣͕̬̥̯͖̯͓̮͉̤͔̦͍̰̺̖͓̲̺̰͛̑̍̐̓̔̃̈́͗̍͗̇̾̍̇̉̈́̂̍̔̈͑͋̀̆͑͆̒̏̋͂͑͌̄̕͘͘͝', 'images/image24.jpg',),
]

cursor.executemany('''
    INSERT INTO products (name, Preço, description, imageURL)
    VALUES (?, ?, ?, ?)
''', products)

connection.commit()
connection.close()

print("Db iniciado")
