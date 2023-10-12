# Fun & Games

Fun & Games is an online portal where anyone can share and/or find interesting ideas on how to spend time in a fun way. Wheter you're simply bored of your routine or you're away and need an inspiration. Users can leave links to pages where they can book an event or simply find out more about a specific activity. Comments section allows users to communicate, share their own experiences or ask questions if needed. Sometimes all it takes to snap out of it is one click away..: [Live Page](https://fun-and-games-a99303d46c12.herokuapp.com/)

![mockup](docs/readme_img/mockup_techsini_screenshot.png)

## Table of Contents
- [Fun & Games](#fun-&-games)
  - [Table of Contents](#table-of-contents)
- [User Experience Design](#user-experience-design)
  - [The Strategy Plane](#the-strategy-plane)
    - [Site Goals](#site-goals)
    - [Agile Planning](#agile-planning)
      - [Milestones](#milestones)
      - [User Stories](#user-stories)

# User Experience Design

## The Strategy Plane

### Site Goals
The site is aimed at anyone who wants to share an interesting and fun way to spend time. This could be anything from activity indoor, outdoor or great locations where you can book an experience with your family or friends.
It is also aimed at people who are simply searching for insporation when they're lacking ideas on what to do wheter it's due to a burn out, change of location or a need to experience new and crazy things.

### Agile Planning

The project was developed using agile methodology. Small features have been assigned to 6 milestones. This was then divided into 4 sprints. Labels have been used to mark which features the project : 'must have', 'should have', 'could have'. This was done so that I create a MVP in the time I have and only focus on the 'should have's' or 'could have's' if time allows. 
Each user story was closed if all acceptance criteria have been met.

Project board has been used to help me with the process [PROJECT BOARD-link] (https://github.com/users/AsiaWi/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Milestone%22%2C%22Labels%22%5D)

![PROJECT BOARD](docs/readme_img/project_board.png)
#### Milestones
- 1-Project setup:
   This was a first task without it I wouldn't be able to continue with any of the project features so it was necessary to set up a basic structure of the project following the user stories included in this milestone.
- 2-Authentication:
   This milestone was needed to allow users to actually use the page so that the page is interactive
- 3-Post Functions:
   Includes all features enabling the CRUD functionality for the user
- 4-UX/UI:
   This improves users journey throughout the page and makes it a smooth experience for everyone.
- 5-Documentation:
   Needed to document the project
- 6-Final deployment: 
   Absolutely necessary step to make sure the page is deployed with no erros and allows anyone access to all features.

#### User Stories
 Each Milestone contains user stories allowing me to build up the project with small features:

- Milestone 1- Project setup
  - As a developer I need to set up the project so that I can build on it and create a mvp
     - Install Django
     - Create project
     - Add first main app
     - Add env.py file
     - Add Procfile
     - Install supporting libraries
     - image database - Cloudinary
     - database - ElephantSQL
     - Settings.py edited to notify django of the supporting libraries
     - Project deployed to Heroku
  - As a developer I need to add static files so that *the website is user friendly
  - As a developer I need to **create base.html file ** so that I have a basic structure of the page for the project
  - As a developer I need to create navigation menu so that a website user can easily navigate between pages
     - Home - for all users
     - SignUp - for unauthorised users
     - Login - for unauthorised users
     - LogOut- for authorised users
     - Profile (drop down) - for authorised users with function to:
       - view profile
       - add entry
  - As a developer I need to create a footer so that I can include social media links
  - As a developer I need to implement a superuser so that I can manage the website
- Milestone 2-Authentication:
  - As a developer I need to setup allauth so that users can have an option of signing up to the website for more features
     - Install allauth
     - Check that users can register/ login/logout of their account
- Milestone 3-Post Functions:
  - As a user I can add a post so that I can share an interesting activity location with others
  - As a post owner I want others to have an option to leave a like under a post so that I know it has been helpful for others
  - As a user I can add a comment to a post so that I can interact with others
  - As a user I can edit posts I have shared so that I can correct any errors or update if necessary
  - As a user I can open the post so that I can view the full post and it's details
  - As a user I can delete previously shared post so that I can make sure no posts which are no longer relevant based on location or my interests are showing for others 
  - As a user I can go to a page to view only my entries so that I can easily access them if needed
  - As a page user I can view all shared posts on the website so that I can find interesting activity ideas
- 4-UX/UI:
  - As a developer I need to create a home page so that user knows what the page is about from the moment they enter it
  - As a user I can navigate between pages so that the pages aren't too chaotic and overloaded
  - As a developer I can style the signup/login/logout pages in order to improve UI/UX 
  - As a user I can see confirmation messages when taking actions so that I know if they were successful or not
  - As a developer I need to implement 403 error page so that **user can see it when unauthorised to view certain content 
  - As a developer I need to implement 404 error page so that user is notified when accessing a link that doesn't exist
  - As a developer I need to implement error 500 page ** so that user gets notified in case of an internal error
- 5-Documentation:
  - As a developer I need to create readme.md file so that the project is supported by good documentation
- 6-Final deployment:
  - As a developer I need to make sure the project is deployed to heroku so that everything looks and works as it should do