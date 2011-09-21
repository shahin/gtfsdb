from gtfsdb.model import DeclarativeBase
from sqlalchemy import Column, Index, Integer, Sequence, String


class Agency(DeclarativeBase):
    __tablename__ = 'agency'

    required_fields = ['agency_name', 'agency_url', 'agency_timezone']
    optional_fields = ['agency_id', 'agency_lang', 'agency_phone', 'agency_fare_url']

    id = Column(Integer, Sequence(None, optional=True), primary_key=True)
    agency_id = Column(String)
    agency_name = Column(String, nullable=False)
    agency_url = Column(String, nullable=False)
    agency_timezone = Column(String, nullable=False)
    agency_lang = Column(String)
    agency_phone = Column(String)
    agency_fare_url = Column(String)

Index('%s_ix1' %(Agency.__tablename__), Agency.agency_id)
