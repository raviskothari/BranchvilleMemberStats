from src.ambulance_data.ambulance_aide_analysis import AmbulanceAide
from src.ambulance_data.ambulance_drivers_analysis import AmbulanceDriver
from src.ambulance_data.ambulance_crew_analysis import AmbulanceCrew
from src.aws_accessors.s3 import S3
from src.excel.excel_reader import ExcelProcessor
from src.utilities.get_date import Utils

aide = AmbulanceAide()
driver = AmbulanceDriver()
crew = AmbulanceCrew()
s3 = S3()
excelProcessor = ExcelProcessor()
utils = Utils()

path_of_excel_spreadsheet = "/Users/RaviKothari/PycharmProjects/BranchvilleAmbulanceStats/src/Temp Files/" \
                            "BranchvilleStatsLocal.xls"
s3.download_from_s3("MySpreadsheet.xls", "BranchvilleStatsLocal.xls")

excelProcessor.export_to_txt(driver.get_driver_count_curr_month(path_of_excel_spreadsheet),
                             "Driver's Counts for July 2018")
excelProcessor.export_to_txt(aide.get_aides_count_curr_month(path_of_excel_spreadsheet),
                             "Aide's Counts for July 2018")

excelProcessor.export_to_txt(driver.get_driver_count_year(path_of_excel_spreadsheet),
                             "Driver's Count for 2018")
excelProcessor.export_to_txt(aide.get_aide_count_year(path_of_excel_spreadsheet),
                             "Aide 2018")

excelProcessor.export_to_txt(crew.get_aide_driver_totals_for_current_month(path_of_excel_spreadsheet),
                             "Driver + Aide Count for July 2018")
excelProcessor.export_to_txt(crew.get_aide_driver_totals_for_year(path_of_excel_spreadsheet),
                             "Driver + Aide Count for 2018")
