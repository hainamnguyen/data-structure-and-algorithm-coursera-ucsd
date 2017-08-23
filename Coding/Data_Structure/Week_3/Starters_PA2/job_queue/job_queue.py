# python3

class JobQueue:
    def read_data(self):
        self.num_workers, self.m = map(int, input().split())
        self.jobs = list(map(int, input().split()))

    #def write_response(self):
        #print(self.assigned_workers)
        #for i in range(self.m):
            #print(self.assigned_workers[i][0], self.assigned_workers[i][1]) 
            #a = 2
    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        #self.assigned_workers = []
        self.start_times = [[i, 0] for i in range(self.num_workers)]
        #self.jobs.sort()
        for i in range(self.m):
            print(self.start_times[0][0], self.start_times[0][1])
            #print(i, self.start_times)
            self.start_times[0][1] += self.jobs.pop(0)
            self.shift_Down(0)
            #print(i, self.start_times)
        #next_free_time = [0] * self.num_workers
        #for i in range(len(self.jobs)):
          #next_worker = 0
          #for j in range(self.num_workers):
            #if next_free_time[j] < next_free_time[next_worker]:
              #next_worker = j
          #self.assigned_workers[i] = next_worker
          #self.start_times[i] = next_free_time[next_worker]
          #next_free_time[next_worker] += self.jobs[i]
        
    def shift_Down(self,i):
        minIndex = i
        l = self.leftChild(i)
        if l <= self.num_workers - 1:
            if self.start_times[l][1] < self.start_times[minIndex][1] or (self.start_times[l][1] == self.start_times[minIndex][1] and self.start_times[l][0] < self.start_times[minIndex][0]): 
                minIndex = l
        r = self.rightChild(i)
    #print(r)
        if r <= self.num_workers - 1:
            if self.start_times[r][1] < self.start_times[minIndex][1] or (self.start_times[r][1] == self.start_times[minIndex][1] and self.start_times[r][0] < self.start_times[minIndex][0]): 
                minIndex = r
        if i != minIndex:
            self.start_times[i], self.start_times[minIndex] = self.start_times[minIndex],self.start_times[i]
            self.shift_Down(minIndex)
    def leftChild(self,i):
        return 2*i + 1
    def rightChild(self,i):
        return 2*i + 2
        
    def solve(self):
        self.read_data()
        self.assign_jobs()
        #self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

