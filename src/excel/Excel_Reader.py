import os
import sys
import xlrd

from src.utilities.Get_Date import Utils

util = Utils()


class ExcelProcessor:
    @staticmethod
    def open_sheet(path_of_file):
        loc = path_of_file
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)
        return sheet

    @staticmethod
    def export_to_txt(dictionary, name_of_dict):
        name_of_file = name_of_dict + ".txt"
        sys.stdout = open(name_of_file, 'w')
        for k, v in dictionary.items():
            print(k, v)

    @staticmethod
    def remove_temp_files(txt_list):
        for t in txt_list:
            os.remove(t)

    @staticmethod
    def get_curr_month_range(sheet):
        last_index = 1
        for i in range(sheet.ncols):
            if sheet.cell_value(0, i) == "Incident Number":
                list_of_incident_numbers = sheet.col_values(i)
                for j in range(list_of_incident_numbers.__len__()):
                    if list_of_incident_numbers[j] == "Incident Number":
                        continue
                    month_from_invoice_number_full = list_of_incident_numbers[j]
                    month_from_invoice_number = int(month_from_invoice_number_full[2:4])
                    if month_from_invoice_number == util.get_current_month_numerical():
                        last_index = j
        last_index += 1
        return last_index
