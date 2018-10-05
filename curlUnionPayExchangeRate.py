import requests
import json
import datetime
import csv

#Server information and post parameter
url='https://www.unionpayintl.com/cardholderServ/serviceCenter/rate/search'
data =  {'curDate':'', 'baseCurrency': '', 'transactionCurrency': ''}

#Input parameters
data['baseCurrency']= raw_input("Base Currency ( e.g. AUD / CAD / CNY / EUR / GBP / HKD / JPY / MOP / NZD / SGD / THB / USD )\nEnter Base Currency (default:HKD) :").upper() or 'HKD'
data['transactionCurrency']= raw_input("Transaction Currency ( e.g. USD etc )\nEnter Transaction Currency (default:EUR) :" ).upper() or 'EUR'

startDateInput=raw_input("Start Date ( Format:YYYY-MM-DD ) :").upper() or "NOW"
if startDateInput=="NOW":
	startDateObj=datetime.datetime.now()
	endDateObj=datetime.datetime.now()
else:	
	endDateInput=raw_input("End Date ( Format:YYYY-MM-DD ) (default:NOW):").upper() or "NOW"
	if endDateInput=="NOW":
		try:
			startDateObj=datetime.datetime.strptime(startDateInput, '%Y-%m-%d')
		except ValueError as e:
			exit()

		endDateObj=datetime.datetime.now()
	else:
		try:
			startDateObj=datetime.datetime.strptime(startDateInput, '%Y-%m-%d')
			endDateObj=datetime.datetime.strptime(endDateInput, '%Y-%m-%d')
		except ValueError as e:
			exit()

	
history=''

#Load History Data
with open('HKD-EUR.csv') as historydata:
	reader = csv.reader(historydata, delimiter=',')
	historydatalist=list(reader)

#Find String in list
history_date=[i[0] for i in historydatalist]
#history_date.index('2018-09-01')

while (startDateObj<=endDateObj):
	startDateStr=startDateObj.strftime('%Y-%m-%d')
	data['curDate']=startDateStr
	response = requests.post(url, data=data)
	
	if (len(response.content)!=0):
		exchangeRate=json.loads(response.content)
		exchangeRate=str(exchangeRate['exchangeRate'])
		print (startDateStr+" "+exchangeRate)
		history=exchangeRate
	else:
		print (startDateStr+" "+history)
	
	startDateObj=startDateObj+datetime.timedelta(days=1)
