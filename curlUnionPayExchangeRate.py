import requests
import json
import datetime

url='https://www.unionpayintl.com/cardholderServ/serviceCenter/rate/search'
data =  {'curDate':'', 'baseCurrency': 'HKD', 'transactionCurrency': 'EUR'}

upToDate=True
startDateObj=datetime.datetime.strptime('2018-09-17', '%Y-%m-%d')
endDateObj=datetime.datetime.strptime('2018-09-15','%Y-%m-%d')

if upToDate:
	endDateObj=datetime.datetime.now()

while (startDateObj<=endDateObj):
	startDateStr=startDateObj.strftime('%Y-%m-%d')
	data['curDate']=startDateStr
	#print startDateStr
	response = requests.post(url, data=data)
	#exchangeRate=response.content
	#exchangeRate=json.dumps(exchangeRate.__dict__)
	exchangeRate=json.loads(response.content)
	print (startDateStr+" "+str(exchangeRate['exchangeRate']))
	startDateObj=startDateObj+datetime.timedelta(days=1)


