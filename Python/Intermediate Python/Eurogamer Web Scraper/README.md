## Eurogamer Blog Scraper

This is a Python script that scrapes the latest blog posts from [Eurogamer.net's blog page](https://www.eurogamer.net/blogs).

It collects the following information from each blog post:

- Title
- Headline
- Author
- Date Published

The data is saved in two formats:
- `blogs.json` – structured data for developers or APIs
- `blogs.csv` – easy to open in Excel or Google Sheets

---

## Requirements

- Python 3
- Packages:
  - `requests`
  - `beautifulsoup4`

To install the required packages, run:

```bash
pip install requests beautifulsoup4
