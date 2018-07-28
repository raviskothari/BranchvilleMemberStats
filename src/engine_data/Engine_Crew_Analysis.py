from src.ambulance_data.Ambulance_Crew_Analysis import AmbulanceCrew
from src.engine_data.Engine_OIC_Analysis import EngineOIC
from src.engine_data.Engine_Drivers_Analysis import EngineDriver

oic = EngineOIC()
driver = EngineDriver()
ambulance_crew = AmbulanceCrew()


class EngineCrew:
    @staticmethod
    def get_oic_driver_totals_for_current_month(path_of_file):
        driver_oic_sorted = {}
        driver_count_curr_month = driver.get_driver_count_curr_month(path_of_file)
        oic_count_curr_month = oic.get_oic_count_curr_month(path_of_file)

        driver_oic_unsorted = {k: driver_count_curr_month.get(k, 0) + oic_count_curr_month.get(k, 0)
                               for k in set(driver_count_curr_month) | set(oic_count_curr_month)}
        array_of_driver_oic_sorted = [(k, driver_oic_unsorted[k])
                                      for k in sorted(driver_oic_unsorted, key=driver_oic_unsorted.get,
                                                      reverse=True)]
        for k, v in array_of_driver_oic_sorted:
            driver_oic_sorted[k] = v

        return driver_oic_sorted

    @staticmethod
    def get_oic_driver_totals_for_year(path_of_file):
        driver_oic_sorted = {}
        driver_count_year = driver.get_driver_count_year(path_of_file)
        oic_count_year = oic.get_oic_count_year(path_of_file)

        driver_oic_unsorted = {k: driver_count_year.get(k, 0) + oic_count_year.get(k, 0)
                               for k in set(driver_count_year) | set(oic_count_year)}
        array_of_driver_oic_sorted = [(k, driver_oic_unsorted[k])
                                       for k in sorted(driver_oic_unsorted, key=driver_oic_unsorted.get,
                                                       reverse=True)]
        for k, v in array_of_driver_oic_sorted:
            driver_oic_sorted[k] = v

        return driver_oic_sorted
