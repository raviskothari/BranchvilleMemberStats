class Member:

    def __init__(self):
        self.year_call_total = None
        self.month_call_total = None
        self.member_name = None

    def get_member_name(self):
        return self.member_name

    def get_month_total(self):
        return self.month_call_total

    def get_year_total(self):
        return self.year_call_total

    def set_member_name(self, member_name):
        self.member_name = member_name

    def set_month_call_total(self, month_call_total):
        self.month_call_total = month_call_total

    def set_year_call_total(self, year_call_total):
        self.year_call_total = year_call_total
