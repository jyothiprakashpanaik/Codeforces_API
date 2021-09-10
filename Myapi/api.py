import time
import requests
from datetime import datetime,timezone

def timeStamp(Time):
	Time = Time.replace(' ','').replace('(UTC)','')
	time_stamp = datetime.strptime(Time, "%Y-%m-%d|%H:%M:%S")
	time_stamp1 = time_stamp.replace(tzinfo=timezone.utc).timestamp()
	return time_stamp1

def get_data(S,T1,T2,N,ProblemList):
	params = {'handle':S}
	cf_api =  requests.get('https://codeforces.com/api/user.status',params=params)
	time_stamp1 = timeStamp(T1)
	time_stamp2 = timeStamp(T2)
	contestId = int(ProblemList[0][:-1])
	js = cf_api.json()

	result = dict([])

	for dt in js['result']:
		if(dt.get('contestId',-1)==contestId and dt['author']['participantType']=='VIRTUAL' and dt['creationTimeSeconds']<=time_stamp2):
			index = dt['problem']['index']
			submit_time = dt['creationTimeSeconds'] - time_stamp1
			result[index] = result.get(index,{'penalty':None,'wrongSubmission':None})
			if(dt['verdict']=='OK'):
				if(result[index]['wrongSubmission']==None):
					result[index]['wrongSubmission'] = -1
				result[index]['penalty'] = submit_time
				result[index]['wrongSubmission'] += 1
			else:
				if(result[index]['wrongSubmission']==None):
					result[index]['wrongSubmission'] = 0
				else:
					result[index]['wrongSubmission'] += 1
	
	final = list([])
	for ind,dit in list(result.items())[::-1]:
		localDict = {}
		localDict['index'] = str(contestId)+ind
		localDict['penalty'] = dit['penalty']
		localDict['wrongSubmission'] = dit['wrongSubmission'] if dit['penalty']!=None else None
		final.append(localDict)
	return final

def main():
	S = input('Enter the usre name: ')
	T1 = input('Enter the time1: ')
	T2 = input('Enter the time2: ')
	N = int(input('Enter the cnt of problems: '))
	ProblemList = input('Enter the list:\n').split(',')

	result = get_data(S,T1,T2,N,ProblemList)

	for i in result:
		print(i,result[i])

if __name__ == '__main__':
	main()
