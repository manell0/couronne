# Testing

[View website on Heroku](https://manello-couronne.herokuapp.com/)

[GO TO README.md](README.md)

## Testing User Stories

### New/Potential User Goals:

1. As a new user, I want to easily navigate through the website to find the relevant content, effortlessly.

   - The navigation is clearly defined and easily navigable for users to find and use.

   - The pages are appropriately named for users wishing to find out about the site.

   - The register match, league pages and the rest of the pages are found easily on each page, no matter the device.
   
2. As a new user, I want to find league pages, tornament and events and register match page.

   - It is easy to find where and how to Log in/Log out and register wherever you are on the site.

3. As a new user, I Want to easily have the ability to get the rules and criteria of the site.

   - The info Modals and info button drop-downs are helps to find what you are looking for.

4. As a new user, I Want to easily have the ability to get to the register match area and start playing couronne games with my friends.

   - The register page can be started directly from the front page in a simple way.

5. As a new user, I want some features on the site:

   - [x] I want to be able to register matches.

   - [x] I want to be able to see the league position.

   - [x] I want to be able to update my profile.

   - [x] I want to be able to get back to the front page.

   - [x] I want to be able to see my  results.

## Manual Testing

### Elements / Items Testing


#### Start Page

The front page works flawlessly in all screen sizes and is self-explanatory.

1. Launched... ✰  links:
   - [x] Modal function 
2. Start Memory Game link:
   - [x] Hover function works. The link goes to the correct URL (game.html) and starts the game.

#### Game Page

The game page works as expected and, no bugs are detected when the game is play. All sounds and buttons/icons work as expected and work in all screen sizes.

3. Play / Pause icon:
   - [x] Hover function works and switches to pause icon when the game paused.
4. Restart icon:
   - [x] Hover function works and, a confirm drop-down menu verifies the response.
5. Mute On / Off icon:
   - [x] Hover function works and switches to mute off icon when the sound muted.
6. Exit icon:
   - [x] Hover function works. The link goes to the correct URL (index.html).

#### Info Modal

Info Modal that appears when you click on the front page link (Info About The Game) works as expected and works in all screen sizes.

7. Start The Memory Game:
   - [x] Hover function works. The link goes to the correct URL (game.html) and starts the game.
8. Back To Main:
   - [x] Hover function works. The link goes to the correct URL (index.html).

#### Result Modal

The Modal automatically displayed when you have completed a game works as expected and works in all screen sizes. You can also see your high score here.

9. Play Again:
   - [x] Hover function works. The link goes to the correct URL (game.html) and starts the game.
10. Back To Main:
    - [x] Hover function works. The link goes to the correct URL (index.html).

- All links lead to the right place and, no broken links
- All icons, headers, and text is in the right place regardless of screen size
- Hover effects on all links
- All functionality in the game is controlled and works satisfactorily
- All Modals are checked and work satisfactorily in all screen sizes

---

![Testing ScreenShot](assets/readme-resources/alert-confirm.jpg)

#### Fig 1:

- An alert box appears when a user has paused the game and tries to click on the game board.
  - The alert box warning sound and other functions work as intended.

#### Fig 2:

- An confirm box appears when a user press the restart icon to confirm whether the user wants to restart the game or not.
  - The confirm box warning sound and other functions work as intended.

---

## Automated Testing

### code Validation

- The [RESPONSIVE WEB DESIGN CHECKER](https://responsivedesignchecker.com/) service is used to check how responsive the website is.

  - Is also checked with the browser's built-in responsive tool (inspect).

- The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML code used.

- The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) service was used to validate the CSS code used.

- The [jshint](https://jshint.com/) service was used to validate the JavaScript code used.

- All HTML and CSS pages are formatted using [The formatter](https://www.freeformatter.com/).

- Used [corrector](https://www.corrector.co/) for spell checking.

### HTML Validation

#### Results:

- All pages on the site have the same result. See below.

![HTML Validation](assets/readme-resources/html-validaor-image.jpg)

### CSS Validation

#### Results:

- It´s only one CSS file in the project (style.css)
  - (The test is done from Swedish browser, translated into English: Congratulations! No errors were found)

![CSS Validation](assets/readme-resources/css-validaor-image.jpg)

## Lighthouse

Screenshot from the index page (desktop device)

[Lighthouse test as PDF ](assets/readme-resources/lighthouse.pdf)
![lighthouse test](assets/readme-resources/lighthouse-index.jpg)

## User Testing

Family members were asked to review the site and documentation to point out any bugs and/or user experience issues. Their helpful advice throughout the process led to many UX changes to create a better experience.

[Back to the top](#Testing) 
