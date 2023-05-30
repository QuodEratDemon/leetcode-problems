class Solution:
    def minWindow(self, s: str, t: str) -> str:
        requirements = defaultdict(int)
        curr_stats = defaultdict(int)
        total = 0
        req_total = 0
        left = 0
        right = 0
        best = (-1, -1)

        for r in t:
            requirements[r] += 1
            req_total += 1

        while right < len(s):
            curr = s[right]
            if curr in requirements:
                curr_stats[curr] += 1
                if curr_stats[curr] <= requirements[curr]:
                    total += 1

                while left < right:
                    if s[left] in requirements:
                        if curr_stats[s[left]] > requirements[s[left]]:
                            
                            curr_stats[s[left]] -= 1
                            left += 1
                        else:
                            break
                    else:
                        left += 1
            
            if total == req_total:
                if best == (-1, -1) or best[1] - best[0] + 1 > right - left + 1:
                    best = (left, right)

            right += 1

        if best == (-1, -1):
            return ""

        return s[best[0]:best[1] + 1]




            

        