define chapter2_aisyah_scene3_choice1_choosen = False

label chapter2_aisyah_scene3:
    #jalan_d4_kantin

    #Suasana agak intens
    #Raden, Aisyah, Santo netral

    scene jalan_d4_kantin with dissolve:
        zoom 0.5

    show raden kemeja_biasa at flip:
        zoom 0.54 xalign 1.3 yalign 0.05

    show aisyah kemeja_bicara:
        zoom 0.34 xalign 0.5 yalign -1.0

    show santo kemeja_biasa at flip:
        zoom 1.35 xalign 8.0 yalign 0.08
    with dissolve

    "Saat aku, Aisyah, dan Santo berjalan melewati jalan setapak di kampus, Segerombol mahasiswa—sepertinya kakak tingkat tiba-tiba menghadang jalan kami. Matanya menatap kami dengan tajam, mengeluarkan aura tidak bersahabat."

    anon "\"Eh, kalian bertiga, kan? Yang tadi sok,\""#katanya sambil menunjuk ke arah kami.

    "Aku terdiam, mencoba memahami situasi. Sementara itu, Aisyah maju selangkah dengan ekspresi tegas."

    aisyah "\"Kalau ada masalah, ngomong baik—\""#kata Aisyah dengan nada dingin.

    anon "\"Sok-sokan ngatur gue tadi, kan? Nggak usah pura-pura bego!\""

    #Suasana intens

    "Sebelum suasana semakin panas, Aku melangkah maju, berdiri di antara pria itu dan Aisyah."

    menu:
        "Tetap tenang":
            $ chapter2_aisyah_scene3_choice1_choosen = True
        
        "Lawan":
            $ chapter2_aisyah_scene3_choice1_choosen = False

    if (chapter2_aisyah_scene3_choice1_choosen == True):
        #Raden canggung

        raden "\"Kami nggak cari ribut. Kalau ada salah paham, mending dibicarakan baik-baik. Kalau nggak, mending udahan aja,\""

        "Pria itu tampak kesal, tetapi dia tetap mencoba menantang."

        anon "\"Lo sok tenang banget, bocah. Mau ngajarin gue cara hidup?\""

    else:
        #Raden Kesal

        raden "\"Terus mau apa kalian? Capek ngurusin kalian baik-baik terus!\""

        "Pria itu tertawa seolah malah tertantang dengan ucapanku."

        anon "\"Hahaha… Emang perlu dikasih pelajaran.\""

    jump chapter2_aisyah_scene4

    return