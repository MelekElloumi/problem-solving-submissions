class Tab:
    def __init__(self, url, nxt=None, prev=None):
        self.url=url
        self.next=nxt
        self.prev=prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=Tab(homepage)
        self.current=self.history
        self.length=1
        self.position=0
        
    def visit(self, url: str) -> None:
        self.current.next=Tab(url,prev=self.current)
        self.current=self.current.next
        self.position+=1
        self.length=self.position+1
        
    def back(self, steps: int) -> str:
        if not self.current.prev:
            return self.current.url
        steps=min(self.position,steps)      
        while steps!=0:
            self.current=self.current.prev
            steps-=1
            self.position-=1
        return self.current.url

    def forward(self, steps: int) -> str:
        if not self.current.next:
            return self.current.url
        steps=min(steps,self.length-1-self.position)
        if steps==0:
            return self.current.url
        self.position+=steps
        while steps!=0:
            self.current=self.current.next
            steps-=1 
        return self.current.url