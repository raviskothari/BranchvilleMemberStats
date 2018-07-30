from src.ambulance_data.Ambulance_Crew_Analysis import AmbulanceCrew
from src.engine_data.Engine_OIC_Analysis import EngineOIC
from src.engine_data.Engine_Drivers_Analysis import EngineDriver
from src.excel.Excel_Reader import ExcelProcessor

excelProcessor = ExcelProcessor()
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

    @staticmethod
    def calculate_engine_compensation(path_of_file):
        sheet = excelProcessor.open_sheet(path_of_file)
        last_index = excelProcessor.get_curr_month_range(sheet)
        driver_oic_compensation = {}
        for i in range(sheet.ncols):
            if sheet.cell_value(0, i) == "Driver":
                list_of_drivers = sheet.col_values(i)
                list_of_oic = sheet.col_values(10)
                j = 0
                while j in range(list_of_drivers.__len__()) and last_index != 0:
                    last_index -= 1
                    if list_of_drivers[j] == "Driver":
                        j += 1
                        continue
                    if list_of_drivers[j] in driver_oic_compensation:
                        driver_oic_compensation[list_of_drivers[j]] += 5
                    else:
                        driver_oic_compensation[list_of_drivers[j]] = 5
                    if list_of_oic[j] in driver_oic_compensation:
                        driver_oic_compensation[list_of_oic[j]] += 5
                    else:
                        driver_oic_compensation[list_of_oic[j]] = 5
                    j += 1
        array_of_compensation_sorted = [(k, driver_oic_compensation[k])
                                        for k in sorted(driver_oic_compensation, key=driver_oic_compensation.get,
                                                        reverse=True)]
        driver_oic_compensation_sorted = {}
        for k, v in array_of_compensation_sorted:
            driver_oic_compensation_sorted[k] = v

        return driver_oic_compensation_sorted
