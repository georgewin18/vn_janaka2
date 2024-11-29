label scene3:
# [Scene 3]
# Latar : Gerbang Masuk PENS, depan parkiran D3, lapmer, di dalam Pascasarjana, Pascasarjana lantai 6, dan di depan Auditorium.
# Karakter: Raden, Santo, dan Aisyah
    scene bg lapmer with dissolve:
        zoom 0.5

    "Pukul 05.55, aku akhirnya sampai di depan kampus. Aku terdiam sejenak dan berpikir"

    raden "Tidak kusangka aku benar benar menjadi seorang Mahasiswa."

    "Suasana di kampus sangatlah ramai dan penuh semangat dan antrian registrasi terlihat sangat ramai. Terlihat sangat banyak mahasiswa yang sangat antusias. Aku pun pergi untuk mengantri, antrian terlihat sangatlah panjang."
    "Meskipun antrian sudah dibagi menjadi empat Banjar. Untungnya, para panitia terlihat sangat terorganisir yang membuat situasinya tetap terkendali. Kemudian aku mendengar seseorang yang mengeluh dibelakangku."

    anon "Hmmmmm, ini antrinya lama banget sih," # keluh suara dari belakangku. (Aisyah sedikit kesal)

    show aisyah kemeja_bingung at Transform(matrixcolor=(silhouette)):
        zoom 0.26 xalign 0.5 yalign 0.8
    with dissolve

    "Aku menoleh ke belakang dan melihat seorang perempuan berkerudung." 
    
    show aisyah kemeja_bingung with dissolve:
        zoom 0.26 xalign 0.5 yalign 0.8

    "Ekspresi wajahnya terlihat kesal."
    
    "Terlihat dari name card yang dia pakai, sepertinya dia berada dalam satu region yang sama denganku."
    
    "Aku pun mencoba untuk berbicara dengannya."

    raden "Halo." # ucapku. (Raden gugup)
    
    anon "Hah?" # jawab perempuan tersebut, mukanya berkerut menunjukkan kekesalannya. (Siluet Aisyah)

    "Melihat ulang wajahnya, membuatku berpikir akan seseorang yang pernah ku kenal." # Aku berpikir sejenak

    raden "{i}Hmm, muka putih nan cantik, berkerudung, dan rasanya wajahnya sangatlah familiar. Apakah aku pernah bertemu dengannya?{/i}" # (Raden berpikir) ujarku dalam hati.

    "Aku masih berpikir. Sampai ketika, perempuan tersebut berbicara."

    show aisyah kemeja_bicara with dissolve:
        zoom 0.26 xalign 0.5 yalign 0.8

    aisyah "Eh, Raden?" # ucap wanita tersebut. (Aisyah terkejut)

    raden "Waduh, tau namaku dari mana kak?." # ucapku dengan kebingungan. (Raden bingung)

    "Disaat itulah aku akhirnya mengingat siapa perempuan yang ada didepan ku ini. Dia adalah Aisyah seorang mahasiswi yang kutemui ketika mengambil jas almamater beberapa Minggu yang lalu. Kami pun berbincang ringan selama antrian bergerak maju."
    
    "Aisyah sekarang tampak lebih santai dan tidak menunjukkan kekesalannya lagi, dan percakapan juga bisa membuat waktu terasa lebih cepat."

    "Akhirnya, tibalah giliranku di meja registrasi."
    
    hide aisyah with dissolve

    "Seorang panitia dengan senyum ramah menyambutku."

    lo1 "Halo, atas nama..? NRP?"

    raden "Raden, dengan NRP …." # jawabku.

    "Setelah registrasi, aku langsung pergi untuk pengecekan barang dan menunggu Aisyah untuk berangkat menuju ke . Disana seorang Panitia bertanya kepada kami."

    lo2 "Region apa dik?" # tanya kakak tersebut.
    raden "Region {b}Aldebaran{/b}, kak" # jawabku.
    lo2 "Aldebaran, itu ada di galaksi Bima Sakti. Berarti, nanti kalian naik tangga terus sampai lantai 6 ya!"
    raden "Apa?? Lantai 6??" # sontak diriku kaget. (Raden kaget)
    lo2 "Hahaha, terimalah nasib kalian dan tetap semangat" # kata kakak Panitia tersebut sambil tersenyum. (Panitia senyum)

    "Tidak ada hal yang bisa ku ributkan. Meskipun begitu, berpikir untuk naik menuju lantai 6 saja sudah membuatku malas. Aku pun mencoba untuk mengobrol dengan Aisyah sembari menaiki tangga ini."

    # Singkat cerita. Kami akhirnya sampai di lantai 6. 
    raden "{i}Ternyata, tidak secapek yang kupikir.{/i}" # ujarku dalam hati.

    scene bg depan_auditorium with dissolve:
        zoom 0.5

    "Kami berdiri di tempat untuk beberapa saat. Sampai ketika, seorang kakak panitia yang menjaga di sekitar sini bertanya kepada kami."

    lo3 "Region apa dik?" # tanya panitia tersebut.

    sekelompok "Kami dari region Aldebaran kak." # ucap kami secara bersamaan.
    
    lo3 "Aldebaran?, kalau gitu langsung saja menuju ruangan Auditorium ya!, disana kamu bisa melihat panitia di sana yang menunggu di depan ruangan. Itu adalah ruangan kalian." # jawab kakak panitia tersebut.
    
    sekelompok "Terimakasih kak."

    "Meskipun rasa lelah ini masih terasa. Kami langsung saja menuju ruangan tersebut, dengan pikiran kalau kita bisa langsung duduk setelah memasuki ruangan."

    scene black with dissolve
    with Pause(0.2)

    jump scene4

    return


