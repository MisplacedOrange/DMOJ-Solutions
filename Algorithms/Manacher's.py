class Manacher:
    
    # p[i] = radius of longest palindrome centered at i 
    # in transformed string
    def __init__(self, s):
        # transformed string with # and sentinels
        # sentinels to avoid bounds checking
        self.ms = "@"
        for c in s:
            self.ms += "#" + c
        self.ms += "#$"
        # @b#a#b#a#$

        # run Manacher’s algorithm
        self.p = [0] * len(self.ms)
        self.runManacher()

    def runManacher(self):
        n = len(self.ms)
        l = r = 0

        for i in range(1, n - 1):
            # mirror of i around center (l + r)/2
            mirror = l + r - i

            # initialize p[i] based on its mirror 
            # if within bounds
            if i < r:
                self.p[i] = min(r - i, self.p[mirror])

            # expand palindrome centered at i
            while self.ms[i + 1 + self.p[i]] == \
                            self.ms[i - 1 - self.p[i]]:
                self.p[i] += 1

            # update [l, r] if the palindrome expands 
            # beyond current r
            if i + self.p[i] > r:
                l = i - self.p[i]
                r = i + self.p[i]

    # returns length of longest palindrome centered 
    # at 'cen' in original string
    # 'odd' = 1 → check for odd-length, 'odd' = 0 → even-length
    def getLongest(self, cen, odd):
        # map original index to transformed string index
        pos = 2 * cen + 2 + (0 if odd else 1)
        return self.p[pos]

    # checks if s[l..r] is a palindrome in O(1)
    def check(self, l, r):
        length = r - l + 1
        cen = (l + r) // 2
        return length <= self.getLongest(cen, length % 2)