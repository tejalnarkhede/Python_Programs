a=0
try:
    b=5/a
    print(b)
except Exception as e:
    print('Error:',e)
finally:
    print('Always Executed..!!!')

