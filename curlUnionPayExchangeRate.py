import requests
import json
import datetime

url='https://www.unionpayintl.com/cardholderServ/serviceCenter/rate/search'
data =  {'curDate':'2018-09-15', 'baseCurrency': 'HKD', 'transactionCurrency': 'EUR'}

upToDate=True
startDateObj=datetime.datetime.strptime('2018-09-01', '%Y-%m-%d')
endDateObj=datetime.datetime.strptime('2018-08-31','%Y-%m-%d')

if upToDate:
	endDateObj=datetime.datetime.now()

while (startDateObj<=endDateObj):
	startDateStr=startDateObj.strftime('%Y-%m-%d')
	data['curDate']=startDateStr
	response = requests.post(url, data=data)
	exchangeRate=response.content
	exchangeRate=json.dumps(exchangeRate.__dict__)
	print json.loads(exchangeRate)
	#print (exchangeRate['exchangeRate'])
	startDateObj=startDateObj+datetime.timedelta(days=1)


