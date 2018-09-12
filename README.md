# Stock DashBoard

The idea for this project came from a D3 Stock DasBoard that I had prevouisly seen. After completing the modules in our
 syllabus & seeing that they are small I wanted to find a libereirey that I could build a dashboard with minimil
 code & still have the same effect, but most importantly I wanted the dashboard to clearly define the data & work, & operate
 efficently & seemlsy, & the fact I could use python while this is not a massive dash board , it does excalty what it suppossed to do ,
 it is also very easy to use, with minmil color so as to not distracte from the objective, which is to 
 allows users to select one or more stocks, a start and end date, and have the closing stock prices displayed as a time series,
 
 So I started looking into liberiers such excel, tableau, even power point,& then I discoverd the annocement by plotly,
 While there are some draw backs to ploty , such as a very basic authorisation package that comes in the way a separate dash-auth package.
 dash-auth provides two methods of authentication: HTTP Basic Auth and Plotly OAuth.
 
 HTTP Basic Auth is one of the simplest forms of authentication on the web. 
 
 you the developer hardcode a set of usernames and passwords in your code and send those usernames and passwords to your viewers. There are a few limitations to HTTP Basic Auth:
 Users can not log out of applications
 
 You are responsible for sending the usernames and passwords to your viewers over a secure channel
 
 Your viewers can not create their own account and cannot change their password
 
 You are responsible for safely storing the username and password pairs in your code.   

While these draw backs are sugnifecent , the ease in which plotly is designed really makes up for the draw backs,

Such as creating a whole dashboard using html ,css ,python ,markdown in just 1 file.
 
with the flask framework for the ease of deployment to heroku,

it becomes a very small light but powerfull stack of software technologys.

Creating an account on plotly was a breese , but the cloud console does take some getting used to,

the ploty documentaion is excellent


 
## UX
The UX on this dash board is very simple, purposly so , it does not needlsy take away from fuctioning aspect of the click effects ,

the click effects & hover points are also very mild, but work as intended , the dashboard is very intutive just by observation ,

it is very clear to see the date picker , the user can find & see the Enter a stock symbol: dropdown click box,

these colors are also very mild so to let the user just find & choose the given company in which to run the data against,

Similer also go,s for our Select start and end dates: these elemnets on our dashboard are clearly defined with
a bold but light strong blue, it serves it purpose well,

Our Submit button is ajason to our main elements , leading to the right, but with suffieceint space &
clarity to be easly seen & interperrted,

Our Ploty Interactive Tabs are ajason to our submit button , leading to the right, this tool bar is very powerfull &
is for the more advanced users

The DashBoard its self sits on a barly viisble cross checked grey grid , but protomlitly it is white ,
which creates almost like a interactive white sheet of paper, this is very effective when it comes to reading the data &
visually interpertting the outcome of comparison of stock change, agian very easy to use.

Our Tool Tips are very effetive in there seemless intergration to our calender on the x axis , protraying the rise & fall
on the stock price,

Our line Chart is the main focus , with the chosen company & the chosen date, we see the data clearly defined in light but very contrasting colors
so as to not obscure from it rivals on the main interface , our line chart is very successfull in its operations  










 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process.
 These files should themselves either be included in the project itself (in an separate directory),
or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

- [HTML5](https://https://www.w3schools.com/)
    - The project uses **HTML5** to house the sturcture & the base semantics.
    
- [CSS3](https://https://www.w3schools.com/)
    - The project uses **CSS3** to to Style the elements
    
- [Python3](https://fontawesome.com/)
    - The project uses **fontawesome** to inhance webfonts & increase seo conversion, also to assist the developer in creating a consistant textual flow 
    
- [Python3PandasLibrary](LightHouseChromeExstention)
    - The project uses **tinypng** to compress pictures & ilustrations
    
- [PieCharm](https://www.jetbrains.com/webstorm)
    - The project uses **webstorm** to Write/Code & format the syntax in various languages.
    
- [Flask](https://www.adobe.com/ie/products/illustrator.html)
    - The project uses **Adobe Ai** to create Isomorphic Illustrations & Logos & MockUps
    
- [PlotlyDataVizsulisationLiberary](http://linea.io/)
    - The project uses **LineaBasicIconFonts** to create a strong & characteristic visual refrence to point of focus.
    
- [PlotlyBasicAuth](https://fonts.google.com/)
    - The project uses **GoogleFonts** to enhance the use visual text & ensure readabilty on various platforms & screens

- [Heroku](https://developers.google.com/maps/documentation/geolocation)
    - The project uses **GoogleGeoLocationAPI** to locate the users location thru the use of wifi
    
- [WordPress](LightHouseChromeExstention)
    - The project uses **tinypng** to compress pictures & ilustrations
    
- [WordPress](LightHouseChromeExstention)
    - The project uses **tinypng** to compress pictures & ilustrations
   

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach,
 link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant.
 A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

I was notified of a security issue from GitHub support or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

## HOW THE PROJECT WAS DEPLOYED
## First task was to version control my application on GitHub
## Next task is to create a heroku app using the HerokuCLI. This is turn will create a remote Git Repository that we can link to 
## I already have my Flask venv activated, so next I had to install a new dependency by the package name 
## gunicorn for deploying the app: I accomplished this with the command  pip install gunicorn
## My next task was to create a .gitignore file for my application & code in the recommended /files/folders
- venv
- *.pyc
- .DS_Store
- .env

## Next task was to create  procfile for my application ,these are files that tell Heroku what to do once the project has been deployed.
 
#### Where we enter web:- gunicorn app:server 

## - Here app refers to the filename of our application (app.py) and server refers to the variable server inside that file.
 
##### - To make sure all my dependencies were added to my requirements.txt file I used the pip freeze command and then synchronized them.
##### My dependencies are 
- chardet==3.0.4
- click==6.7
- Cython==0.28.2
- dash==0.21.0
- dash-core-components==0.22.1
- dash-html-components==0.10.0
- dash-renderer==0.12.1
- decorator==4.3.0
- nbformat==4.4.0
- numpy==1.14.2
- pandas==0.22.0
- pandas-datareader==0.6.0
- plotly==2.5.1
- python-dateutil==2.7.2
- pytz==2018.4
- requests==2.18.4
- urllib3==1.22
- Werkzeug==0.14.1
- gunicorn==19.0.0
- psycopg2==2.7.5
- dash-auth==1.0.0
##### - I then logged into heroku 
##### - I did my initial add, commit and push of my project to the git created by Heroku.
##### - I started a dyno/worker a thread to run in the background infinitly to keep my app running with the command ps:scale web=-1
##### - I installed a Heroku addon called mLab to host and monitor my database 24/7 and back it up daily. This involved creating a user, connecting to the database, creating a collection, importing the csv file and making a connection from the Mongo Management Studio.
##### - I imported the os module in my python file, this module allows the code to interact with the underlying operating system you are using, In my file I am using the getenv method this obtains environment variables from the host operating system.
##### - I added my environment variables to my heroku app and to my Flask project in Pycharm.
##### - I updated the python file and did a final add, commit and push to the Heroku Git.
##### My project can be viewed fully deployed on Heroku [here]().

- This is the development & deployed version
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- My Separate git branch can be found here  [GitHub](https://github.com/90t/my_dash_app.git)


In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- I created All the content

### Media
- The photos used in this site were obtained PixelBay.

### Acknowledgements

- I received inspiration for this project from X
