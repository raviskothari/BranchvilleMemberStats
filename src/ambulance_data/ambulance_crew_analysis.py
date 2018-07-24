from src.ambulance_data.ambulance_drivers_analysis import AmbulanceDriver
from src.ambulance_data.ambulance_aide_analysis import AmbulanceAide

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
