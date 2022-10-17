import model

def main():
    n=int(input())
    if n<=0:
        return

    lista=[]
    for i in range(n):
        line=input()
        tokens=line.split(";")
        if len(tokens)==3:
            sportolo=model.sport(tokens[0],tokens[1],int(tokens[2]))
            lista.append(sportolo)

        if len(tokens)==4:
            focista=model.sport(tokens[0],tokens[1],int(tokens[2]),int(tokens[3]))
            lista.append(focista)

        lista.sort()
        for i in lista:
            print(i)


    if __name__ == "__main__":
        main()