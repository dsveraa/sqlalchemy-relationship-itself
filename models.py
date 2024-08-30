from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True)
    

class FollowingAssociation(BaseModel):
    __tablename__ = "following_association"
    
    user_id = Column(Integer, ForeignKey('users.id'))
    following_id = Column(Integer, ForeignKey('users.id'))
    

class User(BaseModel):
    __tablename__ = "users"
    __allow_unmapped__ = True
     
    username = Column(String)
    
    following = relationship('User', secondary="following_association",
                             primaryjoin=("FollowingAssociation.user_id == User.id"),
                             secondaryjoin=("FollowingAssociation.following_id == User.id"),
                             )
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}, following={self.following}')>"
    

Base.metadata.create_all(engine)
