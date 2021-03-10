import datetime
import pytz

now = datetime.datetime.now(tz=pytz.timezone("Asia/Yekaterinburg"))

print(now.strftime("%Y-%m-%d %H-%M-%S +05"))

