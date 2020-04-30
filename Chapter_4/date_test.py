import iso8601
import datetime
from dateutil import tz
from dateutil.zoneinfo import get_zonefile_instance


current_date_utc = datetime.datetime.utcnow()
print(current_date_utc)
print(current_date_utc.tzinfo is None)

current_date_local = datetime.datetime.now()
print(current_date_local)
print(current_date_local.tzinfo is None)

print(tz.gettz("Europe/Paris"))
print(tz.gettz("GMT+1"))

now = datetime.datetime.now()
print(now)
now = now.replace(tzinfo=tz.gettz("Europe/Paris"))
print(now)
print(now.tzinfo)

zones = list(get_zonefile_instance().zones)
print(sorted(zones)[:5])
print(len(zones))

now = datetime.datetime.now()
localzone = tz.gettz()
print(localzone)
print(localzone.tzname(datetime.datetime(2018, 10, 19)))
print(localzone.tzname(datetime.datetime(2018, 11, 19)))


def utcnow():
    return datetime.datetime.now(tz=tz.tzutc())


now = datetime.datetime.utcnow()
print(now.isoformat())
parsed = iso8601.parse_date(now.isoformat())
print(parsed)
print(parsed == now.replace(tzinfo=tz.tzutc()))

localtz = tz.gettz("Europe/Paris")
confusing = datetime.datetime(2017, 10, 29, 2, 30)
print(localtz.is_ambiguous(confusing))
utc = tz.tzutc()
confusing = datetime.datetime(2017, 10, 29, 2, 30, tzinfo=localtz)
print(confusing.replace(fold=0).astimezone(utc))
print(confusing.replace(fold=1).astimezone(utc))