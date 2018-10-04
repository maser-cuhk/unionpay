import requests
import json
import datetime
import csv

#Server information and post parameter
url='https://www.unionpayintl.com/cardholderServ/serviceCenter/rate/search'
data =  {'curDate':'', 'baseCurrency': '', 'transactionCurrency': ''}

#Post command parameters vlaue
baseCurrency='HKD'
transactionCurrency='EUR'
upToDate=True
startDateObj=datetime.datetime.strptime('2018-10-01', '%Y-%m-%d')
endDateObj=datetime.datetime.strptime('2018-09-15','%Y-%m-%d')

data['baseCurrency']=baseCurrency
data['transactionCurrency']=transactionCurrency
history=''

#Load History Data
with open('HKD-EUR.csv') as historydata:
	reader = csv.reader(historydata, delimiter=',')
	historydatalist=list(reader)

#Find String in list
history_date=[i[0] for i in historydatalist]
#history_date.index('2018-09-01')

#If Statement for uptoDate
if upToDate:
	endDateObj=datetime.datetime.now()

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


