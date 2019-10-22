# 형님 코드를 가지고와서 스터디 하기 

#!/usr/bin/python

# doKhaiii.py

import os
import sys
import re
from khaiii import KhaiiiApi 

# 임포트하는건 다행이 만국 공통인데 마지막에 khaiii는 신기하게 카히로 부터 임포트를 해온다.

api = KhaiiiApi()

# 전달 인자 읽기 및 파일 패스 생성
if len(sys.argv) < 3:
    
#파이썬에는 명령행을 받기 위해서는 sys 라이브러리를 import 해주어야 합니다.

#len() : 전체입력값의 길이를 돌려주는 함수이다.

#sys.argv 인자 읽고 요녀석은 배열을 뜻합니다. 만약 sys.argv[0]으로 하면 기본적으로 길이가 1이다.
   
#고로 위에는 3보다 작은 인자라면...
    """ 
    f = open("/home/hadoop/dev/test/1.txt","r")
    while True:
    	line = f.readline()
    	if not line: break    
    	print(line)
    f.close()
    """
    
    exit(1)
# exit 당연하게도 종료코드라고 보면 된다. 그런데 아래에 보니 [1],[2] 이렇게 숫자가 매겨져 있는 것을 보아 다른 의미를 가지고 있을 것 같아서 찾아보니

# exit(0)은 오류나 문제가 없는 코드 종료
# exit(1)은 몇가지 문제 오류 있는 코드를 종료

# 라고 개발자들끼리 정해놓은 것 같다. 

inputPath = sys.argv[1]
outputPath = sys.argv[2]

#위의 코드 [1],[2]는 인덱싱을 뜻한다고 한다.

fileList = os.listdir(inputPath)

unitListList = []
for file in fileList :
    #print('/home/hadoop/dev/test/1.txt')
    print(file)
	
    # file이라는 소스 읽기 
    
    # 입력 파일 읽기 및 기본 형태소 분석 수행
    # open(파일을 연다.)
    # 'r' = 읽기모드, 'w'쓰기모드, 'a'추가모드
    # 참고 : https://wikidocs.net/26
    
    f = open(inputPath + "/" + file, "r", encoding='utf-8-sig')
    
    strList = []
    while True:
        line = f.readline()
		
        #파일을 읽어온다.
        
        if not line: break
        if line == "\n": continue
            
		#읽어온 파일에 line이 아니라면 멈추고 라인이라면, \n처리를 해서 계속해서 진행을 한다.
        
        # 나중에 고도화 및 모듈화 해야할 곳
        ##############################################################
        
        #형태소 분석 전 전처리 작업 (형태소 분석에 악영향을 주는 기호 삭제)
        
        line = line.replace("'", "").replace('"', "").replace("‘", "").replace("’", "").replace("“", "").replace('”', "")
        ##############################################################


        for word in api.analyze(line):
            strList.append("{0}".format(word))
    f.close()
	# api.analyze 이게 khaiii Api에서 읽어오는것?
    # 나중에 고도화 및 모듈화 해야할 곳
    #############################################################################
    # unit(의미 있는 어절 단위; 자체정의)
    # unit 을 담을 unitList 생성 및 unit parsing 작업 시작
    
    unitList = []
    for i, line in enumerate(strList):
        morpParcelList = line.split("\t")[1].replace(
        '"', '').replace("'", "").split(" + ")

        morpMetaList = []
        for elem in morpParcelList:
            splited = elem.split("/")
            if splited[0] != "" and \
            splited[1] != "NP" and \
            splited[1] != "NR" and \
            splited[1] != "NNB" and \
            ( splited[1][0] == "N" or \
            splited[1][0] == "S" ) :
                morpMetaList.append(splited)
		##여기서 왜 인덱싱이 [1]이 되는거죠????
        # 1글자인 경우 일반명사, 고유명사, 외래어만 셋 중 하나가 아닐 경우 스킵
        if len(morpMetaList) == 1 and len(morpMetaList[0][0]) == 1 :
            type = morpMetaList[0][1]
            if type != "NNG" and type != "NNP" and type != "SL" :  continue

        # 기타 일반적인 상황인 경우 계속 수행
        unit = ""
        for elem in morpMetaList:
            unit += elem[0]

        # 결과에서 의미없는 특문 제거
        unit = re.sub('([,.]$)|(^[,.])', '', unit)

        # 최종적으로 () [] 등으로 구분하여 나눈 후 각각 추가
        unitSplit = re.split("[\(\)\[\]\{\} ]", unit)
        for i, elem in enumerate(unitSplit) :
            unitSplit[i] = elem.strip()
        
        if len(unitSplit) > 1 :
            for elem in unitSplit :
                if len(elem) > 0 : unitList.append(elem) 
        else :
            if len(unitSplit[0]) > 0 :
                unitList.append(unitSplit[0])
        

        # 마지막으로 놓친 부분을 한 번 더 검증
        for unit in unitList :
            if re.match(r"[!@#$%^&*():;\[\]\{\}]", unit) != None :
                unitList.remove(unit)
        
    #############################################################################

    # unitList를 담는 list에 담기
    unitListList.append(unitList)

# 결과 파일로 출력
f = open(outputPath, "w")
for unitList in unitListList :
    for unit in unitList :
        f.writelines(unit + "\n")
f.close()
