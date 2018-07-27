from src.ambulance_data.Ambulance_Crew_Analysis import AmbulanceCrew
from src.utilities.Get_Date import Utils
import boto3

crew = AmbulanceCrew()
utils = Utils()

DYNAMODB_TABLE = "BVFCOMemberData"
DYNAMODB_REGION = "us-east-2"


class DynamoDB:
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table("BVFCOMemberData")

    @staticmethod
    def put_member_in_dynamo(path_of_file):
        list_of_members = crew.construct__list_of_members(path_of_file)
        header_month = "Calls For " + utils.get_current_month_mapped()
        header_year = "Calls For " + utils.get_current_year()
        for member in list_of_members:
            DynamoDB.table.put_item(
                Item={
                    "MemberName": member.get_member_name(),
                    header_month: member.get_month_total(),
                    header_year: member.get_year_total()
                }
            )
