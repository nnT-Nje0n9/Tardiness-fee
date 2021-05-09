import datetime as dt
import os
import time
import getpass

student = {0:'선생님', 1:'구본희', 2 : '권민서', 3 : '김도형', 4 : '김민주', 5 : '김시영', 6 : '김 준', 7 : '김지수', 8 : '김태오', 9 : '김태운', 10 : '노승재', 11 : '박정은', 12 : '배다경', 13 : '손호영', 14 : '송찬혁', 15 : '신건호', 16 : '육심균', 17 : '이다빈', 18 : '이석민', 19 : '이정민', 20 : '임병헌', 21 : '장예주', 22 : '정구민', 23 : '한승주', 24 : '허 윤'}
fine = [10000,2500,2000,3000,2500,2000,3000,2500,2500,2000,1500,1000,2500,2000,2500,3000,3000,0,3000,3000,2500,2000,500,0,1000]

print(
    '''
    
 ________  _________  ________  ________  ___            
|\   ____\|\___   ___\\\\   __  \|\   __  \|\  \           
\ \  \___|\|___ \  \_\ \  \|\  \ \  \|\  \ \  \          
 \ \_____  \   \ \  \ \ \  \\\\\  \ \   ____\ \  \         
  \|____|\  \   \ \  \ \ \  \\\\\  \ \  \___|\ \__\        
    ____\_\  \   \ \__\ \ \_______\ \__\    \|__|        
   |\_________\   \|__|  \|_______|\|__|        ___      
   \|_________|                                |\__\     
                                               \|__|     
                                                         
 _________  ________  ________  ________      ___    ___ 
|\___   ___\\\\   __  \|\   __  \|\   ___ \    |\  \  /  /|
\|___ \  \_\ \  \|\  \ \  \|\  \ \  \_|\ \   \ \  \/  //
     \ \  \ \ \   __  \ \   _  _\ \  \ \\\\ \   \ \    // 
      \ \  \ \ \  \ \  \ \  \\\\  \\\\ \  \_\\\\ \   \/  / /  
       \ \__\ \ \__\ \__\ \__\\\\ _\\\\ \_______\__/  / /    
        \|__|  \|__|\|__|\|__|\|__|\|_______|\___/ /     
                                            \|___|/      made by 63um3um
                                                         
                                                         
    
    '''
)


password = '031201'


tmps = getpass.getpass("Input PassWord : ")

if tmps != password :
    print('\n\nwrong password!')
    input('PRESS ENTER TO EXIT')
    exit()

print(
    '''
    
  ____  _   _  ____ ____ _____ ____ ____  _ 
 / ___|| | | |/ ___/ ___| ____/ ___/ ___|| |
 \___ \| | | | |  | |   |  _| \___ \___ \| |
  ___) | |_| | |__| |___| |___ ___) |__) |_|
 |____/ \___/ \____\____|_____|____/____/(_)
                                            

    '''
)
time.sleep(1)
os.system('cls')


print(
    '''
    
 ________  _________  ________  ________  ___            
|\   ____\|\___   ___\\\\   __  \|\   __  \|\  \           
\ \  \___|\|___ \  \_\ \  \|\  \ \  \|\  \ \  \          
 \ \_____  \   \ \  \ \ \  \\\\\  \ \   ____\ \  \         
  \|____|\  \   \ \  \ \ \  \\\\\  \ \  \___|\ \__\        
    ____\_\  \   \ \__\ \ \_______\ \__\    \|__|        
   |\_________\   \|__|  \|_______|\|__|        ___      
   \|_________|                                |\__\     
                                               \|__|     
                                                         
 _________  ________  ________  ________      ___    ___ 
|\___   ___\\\\   __  \|\   __  \|\   ___ \    |\  \  /  /|
\|___ \  \_\ \  \|\  \ \  \|\  \ \  \_|\ \   \ \  \/  //
     \ \  \ \ \   __  \ \   _  _\ \  \ \\\\ \   \ \    // 
      \ \  \ \ \  \ \  \ \  \\\\  \\\\ \  \_\\\\ \   \/  / /  
       \ \__\ \ \__\ \__\ \__\\\\ _\\\\ \_______\__/  / /    
        \|__|  \|__|\|__|\|__|\|__|\|_______|\___/ /     
                                            \|___|/      made by 63um3um
                                                         
                                                         
    
    '''
)


current_time = dt.datetime.now() # 현재 시간 받기

