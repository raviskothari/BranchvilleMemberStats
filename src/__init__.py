from src.ambulance_data.Ambulance_Aide_Analysis import AmbulanceAide
from src.ambulance_data.Ambulance_Drivers_Analysis import AmbulanceDriver
from src.ambulance_data.Ambulance_Crew_Analysis import AmbulanceCrew
from src.aws_accessors.S3_Accessor import S3
from src.aws_accessors.Dynamo_DB_Accessor import DynamoDB
from src.excel.Excel_Reader import ExcelProcessor
from src.utilities.Get_Date import Utils

aide = AmbulanceAide()
driver = AmbulanceDriver()
crew = AmbulanceCrew()
s3 = S3()
dynamoDB = DynamoDB()
excelProcessor = ExcelProcessor()
utils = Utils()

path_of_excel_spreadsheet = "/Users/RaviKothari/PycharmProjects/BranchvilleAmbulanceStats/src/" \
                            "BranchvilleStatsLocal.xls"
s3.download_from_s3("MySpreadsheet.xls", "BranchvilleStatsLocal.xls")

# excelProcessor.export_to_txt(driver.get_driver_count_curr_month(path_of_excel_spreadsheet),
#                              "Driver's Counts for July 2018")
# excelProcessor.export_to_txt(aide.get_aides_count_curr_month(path_of_excel_spreadsheet),
#                              "Aide's Counts for July 2018")
#
# excelProcessor.export_to_txt(driver.get_driver_count_year(path_of_excel_spreadsheet),
#                              "Driver's Count for 2018")
# excelProcessor.export_to_txt(aide.get_aide_count_year(path_of_excel_spreadsheet),
#                              "Aide 2018")
#
# excelProcessor.export_to_txt(crew.get_aide_driver_totals_for_current_month(path_of_excel_spreadsheet),
#                              "Driver + Aide Count for July 2018")
# excelProcessor.export_to_txt(crew.get_aide_driver_totals_for_year(path_of_excel_spreadsheet),
#                              "Driver + Aide Count for 2018")

dynamoDB.put_member_in_dynamo(path_of_excel_spreadsheet)
# dynamoDB.put_member_in_dynamo_year(path_of_excel_spreadsheet)


# TODO Make a member object that has a key of the member's name, and two attributes (the current month's call and the
# TODO year call total
