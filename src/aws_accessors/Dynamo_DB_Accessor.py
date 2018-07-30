from src.ambulance_data.Ambulance_Crew_Analysis import AmbulanceCrew
from src.engine_data.Engine_Crew_Analysis import EngineCrew
from src.utilities.Get_Date import Utils
from src.utilities.Construct_Member import ConstructMember

import boto3

ambulance_crew = AmbulanceCrew()
engine_crew = EngineCrew()
utils = Utils()
construct_member = ConstructMember()


DYNAMODB_TABLE = "BVFCOMemberData"
DYNAMODB_REGION = "us-east-2"


class DynamoDB:
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table("BVFCOMemberData")

    @staticmethod
    def put_member_in_dynamo(path_of_file1, path_of_file2):
        list_of_engine_members = construct_member.construct_list_of_members(path_of_file1, path_of_file2)
        header_month_ambulance = "Ambulance Calls For " + utils.get_current_month_mapped()
        header_year_ambulance = "Ambulance Calls For " + utils.get_current_year()
        header_month_engine = "Engine Calls For " + utils.get_current_month_mapped()
        header_year_engine = "Engine Calls For " + utils.get_current_year()
        header_compensation = "Compensation For " + utils.get_current_month_mapped()

        for member in list_of_engine_members:
            DynamoDB.table.put_item(
                Item={
                    "MemberName": member.get_member_name(),
                    header_month_ambulance: member.get_ambulance_month_total(),
                    header_year_ambulance: member.get_ambulance_year_total(),
                    header_month_engine: member.get_engine_month_total(),
                    header_year_engine: member.get_engine_year_total(),
                    header_compensation: member.get_member_compensation()
                }
            )
