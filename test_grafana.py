import sqlalchemy
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base

file = pd.read_csv('donnee_temp/depense_age.csv',dtype={
    'annee':'float64'
    ,'patho_niv1':'category'
    ,'patho_niv2':'category'
    ,'patho_niv3':'category'
    ,'top':'category'
    ,'dep_niv_1':'category'
    ,'dep_niv_2':'category'
    ,'montant':'float64'
    ,'nombre de patients traités pour la pathologie selectionnée':'float64'
    ,'nombre de patient traités pour une autre pathologie mais necessitant des soins du poste':'float64'
    ,'montant_moy':'float64'
    ,'type_somme':'category'
    ,'sexe':'float64'
    ,'cla_age_5':'category'
    ,'Ntop':'float64'
    ,'Ntop_total':'float64'
    ,'pourcentage acte selon la classe d\'age':'float64'
    ,'nombre de patients traités pour la pathologie selectionnée par classe d\'age':'float64'
    ,'nombre de patient traités pour une autre pathologie mais necessitant des soins du poste par classe d\'age':'float64'
    ,'montant par classe d\'age':'float64'
    ,'pop':'float64'})

hostname= "127.0.0.1:3306"
database= "mydatabase"
username= "root"
password= "password"

engine = sqlalchemy.create_engine("mariadb+mariadbconnector://{user}:{pw}@{host}/{db}".format(host=hostname, db=database, user=username, pw=password))

# boucler sur le dataframe :
file.to_sql('data_ameli', engine, if_exists='replace', index=False,chunksize=1000)
