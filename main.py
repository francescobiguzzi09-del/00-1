from brano import Brano
from CD import CD

if __name__=="__main__":
    brano1 = Brano("kahba","mock", 67)
    brano2 = Brano("zebby","mock", 100)
    brano3 = Brano("kariben","mock", 120)
    
    print(brano1)
    print(brano2)
    print(brano3)
    
    cd1 = CD("la kasba", "mock", [brano1, brano2, brano3])
    print(cd1.durata_totale)
    print(cd1)
    