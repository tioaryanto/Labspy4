#PRAKTIKUM 1
#TUGAS PRAKTIKUM
#TIO ARYANTO

Datanama      =[]
Datanim       =[]
Datatugas     =[]
Datauts       =[]
Datauas       =[] 
Datanilaiakhir=[]

jawab="y"
while jawab=="y":
    nama       = (input("Nama        : "))
    nim        = (input("Nim         : "))
    nilaitugas = (input("Nilai tugas : "))
    nilaiuts   = (input("Nilai uts   : "))
    nilaiuas   = (input("Nilai uas   : "))
    ntugas     = float (nilaitugas) * 0.30
    nuts       = float (nilaiuts) * 0.35
    nuas       = float (nilaiuas) * 0.35
    nilaiakhir = ntugas + nuts + nuas

    Datanama.append(nama)
    Datanim.append(nim)
    Datatugas.append(nilaitugas)
    Datauts.append(nilaiuts)
    Datauas.append(nilaiuas)
    Datanilaiakhir.append(nilaiakhir)

    jawab=input("Tambah data (y/t)?")
    if jawab=="t":
        print    ("============================================================")
        print    ("|NO| NAMA | NIM | TUGAS | UTS | UAS | AKHIR |")
        print    ("============================================================")
        for i in range (len(Datanama)):
            print("|",i+i,"|",Datanama[i],"|",Datanim[i],"|",Datatugas[i],"|",Datauas[i],"|",Datanilaiakhir[i],"|")
            print("============================================================")






