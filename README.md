########################################################################################################################################
                                                              WordPress
########################################################################################################################################
#### Clive Noonan , Full Stack Student In CODE INSTITUTE
## [DataDiscoverys.com](https://datadiscoverys.com/)
##### Is the Super Front End To The 3 DataDash Boards In this project, thus making it 1 
- I am currently a student at the Code Institute Studing Full Stack Diploma in Software Development. 
- This is DataDiscoverys.com which is the Mother Project To House, Display, Showcase, Connect, Document, Instructe
- The User on how to use, study, test, compare, learn, in this UI Testing Arena
- The driving force behind this project was to create a system in which any developer that is testing data dashboards can write there tests
- While it is very obvious that all tests will be carried out on the actuall dash board itself, I have found & I aslo have been told by
- more students that after
- they have build ther dashboards they find it diffucult to explain the fuctionalitys of there dashborad, which they have been working on &
- developing for hard & so long
- Because of this fact, this issue can be very fustrating for the developer of the data dashboard
- In the process of developing this Arena, my UI testing abilitys inhanced ten fold, so much so to the point of being able to test 3
- different tests on 3
- different dashboards with accurate rersults each time
- I really beleive this was because of the UX,
- It is obvious that I needed to concieve & construct my own tests before ever entering the test block into WordPress
- But this is where the magic did happen, On the first try, after comparing my data in my notes after I ran all my tests on my dashboards
- manualy
- I had alot of info, this became confusing very quickly
- This is when datadiscoverys came into play, when I transferred all my tests & layed them out in a clear easy to understand format with
- alot of promts
- The abilty to read the data became a pure Joy
- I agian proved this to myself agian by consrtucting another 2 dashboards, it was like the missing piece of the puzzle
- After testing one so rigourisly, I just needed to follow my origanl pattern
- But all dash boards have a different tests
- With a dedicated blog in production & on the way


- This is the third of five projects which I must complete in order to be awarded the globally recognised Diploma 
- from Edinburgh Napier University. This Project utilises whole miriad of technology.
- Consult the tech section in each README.md or the Super README.md to Find Out the exact tech stack taht was used to complete my project


### The Super Model Wordpress Configueration
- The Front End to this project is without doubht wordpress, with the OceanWP Wordpress Theme
- I only used the theme to gain access to the blocks, from then onward I used Elemenoter to create my own theme
- With the power of Nginx ???????????????????
- The simplcity & advantage I had was Sucnificent, due to the fact I configured the server & obatianed a domain name
- this meant that I had & have complete controll over my own server which is hosted on Ditigital Ocean 
- I attached a floating ip & configerd the back end with PHPMYAdmin
- with no SQL as the chosen query language
- This meant that I could concentrate on the 3 dashbaords & not have to worry about the frontend
- this was an excellent solution to the fact I was developing on my own & needed an assistant
- WordPress was that assistant, this gave me the abilty to create this DataDashBoard Showcase
- Without WordPress this project would not of been possilble

### WordPress WorkFlow (LempStack) Stack on a Virtual Server (Linux, NGINX, MySQL, PHP)
- Step:1
- To Deploy a Virtual Server on Digital Ocean with Ubuntu 18.04
- The very First step I took was to buy a domain name from GoDaddy.com
- This introduced me to Virtual Servers, Digital Ocean Was the company of chioce
- Documentaion & tutorials on to configure all different types of server Stacks are at an abundance & are of an amazing Qautily on Digital
- Ocean 
- The next task to consider was that of IP,s & Floating IP,s
- after observation of documenatation on how eaxctly to accomplish this
- After attaching a Floating IP to a Digital Ocean Virtual Server
- I proceeded to build my first (LempStack) Stack on a Virtual Server (Linux, NGINX, MySQL, PHP)

- Step:2
- My Next Task was to Connect to a remote Virtual Server using an SSH Client
- I accomplished this by downloading the Amazing & Unbelievably powerfull SSH Client Putty
- I connected by starting Putty Session & enetering in my Floating Ip Address That I had Obtained from Digital Ocean
- This gave me a secure SSL Connection to my Ubuntu (18.04) Virtual Server

- Step:3
- Install & Configure LEMP Stack (Linux, NGINX, MySQL, PHP)
- To Install & Configure NGINX I needed to update my linux Ubuntu 18.04 on Digital Ocean
- I accomplished this in my Putty terminal while bieng a Session with the command
- apt update

- Step:3.1
- Next I needed to Install my NGINX SERVER
- I accomplished this in my Putty terminal while bieng a Session with the command
- apt install nginx

- Step:3.2
- Next was to Install  & Configure MYSQL on my NGINX 
- I accomplished this in my Putty terminal while bieng a Session with the command
- sudo apt install mysql-server-5.7

- Step:3.3
- Next was to Secure MYSQL on my NGINX 
- I accomplished this in my Putty terminal while bieng a Session with the command
- mysql_secure_installation

- Step:3.4
- Next was to alter MYSQL password so I can have privilges for both MYSQL Database Querys & PHPMYAdmin
- I next Altered the root user & flushed privilages
- I accomplished this in my Putty terminal while bieng a Session with the command
- mysql_secure_installation

- Next was to Configure my Php TestFile

- Step:3.5
- Next was to Install  & Configure PHP on my NGINX 
- I accomplished this in my Putty terminal while bieng a Session with the command
- sudo apt install php-fpm php-mysql
- Up Next was I had to configure nano file
- I accomplished this in my Nano Text Editor which comes build in with all Ubuntu vm,s
- My next task was to test my configuration 
- I accomplished this in my Putty terminal while bieng a Session with the command
- nginx -t

- Step:3.6
- After my test was 100%, I then reloaded the server
- I accomplished this in my Putty terminal while bieng a Session with the command
- systemctl reload nginx

