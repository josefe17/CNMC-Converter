import pandas
import numpy

df = pandas.read_csv('consumo_periodo_22-12-2020_13-01-2021.csv',
            sep=' |;|:',
            header=0,
            parse_dates=['Fecha'],
            dayfirst=True,
            decimal=',',
            names=['CUPS', 'Fecha', 'Hora', 'Minutos', 'DST', 'Consumo_kWh', 'Metodo_obtencion', 'crap1', 'crap2', 'crap3'])


df['Consumo_kWh']=df['Consumo_kWh']/1000
df['Metodo_obtencion']='R'
df['Fecha']=numpy.where(df['Hora']==0, df['Fecha'] - pandas.to_timedelta(1, unit='d'), df['Fecha'])
df['Hora']=numpy.where(df['Hora']==0, 24, df['Hora'])

print(df)

df.to_csv('salida.csv',
   sep=';',
   decimal=',',
   date_format='%d/%m/%Y',
   index=False,
   columns=['CUPS', 'Fecha', 'Hora', 'Consumo_kWh', 'Metodo_obtencion'])