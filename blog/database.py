from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Session



SQLALCHEMY_DATABASE_URL='sqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={
    "check_same_thread":False
})
sessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)


Base=declarative_base()


def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()