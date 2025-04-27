# News Feed Slack Bot

A simple Python script that fetches the latest headlines from ITmedia AI+ RSS and posts them to a Slack channel via an Incoming Webhook.

## Prerequisites

- Python 3.6 or higher
- A Slack Incoming Webhook URL

## Setup

1. Navigate to the `news-feed` directory:
   ```bash
   cd /path/to/news-feed
   ```
2. Create a Python virtual environment:
   ```bash
   python3 -m venv .venv
   ```
3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
4. Install required libraries:
   ```bash
   pip install feedparser requests
   ```

## Configuration

1. Open `news_post.py` in an editor.
2. Set your Slack webhook URL by replacing the placeholder:
   ```python
   WEBHOOK_URL = "https://hooks.slack.com/services/XXX/YYY/ZZZ"
   ```
3. (Optional) Adjust `RSS_URL` or `MAX_ITEMS` to change the RSS feed source or number of items.

## Usage

With the virtual environment activated, run:

```bash
python news_post.py
```

- The script will post the latest headlines to Slack.
- Logs are written to `newsbot_itmedia.log` in the same directory.

## Author

- Murasan ([https://murasan-net.com/](https://murasan-net.com/))

## License

This project is released under the MIT License.
