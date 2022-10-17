from __future__ import annotations
from functools import total_ordering
@total_ordering   #7-es 3.
class SPORT:     #1-es feladat
    nev: str
    __nemzetiseg: str
    __kor: int

    @property #2-es feladat
    def prop(self):
        return self.__nemzetiseg, self.__kor

    @prop.setter #2-es feladat
    def prop(self , value: str, value1: str, value2: int):
        self.__nev = value
        self.__nemzetiseg = value1
        self.__kor = value2

    def __init__(self, nev: str, kor: int, nemzetiseg = "Hungary") -> None:    #3-as feladat
        self.nev = nev
        self.__kor = kor
        self.__nemzetiseg= nemzetiseg

    def __repr__(self) -> str:    #4-es feladat
        return f'{self.nev}, {self.__nemzetiseg}, {self.__kor}'

    def __str__(self) -> str:  #5-os feladat
        return f'{self.nev} ({self.__nemzetiseg}, {self.__kor})'

    def __eq__(self, o: object) -> bool:   #6-os feladat
        if not isinstance(o, SPORT):
            return NotImplemented
        return(self.nev, self.__nemzetiseg, self.__kor) == (o.nev, o.__nemzetiseg, o.__kor)

    def __lt__(self, other):  #7-es 1.
        if not isinstance(other, SPORT):
            return NotImplemented
        return self.__kor < other.__kor

    def __gt__(self, other):  #7-es 2.
        if not isinstance(other, SPORT):
            return NotImplemented
        return (self.nev, self.__nemzetiseg) > (other.nev, other.__nemzetiseg)

    @staticmethod
    def fiatalok(lista: list[SPORT], evszam: int) -> list[str]:
        nevek = []
        adott_kor= 2022 - int(evszam)
        for i in lista:
            if i.__kor > adott_kor:
                nevek.append(i.nev)
        return nevek


class focistak(SPORT):
    _labda: int

    @property
    def prop(self):
        return self._labda

    @prop.setter
    def prop(self, value: int):
        self._labda = value

    def __init__(self, nev: str, kor: int, labda: int, nemzetiseg="Hungary") -> None:
        super().__init__(nev, kor, nemzetiseg)
        self._labda = labda

    def __repr__(self) -> str:
        return f'{super().__repr__()}, {self._labda}'

    def __str__(self) -> str:
        return f'{super().__str__()}: {self._labda}'