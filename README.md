# WSD-Project

1) Team Members
    - Dawid Worek (795674)
    - Ye Yizhou (795852)
    - Parinaz Avaznejad (795836)

****************************************************************************************************************

2) Features:

1) Authentication :
 - Login, logout and registration (both as a player and a developer)
 - Edit profile (both as a developer and a player)
 - Email validation after signing up
 - Password recovery 
 - 3rd party login (OpenID , Gmail)

2) Player functionalities
 - Purchasing games
 - Playing games
 - Removing games from one's own list
 - Reviewing games and also rating them
 - Searching for games
 - Security restrictions
 - Filtering games by game categories, price and name
 - Listing games owned by oneself

3) Developer functionalities
 - Adding a game (URL)
	- Adding a description or a screenshot
	- Assigning categories for the game
 - Setting a price for a game (or free)
 - Managing a game 
	- Modifying the description or screenshots
	- Modify the game
	- Removing the game
 	- Changing the price
 - Providing feedback to player reviews
 - Sales statistics
 - Security restrictions

4) Game/service interaction
 - Implement game and the game service communication (Score, Save, Load , Error, Setting, Load request)

5) Creating a game

6) RESTful API
	- Searching for games
	- Filtering games
	- Displaying highscores for a game


****************************************************************************************************************

3) 
Extra Features : 
	- Edit profile (both as a developer and a player)
	- Email validation after signing up
	- Pasword recovery
	- Remove games from one's own list
	- Reviewing games and also rating them
	- Filtering games by game categories, price and name
	- Adding a description or a screenshott
	- Assigning categories for the game
	- Providing feedback to player reviews

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

5) Edit Profile will be implemented from scratch

****************************************************************************************************************

Player functionality features:

1) URLs for Player functionalities
	- home/
	- game/<game_id>/<game_name>
	- games

In home url, a player profile is displayed along with the games that the player in question owns.
The user can remove these games from their list if they choose so.
The user also has access to a purchase history page. Upon selecting a game from their list, they will be 
redirected to game/<game_id>/<game_name> and can either proceed to play the chosen game or add textual reviews
coupled with numeric ratings. In game/<game_id>/<game_name> the user can buy the game. In "games" URL
user can see all the available games, and can filter or search games.

** In home url, when user is not authenticated, only searching the games is permitted.

2) This part will be implemented based on MVC (Model, View, Controller) pattern.

****************************************************************************************************************

Developer functionality features

1) URLs for Developer functionalities
	- home/
	- games/add/
	- game/<game_id>/<game_name>

In home url, developer profile, list of published games by the developer will be displayed.
Also, developer can add the URL of the game and they will be redirected to /games/add
URL. In games/add URL, the developer can set the description and upload screenshots of the game,
assign categories to the game, and set a price.
In game/<game_id>/<game_name>, the developer can manage the game by modifying the descriptions 
and screenshots, updating the game's URL or changing the price. On this page the developers
see the player reviews and can write responses to them. Here they also see
sales statistics.

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
for the specific game, where 'n' is optional parameter (default value is 10).

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
			2) Login, Logout, and registration
			3) Password recovery
			4) Email validation
			5) Edit profile

	Milestone 2:
		Title = Basic Developer and players Functionalities 
		Expected Deadline = 24.01.2020
		Tasks:
			1) Adding a game (URL) with description, screenshots, category, and price
			2) Managing the game (Modify game, description, and price)
			3) Removing the game
			4) Purchasing games
			5) Listing one's games
			6) Removing a game from their list
			7) Playing games
	
	Milestone 3:
		Title = Finishing Developer and players Functionalities
		Expected Deadline = 31.01.2020
		Tasks: 
			1) Adding reviews, ratings for the game
			2) Providing feedback to player reviews
 			3) Generating sales statistics
			4) RESTful APIs for (Searching games, Filtering games, and showing highscores
			5) Game/Service Interactions

	Milestone 4:
		Title = Advanced features
		Expected Deadline = 07.02.2020
		Tasks:
			1) 3rd party login
			2) Creating a game
			3) Testing
			4) Fixing Bugs

	Expected Finish Date = 10.02.2020
	
	
