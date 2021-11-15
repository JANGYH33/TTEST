# 키보드로 동이름을 입력해 해당 자료 읽기

try:
    dong = input('동이름 입력:')
    
    with open('zipcode.txt', mode = 'r' , encoding='utf-8') as f:
        line = f.readline()
        #print(line)
        
        while line:
            
            #lines = line.split('\t')
            #print(line)
            lines = line.split(chr(9)) # 10진수 9를 Ascii 코드로 변환하면 tab 키
            
            #if lines[3].startswith('개포'): 
            if lines[3].startswith(dong):
                #print(lines)
                print('[' + lines[0] + ']' + ' ' + lines[1] + \
                      ' ' + lines[2] + ' ' + lines[3] + ' ' + lines[4]) 
                
                
            line = f.readline()
            
except Exception as e:
    print('err :' , e)