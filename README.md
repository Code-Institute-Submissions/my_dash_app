#### Clive Noonan , Full Stack Student In CODE INSTITUTE
## NASTAC Plotly Stock DashBoard
##### Child To Data Discoverys.com[datadiscoverys.com](https://datadiscoverys.com/)

- I am currently a student at the Code Institute Studing Full Stack Diploma in Software Development. 
- This is part of the Four frontends which make the whole project of DataDiscoverys.com which is the last project
- that I will be Submittings

- This is the third of five projects which I must complete in order to be awarded the globally recognised Diploma 
- from Edinburgh Napier University. This Project utilises wholemiriad of technology.
- Consult the tech section in each README.md or the Super README.md

- The idea for this project came from a D3 Stock DasBoard that I had prevouisly seen. After completing the modules in our
 - syllabus & seeing that they are small I wanted to find a libereirey that I could build a dashboard with minimil
 - code & still have the same effect, but most importantly I wanted the dashboard to clearly define the data & for the dashboard operate
 - efficently & seemlsy, & the fact I could use python while this is not a massive dash board , it does excalty what it suppossed to do ,
 - it is also very easy to use, with minimil color so as to not distracte from the objective, which is to 
 - allow users to select one or more stocks, a start and end date, and have the closing stock prices displayed as a time series,
 
 - So I started looking into liberiers such excel, tableau, even power point,& then I discoverd the annocement by plotly,
 - While there are some draw backs to ploty , such as a very basic authorisation package that comes in the way a separate dash-auth package.
 - dash-auth provides two methods of authentication: HTTP Basic Auth and Plotly OAuth.
 
 - HTTP Basic Auth is one of the simplest forms of authentication on the web. 
 
 - you the developer hardcode a set of usernames and passwords in your code and send those usernames and passwords to your viewers.
 - There are a few limitations to HTTP Basic Auth:
  
 - Users can not log out of applications
 
 - You are responsible for sending the usernames and passwords to your viewers over a secure channel
 
 - Your viewers can not create their own account and cannot change their password
 
 - You are responsible for safely storing the username and password pairs in your code.   

 - While these draw backs are sugnifecent , the ease in which plotly is designed really makes up for the draw backs,

 - Such as creating a whole dashboard using html ,css ,python ,markdown in just 1 file.
 
 - with the flask framework for the ease of deployment to heroku,

 - it becomes a very small light but powerfull stack of software technologys.

 - Creating an account on plotly was a breese , but the cloud console does take some getting used to,

 - the ploty documentaion is excellent


 
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


##### To View Exstensive User Testing With The NASTAC StockTracker please Visit
- [datadiscoverys.com](https://datadiscoverys.com/)
- In carrying out the data analysis I also tested the functionality 

## Features
- The features in my project are simple but very powerful,
- 1: A Drop down menu with a list of 275 Companies fom the NASTAC StockMarket
- 2: A Drop down calender which go,s back to 2015
- 3: The main DashBoards Chart is a simple but powerful Line Chart Visualisation that responds to user selection & input
- 4: The Submit Button is the trigger that fires the data Request
- 5: The finished Visualisation 

## Technologies Used


- [HTML5](https://https://www.w3schools.com/)
    - The project uses **HTML5** to house the sturcture & the base semantics.s
    
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
    
- [nginx](LightHouseChromeExstention)
    - The project uses **tinypng** to compress pictures & ilustrations
    
- [puttySSL](LightHouseChromeExstention)
    - The project uses **tinypng** to compress pictures & ilustrations
    
- [DigitalOcean](LightHouseChromeExstention)
    - The project uses **tinypng** to compress pictures & ilustrations
   

## Deployment
##### clivedennisnoonan@gmail.com heroku account

#### HOW THE PROJECT WAS DEPLOYED
##### First task was to version control my application on GitHub
##### I then logged into heroku in my cli in pycharm
##### Next task was to create a heroku app using the HerokuCLI. This is turn will create a remote Git Repository that I can link to 
##### I already have my Flask venv activated, so next I had to install a new dependency by the package name gunicorn
##### for deploying the app
##### I accomplished this with the command pip install gunicorn
##### My next task was to create a .gitignore file for my application & ignore the recommended /files/folders
- venv
- *.pyc
- .DS_Store
- .env

#####  Next task was to create procfile for my application ,procfile will tell Heroku what to do once the project has been deployed.
- In my procfile entered web:- gunicorn app:server 
- Here app refers to the filename of our application (app.py) and server refers to the variable server inside that file.
- To make sure all my dependencies were added to my requirements.txt file I used the pip freeze command and then synchronized them.
### My dependencies are 
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

##### I did my add, commit and push of my project to the git repo created by Heroku.
### My project can be viewed fully deployed on Heroku[here](https://clives-plotly-dash-board.herokuapp.com/)

- This is the development & deployed version
- My Separate git branch can be found here[GitHub](https://github.com/90t/my_dash_app.git)

- In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits
##### [Plotly](https://plot.ly/)

### Content
- I Sourced My data from 
##### [Plotlyhttps://github.com/plotly/datasets](https://github.com/plotly/datasets)


### Acknowledgements

- [Plotly](https://plot.ly/)
