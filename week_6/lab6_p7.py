#lab6_p7.py

def piCalculator(tol):
    loop_exit = False #boolean flag
    pi = 2 #초기 pi항
    n = 1
    while not loop_exit:
        pi_new = pi * (2*n)/(2*n-1) * (2*n)/(2*n+1)
        if abs(pi_new - pi) < tol:
            pi = pi_new
            loop_exit = True #tol 범위 안에 있으면 loop break
        else:
            pi = pi_new #pi_new = pi 동일화
            n += 1 #n항 숫자 늘려주기 다음에 곱해질 항을 위해서

    return pi

