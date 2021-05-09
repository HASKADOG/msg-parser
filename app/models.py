from app import db

class Platforms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform_name = db.Column(db.String(64), index=True, unique=True)
    groups = db.relationship('Groups', backref='platform', lazy='dynamic')

    def __repr__(self):
        return '<Platform {}>'.format(self.platform_name)

class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assigned_name = db.Column(db.String(64), index=True, unique=True)
    messages = db.relationship('Messages', backref='group', lazy='dynamic')
    platform_id = db.Column(db.Integer, db.ForeignKey('platforms.id'))

    def __repr__(self):
        return '<Group {}>'.format(self.assigned_name)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.BigInteger, index=True, unique=True)
    user_id = db.Column(db.Integer)
    messages = db.relationship('Messages', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {} | {}>'.format(self.phone_number, self.user_id)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text(1024))
    photo = db.Column(db.Text(512))
    audio = db.Column(db.Text(512))
    pdf = db.Column(db.Text(512))
    attachments = db.Column(db.Text(2048))
    datetime = db.Column(db.DateTime, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    def __repr__(self):
        return '<User {} | {}>'.format(self.text, self.group_id)
