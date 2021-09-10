# CodeForces Api 🤓

*Quick Starter ⏳💨*
> **GO TO:** https://codeforces-007.herokuapp.com/
> > ___Fill the form or `/get_json` pass required params.
> > This wil return u a json file.

💡 STOP Wanna Contribute to!! 🛑🛑

---
<br>

# 👩‍💻CodeForces Api



## Directory Tree 
```
├── codeforces_api 
├── Myapi
├── templates
│   ├── index.html
├── Procfile
├── README.md
├── CLIApi.py
├── manage.py
├── requirements.txt
```
## Installation
The Code is written in Python 3.8.5. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```
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

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://twilio-cms-prod.s3.amazonaws.com/images/django-dark.width-808.png" width=170>](https://www.djangoproject.com/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png" width=170>](https://docs.python-requests.org/en/master/) 


## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/jyothiprakashpanaik/Codeforces_API/issues) here by including your search query and the expected result
