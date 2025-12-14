import os
from dotenv import load_dotenv
load_dotenv()

ORACLE_USER = os.getenv("ORACLE_USER", "TU_USUARIO")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD", "TU_CONTRASEÑA")
ORACLE_DSN = os.getenv("ORACLE_DSN", "localhost/XEPDB1")
USD_TO_CLP = float(os.getenv("USD_TO_CLP", "900.0"))
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
