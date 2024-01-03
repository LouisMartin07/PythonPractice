#You sell lemonade over two weeks, the list show number of lemonades sold per week
#profit for each lemonade sold is 1.5$
#add another day to week 2 list by capturing a number as input
#Combine the two lists into the list called 'sales'
#Calc/ print how much you haver earned on the following
#best day/ worst day/ seperately and in total

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

day14=input("please enter how much lemonade was sold on day 14? ")

sales_w2.append(int(day14))
sales = sales_w1 + sales_w2
bestDay = (max(sales)) * 1.5
worstDay = (min(sales)) * 1.5
total = (sum(sales)) * 1.5

print(f'The best days sales were {bestDay}, the worst days sales were {worstDay} and the total sales were {total}')