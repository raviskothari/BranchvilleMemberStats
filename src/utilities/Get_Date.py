from datetime import datetime

map_of_month_to_numerical_value = {
    1: "JANUARY",
    2: "FEBRUARY",
    3: "MARCH",
    4: "APRIL",
    5: "MAY",
    6: "JUNE",
    7: "JULY",
    8: "AUGUST",
    9: "SEPTEMBER",
    10: "OCTOBER",
    11: "NOVEMBER",
    12: "DECEMBER"
}


class Utils:
    @staticmethod
    def get_current_month_numerical():
        return datetime.now().month

    @staticmethod
    def get_current_month_mapped():
        today = datetime.now().month
        return map_of_month_to_numerical_value.get(today)

    @staticmethod
    def get_current_year():
        return str(datetime.now().year)
