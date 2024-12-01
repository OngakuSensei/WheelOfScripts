import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON, ARRAY
from datetime import datetime

# Create a base class for declarative models
Base = declarative_base()

class User(Base):
    """
    User table definition representing user information
    """
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, start=1)
    discord_auth_token = sa.Column(sa.String(255), nullable=False, unique=True)
    is_admin = sa.Column(sa.Enum('Y', 'N'), default='N')
    username = sa.Column(sa.String(100), nullable=False)
    display_name = sa.Column(sa.String(100))
    email = sa.Column(sa.String(255), unique=True)
    profile_pic_url = sa.Column(sa.String(500))
    about = sa.Column(sa.Text)
    links = sa.Column(sa.JSON)  # Python list of links
    uploaded_scripts = sa.Column(sa.ARRAY(sa.Integer))  # List of Script IDs
    blocked_scripts = sa.Column(sa.ARRAY(sa.Integer))  # List of Script IDs
    favorite_scripts = sa.Column(sa.ARRAY(sa.Integer))  # List of Script IDs

    # Personal Wheel Odds
    recency_bias = sa.Column(sa.Integer, default=9500)  # 0-10000 scale
    frequency_bias = sa.Column(sa.Integer, default=9900)  # 0-10000 scale
    author_bias = sa.Column(sa.Integer, default=0)  # 0-10000 scale
    use_author_bias = sa.Column(sa.Boolean, default=False) # Lets user decide whether to use this attribute or not

    # Relationships
    scripts = relationship("Script", back_populates="uploader")
    spins = relationship("Spin", back_populates="user")

class Script(Base):
    """
    Script table definition representing script information
    """
    __tablename__ = 'scripts'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    uploader_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    title = sa.Column(sa.String(255), nullable=False)
    author = sa.Column(sa.String(100))
    author_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=True)
    submitted_to_public = sa.Column(sa.Enum('Y', 'N'), default='N')
    added_to_public_wheel = sa.Column(sa.Enum('Y', 'N'), default='N')
    logo_url = sa.Column(sa.String(500))
    background_image_url = sa.Column(sa.String(500))
    is_teensy = sa.Column(sa.Boolean, default=False)
    description = sa.Column(sa.Text)
    characters = sa.Column(sa.ARRAY(sa.String))
    fabled_list = sa.Column(sa.ARRAY(sa.String))
    travelers = sa.Column(sa.ARRAY(sa.String))
    date_last_modified = sa.Column(sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    version = sa.Column(sa.Integer, default=1)

    # Relationships
    uploader = relationship("User", back_populates="scripts")
    versions = relationship("ScriptVersion", back_populates="script")
    spins = relationship("Spin", back_populates="script")

class ScriptVersion(Base):
    """
    Versions table to track script changes
    """
    __tablename__ = 'script_versions'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    script_id = sa.Column(sa.Integer, sa.ForeignKey('scripts.id'))
    version = sa.Column(sa.Integer)
    date_uploaded = sa.Column(sa.DateTime, default=datetime.utcnow)
    characters = sa.Column(sa.ARRAY(sa.String))
    fabled_list = sa.Column(sa.ARRAY(sa.String))
    travelers = sa.Column(sa.ARRAY(sa.String))
    description = sa.Column(sa.Text)

    # Relationship
    script = relationship("Script", back_populates="versions")

class Odds(Base):
    """
    Odds table tracking script odds for each user
    """
    __tablename__ = 'odds'

    script_id = sa.Column(sa.Integer, sa.ForeignKey('scripts.id'), primary_key=True)
    
    # Dynamic columns for each user will need to be added programmatically
    # This is a base model, and actual implementation will require 
    # dynamic column generation when a new user is added

class Spin(Base):
    """
    Spins table tracking wheel spin events
    """
    __tablename__ = 'spins'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    script_id = sa.Column(sa.Integer, sa.ForeignKey('scripts.id'))
    timestamp = sa.Column(sa.DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="spins")
    script = relationship("Script", back_populates="spins")

def create_database(engine):
    """
    Create all tables in the database
    """
    Base.metadata.create_all(engine)

def initialize_database(engine):
    """
    Example initialization function 
    """
    create_database(engine)
    # Additional initialization logic can be added here

# Example usage
if __name__ == '__main__':
    from sqlalchemy import create_engine

    # Replace with your actual MySQL connection string
    DATABASE_URL = "mysql+pymysql://username:password@localhost/wheel_of_scripts"
    
    engine = create_engine(DATABASE_URL)
    initialize_database(engine)
    print("Database initialized successfully!")

# Notes on implementation:
# 1. This uses SQLAlchemy's declarative base for ORM
# 2. Uses PostgreSQL-style ARRAY for list storage (most compatible)
# 3. Provides relationships between tables
# 4. Includes basic timestamp and versioning logic
# 5. The Odds table will require dynamic column generation
