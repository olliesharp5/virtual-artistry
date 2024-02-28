# Virtual Artistry

Virtual Artistry is an online platform designed to showcase and sell artwork from various artists. It serves as a digital marketplace where artists can connect with art enthusiasts and potential buyers worldwide.

# Table of Contents
- [Virtual Artistry](#virtual-artistry)
- [Table of Contents](#table-of-contents)
  - [Demo](#demo)
    - [A live demo to the website can be found here](#a-live-demo-to-the-website-can-be-found-here)
  - [UX](#ux)
  - [User stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Skeleton](#skeleton)
    - [Planning](#planning)
    - [Surface](#surface)
  - [Technologies](#technologies)
    - [Libraries](#libraries)
    - [Frameworks & Extensions](#frameworks--extensions)
    - [Others](#others)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
  - [Testing](#testing)
    - [Validator Testing](#validator-testing)
      - [HTML](#html)
      - [CSS](#css)
      - [WebAim Contrast checker](#webaim-contrast-checker)
      - [Fixed Bugs](#fixed-bugs)
      - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)

## Demo

![Website look on different devices](INSERT FILEPATH)

### A live demo to the website can be found [here](INSERT LINK TO LIVE SITE)

## UX
WHO IS THE SITE TARGETING

## User stories
INSERT USER STORIES

### Strategy


### Scope

**User Management**
   - User registration and authentication.
   - User roles and permissions for various levels of access.
   - Profile creation and management.

**Communication Features**
   - Real-time messaging functionality for group discussions in channels.
   - Direct messaging for private one-on-one conversations.
   - Multimedia support, including file attachments and emoji reactions.

**Channel Management**
   - Creation, joining, and leaving of channels.
   - Categorization of channels based on Code Innovate topics or modules.
   - Ability to search and discover relevant channels.

**User Interface and Experience**
   - Intuitive and user-friendly interface for seamless navigation.
   - Responsive design for accessibility on various devices.
   - Personalization options for user profiles.

**Responsiveness**<br>
* Create a responsive design for desktop, tablet and mobile devices.<br><br>


**Website Sections:**
1. **_Artwork_** 
2. **__** 
3. **__** 
4. **_** 
5. **__** 
6. **__**  
7. **__**  
8. **_Footer:_** This is not the main section of the website but rather an ending to the website with social media links. 

### Skeleton
The website is designed to be clear and simple. The site has a simple tree structure with hierarchical flows from top to bottom.

**Wireframe**
The wireframe is designed using Balsamiq software.

![wireframe](INSERT FILEPATH)

### Planning
The project was designed meticulously using the agile framework, epitomizing the benefits of a dynamic team-based workflow. Our major planning and communication tool was a Kanban board, used to visualize tasks, outline their status and progress, and precisely denote who was responsible for what. The project was broken down into several manageable tasks and then plotted on the Kanban board, structured into columns specifying stages such as 'To-Do', 'In Progress', and 'Done'. The use of the Kanban board ensured real-time communication of work status to the team, providing a rich landscape of our project progress at any given time. This fostered timely reviews, quick alterations, and overall fluidity, propelling the project towards successful accomplishment.

![kanban](INSERT FILEPATH)


### Surface

The color pallette for the site was chosen because it matched the colour associated with currency and also provided good contrast and accessibility. The font family was chosen as it is easy to read.

| Hex | RGB |
| -------------- | ----------------- |
| #244c3c | (36,76,60) |
| #526c5b | (82,108,91) |
| #dcdcbb | (220,220,187) |
| #425e6a | (66,94,106) |
| #fa6e06 | (250,110,6) |

## Technologies <hr>

The website is designed using following technologies: HTML, CSS, Bootstrap, Javascript, Django, MarkDown

### Libraries

* [Font Awesome](https://fontawesome.com/v4.7.0/) - Font Awesome icons were used throughout the web-site.

### Frameworks & Extensions

* [Django](https://www.djangoproject.com/) – Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Bootstrap](https://getbootstrap.com/) – Bootstrap is a web framework that focuses on simplifying the development of informative web pages.

### Others

* [GitHub](https://github.com/) - GitHub is a global company that provides hosting for software development version control using Git.
* [Gitpod](https://gitpod.io/workspaces/) - One-click ready-to-code development environments for GitHub.
* [Heroku](https://dashboard.heroku.com/) - Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps.

## Features

### Existing Features

* SECTION OF WEBSITE 
DESCRIPTION OF SITE 
  
![SCREENSHOT](INSERT FILEPATH)


INSERT OTHER SITE PAGES 


### Features Left to Implement

In the future I would like to add, 
* 
## Testing

* I tested the site, and it works in different web browsers: Chrome, Firefox, and Microsoft Edge.
* On mobile devices, I tested the my site on a Samsung Galaxy S21 Ultra with the Samsung browser and an iPhone 13 with the Safari browser.
* I confirmed that the site is responsive and functions on different screen sizes using the devtools device toolbar.

### Validator Testing

#### HTML
No errors were found when passing through the official W3C validator.

![html_validator](INSERT FILEPATH)

#### CSS
No errors were found when passing through the official (Jigsaw) validator.

![css_validator](INSERT FILEPATH)

#### Python Linter

#### JSHint

#### WebAim Contrast checker 
No errors were found when passing through the contrast validator.

![contrast_validator](INSERT FILEPATH)


#### Fixed Bugs

* Unable to render crispyforms 
* Form unable to POST to update a review due to an error in url.py filepath. /art/ needed in front of urlpattern
* reviewId coming throuigh as null. Debugged Js using console.log queries, amended the getAttribute value to data-review_id from review_id to obtain the correct reviewid value. 

#### Unfixed Bugs


## Deployment

### Version Control

The following git commands were used throughout development to push code to the remote repo:

- git add - This command was used to add the file(s) to the staging area before they are committed.

- git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.

- git push - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

- Heroku provides a platform for hosting web applications.
- The deployed site will update automatically upon new commits to the main branch.


### Performance
The performance of the website was tested with [Google Lighthouse](INSERT LINK TO REPORT)

**Lighthouse reports:**<br>


## Credits

### Content


### Media

* The icon used for the favicon is from favicon.io
* The icons in the footer were taken from Font Awesome