- Step:3.7
- Up next was to create a test file to test php configuration
- I accomplished this in my Nano Text Editor which comes build in with all Ubuntu vm,s
- After my test was 100%, I destroyed the test php configuration file
- After I configured my values to www and example.com I reloaded my server
- I accomplished this in my Putty terminal while bieng a Session with the command
- After this I also reloaded my NGINX  
- I accomplished this in my Putty terminal while bieng a Session with the command
- systemcti reload nginx


- Step:4
- Domain Names & SSL install SSL on NGINX using Let's Encrypt
- To Install Let’s Encrypt SSL For My Domain In DigitalOcean Droplet I first needed to install the package certbot
- I accomplished this in my Putty terminal while bieng a Session with the commands
- sudo add-apt-repository ppa:certbot/certbot
- sudo apt install python-certbot-nginx


- Step:4.1
- Next I needed to incrypt my server
- I accomplished this in my Putty terminal while bieng a Session with the command
- sudo certbot --nginx -d datadiscoverys.com -d www.datadiscoverys.com
- I also needed to configure my email
- I accomplished this in my Putty terminal while bieng a Session with the command
- new email clivedennis90@gmail.com
- Up next task was to test my configuration 
- I accomplished this in my Putty terminal while bieng a Session with the command
- https://www.ssllabs.com/ssltest
- sudo certbot renew --dry-run




- Step:5
- Securing PhpMyAdmin using symbolic links and NGINX’s built in authentication gateway.
- PhpMyAdmin on NGINX Install & Secure PhpMyAdmin for Database Management
- I accomplished this in my Putty terminal while bieng a Session with the command
- apt-get install phpmyadmin
- I then configured a symbolic link for extra secuirity


- Step:6
- WordPress on NGINX Install and Configure WordPress on NGINX
- With my server onfigured I could now install WordPress
- I needed to create a database
- So I logged into mysql
- With my database onfigured I could now install WordPress
- I accomplished this in my Putty terminal while bieng a Session with the command
- sudo apt install php-curl php-gd php-mbstring php-soap php-xml php-xmlrpc php-zip


##### Wordpress Bug
- I have a small wordpress issue going on at the moment, I am unable to update certain parts of my website with elementor
- & it is proving to be quite diffucult to debug since I have no log files
- I am nearly positve the problem is in my wordpress memory
- I am currently working on this issue & will most defintly have resolved the bug before the release of his website
- Which will be after I recive my results & the bug is resolved




### Content
- I created All The Content 
##### 

### Acknowledgements
- I received inspiration for this project from studying the Awesome
- Python Programming Language | JavaScript Programming Language
- Data Visualization | DataBase Development & Managment
- ServerSide Development | BackEndDevelopment | FrontEndDevelopment
- for the whole year , it was & is amazing
##### 10/09/2018 This is Clive Noonan , Code Initstute , Project Number 3.1 Data Visualization[DataDiscoverys.com ](https://datadiscoverys.com/) , Signing Off......


########################################################################################################################################
                                                              Plotly-StockTracker 
########################################################################################################################################

#### Clive Noonan , Full Stack Student In CODE INSTITUTE
## NASTAC Plotly StockTracker DashBoard is a
##### Child To [DataDiscoverys.com ](https://datadiscoverys.com/)
- I am currently a student at the Code Institute Studing Full Stack Diploma in Software Development. 
- This is part of the Four frontends which make the whole project of DataDiscoverys.com which is the last project
- that I will be Submitting

- This is the third of five projects which I must complete in order to be awarded the globally recognised Diploma 
- from Edinburgh Napier University. This Project utilises whole miriad of technology.
- Consult the tech section in each README.md or the Super README.md to Find Out the exact tech stack that was used to complete my project


# NASTAC Plotly Stock DashBoard

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
- The UX on this dash board is very simple, purposly so , it does not needlsy take away from fuctioning aspect of the click effects ,

- the click effects & hover points are also very mild, but work as intended , the dashboard is very intutive just by observation ,

- it is very clear to see the date picker , the user can find & see the Enter a stock symbol: dropdown click box,

- these colors are also very mild so to let the user just find & choose the given company in which to run the data against,

- Similer also go,s for our Select start and end dates: these elemnets on our dashboard are clearly defined with
- a bold but light strong blue, it serves it purpose well,

- Our Submit button is ajason to our main elements , leading to the right, but with suffieceint space &
- clarity to be easly seen & interperrted,

- Our Ploty Interactive Tabs are ajason to our submit button , leading to the right, this tool bar is very powerfull &
- is for the more advanced users

- The DashBoard its self sits on a barly viisble cross checked grey grid , but protomlitly it is white ,
- which creates almost like a interactive white sheet of paper, this is very effective when it comes to reading the data &
- visually interpertting the outcome of comparison of stock change, agian very easy to use.

- Our Tool Tips are very effetive in there seemless intergration to our calender on the x axis , protraying the rise & fall
- on the stock price,

- Our line Chart is the main focus , with the chosen company & the chosen date, we see the data clearly defined in light but very
- contrasting colors
- so as to not obscure from it rivals on the main interface , our line chart is very successfull in its operations 
- I wanted to find a libereirey that I could build a dashboard with minimil code 
 - still have the same effect, but most importantly I wanted the dashboard to clearly define the data & for the dashboard operate
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

## Features
- The features in my project are simple but very powerful
- 1: A Drop down menu with a list of Companies fom the NASTAC StockMarket
- 2: A Drop down calender which has a timeline from 2015 to 2018
- 3: The main DashBoards Chart is a simple but powerful Line Chart Visualisation that responds to user selection & input
- 4: The Submit Button is the trigger that fires the data Request
- 5: The finished Visualisation 


## User Testing & Analitics

