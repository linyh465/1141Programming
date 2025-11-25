a_tickets = 280
eb_tickets = 224
c_tickets = 140

def tickets(age,time):
    if age <= 12 or age >= 65 :
        price = c_tickets

    elif time < 1200 :
        price = eb_tickets

    else :
        price = a_tickets
    return price

age,time = map(int,input().split())
print(tickets(age, time))