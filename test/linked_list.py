class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.current = InternetPage(val=homepage)

    def visit(self, url: str) -> None:
        self.current.next = InternetPage(self.current, val=url)
        self.current = self.current.next

    def back(self, steps: int) -> str:

        while steps > 0 and self.current.prev is not None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next is not None:
            steps -= 1
            self.current = self.current.next
        return self.current.val


class InternetPage:
    def __init__(self, prev=None, val="visitPageUrl", next=None):
        self.prev = prev
        self.val = val
        self.next = next


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
