from sqlalchemy import create_engine, __version__, MetaData, Table, Column, Integer, String

print(__version__)

# Usa url più esplicito e aggiungendo il driver mysqldb
engine = create_engine("mysql+mysqldb://root:root@localhost/italy")

# Verifica che la connessione funzioni
try:
    connection = engine.connect()
    print("Connessione riuscita!")
    connection.close()
except Exception as e:
    print(f"Errore di connessione: {e}")

metadata_obj = MetaData()

province = Table(
    "provincia",
    metadata_obj,
    Column("sigla", String(2), primary_key=True),
    Column("nome", String(50), nullable=False),
    Column("popolazione", Integer, nullable=False),
)

# Crea la tabella
try:
    metadata_obj.create_all(engine)
    print("Tabella creata con successo!")
except Exception as e:
    print(f"Errore nella creazione della tabella: {e}")