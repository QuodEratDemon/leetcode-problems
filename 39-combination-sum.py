class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sums = defaultdict(set)

        combo_sums = []

        for i in range(len(candidates)):
            curr = 1
            possible_candidate = target - candidates[i]
            while possible_candidate > 0 and curr <= possible_candidate:
                for s in sums[curr]:
                    sums[curr + candidates[i]].add(s + (candidates[i], ))
                curr += 1

            total = candidates[i]
            new_combo = (candidates[i], )
            while total <= target:
                sums[total].add(new_combo)
                new_combo += (candidates[i], )
                total += candidates[i]

        return [list(final) for final in sums[target]]
