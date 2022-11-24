from .models import TimesheetPeriod
import pytz
import datetime


class TimesheetUtil():

    def __init__(self):
        pass

    def get_timesheet_period(self, date, org):
        period = TimesheetPeriod.objects.filter(org=org, date_start__lte=date, date_end__gt=date)
        print("TS date ", str(date))
        if period.count() > 0:
            return period[0]
        else:
            span = org.periodtype.get_start_and_end_date(org.timezone)
            new_period = TimesheetPeriod(id=None, date_start=span['date_start'], date_end=span['date_end'],
                                         org=org)
            new_period.save()
            return new_period

    def get_time_with_timezone(self, naive_date, format, timezone):
        tz = pytz.timezone(timezone)
        return tz.localize(datetime.datetime.strptime(naive_date, format))
