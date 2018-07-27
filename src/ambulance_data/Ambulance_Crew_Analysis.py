from src.ambulance_data.Ambulance_Drivers_Analysis import AmbulanceDriver
from src.ambulance_data.Ambulance_Aide_Analysis import AmbulanceAide
from src.models.Member import Member

aide = AmbulanceAide()
driver = AmbulanceDriver()


class AmbulanceCrew:
    @staticmethod
    def get_aide_driver_totals_for_current_month(path_of_file):
        driver_aide_sorted = {}
        driver_count_curr_month = driver.get_driver_count_curr_month(path_of_file)
        aide_count_curr_month = aide.get_aides_count_curr_month(path_of_file)

        driver_aide_unsorted = {k: driver_count_curr_month.get(k, 0) + aide_count_curr_month.get(k, 0)
                                for k in set(driver_count_curr_month) | set(aide_count_curr_month)}
        array_of_driver_aide_sorted = [(k, driver_aide_unsorted[k])
                                       for k in sorted(driver_aide_unsorted, key=driver_aide_unsorted.get,
                                                       reverse=True)]
        for k, v in array_of_driver_aide_sorted:
            driver_aide_sorted[k] = v

        return driver_aide_sorted

    @staticmethod
    def get_aide_driver_totals_for_year(path_of_file):
        driver_aide_sorted = {}
        driver_count_year = driver.get_driver_count_year(path_of_file)
        aide_count_year = aide.get_aide_count_year(path_of_file)

        driver_aide_unsorted = {k: driver_count_year.get(k, 0) + aide_count_year.get(k, 0)
                                for k in set(driver_count_year) | set(aide_count_year)}
        array_of_driver_aide_sorted = [(k, driver_aide_unsorted[k])
                                       for k in sorted(driver_aide_unsorted, key=driver_aide_unsorted.get,
                                                       reverse=True)]
        for k, v in array_of_driver_aide_sorted:
            driver_aide_sorted[k] = v

        return driver_aide_sorted

    def construct__list_of_members(self, path_of_file):
        driver_aide_month_sorted = self.get_aide_driver_totals_for_current_month(path_of_file)
        driver_aide_year_sorted = self.get_aide_driver_totals_for_year(path_of_file)

        list_of_members = []
        for k, v in driver_aide_month_sorted.items():
            member = Member()
            member.set_member_name(k)
            member.set_month_call_total(v)
            year_total = driver_aide_year_sorted.get(k)
            member.set_year_call_total(year_total)
            list_of_members.append(member)

        return list_of_members
