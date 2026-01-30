class Numbers:
    def __init__(self):
        self.Value = int(input("Enter number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors of", self.Value, ":")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        return self.SumFactors() == self.Value


def main():
    Obj1 = Numbers()
    Obj2 = Numbers()

    print("Is Prime:", Obj1.ChkPrime())
    Obj1.Factors()
    print("Sum of Factors:", Obj1.SumFactors())
    print("Is Perfect:", Obj1.ChkPerfect())
    print("---------------------")

    print("Is Prime:", Obj2.ChkPrime())
    Obj2.Factors()
    print("Sum of Factors:", Obj2.SumFactors())
    print("Is Perfect:", Obj2.ChkPerfect())


if __name__ == "__main__":
    main()
