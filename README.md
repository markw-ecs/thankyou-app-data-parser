# thankyou-app-data-parser

A simple app that will print out the league participant and lottery participants for the specified month (Leauge participants are printed with their number of thank yous)

To change the month update the MONTH_KEY field in the script using the format YYYY-MM - For example to view results for thank yous in may 2021 use '2021-05'

The script expects a dump of the data to be in file /tmp/thankyou-data, this can be achieve by running the aws command (with credentials set up):

	aws dynamodb scan --table-name thankyou-engcs-prod > /tmp/thankyou-data	

TODO: Make filename and Month command line parameters
