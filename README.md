# <img src="https://user-images.githubusercontent.com/79513906/133940646-d0d40127-6465-46aa-9d11-10d29232d00d.gif" width="50" height="45"> Twitter Bot 

In this project, I'm creating a simple Twitter Bot that will post tweets about movies every hour.

## Get the data

Using Web Scraping tools, I build a [scraper](https://github.com/NawfelBC/Twitter-Bot/blob/main/scraper.py) to extract data (title, release date, rate, image) from a [website](https://www.listchallenges.com/top-1000-movies-of-the-21st-century-tspdt) that lists the top 1000 movies of the 21st Century and stored everything into a [JSON file](https://github.com/NawfelBC/Twitter-Bot/blob/main/data.json).

## Build the bot

- The first step is to build the [services](https://github.com/NawfelBC/Twitter-Bot/blob/main/services.py) that will make the bot do the things we want. The goal is to extract the data of a random element/movie from the JSON file and format everything into a Tweet. We also want to download the corresponding image of the movie selected and store it into a JPG file that will be overwritten everytime we generate a new movie for storage optimization purposes. 

- Next, we want to build the [bot](https://github.com/NawfelBC/Twitter-Bot/blob/main/bot.py). Using the Twitter API and the package tweepy, we are now able to post a tweet containing a random movie and the corresponding image below.

## Deploy the bot

The bot needs to run continuously, but not on our own machine. Therefore, we use a platform called [Heroku](https://www.heroku.com) that allows us to deploy any app and run it on a remote server. 

<p align="center">
<img src="https://user-images.githubusercontent.com/79513906/132551693-62e8a8a1-e9b6-4e5e-8681-03e8f7771f19.PNG" width="350" height="550">
<br><strong>Figure 1 : Screenshot of the bot</br></strong>
</p>

## Try it yourself

If you want to try the bot, apply for a [Developer Account](https://developer.twitter.com/en/apply-for-access) to get your API keys, and insert them into the [KEYS.py](https://github.com/NawfelBC/Twitter-Bot/blob/main/KEYS.py) file. Then, run the [bot.py](https://github.com/NawfelBC/Twitter-Bot/blob/main/bot.py) file to host it locally. And that's it, here is your bot.

## Packages and Services used :
- [Tweepy](https://www.tweepy.org/)  
- [Bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
- [Requests](https://docs.python-requests.org/en/master/)  
- [Heroku](https://www.heroku.com/)
