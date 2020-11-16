"""Data Model for mocking bird. Database name = mockingbird """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    is_active_fb_oauth = db.Column(db.Boolean, default='F', unique=False) # Users using facebook o-auth for login
    # first_name = db.Column(db.String)
    # last_name = db.Column(db.String)
    
    # * regenerated_texts = a list of text objects (because of backref in regenerated_texts )

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email} first_name={self.first_name}>'


class Generated_Text(db.Model):
    """a text generated by a user using Markov Chain Algorithm"""

    __tablename__ = 'generated_texts'

    gen_text_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    gen_text = db.Column(db.Text)

    user = db.relationship('User', backref='generated_texts')
    def __repr__(self):
        return f'<Generated_Text gen_text_id={self.gen_text_id} user_id={self.user_id} gen_text={self.gen_text} >'


class Sample_Text(db.Model):
    """A sample stored text provided to the user in a drop-down interface to used as seed for markov chain"""

    __tablename__ = 'sample_texts'

    text_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    source = db.Column(db.Text) #eg: Twitter, Book excerpt, Article etc.
    author = db.Column(db.Text) #eg: twitter handle, author name etc.
    source_imgurl = db.Column(db.String) #use this url for a source ref image (book cover, twitter account etc)
    overview = db.Column(db.Text)
    text = db.Column(db.Text)

# * sample_text_source =  (because of backref in sample_text_sources )

    def __repr__(self):
        return f'<Sample_Text text_id={self.text_id} overview={self.overview} >'

class Sample_Text_Source(db.Model):
    """A sample stored text provided to the user in a drop-down interface to used as seed for markov chain"""

    __tablename__ = 'sample_text_sources'

    source_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    text_id = db.Column(db.Integer, db.ForeignKey('sample_text.text_id'))
    source = db.Column(db.Text) #eg: Twitter, Book excerpt, Article etc.
    author = db.Column(db.Text) #eg: twitter handle, author name etc.
    source_url = db.Column(db.String) #use this url for a source ref image (book cover, twitter account etc)

    sample_text = db.relationship('Sample_Text', backref='sample_text_sources')

    def __repr__(self):
        return f'<Sample_Text_Source source_id={self.source_id} source={self.source} >'





def connect_to_db(flask_app, db_uri='postgresql:///mockingbird', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets messy/too much;
    # this will tell SQLAlchemy not to print out every query it executes.

    connect_to_db(app)
