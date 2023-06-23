class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        valid = []
        pairs = []
        counter = 0

        for i in range(len(currentState)):
            if i + 1 == len(currentState):
                break
            if currentState[i] == "+" and currentState[i+1] == "+":
                pairs.append((i, i + 1))

        for pair in pairs:
            next_valid = ""
            j = 0
            while j  < len(currentState):
                if j == pair[0]:
                    next_valid += "--"
                    j += 2
                    continue
                next_valid += currentState[j]
                j += 1
            valid.append(next_valid)


        return valid
