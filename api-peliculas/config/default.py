from sqlalchemy import create_engine, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'
PROPAGATE_EXCEPTIONS = True
# Database configuration 
SQLALCHEMY_DATABASE_URI = 'postgresql://koalvwnd:clSZeSvtDEcrT-u5iq1qInt_L-2892zn@suleiman.db.elephantsql.com/koalvwnd'
SQLALCHEMY_TRACK_MODIFICATIONS = False 
SHOW_SQLALCHEMY_LOG_MESSAGES = False
ERROR_404_HELP = False