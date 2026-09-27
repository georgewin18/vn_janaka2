label prolog_day1_scene2:
# [Scene 2]
# Latar : Gerbang Masuk PENS, depan parkiran D3, lapmer, di dalam Pascasarjana, Pascasarjana lantai 6, dan di depan Auditorium.
# Karakter: Raden, Santo, dan Aisyah
    scene bg lapmer_ramai with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kemeja_biasa2:
        xalign 0.45
        zoom raden_default.zoom
        yalign raden_default.yalign
    with dissolve

    "Pukul 05.55, aku akhirnya sampai di depan kampus. Aku terdiam sejenak dan berpikir"

    raden "\"Tidak kusangka aku benar benar menjadi seorang Mahasiswa.\""

    "Suasana di kampus sangatlah ramai dan penuh semangat dan antrian registrasi terlihat sangat ramai. Terlihat sangat banyak mahasiswa yang sangat antusias. Aku pun pergi untuk mengantri, antrian terlihat sangatlah panjang."
    "Meskipun antrian sudah dibagi menjadi empat Banjar. Untungnya, para panitia terlihat sangat terorganisir yang membuat situasinya tetap terkendali. Kemudian aku mendengar seseorang yang mengeluh dibelakangku."

    stop music fadeout 2.0

    voice "audio/vo/aisyah/pkkmb1_antriannya_lama.ogg"
    anon "\"Hmmmmm, ini antrinya lama banget sih,\"" # keluh suara dari belakangku. (Aisyah sedikit kesal)

    voice sustain

    show blank at Transform(xsize=config.screen_width, ysize=config.screen_height, xpos=0, ypos=0) with dissolve

    voice sustain

    hide blank with dissolve

    voice sustain

    show raden kemeja_biasa2:
        xalign -0.2
        zoom raden_default.zoom
        yalign raden_default.yalign
    with moveinleft

    show aisyah kemeja_kesal at Transform(matrixcolor=(silhouette)):
        zoom aisyah_default.zoom
        xalign 1.0
        yalign aisyah_default.yalign
    with dissolve

    "Aku menoleh ke belakang dan melihat seorang perempuan berkerudung." 

    hide aisyah with dissolve

    show aisyah kemeja_kesal:
        xalign 1.0
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    with dissolve

    play music aisyah_bgm fadein 1.0

    "Ekspresi wajahnya terlihat kesal."
    
    "Terlihat dari name card yang dia pakai, sepertinya dia berada dalam satu region yang sama denganku."
    
    "Aku pun mencoba untuk berbicara dengannya."

    show raden kemeja_gugup:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Halo.\"" # ucapku. (Raden gugup)
    
    voice "audio/vo/aisyah/pkkmb2_hah.ogg"
    show aisyah kemeja_bingung with dissolve:
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    anon "\"Hah?\"" # jawab perempuan tersebut, mukanya berkerut menunjukkan kekesalannya. (Siluet Aisyah)

    show raden kemeja_bingung:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Melihat ulang wajahnya, membuatku berpikir akan seseorang yang pernah ku kenal." # Aku berpikir sejenak

    raden "{i}Hmm, muka putih nan cantik, berkerudung, dan rasanya wajahnya sangatlah familiar. Apakah aku pernah bertemu dengannya?{/i}" # (Raden berpikir) ujarku dalam hati.

    "Aku masih berpikir. Sampai ketika, perempuan tersebut berbicara."

    show aisyah kemeja_terkejut with dissolve:

        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    voice "audio/vo/aisyah/pkkmb3_eh_raden.ogg"
    aisyah "\"Eh, Raden?\"" with vpunch # ucap wanita tersebut. (Aisyah terkejut)

    menu:
        "Waduh, tau namaku dari mana kak?":
            show raden kemeja_gugup:

                zoom raden_default.zoom
                yalign raden_default.yalign
            jump scene3_choice1
        "Owh, Aisyah ya":
            show raden kemeja_biasa:

                zoom raden_default.zoom
                yalign raden_default.yalign
            show aisyah kemeja_senyum2:
                zoom aisyah_default.zoom
                yalign aisyah_default.yalign
            aisyah "\"Hai!!\""

            jump scene3_after_choice
        "Owh, Fania ya":
            show raden kemeja_biasa:

                zoom raden_default.zoom
                yalign raden_default.yalign
            jump scene3_choice3

    return

label scene3_choice1:
    #$ renpy.block_rollback()

    show aisyah kemeja_serius:
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    voice "audio/vo/aisyah/pkkmb4_masa_udah_lupa.ogg"
    aisyah "\"Masa udah lupa?\""

    aisyah "\"Kita kan udah kenalan minggu lalu\""

    jump scene3_after_choice

