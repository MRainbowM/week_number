import datetime

from django.test import TestCase

from .views import get_week_number


class WeekTestCase(TestCase):
    def test_get_week_number(self):
        self.assertEqual(
            get_week_number(
                input_date=datetime.date(2019, 1, 1),
                start_date=datetime.date(2019, 1, 1)
            ),
            1
        )

        self.assertEqual(
            get_week_number(
                input_date=datetime.date(2019, 1, 6),
                start_date=datetime.date(2019, 1, 1)
            ),
            2
        )

        self.assertEqual(
            get_week_number(
                input_date=datetime.date(2019, 3, 1),
                start_date=datetime.date(2019, 1, 1)
            ),
            9
        )
