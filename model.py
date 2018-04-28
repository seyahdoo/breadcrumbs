
from flask_sqlalchemy import SQLAlchemy

import datetime

from sqlalchemy_searchable import make_searchable
from sqlalchemy_utils.types import TSVectorType

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)
db = SQLAlchemy()

make_searchable()


##############################################################################
# Model definitions

class User(db.Model):
    """User of Issue system."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    worked_department=db.Column(db.Integer, db.ForeignKey('departments.department_id'), nullable=False)
    active=db.Column(db.Boolean, nullable=False)






    search_vector = db.Column(TSVectorType('first_name', 'last_name'))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id,
                                               self.email)


class Issue(db.Model):
    """Issue info."""

    __tablename__ = "issues"

    issue_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.department_id'), nullable=False)
    issuer_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    solver_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    type_id = db.Column(db.Integer, db.ForeignKey('issuetypes.type_id'), nullable=True)
    state_id = db.Column(db.Integer, db.ForeignKey('issuestates.state_id'), nullable=True)
    entry_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    finish_date = db.Column(db.DateTime, nullable=True)
    summary = db.Column(db.String(140), nullable=True)
    detail_text = db.Column(db.String(400), nullable=True)
    attachments = db.relationship("Attachment", backref=db.backref("attachments"))
    logs= db.relationship("IssueLog",  backref=db.backref("logs"))
    reports= db.relationship("IssueReport", backref=db.backref("reports"))
    interruptions=db.relationship("Issue", secondary="interruptions", backref="interruptions")

    
class Interruption(db.Model):

        __tablename__ = "interruptions"

        interruption_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
        master_id= db.Column(db.Integer, db.ForeignKey('issues.issue_id'), nullable=False)
        slave_id = db.Column(db.Integer, db.ForeignKey('issues.issue_id'), nullable=False)

        master_a = db.relationship("Issue", foreign_keys=[master_id], backref=db.backref("master"))
        slave_b = db.relationship("Issue", foreign_keys=[slave_id], backref=db.backref("slave"))


class IssueState(db.Model):
    """States of an Issue."""

    __tablename__ = "issuestates"
    state_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    state_name = db.Column(db.String(30), nullable=False)


class IssueType(db.Model):
    """Types of an Issue."""

    __tablename__ = "issuetypes"
    type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type_name = db.Column(db.String(30), nullable=False)

class Attachment(db.Model):

    __tablename__= "attachments"

    attachment_id=db.Column(db.Integer,autoincrement=True, primary_key=True)
    issue_id=db.Column(db.Integer,db.ForeignKey('issues.issue_id'),  nullable=False)
    attachment_path=db.Column(db.String(1000), nullable=False)


class Department(db.Model):
    """Department info."""

    __tablename__ = "departments"

    department_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    parent_department = db.Column(db.Integer, db.ForeignKey('departments.department_id'), nullable=True)
    supervisor_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    name = db.Column(db.String(100), nullable=False)



class IssueLog(db.Model):
    """Log of a state of an Issue when changed."""

    __tablename__ = "issuelogs"

    issue_log_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    issue_id = db.Column(db.Integer, db.ForeignKey('issues.issue_id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    new_state_id = db.Column(db.Integer, db.ForeignKey('issuestates.state_id'), nullable=True)


class IssueReport(db.Model):
    """Additional info about an Issue."""

    __tablename__ = "issuereports"

    issue_report_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    issue_id = db.Column(db.Integer, db.ForeignKey('issues.issue_id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    attachments=db.relationship("Attachment", backref=db.backref("attachments"))
    message = db.Column(db.String(400), nullable=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)


##############################################################################
# Helper functions

def connect_to_db(app, db_uri=None):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgresql://dbuser:1234@localhost/issuetracker'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
