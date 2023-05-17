class Solution:
    def countAndSay(self, n: int) -> str:

        def say(num):
            count = 0
            curr = num[0]
            final = ""
            for s in num:
                
                if s == curr:
                    count += 1
                else:
                    final += str(count) + curr
                    curr = s
                    count = 1
            
            final += str(count) + curr
            return final

        say_string = "1"
        for i in range(n - 1):
            print(say_string)
            say_string = say(say_string)
        
        return say_string