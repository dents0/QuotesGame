import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com"


def read_quotes(filename):
    with open(filename, "r", encoding="utf-8") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("\nWho said the following quote?: ")
    print(quote["text"])
    print()

    guess = ""
    while remaining_guesses:
        guess = input(f"(Guesses remaining: {remaining_guesses}) --> ")
        if guess.lower() == quote["author"].lower() or guess.lower() == quote["author"].lower().split()[-1]:
            print(f"You got it right! It's {quote['author']}!\n".upper())
            break
        remaining_guesses -= 1
        get_hint(quote, remaining_guesses)

    play_again = ""
    while play_again.lower() not in ("yes", "no", "y", "n", "yep", "nope", "yeah", "nah"):
        play_again = input("Would you like to play again? ")
    if play_again.lower() in ("yes", "y", "yep", "yeah"):
        print("You're playing a new game!")
        return start_game(quotes)
    print("Thanks for playing! Goodbye!\n")


def get_hint(quote, remaining_guesses):
    if remaining_guesses == 3:
        bio_page = requests.get(
            f"{BASE_URL}{quote['bio']}")
        soup = BeautifulSoup(bio_page.text, "lxml")
        dob = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(f"The author was born on {dob} {birth_place}.", "\n")
    elif remaining_guesses == 2:
        print(f"Here's a little hint: author's name starts with {quote['author'][0]}", "\n")
    elif remaining_guesses == 1:
        print(
            f"First letter of author's lastname is {quote['author'].strip('.').split()[-1][0]}", "\n")
    else:
        print(f"Game over! The author was {quote['author']}", "\n")


quotes = read_quotes("quotes.csv")
start_game(quotes)
