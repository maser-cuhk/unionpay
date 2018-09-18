import requests
import json
import datetime

url='https://www.unionpayintl.com/cardholderServ/serviceCenter/rate/search'
data =  {'curDate':'', 'baseCurrency': 'HKD', 'transactionCurrency': 'EUR'}

upToDate=True
startDateObj=datetime.datetime.strptime('2018-09-01', '%Y-%m-%d')
endDateObj=datetime.datetime.strptime('2018-09-15','%Y-%m-%d')
history=""

if upToDate:
	endDateObj=datetime.datetime.now()

while (startDateObj<=endDateObj):
	startDateStr=startDateObj.strftime('%Y-%m-%d')
	data['curDate']=startDateStr
	response = requests.post(url, data=data)
	if (len(response.content)!=0):
		exchangeRate=json.loads(response.content)
		exchangeRate=str(exchangeRate['exchangeRate'])
		print (startDateStr+"\t"+exchangeRate)
		history=exchangeRate
	else:
		print (startDateStr+"\t"+history)
	startDateObj=startDateObj+datetime.timedelta(days=1)


