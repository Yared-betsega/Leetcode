def has_cycle(head):
    if head.next == None:
        return 0
    temp = head
    repo = []
    while temp:
        if temp in repo:
            return 1
        repo.append(temp)
        temp = temp.next
    return 0
