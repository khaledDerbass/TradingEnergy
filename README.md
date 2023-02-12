## About The Project

### I've built a simple web application using Python3 in VSC IDE called Industry Trading. Energy traders is the target audience to help them get the best outcomes on the markets by generate insights and data-driven trading decisions. 

## Installation

To use Industry Trading and run the project:
#### Case 1.  Existing virtualenv
#### If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
#### 

And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=[https://github.com/](https://github.com/khaledDerbass/TradingEnergy.git) \
      --extension=py,md \
      
#### Case 2.  Existing virtualenv

#### If you don't have django installed for python3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=h[ttps://github.com/](https://github.com/khaledDerbass/TradingEnergy.git) \
      --extension=py,md \
      
      
#### After that just install the local dependencies, run migrations, and start the server.

# Getting Started

#### First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    
#### Activate the virtualenv for your project. Then simply apply the migrations:

    $ python manage.py makemigrations
    
    $ python manage.py migrate
    
#### Now run the development server:

    $ python manage.py runserver
    
#### Also, you can open Swagger Viewer after install the extension of Swagger in VSC, so preview to start :
#### Open the swagger file and press F1.
#### Run the Command Preview Swagger. OR press alt + shift + P 
#### for more configurations see: https://marketplace.visualstudio.com/items?itemName=Arjun.swagger-viewer

### In addition to present the status of each trading strategy in case of profit or loss by using method PNL_Strategy and other API declaration located in trading/tradingEnergyApi/views.py
### The web compute and submit orders like buy or sell energy clearly, each trade strategy are splitted in a url pathaccording to starategy side,
ex. Sell_Trades_url=[http://127.0.0.1:8000/sell/trades/](http://127.0.0.1:8000/sell/trades/)

![sellTradesSnap](https://user-images.githubusercontent.com/83577077/218302987-aaf03235-9c52-4c91-bb82-81f7e85944e5.PNG)


Buy_Trades_url=[http://127.0.0.1:8000/buy/trades/](http://127.0.0.1:8000/buy/trades/)

![buyTradesSnap](https://user-images.githubusercontent.com/83577077/218302952-143f666f-3891-4aba-94ce-9e80cd75ac05.PNG)


## The implementation of two functions as required in task 1 located in # trading/repository.py
## The implementation of compute_pnl function as required in task 2 located in # trading/connectdb.py
## Note: It's my first time using Django and it took me about 20+ hours to learn it. For sure i'll do my best to solve the issue and everything about it described as comment.


#### Built With
* Python v 3.10.6 
* Django v 4.1.6
* Docker v 1.23.3
* SQLite v 3.1.0
* Swagger viewer v 3.1.2
