# MacDonalds Scraper 


## Environment Setup
You will need to use PIP to install the dependencies first.
`pip install -r requirements.txt`

Go to http://phantomjs.org/download.html and download latest the version of phantomjs for your OS.

Update `PHANTOMJS_PATH` in *main.py* to point to the location of the binary/executable file for phantomjs.


## Usage
`sudo python main.py`


## Things to note
* MacDonald's only loads the first 5 locations. Use selenium to simulate click on *Load More* button to fetch more data.
* The MacDonald's website fetches data asynchronously. To ensure all the data has been fetched, wait for it to finish loading before instantiating a BeautifulSoup object.

