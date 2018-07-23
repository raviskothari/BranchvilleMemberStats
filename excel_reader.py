import xlrd
import boto3
import botocore
import sys
import os

num_calls_per_driver_unsorted = {}
num_calls_per_driver_sorted = {}
num_calls_per_aide_unsorted = {}
num_calls_per_aide_sorted = {}
num_calls_per_person_sorted = {}

S3_BUCKET_NAME = "branchville-ems-stats"
S3_REGION = "us-east-2"


def download_from_s3(file_to_download, local_file_to_save_as):
    s3 = boto3.resource("s3")
    try:
        s3.Bucket(S3_BUCKET_NAME).download_file(file_to_download, local_file_to_save_as)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            return


def write_file_to_s3(file_path, filename):
    s3 = boto3.client("s3")
    s3.upload_file(file_path, S3_BUCKET_NAME, filename)


def open_sheet(path_of_file):
    loc = path_of_file
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    return sheet


def get_driver_count_year(path_of_file):
    sheet = open_sheet(path_of_file)
    for i in range(sheet.ncols):
        if sheet.cell_value(0, i) == "Driver":
            list_of_drivers = sheet.col_values(i)
            for j in range(list_of_drivers.__len__()):
                if list_of_drivers[j] == "Driver":
                    continue
                elif not list_of_drivers[j] in num_calls_per_driver_unsorted:
                    num_calls_per_driver_unsorted[list_of_drivers[j]] = 1
                else:
                    num_calls_per_driver_unsorted[list_of_drivers[j]] += 1

    array_of_drivers_sorted = [(k, num_calls_per_driver_unsorted[k])
                               for k in sorted(num_calls_per_driver_unsorted, key=num_calls_per_driver_unsorted.get,
                                               reverse=True)]
    for k, v in array_of_drivers_sorted:
        num_calls_per_driver_sorted[k] = v

    return num_calls_per_driver_sorted


def get_aide_count_year(path_of_file):
    sheet = open_sheet(path_of_file)
    for i in range(sheet.ncols):
        if sheet.cell_value(0, i) == "Aide/Officer":
            list_of_aides = sheet.col_values(i)
            for j in range(list_of_aides.__len__()):
                if list_of_aides[j] == "Aide/Officer":
                    continue
                elif not list_of_aides[j] in num_calls_per_aide_unsorted:
                    num_calls_per_aide_unsorted[list_of_aides[j]] = 1
                else:
                    num_calls_per_aide_unsorted[list_of_aides[j]] += 1

    array_of_aides_sorted = [(k, num_calls_per_aide_unsorted[k])
                             for k in sorted(num_calls_per_aide_unsorted, key=num_calls_per_aide_unsorted.get,
                                             reverse=True)]
    for k, v in array_of_aides_sorted:
        num_calls_per_aide_sorted[k] = v

    return num_calls_per_aide_sorted


def get_total_calls_drivers_aides():
    num_calls_per_person_unsorted = {k: num_calls_per_driver_sorted.get(k, 0) + num_calls_per_aide_sorted.get(k, 0)
                                     for k in set(num_calls_per_driver_sorted) | set(num_calls_per_aide_sorted)}
    array_of_people_sorted = [(k, num_calls_per_person_unsorted[k])
                              for k in sorted(num_calls_per_person_unsorted, key=num_calls_per_person_unsorted.get,
                                              reverse=True)]
    for k, v in array_of_people_sorted:
        num_calls_per_person_sorted[k] = v

    return num_calls_per_person_sorted


def export_to_txt(dictionary, name_of_dict):
    name_of_file = name_of_dict + ".txt"
    sys.stdout = open(name_of_file, 'w')
    for k, v in dictionary.items():
        print(k, v)


def remove_temp_files(txt):
    for t in txt:
        os.remove(t)


path_of_excel_spreadsheet = "/Users/RaviKothari/PycharmProjects/BranchvilleAmbulanceStats/BranchvilleStatsLocal.xls"
download_from_s3("MySpreadsheet.xls", "BranchvilleStatsLocal.xls")

export_to_txt(get_driver_count_year(path_of_excel_spreadsheet), "Driver Count 2018")
write_file_to_s3("/Users/RaviKothari/PycharmProjects/BranchvilleAmbulanceStats/Driver Count 2018.txt",
                 "Drivers Count 2018.txt")
export_to_txt(get_aide_count_year(path_of_excel_spreadsheet), "Aide Count 2018")
write_file_to_s3("/Users/RaviKothari/PycharmProjects/BranchvilleAmbulanceStats/Aide Count 2018.txt",
                 "Aide Count 2018.txt")
export_to_txt(get_total_calls_drivers_aides(), "Driver & Aide Count 2018")
write_file_to_s3("/Users/RaviKothari/PycharmProjects/BranchvilleAmbulanceStats/Driver & Aide Count 2018.txt",
                 "Driver & Aide Count 2018.txt")

files_to_remove = ["Driver Count 2018.txt", "Aide Count 2018.txt", "Driver & Aide Count 2018.txt",
                   "BranchvilleStatsLocal.xls"]
remove_temp_files(files_to_remove)
