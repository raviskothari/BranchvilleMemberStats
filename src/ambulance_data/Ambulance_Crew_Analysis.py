from src.ambulance_data.Ambulance_Drivers_Analysis import AmbulanceDriver
from src.ambulance_data.Ambulance_Aide_Analysis import AmbulanceAide
from src.excel.Excel_Reader import ExcelProcessor

excelProcessor = ExcelProcessor()
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

    @staticmethod
    def calculate_ambulance_compensation(path_of_file):
        sheet = excelProcessor.open_sheet(path_of_file)
        last_index = excelProcessor.get_curr_month_range(sheet)
        driver_aide_compensation = {}
        for i in range(sheet.ncols):
            if sheet.cell_value(0, i) == "Transport":
                list_of_drivers = sheet.col_values(11)
                list_of_aides = sheet.col_values(12)
                list_of_transport_values = sheet.col_values(i)
                j = 0
                while j in range(list_of_transport_values.__len__()) and last_index != 0:
                    last_index -= 1
                    if list_of_transport_values[j] == "Transport":
                        j += 1
                        continue
                    elif list_of_transport_values[j] == "Yes":
                        if list_of_drivers[j] in driver_aide_compensation:
                            driver_aide_compensation[list_of_drivers[j]] += 10
                        else:
                            driver_aide_compensation[list_of_drivers[j]] = 10
                        if list_of_aides[j] in driver_aide_compensation:
                            driver_aide_compensation[list_of_aides[j]] += 10
                        else:
                            driver_aide_compensation[list_of_aides[j]] = 10
                    elif list_of_transport_values[j] == "No":
                        if list_of_drivers[j] in driver_aide_compensation:
                            driver_aide_compensation[list_of_drivers[j]] += 5
                        else:
                            driver_aide_compensation[list_of_drivers[j]] = 5
                        if list_of_aides[j] in driver_aide_compensation:
                            driver_aide_compensation[list_of_aides[j]] += 5
                        else:
                            driver_aide_compensation[list_of_aides[j]] = 5
                    j += 1

        array_of_compensation_sorted = [(k, driver_aide_compensation[k])
                                        for k in sorted(driver_aide_compensation, key=driver_aide_compensation.get,
                                                        reverse=True)]
        driver_aide_compensation_sorted = {}
        for k, v in array_of_compensation_sorted:
            driver_aide_compensation_sorted[k] = v

        return driver_aide_compensation_sorted
