# Week1 Mission

### Q1. 파이썬으로 컴퓨터에게 우리가 원하는 일을 시킬 수 있다고 하였습니다. 파이썬으로 할 수 있는 일은 어떤 것들이 있고, 나는 그중에서 무엇을 하고 싶은지 적어봅시다.
------------
파이썬으로 할 수 있는 일은 무궁무진하다. 매우 빠른 속도를 요구하거나 하드웨어, 모바일 프로그래밍과 관련된 것이 아니면 프로그래머가 원하는 일 대부분을 파이썬으로 할 수 있다. 예를들면 웹, 수치연산, 데이터베이스, 데이터 분석 프로그래밍 등이 있다.

현재, LHC(Large Hadron Collider)를 이용해 입자들을 가속시키고 충돌시켜 나오는 입자들의 데이터를 분석하는 일을 하고 있다. 복잡하고 빠른 연산을 요구하기 때문에 low level 언어인 c++를 이용해서 데이터 분석을 진행하고 있다. 현재 사용하는 데이터의 크기는 약 100PB인데 이러한 빅데이터 안에서 특정한 입자만 찾기 위해서는 contamination을 제거해 데이터 크기를 줄이고, 좋은 알고리즘을 이용해 signal을 찾아내야 한다. 따라서 Python에서 사용되는 빅데이터를 다루는 스킬과 Machine learnig 알고리즘 등을 배우는 것을 목표로 한다.


### Q2. 파이썬 코딩을 하기에 앞서 하드웨어를 이해하는 것이 중요하다고 했습니다. 하드웨어 아키텍쳐에서 CPU와 Main Memory 그리고 Secondary Memory의 역할을 간단하게 정리하여 봅시다.
------------
+ CPU : Main memory에서 전달되는 명령을 실행하는 부분. 프로그래밍 연산을 담당.
+ Main memory : CPU에 전달할 명령을 저장하는 부분, 휘발성 메모리로 프로그램을 저장함.
+ Second Memory : 운영체제 및 데이터를 저장하는 부분, 비휘발성 메모리로 데이터를 보존할 수 있음.


### Q3. 파이썬은 우리의 명령을 이해하지 못했을 때, 친절하게 Error Message를 통해 어떤 명령을 이해하지 못했는지 알려줍니다. 그것을 보고 코드의 버그를 수정해가는 과정을 Debugging이라고 합니다. 이것은 코딩에 있어서 매우 중요합니다. 따라서, Error Message에 대해서 이해하는 시간을 가져봅시다. 강의에서는 SyntaxError, ValueError, TypeError 3가지가 등장했습니다.
#### 1. 각각의 Error를 발생시키는 코드를 2가지씩 만들어보고
#### 2. Debugging한 코드도 만들어 봅시다.
#### 3. 그리고 그 밖에 다른 Error도 3가지를 찾아 그 Error를 발생시키는 코드와
#### 4. Debugging한 코드를 1가지씩 만들어 봅시다.
------------
+ 1. 
    + SyntaxError
    ```C
    from os import path
    home = path.expanduser("Desktop")
    working_path = path.join(home, "study/PY4E/week1/example")
    data = loadtxt(momentum_anisotropy_eta_-0.5_0.5.dat,dtype=float32) #Invalid syntax
    ```

    + ValueError
    
    + TypeError

+ 2.
    + SyntaxError
    ```C
    from os import path
    home = path.expanduser("Desktop")
    working_path = path.join(home, "study/PY4E/week1/example")
    data = loadtxt("momentum_anisotropy_eta_-0.5_0.5.dat",dtype=float32) #Add "" to inform the data name
    ```

    + ValueError
    
    + TypeError

+ 3. 
    + OSError
    ```C
    from os import path
    home = path.expanduser("Desktop")
    working_path = path.join(home, "study/PY4E/week1") #Cannot find the data since the path is uncorrect
    data = loadtxt("momentum_anisotropy_eta_-0.5_0.5.dat",dtype=float32)
    ```

    + NameError
     ```C
     import matplotlib as mpl
     mpl.rcParams['figure.figsize'] = [6., 4.5]
     mpl.rcParams['lines.linewidth'] = linewidth # name 'linewidth' is not defined
    ```
    
    + TypeError

+ 4. 
    + OSError
    ``` C
    from os import path
    home = path.expanduser("Desktop")
    working_path = path.join(home, "study/PY4E/week1/example") #modify the path
    data = loadtxt("momentum_anisotropy_eta_-0.5_0.5.dat",dtype=float32)
    ```

    + NameError
     ``` C
     import matplotlib as mpl
     linewidth = 2 #Define linewidth
     mpl.rcParams['figure.figsize'] = [6., 4.5]
     mpl.rcParams['lines.linewidth'] = linewidth 
    ```
    
    + TypeError


    




### Q4. 강의에서 미국과 유럽의 엘리베이터 층수를 변환하는 프로그램이 나왔습니다. 그와 비슷하게 우리는 한국 나이를 미국 나이로 변환하는 프로그램을 코딩 해봅시다.
#### hint: 미국 나이는 생일이 지났는지 안지났는지가 중요하죠!

     birth = int(input(“생일이 지났습니까? 맞으면 0 아니면 -1 : “))
------------
    