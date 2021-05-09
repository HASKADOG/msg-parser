from app import db
from app.models import Platforms, Groups, Users, Messages
from datetime import datetime


class Whatsapp_handler():

    # Handler initialization
    def __init__(self, json):
        print('WhatsApp handler has been initiated')
        self.json = json

    def _parse_data(self):
        message = {
            'text' : self.json['text'][14:],
            'audio' : self.json['audio'],
            'photo' : self.json['photo'],
            'pdf' : self.json['pdf'],
            'attachments': self._get_attachments(),
            'datetime' : self._get_datetime(),
            'author' : self._get_user(),
            'group' : self._get_group()
        }

        return message

    def add_message(self):
        message = self._parse_data()
        message = Messages(text=message['text'], datetime=message['datetime'], author=message['author'], group=message['group'], audio=message['audio'], photo=message['photo'], pdf=message['pdf'], attachments=message['attachments'])

        db.session.add(message)
        db.session.commit()

        print('Message {} added'.format(self.json['text']))
    
    def _get_attachments(self):
        attachs_raw = self.json['attachments']
        attachs_list = []
        for attach in attachs_raw:
            attachs_list.append(attach['file']['url'])
        return str(attachs_list)

    def _get_datetime(self):
        time = self.json['event_time'].split('T')
        date = time[0].split('-')
        time = time[1].split('Z')
        time = time[0].split(':')
        year = date[0]
        month = date[1]
        day = date[2]
        hour = time[0]
        minute = time[1]
        sec = time[2]

        return datetime(int(year), int(month), int(day), int(hour), int(minute), int(sec))
    
    def _get_user(self):
        phone_number = self.json['text'][1:12]

        if self._check_user_exist(phone_number):
            return self._query_user(phone_number)
        else: 
            user = self._create_user(phone_number)
            return user

    def _check_user_exist(self, phone_number):
        user = db.session.query(Users.id).filter_by(phone_number=phone_number).first() is not None

        if user:
            return True
        else:
            return False

    def _query_user(self, phone_number):
        return Users.query.filter_by(phone_number=phone_number).first()
    
    def _create_user(self, phone_number):

        user = Users(phone_number=phone_number)

        db.session.add(user)
        db.session.commit()

        return user

    def _get_group(self):
        assigned_name = self.json['client']['assigned_name']

        if self._check_group_exist(assigned_name):
            return self._query_group(assigned_name)
        else: 
            group = self._create_group(assigned_name)
            return group

    def _check_group_exist(self, assigned_name):
        user = db.session.query(Groups.id).filter_by(assigned_name=assigned_name).first() is not None

        if user:
            return True
        else:
            return False
    
    def _query_group(self, assigned_name):
        return Groups.query.filter_by(assigned_name=assigned_name).first()
    
    def _create_group(self, assigned_name):
        platform = Platforms.query.get(1)
        group = Groups(assigned_name=assigned_name, platform=platform)

        db.session.add(group)
        db.session.commit()

        return group
