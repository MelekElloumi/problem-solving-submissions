class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        workers = [0]*k
        
        self.res = sys.maxsize
        # jobs.sort(reverse = True)
        def dfs(curr):
            if curr == len(jobs):
                self.res = min(self.res, max(workers))
                return
            
            seen = set() # record searched workload of workers
            for i in range(k):
                if workers[i] in seen: continue # if we have searched the workload of 5, skip it.
                if workers[i] + jobs[curr] >= self.res: continue # another branch cutting
                seen.add(workers[i])
                workers[i] += jobs[curr]
                dfs(curr+1)
                workers[i] -= jobs[curr]
        
        dfs(0)
        return self.res