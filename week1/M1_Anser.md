# Week1 Mission

### Q1. 
# 
파이썬으로 할 수 있는 일은 무궁무진하다. 매우 빠른 속도를 요구하거나 하드웨어, 모바일 프로그래밍과 관련된 것이 아니면 프로그래머가 원하는 일 대부분을 파이썬으로 할 수 있다. 예를들면 웹, 수치연산, 데이터베이스, 데이터 분석 프로그래밍 등이 있다.

현재, LHC(Large Hadron Collider)를 이용해 입자들을 가속시키고 충돌시켜 나오는 입자들의 데이터를 분석하는 일을 하고 있다. 복잡하고 빠른 연산을 요구하기 때문에 low level 언어인 c++를 이용해서 데이터 분석을 진행하고 있다. 현재 사용하는 데이터의 크기는 약 100PB인데 이러한 빅데이터 안에서 특정한 입자만 찾기 위해서는 contamination을 제거해 데이터 크기를 줄이고, 좋은 알고리즘을 이용해 signal을 찾아내야 한다. 따라서 Python에서 사용되는 빅데이터를 다루는 스킬과 Machine learnig 알고리즘 등을 배우는 것을 목표로 한다.

------------



### Q2. 
#
+ CPU : Main memory에서 전달되는 명령을 실행하는 부분. 프로그래밍 연산을 담당.
+ Main memory : CPU에 전달할 명령을 저장하는 부분, 휘발성 메모리로 프로그램을 저장함.
+ Second Memory : 운영체제 및 데이터를 저장하는 부분, 비휘발성 메모리로 데이터를 보존할 수 있음.

------------



### Q3. 
#### 1. 
#### 2. 
#### 3. 
#### 4. 
#
The reference code is in [HERE](https://github.com/JinjooSeo/PY4E/blob/main/week1/example/hydro_evo-TestRun.py)

+ 1. Error
    + SyntaxError
     ```Python
     from os import path
     home = path.expanduser("Desktop")
     working_path = path.join(home, "study/PY4E/week1/example")
     data = loadtxt(momentum_anisotropy_eta_-0.5_0.5.dat,dtype=float32) #Invalid syntax
     ```

    + ValueError
     ```Python
     from os import path
     home = path.expanduser("Desktop")
     working_path = path.join(home, "study/PY4E/week1") 
     data = loadtxt("momentum_anisotropy_eta_-0.5_0.5.dat",dtype=int) #The data type of file format and read format is not matched
     ```
    
    + TypeError
     ```Python
     from os import path
     home = path.expanduser("Desktop")
     working_path = path.join(home, "study/PY4E/week1/example")
     print("working path : "+working_path+" workind date : "+20210719) #can only concatenate str (not "int") to str
     ```

+ 2. Debugging
    + SyntaxError
     ```Python
     from os import path
     home = path.expanduser("Desktop")
     working_path = path.join(home, "study/PY4E/week1/example")
     data = loadtxt("momentum_anisotropy_eta_-0.5_0.5.dat",dtype=float32) #Add "" to inform the data name
     ```

    + ValueError
     ```Python
     from os import path
     home = path.expanduser("Desktop")
     working_path = path.join(home, "study/PY4E/week1") 
     data = loadtxt("momentum_anisotropy_eta_-0.5_0.5.dat",dtype=float32) #Match the data type
     ```
    
    + TypeError
     ```Python
     from os import path
     home = path.expanduser("Desktop")
     working_path = path.join(home, "study/PY4E/week1/example")
     print("working path : "+working_path+" workind date : "+"20210719") #change the type to string from int
     ```

+ 3. Error
    + OSError
     ```Python
     from os import path
     home = path.expanduser("Desktop")
     working_path = path.join(home, "study/PY4E/week1") #Cannot find the data since the path is uncorrect
     data = loadtxt("momentum_anisotropy_eta_-0.5_0.5.dat",dtype=float32)
     ```

    + NameError
     ```Python
     import matplotlib as mpl
     mpl.rcParams['figure.figsize'] = [6., 4.5]
     mpl.rcParams['lines.linewidth'] = linewidth # name 'linewidth' is not defined
    ```
    
    + ModuleNotFoundError
     ```Python
     import matplotlib.pyplots as plt #No module named matplotlib.pyplots
     ```

+ 4. Debugging
    + OSError
     ``` Python
     from os import path
     home = path.expanduser("Desktop")
     working_path = path.join(home, "study/PY4E/week1/example") #modify the path
     data = loadtxt("momentum_anisotropy_eta_-0.5_0.5.dat",dtype=float32)
     ```

    + NameError
     ``` Python
     import matplotlib as mpl
     linewidth = 2 #Define linewidth
     mpl.rcParams['figure.figsize'] = [6., 4.5]
     mpl.rcParams['lines.linewidth'] = linewidth 
    ```
    
    + ModuleNotFoundError
     ```Python
     import matplotlib.pyplot as plt #Fix typo in module name
     ```

------------

### Q4. 
#### hint:

     birth = int(input(“생일이 지났습니까? 맞으면 0 아니면 -1 : “))
#
The macro is in [HERE](https://github.com/JinjooSeo/PY4E/blob/main/week1/M1_A4.py)

```Python
from datetime import datetime
from dateutil.relativedelta import relativedelta

birth = input("When is your birthday? (ex) 2021-07-19) \n")
birth = datetime.strptime(birth, "%Y-%m-%d") #convert to date type(?) from string
today = datetime.now() #Get a date of today automatically

 #Vaildity check
if birth > today: 
    print("Invaild date! Please check the birthday.")
    exit()

#initialization
age_month = 0
age_day = 0

if birth.day <= today.day:
    age_day = today.day - birth.day
else:
    age_day = (today.replace(day=1) - relativedelta(days=1)).day + today.day - birth.day
    today -=relativedelta(months=1)

if birth.month <= today.month:
    age_month = today.month - birth.month
    age_year = today.year - birth.year  
else:
    age_month = 12 + today.month - birth.month
    age_year = today.year - birth.year -1

print(str(age_year)+" years, "+str(age_month)+" months, "+str(age_day)+" days")
print("Your age is " + str(age_year))
```
    
