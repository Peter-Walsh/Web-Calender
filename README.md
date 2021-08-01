# Web-Calender
## Description
Simple REST service using the Flask framework to save and manage a calendar of events. Worked with a database using Flask-SQLAlchemy extension and created resources using the Flask-RESTful extension.

## Functionality
### The basics
To start, the web calendar supports 3 basic operations:
* Adding events to the calendar
* Getting events from the calendar
* Deleting events from the calendar   

I will explain how to add, get, and delete events from the calendar eventually.
### Events
Each event in the database has 3 attributes as follows:
* *id* -- a unique integer value.
* *event* -- the name of the event as a string (200 character limit).
* *date* -- a date-time object representing the date and/or time of the event and must of the form YYYY-MM-DD.
When retrieving events from the calendar, all events will be returned in a JSON format as follows:
```
{
    "id": 1,
    "event": "Name of the event goes here",
    "date": "2020-04-20"
}
```
In the case of multiple events, the calendar will return a list of events in a JSON format as follows:
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
To get events from the calendar, you may use any of the following URLs. The parameters (if any) and responses for each of the requests are outlined below.
#### *__/event__* 

* returns a list of all events in the calendar in the response body in the JSON format outlined above.  
* request URL format: 
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

* returns a list of events scheduled for today in the response body in the JSON format outlined above
* request URL format:
```
/event/today
```
* response format (assuming that today's date is April 20, 2021):
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
* request URL format:
```
/event/<int::id>
```
* example URL with valid id number
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
* example URL with invalid id number
```
/event/1
```
* response format
```
{
    "message": "The event doesn't exist!"
}
```
#### *__/event/?start_time=YYYY-MM-DD&end_time=YYYY-MM-DD__*

* returns a list of events in the given date range, from the start date to the end date
* request URL format:
```
/event/?start_time=YYYY-MM-DD&end_time=YYYY-MM-DD
```
* example URL request:
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
To add events to the calendar, you may use any of the following URLs. The response bodies and any parameters are outlined below. All events must contain an event name and date. If one is missing, the event will not be added to the calendar and an appropriate error message will be sent in the response body.
#### *__/event__*

* valid request body:
```
request_body = {
    "event": "Name of event goes here",
    "date": "2001-04-20"
}

response_body = {
    "message": "The event has been added!",
    "event": "Name of event goes here",
    "date": "2001-04-20"
}
```
* invalid request body (missing event name):
```
request_body = {
    "date": "2001-04-20"
}

response_body = {
    "message": {
        "event": "The event name is required!'
    }
}
```
* invalid request body (missing date):
```
request_body = {
    "event": "Event name or something"
}

response_body = {
    "message": {
        "date": "The event date with the correct format is required! The correct format is YYYY-MM-DD!"
    }
}
```

### DELETE Requests
To delete events from the calender, you may use any of the following URLs. In order to delete an event, you must provide the id number of the event in the calendar to the delete request.



