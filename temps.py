from datetime import datetime, date, time, timedelta

maintenant=datetime.now()
print(maintenant)

ma_date=datetime(2025,7,31,16,25,30)
print(ma_date)

print(maintenant.strftime("%d/%m/%Y %H:%M"))

dans_une_semaine=maintenant+timedelta(days=7)
print(dans_une_semaine)

noel=datetime(2025,12,25)
different=noel-maintenant
print(f"jours jusqu'a noel:{different.days}")
#print(noel)
ma_date_exacte =maintenant - datetime(2006,7,31,16,25,30)
print(ma_date_exacte)