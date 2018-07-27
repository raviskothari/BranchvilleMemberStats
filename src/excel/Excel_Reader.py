import os
import sys
import xlrd


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
