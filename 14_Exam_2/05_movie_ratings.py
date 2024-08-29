number_of_films = int(input())

high_film_rating = -10
high_film_rating_name = ""

low_film_rating = 10
low_film_rating_name = ""

total_rating = 0

for film in range(number_of_films):
    film_name = input()
    film_rating = float(input())

    if film_rating > high_film_rating:
        high_film_rating = film_rating
        high_film_rating_name = film_name

    elif film_rating < low_film_rating:
        low_film_rating = film_rating
        low_film_rating_name = film_name

    total_rating += film_rating

print(f"{high_film_rating_name} is with highest rating: {high_film_rating:.1f}")
print(f"{low_film_rating_name} is with lowest rating: {low_film_rating:.1f}")
print(f"Average rating: {total_rating / number_of_films:.1f}")
