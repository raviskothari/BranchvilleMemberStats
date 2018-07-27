from src.excel.Excel_Reader import ExcelProcessor
from src.utilities.Get_Date import Utils

excelProcessor = ExcelProcessor()
utils = Utils()


class AmbulanceDriver:
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
        last_index = 1
        for i in range(sheet.ncols):
            if sheet.cell_value(0, i) == "Incident Number":
                list_of_invoice_numbers = sheet.col_values(i)
                for j in range(list_of_invoice_numbers.__len__()):
                    if list_of_invoice_numbers[j] == "Incident Number":
                        continue
                    month_from_invoice_number_full = list_of_invoice_numbers[j]
                    month_from_invoice_number = int(month_from_invoice_number_full[2:4])
                    if month_from_invoice_number == utils.get_current_month_numerical():
                        last_index = j
        last_index += 1
        return self.get_drivers_count_in_specified_range(sheet, last_index)

    def get_driver_count_year(self, path_of_file):
        sheet = excelProcessor.open_sheet(path_of_file)
        return self.get_drivers_count_in_specified_range(sheet, sheet.nrows)
