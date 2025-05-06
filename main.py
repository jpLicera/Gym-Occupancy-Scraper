import json
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
ACTIVITY_NAME = os.getenv("ACTIVITY_NAME")


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

        reservation_records = process_response(response)
        persist_reservation_records(reservation_records)


def process_response(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    entries = []
    for date_block in soup.select('.booking-date-container'):
        date = extract_date(date_block)
        if not date:
            continue

        time_slots = extract_reservation_records(date_block)
        entries.append({
            "date": date,
            "time_slots": time_slots
        })
        # entries.append(f"{time_slots}")

    return entries


def extract_date(date_block):
    date_element = date_block.select_one(".row.booking-by-date.grey.darken-4.white-text")
    if not date_element:
        return None
    return date_element.text.strip()


def extract_reservation_records(date_block):
    reservation_entries = []
    for block in date_block.select('.row.booking-by-date'):
        test = block.select_one('.new.badge.left')

        if test:
            activity = test.get("data-badge-caption")
            if activity != ACTIVITY_NAME:
                continue

        time_element = block.select_one('.col.s2.m1 b')

        if not time_element:
            continue
        time = time_element.text.strip()
        details = block.select('.clearfix small:last-of-type')

        if not details:
            continue

        occupancy = "None"

        for detail in details:
            if not detail or not detail.text:
                continue
            occupancy = detail.text.strip()

        reservation_entries.append(f"{time}: {occupancy}")

    return reservation_entries


def persist_reservation_records(records):
    with open('gym_occupancy_log.json', 'a', encoding='utf-8') as file:
        file.write(f"\n{json.dumps(records)}\n")


scrape_and_log_occupancy()
