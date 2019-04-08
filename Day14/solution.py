class Difference:
    def __init__(self, a):
        self.__elements = a

        # Add your code here
        def computeDifference(self):
            maxi = 0

            length = len(self.__elements)
            for i in range(length):
                for j in range(length):
                    absol = abs(self.__elements[i] - self.__elements[j])
                    if absol > maxi:
                        maxi = absol

            self.maximumDifference = maxi

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
