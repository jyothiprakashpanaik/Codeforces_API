
import time
import test
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

	result = dict()

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
					
	final = dict()
	for i in result:
		final[str(contestId)+i] = {'penalty':result[i]['penalty'],'wrongSubmission':result[i]['wrongSubmission'] if result[i]['penalty']!=None else None }		 
	return final

def main():
	for _ in range(2):
		S = test.S[_]
		T1 = test.T1[_]
		T2 = test.T2[_]
		N = test.N[_]
		ProblemList = test.ProblemList[_]
		sol = get_data(S,T1,T2,N,ProblemList)
		for i in sol:
			print(i,sol[i])
		print()

if __name__ == '__main__':
	main()