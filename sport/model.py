from __future__ import annotations
from functools import total_ordering
@total_ordering

class sport:
      nev: str
      __nemzet: str
      __kor: int

      @property
      def prop(self):
           return self.__nemzet, self.__kor

      @prop.setter
      def prop(self, value: str,value1: str, value2: int):
           self.nev: value
           self.__nemzet: value1
           self.__kor: value2


      def __init__(self, nev: str,kor: int, nemzet: "Hungary") -> None:
           self.nev = nev
           self.__kor = kor
           self.__nemzet = nemzet

      def __repr__(self) ->str:
           return f'{self.nev}, {self.__kor}, {self.__nemzet}'

      def __str__(self) ->str:
           return f'{self.nev} ({self.__nemzet}, {self.__kor})'

      def __eq__(self, other) -> bool:
           if not isinstance(other , sport):
                return NotImplemented
           return(self.nev, self.__nemzet, self.__kor) == (other.nev, other.__nemzet, other.__kor)

      def __lt__(self, other):
           if not isinstance(other, sport):
                return NotImplemented
           return (self.__kor) < (other.__kor)

      def __gt__(self, other):
           if not isinstance(other,sport):
                return NotImplemented
           return (self.nev, self.__nemzet) > (other.nev,other.__nemzet)

      @staticmethod
      def fiatalok(lista: list[sport], evszam: int) -> list[str]:
           nevek = []
           adott_kor = 22 - int(evszam)
           for i in lista:
                if i.__kor < adott_kor:
                     nevek.append(i.nev)
           return nevek

class focista(sport):
           _labda: int

           @property
           def prop(self):
                return self._labda

           @prop.setter
           def prop_set(self, value: int):
                self._labda=value

           def __init__(self,nev: str,kor: int,labda: int,nemzet: "Hungary") -> None:
                super.__init__(nev,kor, nemzet)
                self._labda= labda

           def __repr__(self) -> str:
                return f'{super.__repr__()},{self._labda}'

           def __str__(self) -> str:
                return f'{super.__str__()}: {self._labda}'



























