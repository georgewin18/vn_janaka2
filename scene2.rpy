label scene2:
# [Scene 2]
# Latar : Gerbang Masuk PENS, depan parkiran D3, lapmer, di dalam Pascasarjana, Pascasarjana lantai 6, dan di depan Auditorium.
# Karakter: Raden, Santo, dan Aisyah
    scene bg lapmer with dissolve:
        zoom 0.5

    show raden biasa with dissolve:
        zoom 0.2 xalign 0.5 yalign 0.0

    "Pukul 05.55, aku akhirnya sampai di depan kampus. Aku terdiam sejenak dan berpikir"

    raden "Tidak kusangka aku benar benar menjadi seorang Mahasiswa."

    "Suasana di kampus sangatlah ramai dan penuh semangat dan antrian registrasi terlihat sangat ramai. Terlihat sangat banyak mahasiswa yang sangat antusias. Aku pun pergi untuk mengantri, antrian terlihat sangatlah panjang."
    "Meskipun antrian sudah dibagi menjadi empat Banjar. Untungnya, para panitia terlihat sangat terorganisir yang membuat situasinya tetap terkendali. Kemudian aku mendengar seseorang yang mengeluh dibelakangku."

    voice "audio/vo/aisyah/pkkmb1_antriannya_lama.mp3"
    anon "Hmmmmm, ini antrinya lama banget sih," # keluh suara dari belakangku. (Aisyah sedikit kesal)

    show raden biasa with moveinleft:
        zoom 0.2 xalign 0.9 yalign 0.0

    show aisyah kemeja_bingung at Transform(matrixcolor=(silhouette)):
        zoom 0.3 xalign 0.2 yalign 6.0
    with dissolve

    "Aku menoleh ke belakang dan melihat seorang perempuan berkerudung." 

    show aisyah kemeja_bingung with dissolve:
        zoom 0.3 xalign 0.2 yalign 6.0

    "Ekspresi wajahnya terlihat kesal."
    
    "Terlihat dari name card yang dia pakai, sepertinya dia berada dalam satu region yang sama denganku."
    
    "Aku pun mencoba untuk berbicara dengannya."

    raden "Halo." # ucapku. (Raden gugup)
    
    voice "audio/vo/aisyah/pkkmb2_hah.mp3"
    anon "Hah?" # jawab perempuan tersebut, mukanya berkerut menunjukkan kekesalannya. (Siluet Aisyah)

    "\"Melihat ulang wajahnya, membuatku berpikir akan seseorang yang pernah ku kenal.\"" # Aku berpikir sejenak

    raden "{i}Hmm, muka putih nan cantik, berkerudung, dan rasanya wajahnya sangatlah familiar. Apakah aku pernah bertemu dengannya?{/i}" # (Raden berpikir) ujarku dalam hati.

    "Aku masih berpikir. Sampai ketika, perempuan tersebut berbicara."

    show aisyah kemeja_bicara with dissolve

    voice "audio/vo/aisyah/pkkmb3_eh_raden.mp3"
    aisyah "Eh, Raden?" # ucap wanita tersebut. (Aisyah terkejut)

    menu:
        "Waduh, tau namaku dari mana kak?":
            jump scene3_choice1
        "Owh, Aisyah ya":
            jump scene3_after_choice
        "Owh, Fania ya":
            jump scene3_choice3

    return

label scene3_choice1:
    voice "audio/vo/aisyah/pkkmb4_masa_udah_lupa.mp3"
    aisyah "Masa udah lupa?"

    aisyah "Kita kan udah kenalan minggu lalu"

    jump scene3_after_choice

label scene3_choice3:
    voice "audio/vo/aisyah/pkkmb4-3_siapa_lagi.mp3"
    aisyah "{size=+10}Siapa lagi itu?!{/size} Aku Aisyah, masa ga ingat!" with vpunch

    jump scene3_after_choice       

label scene3_after_choice:
    $ renpy.block_rollback()

    "Disaat itulah aku mengingat siapa perempuan yang ada didepan ku ini. Dia adalah Aisyah seorang mahasiswi yang kutemui ketika mengambil jas almamater beberapa Minggu yang lalu. Kami pun berbincang ringan selama antrian bergerak maju."
    
    "Aisyah sekarang tampak lebih santai dan tidak menunjukkan kekesalannya lagi, dan percakapan juga bisa membuat waktu terasa lebih cepat."

    "Akhirnya, tibalah giliranku di meja registrasi."

    "Seorang panitia dengan senyum ramah menyambutku."

    lo1 "Halo, atas nama..? NRP?"

    raden "Raden, dengan NRP …." # jawabku.

    "Setelah registrasi, aku langsung pergi untuk pengecekan barang dan menunggu Aisyah untuk berangkat menuju ke . Disana seorang Panitia bertanya kepada kami."

    lo2 "Region apa dik?" # tanya kakak tersebut.
    raden "Region {b}Aldebaran{/b}, kak" # jawabku.
    lo2 "Aldebaran, itu ada di galaksi Bima Sakti. Berarti, nanti kalian naik tangga terus sampai lantai 6 ya!"
    
    show raden capek
    
    raden "{size=+10}Apa?? Lantai 6??{/size}" with vpunch # sontak diriku kaget. (Raden kaget)
    lo2 "Hahaha, terimalah nasib kalian dan tetap semangat" # kata kakak Panitia tersebut sambil tersenyum. (Panitia senyum)

    "Tidak ada hal yang bisa ku ributkan. Meskipun begitu, berpikir untuk naik menuju lantai 6 saja sudah membuatku malas. Aku pun mencoba untuk mengobrol dengan Aisyah sembari menaiki tangga ini."

    # Singkat cerita. Kami akhirnya sampai di lantai 6. 
    raden "{i}Ternyata, tidak secapek yang kupikir.{/i}" # ujarku dalam hati.

    scene bg depan_auditorium with dissolve:
        zoom 0.5

    show raden biasa:
        zoom 0.2 xalign 0.9 yalign 0.0
    show aisyah kemeja_bicara:
        zoom 0.3 xalign 0.2 yalign 6.0
    with dissolve

    "Kami berdiri di tempat untuk beberapa saat. Sampai ketika, seorang kakak panitia yang menjaga di sekitar sini bertanya kepada kami."

    lo3 "Region apa dik?" # tanya panitia tersebut.

    voice "audio/vo/aisyah/pkkmb5_kami_dari_region.mp3"
    aisyah "Kami dari region Aldebaran kak."
    
    lo3 "Aldebaran?, kalau gitu langsung saja menuju ruangan Auditorium ya!, disana kamu bisa melihat panitia di sana yang menunggu di depan ruangan. Itu adalah ruangan kalian." # jawab kakak panitia tersebut.
    
    raden "Terimakasih kak."

    "Meskipun rasa lelah ini masih terasa. Kami langsung saja menuju ruangan tersebut, dengan pikiran kalau kita bisa langsung duduk setelah memasuki ruangan."

    scene black with dissolve
    with Pause(0.2)    

    jump scene3

    return