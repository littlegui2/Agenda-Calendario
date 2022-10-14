from calendar import HTMLCalendar


class Calendario(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendario, self).__init__()
    
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ""
        for event in events_per_day:
            d += f"<li> {event.get_html_url} </li>"
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return "<td></td>"

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f"<tr> {week} </tr>"