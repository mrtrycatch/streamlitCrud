import pyodbc

server = 'seuservidor' 
database = 'seubancodedados' 
username = 'usuario' 
password = 'senha' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()