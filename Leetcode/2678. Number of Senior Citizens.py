class Solution:
    def countSeniors(self, details: List[str]) -> int:

        age = []
        count = 0

        for i in details:
            age.append(int(i[11:13]))
        for j in age:
            if j > 60:
                count += 1
            else:
                pass
        return count