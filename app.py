from flask import Flask

from flask_restful import Api, Resource, reqparse, inputs, abort
from flask_sqlalchemy import SQLAlchemy
from flask import request

import sys
from datetime import *

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calender.db'
api = Api(app)
parser = reqparse.RequestParser()


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(40), nullable=False)
    date = db.Column(db.Date, nullable=False)


class EventTodayResource(Resource):
    def get(self):
        events = []
        for event in Event.query.filter(Event.date == date.today()).all():
            events.append(convert_event(event))
            # events.append({"id": event.id,
            #                "event": event.event,
            #                "date": event.date.strftime("%Y-%m-%d")})
        return events


class EventResource(Resource):
    def get(self):

        if len(request.args) == 0:
            return get_all_events()
        else:
            start_date = datetime.strptime(request.args.get('start_time'), "%Y-%m-%d")
            end_date = datetime.strptime(request.args.get('end_time'), "%Y-%m-%d")
            return get_events_in_range(start_date, end_date)

    def post(self):
        args = parser.parse_args()
        if "message" in args:
            return args

        add_to_database(args['event'], args['date'])

        return {"message":"The event has been added!",
                "event": args['event'],
                "date": args['date'].strftime("%Y-%m-%d")}


class EventIdResource(Resource):

    def get(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if event is None:
            abort(404, message="The event doesn't exist!")

        return convert_event(event)
        # return {"id": event.id,
        #         "event": event.event,
        #         "date": event.date.strftime("%Y-%m-%d")}

    def delete(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if event is None:
            abort(404, message="The event doesn't exist!")
        
        db.session.delete(event)
        db.session.commit()

        return {"message": "The event has been deleted!"}


def get_all_events():
    events = []
    for event in Event.query.all():
        events.append(convert_event(event))
    return events


def get_events_in_range(start_date, end_date):
    events = []

    for event in Event.query.all():
        temp_date = datetime.combine(event.date, datetime.min.time())
        if start_date <= temp_date <= end_date:
            events.append(convert_event(event))
    return events


def add_to_database(event_name, date):
    db.session.add(Event(event=event_name, date=date))
    db.session.commit()


def add_parser_args():
    parser.add_argument('event', type=str, help="The event name is required!", required=True)
    parser.add_argument('date',
                        type=inputs.date,
                        help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
                        required=True)


def convert_event(event_object):
    return {"id": event_object.id,
            "event": event_object.event,
            "date": event_object.date.strftime("%Y-%m-%d")}


# do not change the way you run the program
if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    api.add_resource(EventIdResource, '/event/<int:event_id>')
    api.add_resource(EventTodayResource, '/event/today')
    api.add_resource(EventResource, '/event')
    add_parser_args()

    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
