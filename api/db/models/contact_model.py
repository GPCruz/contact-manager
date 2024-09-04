from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy import Column, DateTime, Float, Integer, Interval, String, Text

from api.db.abstractions.base import Base



class Contact(Base):
    __tablename__ = 'contacts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    call_type = Column(String, nullable=True) # Callback, followup, first contact
    call_frequency = Column(Interval, nullable=True) # Time delta
    notes = Column(Text, nullable=True)	
    last_call_date = Column(DateTime, nullable=True)
    
    
    # Campos carregados ---------------------------------------    
    prj_status = Column(String, nullable=True) 	# Analisar relevância
    const_type = Column(String, nullable=True) 	# Importante: contact_type
    site_area = Column(String, nullable=True) 	# Analisar relevância
    
    site_addrs = Column(String, nullable=True)
    site_coor1 = Column(String, nullable=True)
    site_dir1 = Column(String, nullable=True)
    site_stnam = Column(String, nullable=True)
    site_sttyp = Column(String, nullable=True)
    site_coor2 = Column(String, nullable=True)
    site_dir2 = Column(String, nullable=True)
    site_lot = Column(String, nullable=True)
    site_subd = Column(String, nullable=True)
    site_subno = Column(String, nullable=True)
    site_sidwl = Column(String, nullable=True)
    
    pmt_descrp = Column(String, nullable=True)
    pmt_class = Column(String, nullable=True)
    pmt_sqft = Column(Integer, nullable=True)
    pmt_number = Column(String, nullable=True)
    pmt_date = Column(DateTime, nullable=True)
    pmt_week = Column(String, nullable=True)
    pmt_beg = Column(String, nullable=True)
    pmt_value = Column(Float, nullable=True)
    
    bldr_type = Column(String, nullable=True)
    bldr_cmpny = Column(String, nullable=True)
    bldr_lcse = Column(String, nullable=True)
    bldr_cotel = Column(String, nullable=True)
    bldr_fax = Column(String, nullable=True)
    bldr_first = Column(String, nullable=True)	# Primeiro nome do construtor
    bldr_last = Column(String, nullable=True)	# Sobrenome do construtor
    bldr_pvtel = Column(String, nullable=True)	# Telefone
    bldr_st = Column(String, nullable=True)
    bldr_pobox = Column(String, nullable=True)
    bldr_city = Column(String, nullable=True)
    bldr_state = Column(String, nullable=True)
    bldr_zip = Column(String, nullable=True)
    
    ownr_type = Column(String, nullable=True)
    ownr_cmpny = Column(String, nullable=True)
    ownr_cotel = Column(String, nullable=True)
    ownr_fax = Column(String, nullable=True)
    ownr_first = Column(String, nullable=True)
    ownr_last = Column(String, nullable=True)
    ownr_pvtel = Column(String, nullable=True)
    ownr_st = Column(String, nullable=True)
    ownr_pobox = Column(String, nullable=True)
    ownr_city = Column(String, nullable=True)
    ownr_state = Column(String, nullable=True)
    ownr_zip = Column(String, nullable=True)
    
    pmt_units = Column(Integer, nullable=True) 
    
    bldr_email = Column(String, nullable=True) # email
    bldr_web = Column(String, nullable=True)
    
    permitid = Column(String, nullable=True)
    
    site_lat = Column(Float, nullable=True)
    site_long = Column(Float, nullable=True)
    site_latlong_precision = Column(String, nullable=True)
    site_geocode_date = Column(DateTime, nullable=True)
    
ContactModel = sqlalchemy_to_pydantic(Contact)