weekday = dt.datetime.today().weekday() #요일 받기 0이면 월요일 1이면 화.. 이런 식으로 월요일로 바꿀 때 사용

ftime = open('tardy_sttime.txt','r')
stime = ftime.read()
ftime.close()
standard_time = dt.datetime.strptime(stime,'%Y-%m-%d %H:%M:%S') #이번주 월요일을 기준5.3

print('기준일자 : ', standard_time)

tlen = current_time - standard_time
#print('tlen : ', tlen.days)

fcnt = open("tardy_fcount.txt",'r') # 주간 지각 횟수 목록 지각횟수는 1자리 수 임을 이용하여 파일 입출력을 편하게 해보자
week_cnt = list(fcnt.read())
week_cnt = list(map(int,week_cnt)) ### 지각 횟수를 리스트로 받아옴
fcnt.close()

if tlen.days >= 7: # 일주일이 지났다면

    max = fine[0]*week_cnt[0] #####
    number = 0#####
    sum = fine[0]*week_cnt[0] ##### 선생님으로 초기화
    
    for i in range(1,25) : #이번주 누적 금액
        sum = sum + fine[i]*(2**(week_cnt[i])-1)
        if max < fine[i]*(2**(week_cnt[i])-1) :
            max = fine[i]*(2**(week_cnt[i])-1) #등비수열 합 공식
            number = i
        
    log = open("tardy_log.txt",'a') # 주간정리
    for i in week_cnt :
        log.write(str(i)) #있던 데이터를 내보내고
    log.write('\n')
    log.write(str(standard_time.year))
    log.write('년 ')
    log.write(str(standard_time.month))
    log.write('월 ')
    log.write(str(standard_time.day))
    log.write('일')
    log.write(' 지각비 : ')
    log.write(str(sum))
    log.write('\n')
    log.write('★이번주 지각비 일등공신 : ')
    log.write(student[number])
    log.write(' ')
    log.write(str(max))
    log.write('원★\n\n')
    log.close()

    standard_time = current_time - dt.timedelta(days = weekday, hours= current_time.hour, minutes= current_time.minute, seconds= current_time.second) #기준시간을 이번주 월요일로
    standard_time = dt.datetime(standard_time.year, standard_time.month, standard_time.day)
    ftime = open('tardy_sttime.txt','w')
    ftime.write(str(standard_time))
    ftime.close()

    fcnt = open("tardy_fcount.txt",'w')
    fcnt.write('0000000000000000000000000') #초기화한다.
    fcnt.close()
    fcnt = open("tardy_fcount.txt",'r') # 주간 지각 횟수 목록 지각횟수는 1자리 수 임을 이용하여 파일 입출력을 편하게 해보자
    week_cnt = list(fcnt.read())
    week_cnt = list(map(int,week_cnt)) ### 지각 횟수를 리스트로 받아옴
    fcnt.close()
    print('변경된 기준일자 : ', standard_time)


print(week_cnt,type(week_cnt),len(week_cnt)) #test

fcnt = open("tardy_fcount.txt",'w')


print('현재 시간 : ',current_time.year,'년',current_time.month,'월', current_time.day, '일', current_time.hour ,'시', current_time.minute,'분')
print()
print()
print('전체 출결시 0 입력 \n종료하려면 ENTER을 입력하세요.')
print()

try :
    while(True) :
        auth = input('input number : ')
        auth = int(auth)
        week_cnt[auth] = week_cnt[auth] + 1

        if auth == 17 or auth == 23 : #없는 번호 예외처리
            print('no existence')

        elif auth == 0 : # 선생님 예외처리
            print('선생님 10000원!')
            print(f'개인 누적 금액 : {fine[auth]*week_cnt[auth]}원')
            break

        print(f'\n{auth}번 {student[auth]} : ')
        print(f'이번 주 지각 : {week_cnt[auth]}회')
        print(f'오늘 내야 할 금액 : {fine[auth] * 2**(week_cnt[auth]-1)}원')
        print(f'개인 누적 금액 : {fine[auth]*(2**(week_cnt[auth])-1)}원\n')
except :
    print()
    pass

sum = fine[0]*week_cnt[0]
for i in range(1,25) : #이번주 누적 금액
    sum = sum + fine[i]*(2**(week_cnt[i])-1)

os.system('cls')
print('이번주 누적 금액 : ',sum,'원')

for i in week_cnt :
    fcnt.write(str(i))
fcnt.close()
print()
input('PRESS ENTER TO EXIT')
exit()