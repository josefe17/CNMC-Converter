import pandas
import numpy
import sys

filename = sys.argv[1]
df = pandas.read_csv(filename,
            engine='python',
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

outname = str(sys.argv[1]).split('.')[0]+ '_CNMC_formatted.' + str(sys.argv[1]).split('.')[1]

df.to_csv(outname,
   sep=';',
   decimal=',',
   date_format='%d/%m/%Y',
   index=False,
   columns=['CUPS', 'Fecha', 'Hora', 'Consumo_kWh', 'Metodo_obtencion'])