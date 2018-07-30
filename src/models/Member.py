class Member:

    def __init__(self):
        self.member_name = None
        self.ambulance_year_call_total = None
        self.ambulance_month_call_total = None
        self.engine_year_call_total = None
        self.engine_month_call_total = None
        self.member_compensation = None

    def get_member_name(self):
        return self.member_name

    def set_member_name(self, member_name):
        self.member_name = member_name

    def get_ambulance_month_total(self):
        return self.ambulance_month_call_total

    def set_ambulance_month_call_total(self, month_call_total):
        if month_call_total is None:
            self.ambulance_month_call_total = 0
            return
        self.ambulance_month_call_total = month_call_total

    def get_ambulance_year_total(self):
        return self.ambulance_year_call_total

    def set_ambulance_year_call_total(self, year_call_total):
        if year_call_total is None:
            self.ambulance_year_call_total = 0
            return
        self.ambulance_year_call_total = year_call_total

    def get_engine_month_total(self):
        return self.engine_month_call_total

    def set_engine_month_call_total(self, month_call_total):
        if month_call_total is None:
            self.engine_month_call_total = 0
            return
        self.engine_month_call_total = month_call_total

    def get_engine_year_total(self):
        return self.engine_year_call_total

    def set_engine_year_call_total(self, year_call_total):
        if year_call_total is None:
            self.engine_year_call_total = 0
            return
        self.engine_year_call_total = year_call_total

    def get_member_compensation(self):
        return "$" + str(self.member_compensation)

    def set_member_compensation(self, member_compensation):
        if member_compensation is None:
            self.member_compensation = 0
            return
        self.member_compensation = member_compensation
