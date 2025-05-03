import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

LOGIN_PAGE = os.getenv("LOGIN_PAGE")
LOGIN_URL = os.getenv("LOGIN_URL")
RESERVATION_URL = os.getenv("RESERVATION_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def scrape_and_log_occupancy():

    # Start a session to persist cookies across requests
    with requests.Session() as session:
        login_page = session.get(LOGIN_URL)

        soup = BeautifulSoup(login_page.text, 'html.parser')

        token_input = soup.find('input', attrs={'name': '__RequestVerificationToken'})

        if not token_input:
            print("Couldn't find CSRF token on login page.")
            return

        csrf_token = token_input.get('value')

        # The form that is sent to the authentication endpoint used by the web application
        login_payload = {
            'Email': EMAIL,
            'Password': PASSWORD,
            '__RequestVerificationToken': csrf_token,
        }

        # Assign headers
        login_headers = {
            'Referer': LOGIN_URL
        }

        session.post(LOGIN_URL, data=login_payload, headers=login_headers)

        # Get the "reservations" page
        response = session.get(RESERVATION_URL)

        # Get the occupancy data
        soup = BeautifulSoup(response.text, 'html.parser')
        reservation_entries = []
        for block in soup.select('.row.booking-by-date'):
            timeElement = block.select_one('.col.s2.m1 b')

            if not timeElement:
                continue
            time = timeElement.text.strip()
            details = block.select('.clearfix small:last-of-type')

            if not details:
                continue

            for detail in details:
                if not detail or not detail.text:
                    continue
                occupancy = detail.text.strip()

            reservation_entries.append(f"{time}: {occupancy}")

        # Persist the results
        with open('gym_occupancy_log.txt', 'a', encoding='utf-8') as file:
            file.write(f"\n{datetime.now()}\n")
            for entry in reservation_entries:
                file.write(entry + "\n")


scrape_and_log_occupancy()
