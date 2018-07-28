from src.ambulance_data.Ambulance_Crew_Analysis import AmbulanceCrew
from src.engine_data.Engine_Crew_Analysis import EngineCrew
from src.models.Member import Member

ambulance_crew = AmbulanceCrew()
engine_crew = EngineCrew()


class ConstructMember:

    @staticmethod
    def construct_list_of_members(path_of_file1, path_of_file2):
        driver_aide_month_sorted = ambulance_crew.get_aide_driver_totals_for_current_month(path_of_file1)
        driver_aide_year_sorted = ambulance_crew.get_aide_driver_totals_for_year(path_of_file1)
        driver_oic_month_sorted = engine_crew.get_oic_driver_totals_for_current_month(path_of_file2)
        driver_oic_year_sorted = engine_crew.get_oic_driver_totals_for_year(path_of_file2)

        list_of_members_to_create = []
        for k in driver_aide_year_sorted.items():
            if list_of_members_to_create.__contains__(k):
                continue
            else:
                list_of_members_to_create.append(k)

        for k in driver_oic_year_sorted.items():
            if list_of_members_to_create.__contains__(k):
                continue
            else:
                list_of_members_to_create.append(k)

        list_of_members = []
        for k, v in list_of_members_to_create:
            member = Member()
            member.set_member_name(k)
            member.set_engine_month_call_total(driver_oic_month_sorted.get(k))
            year_total = driver_oic_year_sorted.get(k)
            member.set_engine_year_call_total(year_total)
            member.set_ambulance_month_call_total(driver_aide_month_sorted.get(k))
            member.set_ambulance_year_call_total(driver_aide_year_sorted.get(k))
            list_of_members.append(member)

        return list_of_members
