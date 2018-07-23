import xlrd
import boto3
import boto

num_calls_per_driver_unsorted = {}
num_calls_per_driver_sorted = {}
num_calls_per_aide_unsorted = {}
num_calls_per_aide_sorted = {}
num_calls_per_person_sorted = {}


def open_sheet():
    loc = "/Users/RaviKothari/PycharmProjects/BranchvilleAmbulanceStats/MySpreadsheet.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    return sheet


def get_driver_count_year():
    sheet = open_sheet()
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


def get_aide_count_year():
    sheet = open_sheet()
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


print(get_driver_count_year())
print(get_aide_count_year())
print(get_total_calls_drivers_aides())
