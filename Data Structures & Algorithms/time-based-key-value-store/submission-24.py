class TimeMap:

    def __init__(self):
        self.time_map = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [(value, timestamp)]
        else:
            self.time_map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        #We can initialize result to be empty
        #We can accept when the key is <= the timestamp
        #We cannot accept when it is greater than

        result = ''
        values = self.time_map.get(key, [])

        l,r = 0, len(values)-1

        while l <= r:
            m = (l+r)//2

            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m -1 
        
        return result


