# Branchville Member Statistics
This project was created to analyze Branchville Volunteer Fire Company's member call records. The backend of the project
was written in Python, and the Excel spreadsheet was stored in Amazon S3. The Excel spreadsheet was pulled from the 
Branchville call report, and contains information including the call's incident number, the station run number, the 
location of the call, the time the unit was dispatched, the time the unit came back to the station, the type of the 
incident, the first due company of where the call was, the unit used, the disposition, whether or not a transport was 
completed, the eMeds report number, the driver, the aide, the 3rd (if applicable), any observers (if applicable), any 
notes written. Due to the possibility of breaking HIPAA laws, the Excel spreadsheet will not be accessible to the 
general public.

In order to automate the processing of the Excel spreadsheet, AWS Lambda will be used. The lambda function will be 
triggered every 30 days, as the Excel spreadsheet will be uploaded to the Amazon S3 bucket every 30 days on the 1st of
the month.

This service can be extended to other fire companies for analysis of their member's data. Also, there is a possibility 
of implementing machine learning algorithms into this service so that station officers can predict how many calls their
members will take, how many hours each member will dedicate, etc. This will be helpful for scheduling purposes, as it 
can help alleviate any burden placed on members that may be dedicating more time than others, or if they are often 
bombarded with several calls on their shifts.
