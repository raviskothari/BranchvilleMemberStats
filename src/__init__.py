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

s3.download_from_s3("AmbulanceRuns.xls", "AmbulanceRuns.xls")
s3.download_from_s3("EngineRuns.xls", "EngineRuns.xls")
ambulance_runs = "/Users/RaviKothari/PycharmProjects/BranchvilleAmbulanceStats/src/AmbulanceRuns.xls"
engine_runs = "/Users/RaviKothari/PycharmProjects/BranchvilleAmbulanceStats/src/EngineRuns.xls"

dynamoDB.put_member_in_dynamo(ambulance_runs, engine_runs)
excelProcessor.remove_temp_files({"AmbulanceRuns.xls", "EngineRuns.xls"})