label scene3_choice3:
    #$ renpy.block_rollback()

    show aisyah kemeja_kesal:
        xalign 1.0
        linear 0.2 xalign 0.75

        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    voice "audio/vo/aisyah/pkkmb4-3_siapa_lagi.ogg"
    aisyah "\"{size=+10}Siapa lagi itu?!{/size} Aku Aisyah, masa ga ingat!\"" with vpunch

    show aisyah:
        xalign 1.0
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    with moveinright

    jump scene3_after_choice       

label scene3_after_choice:
    #$ renpy.block_rollback()

    "Disaat itulah aku mengingat siapa perempuan yang ada didepan ku ini. Dia adalah Aisyah seorang mahasiswi yang kutemui ketika mengambil jas almamater beberapa Minggu yang lalu. Kami pun berbincang ringan selama antrian bergerak maju."

    show aisyah kemeja_senyum1:

        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    "Aisyah sekarang tampak lebih santai dan tidak menunjukkan kekesalannya lagi, dan percakapan juga bisa membuat waktu terasa lebih cepat."

    stop music fadeout 2.0

    hide aisyah with dissolve
    show raden kemeja_biasa2:
        xalign 0.45
        zoom raden_default.zoom
        yalign raden_default.yalign
    with moveinright

    "Akhirnya, tibalah giliranku di meja registrasi."

    play music raden_bgm fadein 1.0

    "Seorang panitia dengan senyum ramah menyambutku."

    lo1 "\"Halo, atas nama..? NRP?\""

    show raden kemeja_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Raden, dengan NRP...\"" # jawabku.

    show raden kemeja_biasa2:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Setelah registrasi, aku langsung pergi untuk pengecekan barang dan menunggu Aisyah untuk berangkat menuju ke . Disana seorang Panitia bertanya kepada kami."

    lo2 "\"Region apa dik?\"" # tanya kakak tersebut.

    show raden kemeja_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Region {b}Aldebaran{/b}, kak\"" # jawabku.

    show raden kemeja_biasa2:

        zoom raden_default.zoom
        yalign raden_default.yalign
    lo2 "\"Aldebaran, itu ada di galaksi Bima Sakti. Berarti, nanti kalian naik tangga terus sampai lantai 6 ya!\""
    
    show raden kemeja_panik:
    
        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"{size=+10}Apa?? Lantai 6??{/size}\"" with vpunch # sontak diriku kaget. (Raden kaget)
    lo2 "\"Hahaha, terimalah nasib kalian dan tetap semangat\"" # kata kakak Panitia tersebut sambil tersenyum. (Panitia senyum)

    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    "Tidak ada hal yang bisa ku ributkan. Meskipun begitu, berpikir untuk naik menuju lantai 6 saja sudah membuatku malas. Aku pun mencoba untuk mengobrol dengan Aisyah sembari menaiki tangga ini."

    # Singkat cerita. Kami akhirnya sampai di lantai 6. 
    raden "{i}Ternyata, tidak secapek yang kupikir.{/i}" # ujarku dalam hati.

    scene bg depan_auditorium_ramai with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kemeja_biasa:
        xalign -0.2
        zoom raden_default.zoom
        yalign raden_default.yalign
    show aisyah kemeja_senyum1:
        xalign 1.0
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    with dissolve

    "Kami berdiri di tempat untuk beberapa saat. Sampai ketika, seorang kakak panitia yang menjaga di sekitar sini bertanya kepada kami."

    lo3 "\"Region apa dik?\"" # tanya panitia tersebut.

    show aisyah kemeja_senyum2:
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    voice "audio/vo/aisyah/pkkmb5_kami_dari_region.ogg"
    aisyah "\"Kami dari region Aldebaran kak.\""
    
    show aisyah kemeja_senyum1:
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    lo3 "\"Aldebaran?, kalau gitu langsung saja menuju ruangan Auditorium ya!, disana kamu bisa melihat panitia di sana yang menunggu di depan ruangan. Itu adalah ruangan kalian.\"" # jawab kakak panitia tersebut.
    
    show raden kemeja_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Terimakasih kak.\""

    show raden kemeja_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Meskipun rasa lelah ini masih terasa. Kami langsung saja menuju ruangan tersebut, dengan pikiran kalau kita bisa langsung duduk setelah memasuki ruangan."

    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(0.2)    

    jump prolog_day1_scene3

    return
