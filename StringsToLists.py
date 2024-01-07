# From the list below fill a list(friends_list) properly with the names of all the friends. One per "slot"
# you may need to run same command several times. Use print() statements to work your way through the exercise

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)

#or 
#csv.replace(';',',').replace(':',',').split(','))