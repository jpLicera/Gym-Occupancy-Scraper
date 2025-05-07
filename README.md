# 💡 What is this?

This repo contains a tool built to scrape attendance information from my gym's web application. 

# 🔍 Usage

Given an `.env` file with the following properties:

```dotenv
LOGIN_PAGE=https://placeholder.com/login
LOGIN_URL=https://placeholder.com/authentication
RESERVATION_URL=https://placeholder.com/reservations
EMAIL=example@gmail.com
PASSWORD=123456789
ACTIVITY_NAME=Pilates
```

Executing the `run` script produces the following result:

```json
[
  {
    "scrapped_on": "2025-05-07T14:23:22.816784",
    "activity": "Pilates",
    "date": "2025-05-07",
    "time_slots": [
      {
        "time": "14:00",
        "occupancy": "54",
        "maximum_occupancy": "140"
      },
      {
        "time": "15:00",
        "occupancy": "6",
        "maximum_occupancy": "140"
      },
      {
        "time": "16:00",
        "occupancy": "3",
        "maximum_occupancy": "140"
      },
      {
        "time": "17:00",
        "occupancy": "2",
        "maximum_occupancy": "140"
      },
      {
        "time": "18:00",
        "occupancy": "2",
        "maximum_occupancy": "140"
      },
      {
        "time": "19:00",
        "occupancy": "2",
        "maximum_occupancy": "140"
      },
      {
        "time": "20:00",
        "occupancy": "3",
        "maximum_occupancy": "140"
      },
      {
        "time": "21:00",
        "occupancy": "1",
        "maximum_occupancy": "140"
      }
    ]
  },
  {
    "scrapped_on": "2025-05-07T14:23:22.816784",
    "activity": "Pilates",
    "date": "2025-05-08",
    "time_slots": [
      {
        "time": "07:00",
        "occupancy": "4",
        "maximum_occupancy": "140"
      },
      {
        "time": "08:00",
        "occupancy": "1",
        "maximum_occupancy": "140"
      },
      {
        "time": "09:00",
        "occupancy": "0",
        "maximum_occupancy": "140"
      },
      {
        "time": "10:00",
        "occupancy": "0",
        "maximum_occupancy": "140"
      },
      {
        "time": "11:00",
        "occupancy": "0",
        "maximum_occupancy": "140"
      },
      {
        "time": "12:00",
        "occupancy": "0",
        "maximum_occupancy": "140"
      },
      {
        "time": "13:00",
        "occupancy": "1",
        "maximum_occupancy": "140"
      },
      {
        "time": "14:00",
        "occupancy": "1",
        "maximum_occupancy": "140"
      },
      {
        "time": "15:00",
        "occupancy": "0",
        "maximum_occupancy": "140"
      },
      {
        "time": "16:00",
        "occupancy": "1",
        "maximum_occupancy": "140"
      },
      {
        "time": "17:00",
        "occupancy": "0",
        "maximum_occupancy": "140"
      },
      {
        "time": "18:00",
        "occupancy": "0",
        "maximum_occupancy": "140"
      },
      {
        "time": "19:00",
        "occupancy": "0",
        "maximum_occupancy": "140"
      },
      {
        "time": "20:00",
        "occupancy": "0",
        "maximum_occupancy": "140"
      },
      {
        "time": "21:00",
        "occupancy": "0",
        "maximum_occupancy": "140"
      }
    ]
  }
]

```
