from collections import deque
# LRU에 대해서 이해하기, (가장 오래된 것을 교체하는 작업)
def solution(cacheSize, cities):
    answer = 0
    queue = deque([])
    if cacheSize == 0: 
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        if city in queue:
            answer += 1
            queue.remove(city)
        else:
            answer += 5
            if len(queue) >= cacheSize:
                queue.popleft()
        queue.append(city)
    return answer