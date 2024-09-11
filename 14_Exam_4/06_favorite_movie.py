movie_name = input()

movie_counter = 0
best_movie_name = ""
best_movie_score = 0

while movie_name != "STOP":
    movie_counter += 1
    current_movie_score = 0
    for letter in movie_name:
        if letter.islower():
            current_movie_score += ord(letter) - len(movie_name) * 2
        elif letter.isupper():
            current_movie_score += ord(letter) - len(movie_name)
        else:
            current_movie_score += ord(letter)

    if current_movie_score > best_movie_score:
        best_movie_name = movie_name
        best_movie_score = current_movie_score

    if movie_counter == 7:
        print(
            f"The limit is reached.\nThe best movie for you is {best_movie_name} with {best_movie_score} ASCII sum."
        )
        break

    movie_name = input()

else:
    print(
        f"The best movie for you is {best_movie_name} with {best_movie_score} ASCII sum."
    )