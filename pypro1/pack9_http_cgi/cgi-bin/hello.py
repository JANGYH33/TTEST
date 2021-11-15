# 파이썬 모듈의 값을 html로 출력

my = '파이썬 변수 값' 
tot = 70 + 80

print('Content-type:text/html;charset=utf-8\n')
print('<html><body>')
print('<b>안녕</b> 파이썬 모듈로 작성한 문서 입니다 <br>')
print('와우 성공')
print('<br>변수 값 : %s'%(my))
print('<br>토탈 값 : %d'%(tot))
print('</body></html>')
