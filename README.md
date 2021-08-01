# Web-Calender
## Description
Simple REST service build using the Flask framework to save and manage a calender of events. Worked with a database using Flask-SQLAlchemy extension and created resources using the Flask-RESTful extension.

## Functionality
### The basics
To start, the web-calender supports 3 basic operations:
* Adding events to the calender
* Getting events from the calender
* Deleting events from the calender   

I will explain how to add, get, and delete events from the calender eventually.
### Events
Each event in the database has 3 attributes as follows:
* *id* -- a unique integer value.
* *event* -- the name of the event as a string (200 character limit).
* *date* -- a date-time object representing the date and/or time of the event and must of of the form YYYY-MM-DD.
When retrieving events from the calender, all events will be returned in a JSON format as follows:
```
{
    "id": 1,
    "event": "Name of the event goes here",
    "date": "2020-04-20"
}
```
In the case of multiple events, the calender will return a list of events in a JSON format as follows:
```
[
    {
        "id": 1,
        "event": "Name of an event goes here",
        "date": "2001-04-20"
    },
    {
        "id": 2,
        "event": "Name of another event goes here",
        "date": "2003-05-15"
    }
]
```
### GET Requests
To get events from the calender, you may use any of the following urls. The parameters (if any) and responses for each of the requests are outlined below.
#### *__/event__* 

* returns a list of all events in the calender in the response body in the JSON format outlined above.  
* request url format: 
```
/event
```
* response format: 
```
[ 
    {
        "id": 1,
        "event": "Name of an event goes here",
        "date": "2003-05-15"
    },
    {
        "id": 2,
        "event": "Name of an event goes here",
        "date": "2003-04-12"
    },
    {
        "id": 3,
        "event": "Name of an event goes here",
        "date": "2001-04-20"
    }
]
```
#### *__/event/today__* 

* returns a list of events schduled for today in the response body in the JSON format outlined above
* request url format:
```
/event/today
```
* response format (assuming that todays date is April 20, 2021):
```
[
    {
        "id": 5,
        "event": "Event name goes here",
        "date": "2021-04-20"
    }
]
```
#### *__/event/<int::id>__*

* returns the event with the given id number. If the event with the provided id number does not exist, the response body should include an error message with error code 404.
* request url format:
```
/event/<int::id>
```
* example url
```
/event/1
```
* response format
```
{
    "id": 1,
    "event": "Event name goes here",
    "date": "2021-04-20"
}
```
#### *__/event/?start_time=YYYY-MM-DD&end_time=YYYY-MM-DD__*

* returns a list of events in the given date range, from the start date to the end date
* request url format:
```
/event/?start_time=YYYY-MM-DD&end_time=YYYY-MM-DD
```
* example url request:
```
/event/?start_time=2020-04-12&end_time=2020-05-15
```
* example response body:
```
[
    {
        "id": 1,
        "event": "Name of an event goes here",
        "date": "2020-04-12"
    },
    {
        "id": 2,
        "event": "Name of an event goes here",
        "date": "2020-04-20"
    },
    {
        "id": 3,
        "event": "Name of an event goes here",
        "date": "2020-05-15"
    }
]
```
### POST Requests
To add events to the calendar, you may use any of the following urls. 



