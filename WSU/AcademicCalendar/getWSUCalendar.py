import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import datetime
import icalendar


def download_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # print(response.text)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML content: {e}")
        return None

def parse_html_to_json(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    events = []
    for row in soup.select('table#AcadCal tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        if len(columns) >= 2:  # Ensure there are at least two <td> elements
            event_name = columns[1].get_text().strip()
            event_date = columns[2].get_text().strip()
            events.append({
                "event_name": event_name,
                "event_date": event_date
            })
    events = str(events).replace("'", '"')
    return events

def convert_json_to_csv(json_data):
    df = pd.DataFrame(json_data)
    df.to_csv('events.csv', index=False)


def main():
    url = "https://registrar.wsu.edu/academic-calendar/"
    html_content = download_html(url)
    if html_content:
        events_data = parse_html_to_json(html_content)
        # print(events_data)
        convert_json_to_csv(events_data)

        print("Grabbed WSU current Academic Calendar and converted it to CSV")

        

if __name__ == "__main__":
    main()