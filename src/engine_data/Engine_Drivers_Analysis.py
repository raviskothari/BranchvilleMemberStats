from src.excel.Excel_Reader import ExcelProcessor
from src.utilities.Get_Date import Utils

excelProcessor = ExcelProcessor()
utils = Utils()


class EngineDriver:
    @staticmethod
    def get_drivers_count_in_specified_range(sheet, end_index):
        drivers_unsorted = {}
        for i in range(sheet.ncols):
            if sheet.cell_value(0, i) == "Driver":
                list_of_drivers_full = sheet.col_values(i)
                list_of_drivers = list_of_drivers_full[:end_index]
                for j in range(list_of_drivers.__len__()):
                    if list_of_drivers[j] == "Driver":
                        continue
                    elif not list_of_drivers[j] in drivers_unsorted:
                        drivers_unsorted[list_of_drivers[j]] = 1
                    else:
                        drivers_unsorted[list_of_drivers[j]] += 1

        array_of_drivers_sorted = [(k, drivers_unsorted[k])
                                   for k in sorted(drivers_unsorted, key=drivers_unsorted.get,
                                                   reverse=True)]
        drivers_sorted = {}
        for k, v in array_of_drivers_sorted:
            drivers_sorted[k] = v

        return drivers_sorted

    def get_driver_count_curr_month(self, path_of_file):
        sheet = excelProcessor.open_sheet(path_of_file)
        last_index = excelProcessor.get_curr_month_range(sheet)
        return self.get_drivers_count_in_specified_range(sheet, last_index)

    def get_driver_count_year(self, path_of_file):
        sheet = excelProcessor.open_sheet(path_of_file)
        return self.get_drivers_count_in_specified_range(sheet, sheet.nrows)
