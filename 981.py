# Problem: https://leetcode.com/problems/time-based-key-value-store/

class FastTimeMap:
    '''
    Idea: Use "bisect" to improve the runtime of get().
    '''
    def __init__(self):
        self.fastData = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.fastData:
            self.fastData[key]['values'].append(value)
            self.fastData[key]['timestamp'].append(timestamp)
        else: 
            self.fastData[key] = {'values': [], 'timestamp': []}
            self.fastData[key]['values'] = [value]
            self.fastData[key]['timestamp'] = [timestamp] 
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.fastData: 
            timestamps = self.fastData[key]['timestamp']
            index = bisect_right(timestamps, timestamp)
            if (index > 0):
                return self.fastData[key]['values'][index - 1]
        return ""

class TimeMap:
    '''
    Idea: Data structure maps keys to array of (value, timestamp).
    - We can do this since timestamps are strictly increasing. 
    '''
    def __init__(self):
        self.data = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data: 
            for pair in reversed(self.data[key]):
                if pair[1] <= timestamp:
                    return pair[0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)









