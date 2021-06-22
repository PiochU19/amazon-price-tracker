# 💵 Amazon Price Tracker

## Contributors
* Dominik Pioś

## 🔨  V1.0.0

## [MIT LICENSE](https://github.com/PiochU19/image-loader/blob/master/LICENSE)

## Technologies used:
* Django
* Django Rest Framework (API)
* React
* Celery (Redis as a broker)
* PostgreSQL
* Nginx
* Docker

### 🔏 Swagger API Documentation [here](https://app.swaggerhub.com/apis/PiochU19/amazon_price_tracker/1.0.0)

## Short description

App is using Python built in **requests** and *BeautifulSoup* from **bs4** to scrap Amazon Site. User can set the price, choose product from list taken from Amazon and set the 'Tracker'.

Celery has a periodic task (executes everyday on midnight), which checks if actual product price is less than price provided by user. If True, alert is sending through email and Tracker is deleted.

## Todo
* Ability to change prices
* Better responsivity
* Add more Online Shops (not only Amazon)

## Versions:
* 1.0.0
    1. First Version of Application