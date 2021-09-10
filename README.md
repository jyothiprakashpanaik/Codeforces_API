# CodeForces Api 🤓


---
*Run*
```
python manage.py run server
```

Go to 💻 this link 
```
http://127.0.0.1:8000/
```
params:

| Pram      | Def                                                |  
| --------- |:--------------------------------------------------:| 
| usename   | codeforces Handle                                  |
| from      | Staring of Contest Time [YYYY-MM-DD|HH:MM:SS]      | 
| to        | Ending of Contest Time  [YYYY-MM-DD|HH:MM:SS]      | 
|cnt	      | No of Problems                                     |
|list       | Probem id                                          |


```
http://127.0.0.1:8000/get_json?username=xxx&from=YYYY-MM-DD|HH:MM:SS&to=YYYY-MM-DD|HH:MM:SS&cnt=n&list=xxA,xxB..
```
![alt text](https://github.com/jyothiprakashpanaik/codechef_api/blob/8b541ef736e599ecb360e4681b5eef94c2a1cd17/Screenshot%202021-09-05%20213220.png "Request Pic")