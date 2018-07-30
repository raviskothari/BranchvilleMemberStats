from src.excel.Excel_Reader import ExcelProcessor
from src.utilities.Get_Date import Utils

excelProcessor = ExcelProcessor()
utils = Utils()


class EngineOIC:
    @staticmethod
    def get_oic_count_in_specified_range(sheet, end_index):
        oic_unsorted = {}
        for i in range(sheet.ncols):
            if sheet.cell_value(0, i) == "Officer":
                list_of_oic_full = sheet.col_values(i)
                list_of_oic = list_of_oic_full[:end_index]
                for j in range(list_of_oic.__len__()):
                    if list_of_oic[j] == "Officer":
                        continue
                    elif not list_of_oic[j] in oic_unsorted:
                        oic_unsorted[list_of_oic[j]] = 1
                    else:
                        oic_unsorted[list_of_oic[j]] += 1

        array_of_oic_sorted = [(k, oic_unsorted[k])
                               for k in sorted(oic_unsorted, key=oic_unsorted.get,
                                               reverse=True)]
        oics_sorted = {}
        for k, v in array_of_oic_sorted:
            oics_sorted[k] = v

        return oics_sorted

    def get_oic_count_curr_month(self, path_of_file):
        sheet = excelProcessor.open_sheet(path_of_file)
        last_index  = excelProcessor.get_curr_month_range(sheet)
        return self.get_oic_count_in_specified_range(sheet, last_index)

    def get_oic_count_year(self, path_of_file):
        sheet = excelProcessor.open_sheet(path_of_file)
        return self.get_oic_count_in_specified_range(sheet, sheet.nrows)
