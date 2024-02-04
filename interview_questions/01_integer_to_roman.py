class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
                   ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                   ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
                   ["M", 1000]]
        
        result = ""

        for sym, val in  reversed(symList):
            if num // val:
                count = num // val
                result += (sym * count)
                num %= val
        return result
            
            
if __name__ == "__main__":
    input_number = input("Enter integer: ")
    answer = Solution().intToRoman(int(input_number))
    print(f"Output roman numeral: {answer}")
    