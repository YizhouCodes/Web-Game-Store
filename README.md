# WSD-Project

1) Team Members
    - Dawid Worek (795674)
    - Ye Yizhou ()
    - Parinaz Avaznejad (795836)

****************************************************************************************************************

2) Features:

1)Authentication :
 - Login, logout and register (both as player or developer)
 - Edit Profile (Both as developer or player)
 - Email validation
 - Pasword Recovery 
 - 3rd party login (OpenID , Gmail)

2) Player functionalities
 - Buy games 
 - Play games
 - Remove games from his/her own list
 - Add Reviews, Rating
 - Searching for games
 - Security restrictions
 - Filtering Games
 - List Player's Games

3) Developer functionalities
 - Add a game (URL)
	- Add a description or Screenshot
	- Assigning a category for the game
 - set price for that game or makes the game free
 - Manage the game 
	- Modify the description or Screenshots
	- Modify Game
	- Remove the Game
 	- Change Price
 - Give feedback to player's reviews
 - Sales statistics
 - Security restrictions

4) Game/service interaction
 - Implement Game and the game service communication (Score, Save, Load , Error, Setting, Load request)

5) Creating a game

6) RESTful API
	- Searching for games
	- Filtering Games
	- Showing high scores for a game


****************************************************************************************************************

3) 
Extra Features : 
	- Edit Profile (Both as developer or player)
	- Email validation
	- Pasword Recovery
	- Remove games from his/her own list
	- Add Reviews, Rating
	- Filtering Games
	- Add a description or Screenshot
	- Assigning a category for the game
	- Give feedback to player's reviews

****************************************************************************************************************

4) 
Database : PostgreSQL
Frontend : HTML5 , CSS(Bootstrap), Java Script (jQuery 3.4.1)
Backend : Django 3.0

Authentication Features: 

1) URLs for Authentication feature:
	- accounts/login/  
	- accounts/logout/
	- accounts/signup_player/
	- accounts/signup_developer/
	- accounts/edit_profile/
	- accounts/password_change/
	- accounts/password_change/done/ 
	- accounts/password_recovery/ 
	- accounts/password_recovery/done/ 

2) Using Django registration app for 
	- Login
	- Logout
	- Register
	- Password Recovery

3) Using Django's Console Backend for Email Validation

4) Using 3rd party Django app like social-django or django-socialregisteration for 3rd party login (OpenID , Gmail)

5) Edit Profile will be implemented from scretch

****************************************************************************************************************

Player Functionalities features:

1) URLs for Player functionalities
	- home/
	- game/<game_id>/<game_name>
	- games

In home url, player profile will be displayed and we will list Player's game, and player is able to remove game from the list. 
Also information about all bought games like Date, Price, Payment information will be shown. When user select a game in list, he will be 
redirected to game/<game_id>/<game_name> and can play the chosen game and add reviews
and rating to the game. In game/<game_id>/<game_name> user can buy the game. In "games" URL
user can see all the available games, and can filter or search games.

** In home url, when user is not authenticated, searching for games is only allowed.

2) This part will be implemented based on MVC (Model, View, Controller) pattern.

****************************************************************************************************************

Developer functionalities features

1) URLs for Developer functionalities
	- home/
	- games/add/
	- game/<game_id>/<game_name>

In home url, developer profile, list of published game by developer will be displayed.
Also, developer can add the URL of the game and he/she wil be redirected to /games/add
URL. In games/add URL, developer can add description and screenshots of the game,
assign a category to the game, and set a price.
In game/<game_id>/<game_name>, develper can manage the game like modifying the descriptions 
and screenshots, update game's URL or change price. On this page the developers
see playe's reviews and can write a response to them. Here they also see
sales statisctics.

2) This part is implemented in the same pattern as player's functionalities.

****************************************************************************************************************

1) URLs for restful API:
	- apiv1/search?q=something
	- apiv1/highscore?g=game_id&n=10
	- apiv1/search?q=search_query&c=category1,category2&sort=rating|price

For searching a game we call RESTful API with addess apiv1/search?q=something,
where 'q' is a parameter which defines query. Search results can be also
filtered by adding two optional parameters: 'c' for categories and 'sort'
for sorting (by games' rating - from the best rated game to the worst or 
prices - from the cheapest to the most expensive). RESTful API with address
'apiv1/highscore?g=game_id&n=10' enables us to get the 'n' highest scores
for the specific game, where 'n' is optional parameter (defeult value is 10).

2) Requests are handled by Django and responses are in JSON format.

****************************************************************************************************************

5) We're going to use Trello for tasks managment and GitLab as a server for
git version control system. Every week we're going to meet to discuss issues,
future work and current state of the project. If it is possible, during
these meetings we will integrate ready components. We're going to start
working on implementation after semester break.

****************************************************************************************************************

6) 

Models: 

1) Game Model: 
	id = integerField(unique ,primary_key)
	title = charField()
	developer = foregin_key
	description = textField()
	dateOfUpload = dateField()
	screenshots = urlField()
	averageRating = floatField()
	category = charField()
	price = floatField()
	minimumAge = IntegerField()
	

2) Review Model: 
	id = IntegerField(unique ,primary_key)
	gameId = foreign_key
	playerId = foreign_key
	rating = IntegerField()
	description = textField()


3) Review-game Model:
	gameId = foreign_key
	reviewId = foreign_key

4) Player Model:     # We are extending abstractUser model from Django framework
	id = IntegerField(unique, primary_key)
	username = charField()
	email = EmailField()
	dateOfBirth = DateField()
	

5) Game-player Model: 
	gameId = IntegerField()
	playerId = IntegerField()
	score = floatField()
	gameState = textField()

6) Developer Model:  # We are extending abstractUser model from Django framework
	id = IntegerField(unique, primary_key)
	username = charField()
	email = EmailField()
	paymentInfo = textField()
	
	
7) File-based Session Model: # it will be used for session handling


****************************************************************************************************************


7) 
Timetable: 

	Start Date = 10.01.2020
	
	Milestone 1:
		Title = Authentication Phase
		Expected Deadline= 17.01.2020
		Tasks: 
			1) Database Deployment
			2) Login, Logout, and registeration
			3) Password Recovery
			4) Email Validation
			5) Edit Profile

	Milestone 2:
		Title = Basic Developer and players Functionalities 
		Expected Deadline = 24.01.2020
		Tasks:
			1) Add a game (URL) with description, screenshots, category, and price
			2) Manage the game (Modify game, description, and price)
			3) Remove the game
			4) Buy games
			5) List player's games
			6) Remove games from his/her own list
			7) Play games
	
	Milestone 3:
		Title = Finishing Developer and players Functionalities
		Expected Deadline = 31.01.2020
		Tasks: 
			1) Add Reviews, Rating for the game
			2) Give feedback to player's reviews
 			3) Generating sales statistics
			4) RESTfule APIs for (Searching games, Filtering games, and showing highscores
			5) Game/Service Interactions

	Milestone 4:
		Title = Advanced features
		Expected Deadline = 07.02.2020
		Tasks:
			1) 3rd party login
			2) Creating a game
			3) Start Testing
			4) Fixing Bugs

	Expected Finish Date = 10.02.2020
	
	
