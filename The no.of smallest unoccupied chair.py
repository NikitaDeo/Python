import heapq

class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        
        events = []
        for idx, (arrival, leaving) in enumerate(times):
            events.append((arrival, 'arrive', idx))
            events.append((leaving, 'leave', idx))
            

        events.sort(key=lambda x: (x[0], x[1] == 'arrive'))
        
        available_chairs = []
        heapq.heapify(available_chairs)
        

        for i in range(len(times)):
            heapq.heappush(available_chairs, i)
            

        occupied = {}
        
        for time, event_type, friend in events:
            if event_type == 'arrive':
                
                chair = heapq.heappop(available_chairs)
                occupied[friend] = chair

                if friend == targetFriend:
                    return chair
            elif event_type == 'leave':

                chair = occupied[friend]
                heapq.heappush(available_chairs, chair)