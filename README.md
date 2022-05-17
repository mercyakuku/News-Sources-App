# News-Bulletins

## By mercyakuku

# Description
This is a web application suited best for people who always miss the news and they are very frustrated since they can't keep up with current affairs. This is an application that will help them list and preview news articles from various sources. The application consumes news from the [News API](https://newsapi.org/)

## Live link
https://news-bulletins.herokuapp.com/

## User Story

1. A user would see various news sources on the homepage of the application.
2. A user would also be able to select a news source and see all news articles from the selected news source in the application.
3. A user will be able to see the image, description and the time a news article was created from the News-Articles tab.
4. A user is required to click here to view more  details on an article and read the full article on the source website.


## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  git clone https://github.com/mercyakuku/News-Sources-App.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd News_Bulletins
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export API_KEY='{Enter your News Api Key}'
  ```
4. Running the application
  ```bash
  python3.9 manage.py server
          or
   $ chmod +x start.sh
   $ ./start.sh
  ```
5. Testing the application
  ```bash
  python3.9 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technologies used

* Python3.9.12
* Flask
* Heroku
* css
* HTML
* Other


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [mercyakuku24@gmail.com]

## License
MIT License

Copyright (c) 2022 mercyakuku

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

* Copyright (c) 2022 **mercyakuku**
