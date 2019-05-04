Quotes Game
===========
Project source can be downloaded from https://github.com/dents0/QuotesGame.git
----

Author
------
Deniss Tsokarev

Description
-----------
A game of guessing who said a given quote. All quotes are parsed from http://quotes.toscrape.com/ and saved in a CSV file.

The game starts after running **quotes_game.py**. Users have 4 attempts to guess an author of a quote correctly. Once the guess is correct or there is no attempts left, users will be offered to play again.

Requirements
------------
Python 3.6+ 

Modules:
* [Requests](https://2.python-requests.org/en/master/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

How it works
------------
The project is based on 3 main files: **quotes.csv**, **quotes_game.py** and **scrape_quotes.py**. 

The file **scrape_quotes.py** is using **Requests** and **Beautiful Soup** modules to parse a [website with quotes](http://quotes.toscrape.com/) and then saves the quotes into a CSV file - **quotes.csv**, which is used for the game's logic.

![sc3](https://user-images.githubusercontent.com/28843507/57178894-c6face80-6e77-11e9-998b-c94d47516b03.PNG)
#
Running **quotes_game.py** will start the game.

![sc4](https://user-images.githubusercontent.com/28843507/57178895-c6face80-6e77-11e9-8d64-99260f6f9127.PNG)
#
Users will have **4 attempts** to guess the author correctly. After each attempt a hint will be given. If a guess is correct or there is no attempts left, users will be offered to play again.

![sc5](https://user-images.githubusercontent.com/28843507/57178896-c6face80-6e77-11e9-8c1d-4eef2bd41f50.PNG)
#
Once in a while, users may need to update the quotes. For that, **scrape_quotes.py** should be run.

![sc2](https://user-images.githubusercontent.com/28843507/57178892-c6623800-6e77-11e9-8600-a60655c24d60.PNG)
