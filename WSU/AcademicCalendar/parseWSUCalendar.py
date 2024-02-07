import csv
from icalendar import Calendar, Event
from datetime import datetime

def csv_to_ics(csv_file, output_file):
    cal = Calendar()

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            event = Event()
            event.add('summary', row[0])
            event.add('dtstart', datetime.strptime(row[1], "%A, %B %d, %Y"))
            event.add('dtend', datetime.strptime(row[1], "%A, %B %d, %Y"))
            cal.add_component(event)

    with open(output_file, 'wb') as ics_file:
        ics_file.write(cal.to_ical())

if __name__ == '__main__':
    input_csv_file = 'events.csv'
    output_ics_file = 'events.ics'
    csv_to_ics(input_csv_file, output_ics_file)
    print(f"Conversion complete. ICS file saved as {output_ics_file}")
