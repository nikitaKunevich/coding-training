class Solution:
    # O(n^2*log(n)) time | O(n) space
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # on each 'round' we should first insert most frequent tasks,
        # but no more then N, so that we don't waste 'diversity'
        
        #solution using sorting
        
        #[6, 1, 1, 1, 1, 1, 1]
        #[3, 2, 1], n=2 : A B C A B idle A
        
        #construct dict
        types = {}
        for t in tasks:
            if t in types:
                types[t] += 1
            else:
                types[t] = 1
        values = sorted(types.values(),reverse=True)
        cycles = 0 
        while True: #solution loop
            if values[0] == 0:
                break
            added = 0
            num_idx = 0
            while added < n + 1: # round loop
                if num_idx == len(values) or values[num_idx] == 0:
                    break
                values[num_idx] -= 1
                added += 1
                num_idx += 1
            if added < n + 1 and values[0] > 0:
                cycles += n + 1
            else:
                cycles += added
            values.sort(reverse=True)
            print(values)
        return cycles