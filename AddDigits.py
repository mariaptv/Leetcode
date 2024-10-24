
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        sum = 0
        letter = str(num)

        for i in letter:
            print(i)
            sum += int(i)

        print(f"Suma {sum}")
        if sum > 9:
            return self.addDigits(sum)
        else:
            return sum



new = Solution()
print(new.addDigits(1234))