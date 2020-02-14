# WSD-Project Final Report


### 1. Team Members
- Dawid Worek (795674)
- Ye Yizhou (795852)
- Parinaz Avaznejad (795836)

****************************************************************************************************************

### 2.1. Features
1) Authentication :
    - Login, logout and registration (both as a player and a developer)
    - Email validation after signing up
    - Password recovery (extra)
    - **Expected points:** 200 points. We have done everything required here along with something we consider essential for any service with authentication (password recovery).

2) Player functionalities
    - Purchasing games
    - Playing games
    - Reviewing games and also rating them (extra)
    - Filtering games based on the names and the categories
    - Security restrictions (players can only play the games that they own)
    - Listing games owned by oneself (quality of life)
    - **Expected points:** 300 points. We have done everything required here along with a player review system that provides extra information to other players about any given game.

3) Developer functionalities
    - Adding a game (URL)
	    - Adding a description and a screenshot
	    - Assigning categories for the game
	    - Age restriction
    - Setting a price for a game (or free)
    - Managing a game 
    	- Modifying all the metadata related to the game (description, screenshot, name, category and age restriction)
    - Sales statistics (how many games have been bought in total)
    - Security restrictions (only developers can add games and only the creator of the game can modify it)
    - **Expected points:** 180 points. Our sales statistics only display the number of games bought, hence the reduction in points.

4) Game/service interaction
    - Implement game and the game service communication (Score, Save, Load , Error, Setting, Load request).
    - **Expected points:** 200 points. We have all the features requested here. Games send data to the service (highscores, saving) and the service sends data back to the game (loading).

5) Quality of Work
	- Model-view-template is utilized.
	- Extensive manual testing was performed.
	- Styling that is pleasant to the eye and informative error messages for the user.
	- Extra features listed in other sections.
	- Comments when necessary.
	- **Expected points:** 100 points. We don't have comments everywhere, but our code in general is highly logical (naming conventions with functions and variables) and thus easy to read.

6) Non-functional requirements
	- Project plan (not yet graded)
	- The project was managed well with the use of Git and Trello. We had frequent face-to-face meetings in an fashion similar to agile development. 
	- Our distribution of tasks was very successful which is evident from the relatively small amount of merge conflicts.
	- **Expected points:** 200 points. The project plan and the demo are yet to be graded. However, we believe we managed to achieve everything that was required in this section. 


### 2.2. More Features

1) Save/load and resolution feature
	- Saving and loading games is supported
	- **Expected points:** 100 points. 

2) 3rd party login
	- Facebook login is supported
	- **Expected points:** 100 points. We assume that only one of the third party integrations was required for the full 100 points. 

3) RESTful API
	- Searching for games (name, category, description, developer name)
	- Filtering games (rating, date of upload, price, minimum_age, number of purchases)
	- Ordering by various metadata fields (name, category, rating, price etc.)
	- Displaying highscores for a game
	- A developer account is required to access the API.
	- The API offers some additional parameters, such as:
		- Excluding a field from the response
		- More flexibility in filtering e.g. min_value and max_value of some parameter.
	- **Expected points:** 100 points. We have a fully functional API. 

4) Own game
	- A game about recognizing flags belonging to different countries. 
	- Saving, loading and highscore functionality.
	- The game is hosted on Heroku: https://radiant-refuge-85599.herokuapp.com/static/game/index.html
	- **Expected points:** 100 points. 

5) Mobile friendly
	- Works and looks good on mobile devices.
	- **Expected points:** 50 points. 

6) Social media sharing
	- Not implementd
	- **Expected points:** 0 points.

****************************************************************************************************************

### 3. Instructions

- **Project URL:** http://radiant-refuge-85599.herokuapp.com/

**Player**

Before gaining access to any functionalities available as a player, you have to register a new user using the "Login"-button in the right corner of the navigation bar on top of the screen. Once there, a link is available to register a new account. The "Player"-tab is chosen by default (instead of developer). Once the required data is filled in and the "Sign up"-button is pressed you will receive a confirmation email with a link to finish your registration. You can also opt to register with your Facebook credentials by clicking the Facebook-icon. As a returning user only logging in is required. 

The index page has a carousel-view showcasing the games available and also lists the individual games. There is a search bar on the top left and a categorical filter below it. By clicking the title of a game or the screenshot representing it you can access a page with more detailed information about the given game. In this, view you can purchase the game. If the game is already owned, you get access to playing the game. You also get access to writing a review (and rating) about the game. The rating you provide will affect the average rating of the game that is visible to everyone. You can also see a list of games that you own (and play them) by clicking the "my games"-link on the navigation bar.

**Developer**

As a developer you have to register using the developer-tab. The registration through Facebook is not available to developers. The "Payment ID"-field should be: **YXOizFdTRC1Qcm9qZWN0**.

The developer has access to the same features as the player in the index page. On the page of a specific game the developer can't write reviews or purchase games. On "my games"-page the developer can see the games that they created and also create a new game. This is done by filling in the fields and submitting the form. 

In addition to this, the developer has access to the RESTful API "/apiv1/games" and "apiv1/highscores". Accessing these requires the developer to be either logged in or they can provide the credentials with the request. Pressing the "Filter"-button provides filtering options along with ordering options. The developer can also include additional GET-parameters in the url that are not listed as available filters. These are "excluding", "min_value" and "max_value"."Excluding" removes the specified value from the fields returned as the results. The latter two can be utilized to specify the minimum and the maximum value respectively e.g. min_price=1 would filter only results that have a price higher or equal to 1.



****************************************************************************************************************

### 4.1. Work Distribution

- Dawid Worek (795674) 
	- RESTful API.
	- Buying games.
	- Adding games and game/service interactions.
	- Game page (show_game.html).
	- Models.
- Ye Yizhou (795852)
	- Login and logout.
	- Homepage (index.html) and listing one's games.
	- Reviews and ratings.
	- Searching games and sorting by category.
	- The final report.
- Parinaz Avaznejad (795836)
	- Everything related to registration including password recovery, email validation.
	- 3rd party login (Facebook).
	- Our own game.
	- Polishing css.

- Everyone wrote css and Javascript related to the templates assigned to them. 
- Deployment was a group effort done together.

### 4.2. General Thoughts About The Project

We felt like designing the models was challenging due to insufficient experience in designing systems. More specifically, trying to predict the fields felt very abstract at the beginning. We were also waiting for feedback on the project plan to guide us forward. This wasn't available unfortunately. 

The 3rd party login with Facebook wasn't hard per se, however, combining that with the deployment to Heroku raised some issues that were previously unpredictable. We also found testing to be quite a tedious process with lots of intricacies involving rare corner cases. 

We feel like we were very successful in managing the project as we did not have to deviate a lot from the original plan. Every member was satisfied with the tasks assigned to them and in case of issues, other members would always step up and help. This friendly work environment inspired us to implement extra features that were not listed, such as reviews and password recovery. We're also very happy with the overall look and feel of the project. In terms of usability, nothing feels overly burdensome.