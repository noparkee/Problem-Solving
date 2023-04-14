def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    cache = []
    for c in cities:
        if c.lower() not in cache:
            if len(cache) < cacheSize:
                cache.append(c.lower())
            else:
                cache = cache[1:] + [c.lower()]
            answer += 5
        else:
            answer += 1
            cache.remove(c.lower())
            cache.append(c.lower())
                
    return answer