##### I tested each graph visually to make sure
- everything loaded properly
- when I selected an element on each graph the corresponding graphs responded and showed accurate statistics.

##### In the developer tools I tested that the website was responsive in tablet and mobile mode and again when the project was deployed I ##### tested on my mobile, tablet and laptop that my DashBoard was responsive.
##### All dashboards are responsive to different screen sizes, example would be sony mobile & XL Microsoft 10 to a Tablet to a Smart tv
- But froom the Tablet & upwards is where these dashboards are most fuctional & stunning in there more natrual enviorenmnet

##### To Enjoy an easier & more easy on the eye way to
##### View Exstensive User Testing With The NASTAC StockTracker please Visit
- [datadiscoverys.com](https://datadiscoverys.com/)
- In carrying out the data analysis I also tested the functionality



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
#### HOW I MY DEPLOYED MY PROJECT
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
- My git branch can be found here[GitHub](https://github.com/90t/my_dash_app.git)

- In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits
##### [Plotly](https://plot.ly/)

### Content
- I Sourced All My data from 
##### [Plotlyhttps://github.com/plotly/datasets](https://github.com/plotly/datasets)


## Acknowledgements
##### I didn't base my work off other code, I used only what I had learnt in
##### syllabuss1/LMS1 & syllabuss2/LMS2(cloud-9) & [Plotly](https://plot.ly/)

### Acknowledgements
- I received inspiration for this project from studying the Awesome Python Programming Language & Data Visualization for the whole year , it was & is amazing
##### 10/09/2018 This is Clive Noonan , Code Initstute , Project Number 3.1 Data Visualization[DataDiscoverys.com ](https://datadiscoverys.com/) , Signing Off......


########################################################################################################################################
                                                              SAVY 
########################################################################################################################################
#### Clive Noonan , Full Stack Student In CODE INSTITUTE
#### SAVY Part Of DataDiscoverys.com
##### Child To [DataDiscoverys.com ](https://datadiscoverys.com/)
- I am currently a student at the Code Institute Studing Full Stack Diploma in Software Development. 
- This is part of the Four frontends which make the whole project of DataDiscoverys.com which is the last project
- that I will be Submitting

- This is the third of five projects which I must complete in order to be awarded the globally recognised Diploma 
- from Edinburgh Napier University. This Project utilises whole miriad of technology.
- Consult the tech section in each README.md or the Super README.md to Find Out the exact tech stack that was used to complete my project

### The inspiration for this project came from studying Data Visulisations in syllabuss1/LMS1 & syllabuss2/LMS2(cloud-9),
- With Code Intitstute
- My idea is create a multi connected dashboard showcase for data visulisation ui & ux testing 
- My project has 4 frontends
- It is in all deployed on 3 different servers
- This is the project in which I wanted to bring all my skills together
- Conception, Design, Development, Deployment, Delivery
- With 2 different DataVisulisation libarays
- 3 different styles of creating stunning easy to interpret dashboards
- With WordPress acting as the portal to all of my dashbaords
- With a selfbuild server & a floating IP from Digitil Ocean
- & a double secured backend PHPMySql Ready to go database
- A build in blog, waiting for content

## THE NEEDS THIS PROJECT FULFILLS
##### The needs for this project are numerous,
- Students who want to create a block in adobe xd or just a pencil & white sheet of paper,
- Students can send me there mock up & there UI testing flow
- I can then transfer there mockup into there own testing UI block on datadiacoverys.com
- Students can add there name, description of there dashboard, a short sales pitch to promote there UI Testing
- With the power & ease of elementor on wordpress, any mockup submitted for UI testing can be adapted to there needs
- Students learning data visulisation,
- developers who will want to bring these data visulisations to life with real time data sets from API Sources
- To designers looking to get ideas for there own data visulisations
- this project can also be used as an going basis to showcase data visulisations with the ease of wordpress
- Online colleges can post there students data visulisations here by just contacting the developer for showcasing
- I myself can use this dashboard for my own business to measure fluctuations in website delivery

 
## UX for the whole project
 
- The UX tru out this project is with one style & that is to represent the data in the showcased screenshots
- With a white background & a suttle awesome grey, it is a difficult style to achieve because of it pure simplicity
- The user or reader is slowly traversed down the page to soak up the information & gaze at the visulisations
- The navbar & its elements, my links are situated top center , this is indented to both powerfull & reasurring
- But not overwhelming, with my links indented apon hover or click, this gives a translution type of effect
- These elements are as minimil as possible, to sit nicely with the rest of the flow of the page


## FUNCTIONALITY

##### My Savy DataDashBoard is based on a company that sells wholesale goods
##### My Company has commissoned the development of this dash board to monitor peaks in call duration over the course of a year
##### Also to monitor the number of units sold & there trends troughout the year 
#### Aswell as to monitor revenue per call & there trends troughout the year 
#### Also to tally up the summmary average of the years data

##### On the navigation bar there is a start tour button which invites users to a quick tour of the page.

##### My dashBoard consists of:

##### My whole DashBoard is based on the yearly data of which my company has provided
##### This Data Set is based on Four Sales Teams -Northeast -West -South -Midwest
##### From the beginning of 2017 to the end of 2017


##### My dashboard will measure the trends in CallDurations Times that employees spend on the phone
##### This is measured in seconds for higher accuracy

##### The big graph is a zoom of the smaller graph so the user can analyze the data more accuratly
##### The charts on the right are showing summery data for the data the user has selected

##### everytime the user observes the dates changing, it is a result of the user, by using the mouse as the cursor to brush in the input in the Context Graph
##### So inturn The corressponding dates will change with the selection


##### When choosing a different selection from the dropdown menu
##### The visualisation will also fluktuate with the corresponding dropdown menu selection
##### So inturn The corresponding selection will change with the users selection

##### Elements Features
##### 1 Calender
- The Calender Dates transitions are corressponding with the change in the context graph, with the users selection
- There is only 1 year on the Calender

##### 1 Drop Down Selection
- The dropdwon selection gives the user the option to select between
- Revenue (euro)
- Call Time , which is been measured in seconds
- Units Sold

##### 1 Donot Chart
- The One Donuot Chart updates & displays transitions between compnay size, which is based on three catorgories of 
- Large
- Meduim
- Small 

##### 1 Stacked Area Chart 
- Stacked Area Chart is the main section of my dashboard, with its child , the context graph
- With the ability to zoom in with the use of the context graph which is situated directly below Stacked Area Chart

##### 3 Bar Charts with corresponding line graphs 
##### BarChartNo:1 Units sold per call
- The first Bar Chart is displaying Units sold per call, which is based on the years data
- Interaction with the context graph updates this display as the user clicks & brushs the cross hairs over the context graph
- The Units sold per call Bar Chart up dates accordingly


##### 2 Bar Charts with corresponding line graphs
##### BarChartNo:2  Average call revenue (euro)
- The second Bar Chart is displaying Average call revenue (euro), which is based on the years data
- Interaction with the context graph updates this display as the user clicks & brushs the cross hairs over the context graph
- The Average call revenue (euro) Bar Chart up dates accordingly

##### 3 Bar Charts with corresponding line graphs
##### BarChartNo:3  Average call duration (seconds)
- The second Bar Chart is displaying Average call duration (seconds), which is based on the years data
- Interaction with the context graph updates this display as the user clicks & brushs the cross hairs over the context graph
- The Average call duration (seconds) Bar Chart up dates accordingly


#### So it is a 6 step process,if you are planning to analise the data
#### I have completed my own data analiaizs, if you are interrested in using the same calender for ease to comapare whit the numbers
#### feel free to visit


-  [https://datadiscoverys.com/Tuts](https://datadiscoverys.com)
    - To View A tutorial On the operations & fuctionality click the link above or below
-  [https://datadiscoverys.com/Tuts](https://datadiscoverys.com)

##### No1, choose a Catogoire by clicking the dropdown menu & making a choice
##### No2, choose a team to monitor & analize , lets say Northeast
##### No3, direct your mouse over the context graph, you will see a crosshairs appear
##### No4, drag & hold your mouse(crosshairs) from exactly july to october
##### No5, the best way to achieve this is to slowly move you crosshairs while looking at your dates
##### N06, when you have your dates set, then you will be able to analize each team & there corresponding fluxtutations over the course of a year

##### Since you are using the Context graph , the visiluasation in the main graph is a zoomed version of your graph,

##### Savys barcharts fluxctuat with the manipulation of the context graph , this is summary data of all the teams stats over the course of the year

##### Testing the data against 3 different time lines with all 4 teams was a great way of testing all the fuctionalitys of the my project



-  [https://datadiscoverys.com/Tuts](https://datadiscoverys.com)
    - To View A tutorial On the operations & fuctionality click the link above or below
-  [https://datadiscoverys.com/Tuts](https://datadiscoverys.com)



## Technologies Used in The whole Project  DataDiscoverys | Savy | StockTracker | WorldsCo2Emmisions

#### Add more tech from aal project

- [D3](https://d3js.org)
    - The project uses D3 Version 5.0.0. for data visualisation

- [Flask](https://docs.djangoproject.com/)
    - The project uses Django 2 for rapid web development, clean design & a pragmatic approach

- [Heroku](https://https://www.heroku.com/)
    - The project uses **Heroku** as an app deployment hosting platform for my application

- [FireStore](https://firebase.google.com/docs/firestore/)
    - The project uses **FireStore** as an app deployment hosting platform for my application

- [Nginx](https://www.nginx.com/)
    - The project uses **Nginx** as a Virtul Server on Digitil Ocean

- [WordPress](www.wordpress.com/‎)
    - The project uses **WordPress** as an app deployment hosting platform for my application

- [PHPMYAdmin](https://www.phpmyadmin.net/)
    - The project uses **https://www.phpmyadmin.net/** to supply a backend database for wordpress & for configuration of
    - Virtual Server

- [MySql](https://www.mysql.com/)
    - The project uses **https://www.mysql.com/** to query my PHPMYAdmin Database when the need arises
    - & for configuration of Virtual Server

- [Putty](https://www.putty.org/)
    - The project uses **https://www.mysql.com/** to act as my SSH and telnet client

- [Elementor](https://elementor.com/‎)
    - The project uses **Elementor** as an app deployment hosting platform for my application 

- [Git&GitHub](https://github.com/)
    - The project uses **https://github.com/** to version control the development project 

- [JsIntro.js](https://github.com/)
    - The project uses **https://github.com/** to version control the development project 

- [CSS3](https://https://www.w3schools.com/)
    - The project uses **CSS3** to to Style the elements & Responsive WebDesign.

- [CSS3intro.css](https://https://www.w3schools.com/)
    - The project uses **CSS3** to to Style the elements & Responsive WebDesign.

- [HTML5](https://https://www.w3schools.com/)
    - The project uses **HTML5** to to Style the elements & Responsive WebDesign.
        
- [LightHouseChromeExstention](https://chrome.google.com/webstore/detail/lighthouse)
    - The project uses **LightHouseChromeExstention** to test seo data & accsseibitly & best practices
    
- [validator.w3](https://validator.w3.org/)
    - The project uses **validator.w3** to test seo data & accsseibitly & best practices
    
- [aws](https://jigsaw.w3g/)
    - The project uses **aws**for screen shots for project

- [MARKDOWN](https://https://www.w3schools.com/)
    - The project uses **MARKDOWN** to Document Projects
    
- [BootStrap3](https://https://getbootstrap.com/)
    - The project uses **BootStrap3** to assist the Developer with a build in css libaray ,aswell reusable components
    
- [VisualStudioCode](https://code.visualstudio.com/)
    - The project uses **webstorm** to Write/Code & format the syntax in various languages.
    
- [Adobe Ai](https://www.adobe.com/ie/products/illustrator.html)
    - The project uses **Adobe Ai** to create & Logos & MockUps
    
- [GoogleFonts](https://fonts.google.com/)
    - The project uses **GoogleFonts** to enhance the use visual text & ensure readabilty on various platforms & screens

- [validator.w3](https://validator.w3.org/)
    - The project uses **validator.w3** to test seo data & accsseibitly & best practices
    
- [jigsaw.w3](https://jigsaw.w3g/)
    - The project uses **jigsaw.w3** to test validation of CSS3 
    
- [Nano](https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor//)
    - The project uses **https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/** to Configur server files
    - On Virtual Servers



## Testing

##### I tested each graph visually to make sure
- everything loaded properly
- when I selected an element on each graph the corresponding graphs responded and showed accurate statistics.

##### In the developer tools I tested that the website was responsive in tablet and mobile mode and again when the project was deployed I ##### tested on my mobile, tablet and laptop that my DashBoard was responsive.
##### All dashboards are responsive to different screen sizes, example would be sony mobile & XL Microsoft 10 to a Tablet to a Smart tv
- But froom the Tablet & upwards is where these dashboards are most fuctional & stunning in there more natrual enviorenmnet 


##### Team Analitic Testing 

## The Base Test

### Dates: 02/07/2017 ---> 01/08/2017
### Team:North-East
- User1: David:Area-Manager
- Color: Pink
- Year:2017
- Overall Average Based On The Chosen Date of 02/07/2017 ---> 01/08/2017
- Revenue:240,000 (euros)
- CallsTime:20,000 (Seconds)
- Units-Sold:24,000 ----> 26:00 (units-sold)


### Dates: 02/07/2017 ---> 01/08/2017
### Team:South
- User1: Jane:Area-Manager
- Color: Green
- Year:2017
- Overall Average Based On The Chosen Date of 02/07/2017 ---> 01/08/2017
- Revenue:120,000 (euros)
- CallsTime:10,000  ---->  12,000 (Seconds)
- Units-Sold:18,000 (units-sold)


### Dates: 02/07/2017 ---> 01/08/2017
### Team:Mid-West
- User1: Paul:Area-Manager
- Color: Lilac
- Year:2017
- Overall Average Based On The Chosen Date of 02/07/2017 ---> 01/08/2017
- Revenue:240,000 (euros)
- CallsTime:20,000 ----> 22:000 (Seconds)
- Units-Sold:28,000 (units-sold)


### Dates:02/07/2017 ---> 01/08/2017
### Team:West
- User1: Sarah:Area-Manager
- Color: BabyBlue
- Year:2017
- Overall Average Based On The Chosen Date of 02/07/2017 ---> 01/08/2017
- Revenue:80,000 ----> 120,000 (euros)
- CallsTime:8,000 ----> 12,000 (Seconds)
- Units-Sold:24.000 ----> 26,00 (units-sold)

-  [TheBaseTest](https://datadiscoverys.com)
    - To View these test results on DataDiscoverys click 
-  [TheBaseTest](https://datadiscoverys.com)


##### Dates:02/07/2017 ---> 01/08/2017


#### Observe The big change in my Date Selection


##### Dates: 05/02/2017 ---> 04/12/2017



## The Trial
# Dates: 05/02/2017 ---> 04/12/2017
##### Dates: 05/02/2017 ---> 04/12/2017
### Team:North-East
- User1: David:Area-Manager
- Color: Pink
- Year:2017
- Overall Average Based On The Chosen Date of 02/07/2017 ---> 01/08/2017
- Revenue:240,000 (euros)
- CallsTime:22,000(Seconds)
- Units-Sold:10,000 ----> 40,000 (units-sold)

### Dates: 05/02/2017 ---> 04/12/2017
### Team:South
- User1: Jane:Area-Manager
- Color: Green
- Year:2017
- Overall Average Based On The Chosen Date of 02/07/2017 ---> 01/08/2017
- Revenue:120,000 (euros)
- CallsTime:4,000  ---->  14,000 (Seconds)
- Units-Sold:5,000 ----> 18,000 (units-sold)

### Dates: 05/02/2017 ---> 04/12/2017
### Team:Mid-West
- User1: Paul:Area-Manager
- Color: Lilac
- Year:2017
- Overall Average Based On The Chosen Date of 02/07/2017 ---> 01/08/2017
- Revenue:240,000 (euros)
- CallsTime:16,000 ----> 22:000 (Seconds)
- Units-Sold:19,000 ----> 40,000 (units-sold)

### Dates: 05/02/2017 ---> 04/12/2017
### Team:West
- User1: Sarah:Area-Manager
- Color: BabyBlue
- Year:2017
- Overall Average Based On The Chosen Date of 02/07/2017 ---> 01/08/2017
- Revenue:75,000 ----> 120,000 (euros)
- CallsTime:4,000 ----> 10,000 (Seconds)
- Units-Sold:5,000 ----> 15,000 (units-sold)

-  [TheBaseTest](https://datadiscoverys.com)
    - To View these test results on DataDiscoverys click 
-  [TheBaseTest](https://datadiscoverys.com)



##### Dates: 05/02/2017 ---> 04/12/2017


#### Observe The big change in my Date Selection


#### Dates: 20/11/2017 ----> 19/12/2017




## The Controller Test

# Dates: 20/11/2017 - 19/12/2017
###### Dates: 20/11/2017 - 19/12/2017
### Team:North-East
- User1: David:Area-Manager
- Color: Pink
- Year:2017
- Overall Average Based On The Chosen Date of 02/07/2017 ---> 01/08/2017
- Revenue:190,000  ----> 210,000(euros)
- CallsTime:18,00 ---> 22,000(Seconds)
- Units-Sold:16,000 ---> 29,000(units-sold)

### Dates: 05/02/2017 ---> 04/12/2017
### Team:South
- User1: Jane:Area-Manager
- Color: Green
- Year:2017
- Overall Average Based On The Chosen Date of 02/07/2017 ---> 01/08/2017
- Revenue:50,000 ---> 110,000(euros)
- CallsTime:6,000  ---->  10,000(Seconds)
- Units-Sold:6,000 ---> 16,000(units-sold)

### Dates: 05/02/2017 ---> 04/12/2017
### Team:Mid-West
- User1: Paul:Area-Manager
- Color: Lilac
- Year:2017
- Overall Average Based On The Chosen Date of 02/07/2017 ---> 01/08/2017
- Revenue:220,000 ---> 220,000(euros)
- CallsTime:19,000 ----> 23,000(Seconds)
- Units-Sold:22,000 ---->  29,000(units-sold)

### Dates: 05/02/2017 ---> 04/12/2017
### Team:West
- User1: Sarah:Area-Manager
- Color: BabyBlue
- Year:2017
- Overall Average Based On The Chosen Date of 02/07/2017 ---> 01/08/2017
- Revenue:50,000 ----> 70,000(euros)
- CallsTime:6,000 ----> 6,000(Seconds)
- Units-Sold:6,000 ----> 10,000(units-sold)

-  [https://datadiscoverys.com](https://datadiscoverys.com)
    - To View these test results on DataDiscoverys click 
-  [https://datadiscoverys.com](https://datadiscoverys.com)


### Summary Analitic Testing

##### Dates: 06/06/2017 - 21/07/2017 color:Pink
- The summary Data for Team North East indicates a rise in Revenue
- Between the Dates of 06/06/2017 & 21/07/2017, 
- But a slow down turn Between the dates of 21/04/2017 to 06/06/2017
- Growth was back to normal Between The Dates: 21/04/2017 - 28/07/2017


##### Dates: 21/04/2017 - 06/06/2017 color:Green
- The summary Data for Team South indicates a steep drop in Revenue in Between The Dates of 27/02/2017 & 27/05/2017.
- But a Rise in Revenue Between In The Region of 27/02/2018
- Growth was back to normal Between The Dates Of 05/04/2017 & 08/06/2017



##### Dates: 08/06/2017 - 23/07/2017 color:BabyBlue
- The summary Data for West indicates a Rise in Revenue Between The Dates: 08/06/2017 - 29/07/2017. 
- But a slow down turn Between the Dates: 17/01/2017 - 01/04/2017
- Growth Peaked Between The Dates: 01/04/2017 - 23/06/2017



##### Dates: 08/06/2017 - 23/07/2017 color:Lilac
- The summary Data for West East indicates a steady stream of rileiable Revenue in Between The Dates: 10/01/2017 - 19/12/2017
- A sligth Drop in Revenue Between Dates: 20/05/2017 - 06/08/2017 
- Growth peaked agian back to normal Between The Dates: 06/06/2017 - 16/08/2017

-  [https://datadiscoverys.com](https://datadiscoverys.com)
    - To View these test results on DataDiscoverys click 
-  [https://datadiscoverys.com](https://datadiscoverys.com)




## How I Deployment My project
- Deployment
- On deploying this project , I had origanlly completed Stream2,s DataDashBoard schoolDonations
- Stream2,s DataDashBoard schoolDonations uses MongoDB , when starting down the route of D3 agian to complete my project
- on the installation attempt of MongoDB, on Stream2, I was successfull,
- After Completing that project I had an OS Crash,
- After this apon attempting to install MongoDB Once again I had to pick a 32bit installation, this is because my pc is a 32bit
- After Installation of the 32bit windows installer of MongoDB, I no longer had the abilty to run a mongodb server from my terminal/cli
- I once again uninstalled MongoDB
- This when I decided to go with Google Firebase


- This led me to  Firebase,  Firebase is a service in which we can deploy static websites on a free tier with excellent documentation and
- configeration options
- it a excellent choice & can also be upgraded with relevent ease, all of this operation is carried out in our google firebase
- Cloud-console & Installed
- FireBaseCli,

- To Deploy this project you need to have the latest version of Node.js installed on your local machine/pc

- After installing Node.js & Checking you have a version number, you will have to navigate to your project folder & run firebase init
- this will initilise your
- project directory with a firebase.json file , this file holds the configeration for your deployment

- After initilisation you have to create can account with google firebase, (If you have a gmail, you have a firebase)
- once logged in to google you will have the abilty to access the firebaseCli & its commands

- Once you are satifactory with your project that you will be deploying, you will have to go your google firebase console, go to the
- Hosting tab & create a
- project google will give you a default folder of PUBLISH,

- So now we have 3 projects/folders , one on Firebase & one on Your Local Machine & one on GitHub(Providing you versioned controlled your
-  project), now we will 
- have to make sure we are in the matching named folder on our pc , just like GitHub,

- After we have confirmed we are in our project diretory with our firebase.json

- Then it is just a matter of running the command

- firebase deploy

- Now we have a live DashBoard

- To update my DashBoard it is just a matter of running
- firebase deploy

### Live DashBoard
 ## My project can be viewed fully deployed on Firebase [here](https://d3vsplotly.firebaseapp.com/)

## VERSION CONTROL

- The deployment project folder lives at this address
  [github](https://github.com/90t/d3vsplotly)
  
 
## Credits
[d3js](https://d3js.org/) 


### Content
- The data set for this project was sourced from
- [kaggle](https://www.kaggle.com/datasets)
    - The project uses **kaggle** to supply free datasets for testing

### Media
- I created my Logo In illustrator

### Acknowledgements
##### I didn't base my work off other code, I used only what I had learnt from studying Data Visulisations in syllabuss1/LMS1 & syllabuss2/LMS2(cloud-9),
[d3js](https://d3js.org/) Docs



## THE FUTURE
##### I indend on using this dashboard for my own business since the fact it is fuctioning so well,
##### With many more upgrades to come including a full sidenav for better UX
##### Authentication system for employes
##### Added features such as intergration with google analitics
#### Migration to an nginx server

### Acknowledgements ###ADD MORE####
- I received inspiration for this project from studying the Awesome
- Python Programming Language | JavaScript Programming Language
- Data Visualization | DataBase Development & Managment | Data User Testing
- ServerSide Development | BackEndDevelopment | FrontEndDevelopment
- for the whole year , it was & is amazing
##### 10/09/2018 This is Clive Noonan , Code Initstute , Project Number 3.2 SAVY Data Visualization[DataDiscoverys.com ](https://datadiscoverys.com/) , Signing Off......


########################################################################################################################################
                                                              Co2 emissions 
########################################################################################################################################

# CO2 Emissions Based On UN Data

#####Co2-emissions is a Child To [DataDiscoverys.com](https://datadiscoverys.com/)
- I am currently a student at the Code Institute Studing Full Stack Diploma in Software Development. 
- This is part of the Four frontends which make the whole project of DataDiscoverys.com which is the last project
- that I will be Submitting

- This is the third of five projects which I must complete in order to be awarded the globally recognised Diploma 
- from Edinburgh Napier University. This Project utilises whole miriad of technology.
- Consult the tech section in each README.md or the Super README.md to Find Out the exact tech stack that was used to complete my project


## My inspiration
- for this project was the discovrys mutiversr project itself , after completing my plotly dashboard I had a much deeper
- appreciation & understanding of data visualiasation
- plus it much easier the fifth time around since I had build dashboards successfully with Code Initistute on Sylabus1 & Sylabuss3(cloud9)
- The introduction of Co2Emmisions into datadiscovrys was a game changer for the whole project as a whole
- with the introduction of a completly new concept & such a broad data-set it was sure to fit in very well with the whole project

## UX
 

## FUNCTIONALITY
##### My Co2emmisions Data Dash-Board is based on
- Data for carbon dioxide emissions include gases from the burning of fossil fuels and
- cement manufacture, but excludes emissions from land use such as deforestation
- For a more indepth study into actuall Meaning of Co2emmisions per capita
- Here is a awesome link
-[Co2emmisionspercapita](https://www.indexmundi.com/facts/indicators/EN.ATM.CO2E.PC)
- My Co2emmisions Data Dash-Board also analisis & visualises data on emmissions 

##### On the right center of the page there is a Show Me How button which invites users to a quick tour of the page.

##### My dashBoard consists of:

##### 1 
- Range Slider

##### 2 
- Radio Check Buttons

##### 1 
- Pie Chart

##### 1 
- BarChart

##### 1 
- LineGraph

##### 1 
- Radial Map Chart 

##### My Co2emmisions DataDashBoard features comprise of
##### 1 
- Range Slider
- The Range Slider is the key to analisis
- Statisticil over view of the worlds emmissions data over the course of a 20 year period from 1990 to 2010
- This is where the fuctionality of our range slider comes into play
- by manipulating the range slider to our chosen dates we can test the differencs & compariosns in the data
- again similer to Savys layout of operations The Range Slider is the key to analisis since this is the starting point of all 3 dash-boards

##### 2 
- Radio Check Buttons
- The range buttons gives us the abitly to choose between emmissions & emmissions per captia
- By chooseing a selection between emmissions & emmissions per captia we can analize 2 different catergories
- Which will yield far greater results

##### 3
- Pie Chart
- The pie chart visualises Total emissions by continent and region & dispalys in a poup-box(tool-tip) in a percentage the values
- Here the range slider comes into play before the PieChart
- In order to observe the effects of the PieChart you need to again first of chosen a year
- next observe as the piechart changes it values in percentage in color , you then need to just slide your mouse to view the corresponding
- data which will be displayed in a poup-box(tool-tip) 


##### 4 
- LineGraph
- The Line Graph 
- the Y axis of our LineGraph displays CO2 emissions, metric tons per capita
- By choosing to select the Emissions Per Capita Check Radio Button the Y axis of our LineGraph displays CO2 emissions, metric tons per
- capita as a guide to assist the analist in caging the difference between the years which will be highligthed in our corrsponding barchart
- the X axis of our LineGraph is the time line that will assist in measureing the diffrences in yearly output of data
- in a sinqencule 2 year rise over a twenty year period

##### 5
- Radial Map
- from green(low) to black(high)
- The main function of the map is visualaise the differncews in country by using the use of color  
- The Radial map is of course the main point of focus of the whole dashboard
- This beacuse it controlls our barchart which in turn sits on our line chart
- by clicking a country after choosing a date , we can then see the true power of this dashboard
- as the barchart fluxtuates into postion, the analist has an amAzing view of 4 different data indicators which are

- 1:Total emissions by continent and region(PIECHART) displayed with a Title & a informative tooltip

- 2:CO2 Emissions, Canada Country Title(BARCHART) displayed with a time line & a informative tooltip

- 3:Carbon dioxide emissions (MAPCHART) displayed with a time line & a informative tooltip

- 4:Total emissions by continent and region(LINEGRAPH)
- the Y axis of our LineGraph displays CO2 emissions, metric tons per capita
- By choosing to select the Emissions Per Capita Check Radio Button the Y axis of our LineGraph displays CO2 emissions, metric tons per
- capita as a guide to assist the analist in caging the difference between the years which will be highligthed in our corrsponding barchart
- the X axis of our LineGraph is the time line that will assist in measureing the diffrences in yearly output of data
- in a sinqencule 2 year rise over a twenty year period

#### So it is a 6 step process,if you are planning to analise the data

##### No1, Pick a date withn the range slider, lets the year 2000
##### No2, choose A catogorie, let say emissions Per Capita
##### No3, choose A country, Lets say China 
##### No4, observe the BarChart Slide along the LineGraph
##### No5, observe your PieChart
##### N06, Analize your data


##### Testing the data against 3 different Countrys was an excellent way to test the functionality


#### I have completed my own data analiaizs, if you are interested in using the same Timeline for ease to comapare whit the numbers
#### feel free to visit
-  [https://datadiscoverys.com/Tuts](https://datadiscoverys.com)
    - To View A tutorial On the operations & fuctionality click the link above or below
-  [https://datadiscoverys.com/Tuts](https://datadiscoverys.com)

##### I tested each graph visually to make sure
- everything loaded properly
- when I selected an element on each graph the corresponding graphs responded and showed accurate statistics.

##### In the developer tools I tested that the website was responsive in tablet and mobile mode and again when the project was deployed I ##### tested on my mobile, tablet and laptop that my DashBoard was responsive.
##### All my dashboards are responsive to different screen sizes, example would be sony mobile & XL Microsoft 10 to a Tablet to a Smart tv
- But from the Tablet & upwards is where these dashboards are most fuctional & stunning in there more natrual enviorenmnet



-  [https://datadiscoverys.com/Tuts](https://datadiscoverys.com)
    - To View A tutorial On the operations & fuctionality click the link above or below
-  [https://datadiscoverys.com/Tuts](https://datadiscoverys.com)



## How I Deployment My project
- Deployment
- On deploying this project , I had origanlly completed Stream2,s DataDashBoard schoolDonations
- Stream2,s DataDashBoard schoolDonations uses MongoDB , when starting down the route of D3 agian to complete my project
- on the installation attempt of MongoDB, on Stream2, I was successfull,
- After Completing that project I had an OS Crash,
- After this apon attempting to install MongoDB Once again I had to pick a 32bit installation, this is because my pc is a 32bit
- After Installation of the 32bit windows installer of MongoDB, I no longer had the abilty to run a mongodb server from my terminal/cli
- I once again uninstalled MongoDB
- This when I decided to go with Google Firebase


- This led me to  Firebase,  Firebase is a service in which we can deploy static websites on a free tier with excellent documentation and
- configeration options
- it a excellent choice & can also be upgraded with relevent ease, all of this operation is carried out in our google firebase
- Cloud-console & Installed
- FireBaseCli,

- To Deploy this project you need to have the latest version of Node.js installed on your local machine/pc

- After installing Node.js & Checking you have a version number, you will have to navigate to your project folder & run firebase init
- this will initilise your
- project directory with a firebase.json file , this file holds the configeration for your deployment

- After initilisation you have to create can account with google firebase, (If you have a gmail, you have a firebase)
- once logged in to google you will have the abilty to access the firebaseCli & its commands

- Once you are satifactory with your project that you will be deploying, you will have to go your google firebase console, go to the
- Hosting tab & create a project google will give you a default folder of PUBLISH
- 

- So now we have 3 projects/folders , one on Firebase & one on Your Local Machine & one on GitHub(Providing you versioned controlled your
- project)
- now we will have to make sure we are in the matching named folder on our pc , just like GitHub,

- After we have confirmed we are in our project directory with our firebase.json

- Then it is just a matter of running the command

- firebase deploy

- Now we have a live DashBoard

- To update my DashBoard it is just a matter of running
- firebase deploy

### Live DashBoard

### My project can be viewed fully deployed on Firebase [here](https://emissions-58f03.firebaseapp.com/)

## VERSION CONTROL
- The deployment project folder lives at this address
  [github](https://github.com/90t/emissions)
  

### Content
- The data set for this project was sourced from
- [UNDATA](http://data.un.org/)
- The project uses **http://data.un.org/** to supply free datasets for testing





## THE FUTURE
##### the future for this project is very promising, I indend on remodeling in a kind of reverse fasion
- To analizse the migration patterns of the BigBlue Whales
- So the whole dashboard would be reversed so the oceans would be more of the focus point
- A cimetrical approahch to this challenge is going to be my way forward
- Migration to an nginx server


### Live DashBoard
## My project can be viewed fully deployed on Firebase [here](https://emissions-58f03.firebaseapp.com/)

 ### Recommended Visualisations & Interesting Visualisations Subjects
 - [data.worldbank.org](https://data.worldbank.org/) 
 - [data.world](https://data.world/) 
 - [awesomedata](https://github.com/awesomedata/awesome-public-datasets) 
 - [www.data.gov](https://www.data.gov/) 
 - [youtube](https://www.youtube.com/watch?v=jxMzdUoE7eY)

### Acknowledgements
##### I didn't base my work off other code, I used only what I had learnt from studying Data Visulisations in syllabuss1/LMS1 & syllabuss2/LMS2(cloud-9),
- Python Programming Language | JavaScript Programming Language
- Data Visualization | DataBase Development & Managment | Data User Testing
- ServerSide Development | BackEndDevelopment | FrontEndDevelopment
- [d3js](https://d3js.org/) Docs
- for the whole year , it was & is amazing
##### 10/09/2018 This is Clive Noonan , Code Initstute , Project Number (3.0 3.1 3.2 3.3 = No3)   Co2-emissions Data Visualization[DataDiscoverys.com](https://datadiscoverys.com/) , Signing Off......








