class Chmod:
    NUMERIC = 3
    TEXT = 9

    def __init__(self, s):
        self.s = s

    def getNumeric(self):
        if self.__verify_text():
            u = self.__sumx(self.s[0:3])
            g = self.__sumx(self.s[3:6])
            o = self.__sumx(self.s[6:9])
            return f'{u}{g}{o}'
        return self.s

    def getText(self):
        if self.__verify_numeric():
            u = self.__findx(self.s[0])
            g = self.__findx(self.s[1])
            o = self.__findx(self.s[2])
            return f'{u}{g}{o}'
        return self.s

    def __verify_text(self):
        if len(self.s) is not self.TEXT:
            return False

        elements = 'rwx-'
        for el in self.s:
            if el not in elements:
                return False

        return True

    def __verify_numeric(self):
        if len(self.s) is not self.NUMERIC:
            return False

        elements = '01234567'
        for el in self.s:
            if el not in elements:
                return False

        return True

    def __sumx(self, s):
        sum = 4 if s[0] != '-' else 0
        sum += 2 if s[1] != '-' else 0
        sum += 1 if s[2] != '-' else 0
        return sum

    def __findx(self, n):
        p = ['---', '--x', '-w-', '-wx', 'r--', 'r-x', 'rw-', 'rwx']
        return p[int(n)]
