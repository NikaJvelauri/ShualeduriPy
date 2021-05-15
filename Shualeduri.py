# დავალება 1
# class Ticket:
#     def __init__(self,f_name,price,lang = 'Geo'):
#         self.f_name = f_name
#         self.price = price
#         self.lang = lang
#
#     def __str__(self):
#         return f'წიგნის დასახელება: {self.f_name}, ფასი: {self.price}, ენა: {self.lang}'
#
#
# class User:
#     def __init__(self,b_name,money):
#         self.b_name = b_name
#         self.money = money
#
#     def __str__(self):
#         return f'მყიდველის სახელი: {self.b_name}, არსებული თანხა: {self.money} ლარი'
#
#     def purchase(self,book,num):
#         if self.money > book.price * num:
#             self.money = self.money - num * book.price
#             print(f'თქვენ იყიდეთ {num} ბილეთი')
#         else:
#             print('არ გაქვთ საკმარისი თანხა')
#                 #sxva davalebebze meti dro am ert tasks shevalie errori ver amovxseni ras mtxovda da ra undoda da bolos mivxvdi ro def erti adgilit sheweuli mqonda ris gamoc mesame davaleba ver movaswari :D
#
#
#
#     def deposit(self,pr):
#         print(f'ანგარიშზე ჩაგერიცხათ {pr} ლარი')
#         self.money = self.money + pr
#
#
#
#
# t1 = Ticket('ბეჭდების მბრძანებელი', 25)
# print(t1)
# t2 = Ticket('Avengers',15, "Eng")
# print(t2)
# user1 = User("თამარ აბაშიძე", 100)
# print(user1)
# user1.deposit(200)
# print(user1)
# user1.purchase(t1,2)




#davaleba 2
# import sqlite3
# conn = sqlite3.connect('topgames.sqlite')
# conn.row_factory = sqlite3.Row
# cursor  = conn.cursor()
# c = cursor.execute('SELECT * FROM games WHERE userScore > 8')
# # for each in cursor.fetchall():
# #      print(each['name'])
#
# # for each in cursor.fetchall():
# #     print(each['Publisher'])
#
# cursor.execute('INSERT INTO games(ID, name, genre, ESRBRating, Platform, Publisher, criticScore, userScore, year) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',(501, 'RedDeadRedemption', 'adventure', 'Teen', 'PC', 'Rockstar', 9, 10, 2018))
# #errors agdebs mara  emateba sql cxrilshi chveulebriv
#
#
# conn.commit()
# conn.close()



#დავალება 3
# import json
# with open('questions.json','r') as it:
#     r = json.load(it)
#
# print(r['course'])





















