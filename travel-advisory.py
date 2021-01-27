import requests
from urllib.request import urlopen
import os


url = "https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Travel-Advisory.aspx"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")


updated_at = html[113309:113332]





report = {}
report["value1"] = updated_at
report["value2"] = 'second'
report["value3"] = 'first'


ifttt_key = os.environ["IFTTT_KEY"]


ifttt_url = f"https://maker.ifttt.com/trigger/Scraper/with/key/{ifttt_key}"


if 'Updated January 6, 2021' != updated_at:
	requests.post(ifttt_url,data=report)