is_weekend = True
is_holiday = False
have_time = True
is_sunny = True

# Combining conditions with 'and' and 'or'
if is_weekend or is_holiday:
    if have_time and is_sunny:
        print("Let's go for a picnic!")
    elif have_time:
        print("Let's catch a movie or visit a museum.")
    else:
        print("Time to relax and recharge.")
else:  # It's a weekday and not a holiday
    print("Gotta get to work!")

# Using 'not' for negation
is_raining = False

if not is_raining:  # Equivalent to "if is_raining == False"
    print("No need for an umbrella today.")
else:
    print("Don't forget your raincoat!")

# More complex example with 'and', 'or', and 'not'
money_in_wallet = 20
price_of_book = 15
price_of_movie_ticket = 12

if (money_in_wallet >= price_of_book or money_in_wallet >= price_of_movie_ticket) and have_time:
    print("You can afford either the book or the movie (or both!).")
elif money_in_wallet >= price_of_book:
    print("You can buy the book.")
elif money_in_wallet >= price_of_movie_ticket:
    print("You can watch the movie.")
else:
    print("You don't have enough money for either option.")
