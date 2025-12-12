class Solution(object):
    def countMentions(self, numberOfUsers, events):
        mentions = [0]*numberOfUsers
        back = [0]*numberOfUsers
        events.sort(key=lambda e: (int(e[1]), e[0]=="MESSAGE"))

        for typ, t, data in events:
            t = int(t)
            if typ == "OFFLINE":
                back[int(data)] = t + 60
                continue

            for tok in data.split():
                if tok == "ALL":
                    for u in range(numberOfUsers):
                        mentions[u] += 1
                elif tok == "HERE":
                    for u in range(numberOfUsers):
                        if t >= back[u]:
                            mentions[u] += 1
                else:  
                    mentions[int(tok[2:])] += 1

        return mentions
        