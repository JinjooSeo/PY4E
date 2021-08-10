def make_comma(num):
    try:
        i_num=int(num)
        print('----------처리중----------')
    except:
        print('숫자로 입력하셨는지 확인하시고 프로그램을 다시 시작해주세요!')
        exit()
        # 만약 여기서 다시 숫자 입력 단계로 바로 넘어갈 수 있다면 좋을 것 같습니다.

    #num=str(num)
    need_comma=len(num)//3
    rest=len(num)%3
    # 필요한 comma 개수는 숫자 길이를 3으로 나눈 몫(나머지가 1 또는 2인 경우)이거나 몫-1(나머지가 0인 경우). 그리고 그 나머지로 comma가 들어갈 위치가 달라지므로 나머지도 구해야 함.

    #print(need_comma, rest) 잘 작동함.

    if rest==0:
        for i in range(need_comma):
            if i==0:
                new_number=num
            else:
                new_number=new_number[:(3*i)+(i-1)]+','
                new_number=new_number+number[(3*i):]

    elif rest==1:
        for j in range(need_comma+1):
            if j==0:
                new_number=num
            else:
                new_number=new_number[:(3*j-2)+(j-1)]+','
                new_number=new_number+number[(3*j-2):]

    elif rest==2:
        for k in range(need_comma+1):
            if k==0:
                new_number=num
            else:
                new_number=new_number[:(3*k-1)+(k-1)]+','
                new_number=new_number+number[(3*k-1):]

    print('Comma를 추가한 결과는 다음과 같습니다!')
    print(new_number)

number=input('Comma를 넣을 숫자를 입력하세요!: ')
# print(type(number)) input으로 했으니 str이 나온다. 이를 숫자로 제대로 입력했는지 아닌지 확인이 필요하기 때문에 int로 바꿔서 try해 볼 것. 나중에 comma를 넣을 때에는 다시 str으로 바꾸고 comma 추가.
make_comma(number)
