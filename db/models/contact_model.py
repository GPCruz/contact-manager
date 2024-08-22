from sqlalchemy import Column, DateTime, Float, Integer, Interval, String, Text

from db.abstractions.base import Base



class Contact(Base):
    __tablename__ = 'contacts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Campos Customizados -------------------------------------    
    # name = Column(String, nullable=False)
    # email = Column(String, nullable=False, unique=True)
    # phone = Column(String, nullable=True)
    # address = Column(String, nullable=True)
    # contact_type = Column(String, nullable=False)
    
    call_type = Column(String, nullable=True) # Callback, followup, first contact
    call_frequency = Column(Interval, nullable=True) # Time delta
    notes = Column(Text, nullable=True)	
    last_call_date = Column(DateTime, nullable=True)
    
    
    # Campos carregados ---------------------------------------    
    prj_status = Column(String, nullable=True) 	# Analisar relevância
    const_type = Column(String, nullable=True) 	# Importante: contact_type
    site_area = Column(String, nullable=True) 	# Analisar relevância
    # site_state = Column(String, nullable=True)
    # site_cnty = Column(String, nullable=True)
    # site_juris = Column(String, nullable=True)
    # site_city = Column(String, nullable=True)
    # site_zip = Column(String, nullable=True)
    
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
    
    # Campos ignoráveis ---------------------------------------    
	# dsgr_type = Column(String, nullable=True)
    # dsgr_cmpny = Column(String, nullable=True)
    # dsgr_cotel = Column(String, nullable=True)
    # dsgr_fax = Column(String, nullable=True)
    # dsgr_first = Column(String, nullable=True)
    # dsgr_last = Column(String, nullable=True)
    # dsgr_pvtel = Column(String, nullable=True)
    # dsgr_st = Column(String, nullable=True)
    # dsgr_pobox = Column(String, nullable=True)
    # dsgr_city = Column(String, nullable=True)
    # dsgr_state = Column(String, nullable=True)
    # dsgr_zip = Column(String, nullable=True)
    # dsgr_email = Column(String, nullable=True)
    # dsgr_web = Column(String, nullable=True)
    
    # solar_powersize = Column(Float, nullable=True)
    # solar_powerunit = Column(String, nullable=True)
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    
# from datetime import timedelta, datetime

# # Exemplo de como adicionar um novo contato com os novos campos
# novo_contato = Contact(
#     name="João Silva",
#     email="joao.silva@example.com",
#     phone="123456789",
#     address="Rua Exemplo, 123",
#     contact_type="personal",
#     call_type="follow up",
#     call_frequency=timedelta(days=13),  # Frequência de 13 dias
#     notes="Esta é uma anotação longa sobre o contato.",
#     last_call_date=datetime.now()  # Data da última ligação
# )
# session.add(novo_contato)
# session.commit()