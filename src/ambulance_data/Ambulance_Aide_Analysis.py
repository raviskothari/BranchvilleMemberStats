from src.excel.Excel_Reader import ExcelProcessor
from src.utilities.Get_Date import Utils

excelProcessor = ExcelProcessor()
utils = Utils()


class AmbulanceAide:
    @staticmethod
    def get_aide_count_in_specified_range(sheet, end_index):
        aides_unsorted = {}
        for i in range(sheet.ncols):
            if sheet.cell_value(0, i) == "Aide/Officer":
                list_of_aides_full = sheet.col_values(i)
                list_of_aides = list_of_aides_full[:end_index]
                for j in range(list_of_aides.__len__()):
                    if list_of_aides[j] == "Aide/Officer":
                        continue
                    elif not list_of_aides[j] in aides_unsorted:
                        aides_unsorted[list_of_aides[j]] = 1
                    else:
                        aides_unsorted[list_of_aides[j]] += 1

        array_of_aides_sorted = [(k, aides_unsorted[k])
                                 for k in sorted(aides_unsorted, key=aides_unsorted.get,
                                                 reverse=True)]
        aides_sorted = {}
        for k, v in array_of_aides_sorted:
            aides_sorted[k] = v

        return aides_sorted

    def get_aides_count_curr_month(self, path_of_file):
        sheet = excelProcessor.open_sheet(path_of_file)
        last_index = excelProcessor.get_curr_month_range(sheet)
        return self.get_aide_count_in_specified_range(sheet, last_index)

    def get_aide_count_year(self, path_of_file):
        sheet = excelProcessor.open_sheet(path_of_file)
        return self.get_aide_count_in_specified_range(sheet, sheet.nrows)
