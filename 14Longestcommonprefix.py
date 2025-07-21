class LongestCommonPrefix:
    def longest_common_prefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        lastresult = ""
        result = ""
        j = 1
        for i in range(len(strs[0])):
            if j > len(strs[0]) or j > len(strs[1]) or j > len(strs[2]):
                break
            
            if strs[0][i:j] in strs[1][i] and strs[0][i:j] in strs[2][i]:
                print(f"Checking prefix: {strs[0][i:j]}")
                print(f"Current result: {result}")
                result += strs[0][i]
                j += 1
            elif len(result) > len(lastresult):
                lastresult = result
                result = ""
                j = i + 2
        if len(result) > len(lastresult):
            lastresult = result
        return lastresult
    
# Example usage:
if __name__ == "__main__":
    lcp = LongestCommonPrefix()
    print(lcp.longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
    print(lcp.longest_common_prefix(["dog", "racecar", "car"]))      # Output: ""
    print(lcp.longest_common_prefix(["interspecies", "interstellar", "interstate"]))  # Output: "inters"

                