# YouTube Scraper and Sentiment Analysis Project

## Overview

This Python project scrapes YouTube for video and channel details based on a keyword, extracts comments from the videos, and performs sentiment analysis on the comments. It also downloads the YouTube videos and saves the results into CSV files for further use.

### Features:
- Scrapes video links and channel details using **Selenium**.
- Extracts YouTube comments using **youtube-comment-scraper-python**.
- Analyzes sentiment of the comments using **TextBlob**.
- Downloads YouTube videos using **Pytube**.
- Saves all data (channel details, comments, sentiment analysis, etc.) in CSV format.

## Prerequisites

1. **Python 3.x** (Ensure you have a recent version installed.)
2. **Browser & WebDriver** (Firefox and its compatible GeckoDriver in this case.)
3. **Necessary Python Packages:**

Install the required Python libraries using `pip`:

bash
pip install selenium
pip install pytube
pip install youtube-comment-scraper-python
pip install pandas
pip install nltk
pip install textblob

Here’s a README.md file for your project:

markdown
Copy code
# YouTube Scraper and Sentiment Analysis Project

## Overview

This Python project scrapes YouTube for video and channel details based on a keyword, extracts comments from the videos, and performs sentiment analysis on the comments. It also downloads the YouTube videos and saves the results into CSV files for further use.

### Features:
- Scrapes video links and channel details using **Selenium**.
- Extracts YouTube comments using **youtube-comment-scraper-python**.
- Analyzes sentiment of the comments using **TextBlob**.
- Downloads YouTube videos using **Pytube**.
- Saves all data (channel details, comments, sentiment analysis, etc.) in CSV format.

## Prerequisites

1. **Python 3.x** (Ensure you have a recent version installed.)
2. **Browser & WebDriver** (Firefox and its compatible GeckoDriver in this case.)
3. **Necessary Python Packages:**

Install the required Python libraries using `pip`:
bash
pip install selenium
pip install pytube
pip install youtube-comment-scraper-python
pip install pandas
pip install nltk
pip install textblob

Additionally, ensure that the following NLTK resources are downloaded:
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


Project Structre
├── Youtube_Scraping_Project/
│   ├── main.py
│   ├── README.md
│   ├── DATA_YOUTUBE.csv
│   ├── Scrapped_comments.csv
│   ├── polization.csv
│   ├── output.csv
└───└───
Files:
main.py: The main script that handles scraping, comment extraction, sentiment analysis, and video downloading.
DATA_YOUTUBE.csv: Contains scraped data about the YouTube channels.
Scrapped_comments.csv: Contains all the comments scraped from YouTube videos.
polization.csv: Contains the polarity (sentiment) analysis of the comments.
output.csv: Combines comments and polarity for final results.

Project Workflow
1. Scraping YouTube Data
The program scrapes YouTube for videos and channels based on a keyword provided in the script (Iphone 16 in this case).
It retrieves details such as:
Channel name
Channel description
Subscriber count
Channel URL
Video URLs
2. Extracting Video Comments
Comments are extracted from the videos listed in the scraped data.
The extracted comments are stored in Scrapped_comments.csv.
3. Sentiment Analysis of Comments
The comments are analyzed for sentiment polarity using TextBlob.
The result of the sentiment analysis (polarity) is saved in polization.csv.
4. Downloading Videos
The script downloads the YouTube videos using Pytube and saves them in the specified directory.
Usage
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/your-username/youtube-scraping-project.git
cd youtube-scraping-project
Step 2: Update Path Configuration
Update the base_path variable inside main.py to set the directory where files will be saved and where downloaded videos will be stored. Example:

python
Copy code
base_path = os.path.abspath("E:/python_code")  # Change this to your desired path
Step 3: Run the Script
Execute the main.py script to start scraping YouTube data, extracting comments, performing sentiment analysis, and downloading videos.

bash
Copy code
python main.py
Step 4: Output Files
Once the script finishes executing, you’ll find the following CSV files generated in the specified base_path:

DATA_YOUTUBE.csv: Contains channel and video details.
Scrapped_comments.csv: Contains scraped comments.
polization.csv: Contains sentiment analysis results (polarity).
output.csv: Merged data of comments and polarity.
The downloaded videos will also be saved in the base_path directory.

Notes
Make sure the GeckoDriver is installed and added to the system’s PATH variable for Firefox automation.
You can modify the keyword variable in main.py to search for different topics on YouTube.
License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy code

### Instructions:
1. Place this file in the root of your project directory and save it as `README.md`.
2. You can modify sections like the repository link and `base_path` details based on your local setup.

This README should help anyone understand and run your project without issues.












