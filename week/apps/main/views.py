import datetime

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return render(request, 'index.html', {})


def get_week_number(input_date: datetime, start_date: datetime) -> int:
    # The start of the week of the specified date
    start_week = start_date - datetime.timedelta(days=start_date.weekday())

    if start_date == input_date:
        return 1

    # Let's find the difference between the input date and the start date of the first week
    day_diff = (input_date - start_week).days + 1

    # Find the number of complete weeks
    count_week = day_diff // 7

    # Let's check if there is an incomplete week
    if day_diff % 7 > 0:
        count_week += 1

    # By convention, Sunday is the start of the week
    if input_date.weekday() == 6:
        count_week += 1

    return count_week


class WeekView(APIView):

    def get(self, request):
        # Passed date in parameters
        input_date = self.request.query_params.get('date')
        # Convert to date format
        try:
            input_date = datetime.date.fromisoformat(input_date)
        except Exception as e:
            return Response({
                "status": "error",
                "msg": "Неверный формат даты"
            })

        # Start date according to the conditions of the task
        start_date = datetime.date(2019, 1, 1)

        if start_date > input_date:
            return Response({
                "status": "error",
                "msg": f"Отсчет недель начинается с {start_date}"
            })

        week_number = get_week_number(input_date=input_date, start_date=start_date)

        return Response({
            "status": "success",
            "week_number": week_number,
        })
