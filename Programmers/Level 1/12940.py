def solution(n, m):
    answer = []
    
    max_n = max(n, m)
    min_n = min(n, m)
    
    divisor = 1
    factor = 0
    
    for i in range(1, min_n+1):
        if n % i == 0 and m % i == 0:
            divisor = i
        elif min_n < i or max_n < i:
            break
    answer.append(divisor)
    
    if max_n % min_n == 0:
        answer.append(max_n)
    else:
        factor_n, factor_m = n, m
        while True:
            if factor_n == factor_m:
                answer.append(factor_n)
                break

            if factor_n < factor_m:
                factor_n += n
            elif factor_n > factor_m:
                factor_m += m
    
    return answer