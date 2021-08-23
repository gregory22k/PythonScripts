#Mad Libs Game
#A game in which the user completes the blanks and thus creates his own story

import time

#story



p1 = print("Οταν ο . . . ")
blank1 = input('Ποιος? \n')

p2 = print(f"\n{blank1} πηγε για να . . . \n")
blank2 = input('Τι πηγε να κανει? \n')

p3 = print(f"\n{blank2} στο . . . \n")
blank3 = input('Που πηγε? \n')

p4 = print(f"\n{blank3} τότε ανακάλυψε ένα . . .\n")
blank4 = input(f'Τι βρήκε ο {blank1}? \n')

p5 = print(f"\n Πηρε το {blank4} και μετα . . .\n")
blank5 = input('Και μετα τι εκανε??? ')

p6 = print(f"\n {blank5} για να μπορεσει να . . .\n")
blank6 = input('Να μπορεσει να κανει τι? ')

p7 =print(f"\n{blank6} το μεγαλο . . .\n")
blank7 = input('Τι ειναι αυτο το μεγαλο??? ')

p8 = print(f"\n{blank7}. Υστερα, ετρεξε γρηγορα προς . . .\n")
blank8 = input('Προς τα που ετρεξε? ')

p9 = print(f"\n {blank8} για να ....\n")
blank9 = input('Για να τι? Τι παλι? Τι? ')

p10 = print(f"\n{blank9}. Στη συνεχεια, σκεφτηκε πως ηταν αργα και . . .\n")
blank10 = input('Και τι εκανε....?....')

p11 = print(f"\n{blank10}. Eιχε ερθει η ωρα για . . .\n")
blank11 = input('Η ωρα για??? "\U0001F436"\n\n')

print("Η πεποϊστορια ξεκιναει σε \n")

for i in range(3,0,-1): print(i) ; time.sleep(1)

story = print((f' Οταν ο {blank1} πηγε για να {blank2} στο {blank3} τοτε ανακαλυψε ενα {blank4}.') +
        (f'Πηρε το {blank4} και μετα {blank5} για να μπορεσει να {blank6} το μεγαλο {blank7}')+
         (f' Υστερα, ετρεξε γρηγορα προς {blank8} για να {blank9}. Στη συνεχεια, σκεφτηκε πως ηταν αργα και ')+
        (f'{blank10} γιατι ειχε ερθει η ωρα για {blank11}'))

print(story)