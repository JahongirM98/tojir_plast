from datetime import timedelta
from django.utils import timezone


def weather_context(request):
    today = timezone.localdate()
    days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    week = []
    for i in range(7):
        day = today + timedelta(days=i)
        week.append({
            'label': f"{days[day.weekday()]}, {day.day} {day.strftime('%b')}",
            'day_temp': 25 + i,
            'night_temp': 15 - i,
            'day_icon': 'bi-cloud-sun',
            'night_icon': 'bi-moon-stars'
        })
    return {'weather_week': week}
