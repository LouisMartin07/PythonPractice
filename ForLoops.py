#You're having a party and want to invite your friends
#You want to print out invitations for each friend using loops
#The names are in two list's 'names' and 'names1'
#you also need to add two extra names to the list using an 'input' box when you run the code
#Printout one invitation to each friend per line 
#Names should be properly capatlized
#example - "John Cleease! You are invited to the party on Saturday."
#hint, you may need two for loops to do this exercise

names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

names.append(input('Who would you like to add to the party? '))
names1.append(input('Who else would you like to add to the party? '))

party_list = (names) + (names1)

for people in party_list:
     print(f'{people.title()}! You are invited to the party on Saturday.')
    
