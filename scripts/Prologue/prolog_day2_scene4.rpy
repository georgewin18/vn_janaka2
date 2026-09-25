init:
    transform pan_up:
        yalign 1.0
        linear 5.0 yalign 0.2

label prolog_day2_scene4:
    #bg gang
    scene bg jalan_gang with dissolve:
        zoom 0.5

    show raden kemeja_biasa with dissolve:
        zoom 0.54 xalign -0.2 yalign 0.05
    "Saat itu, aku tiba-tiba berhenti, mengingat pertemuanku dengan Fania kemarin. Fania yang saat itu terlihat begitu santai terasa sangat berbeda dari yang sekarang. Ini mengganggu pikiranku, serasa ingin menghampirinya."

    show fania kemeja_dingin with dissolve:
        zoom 1.35 xalign 1.5 yalign 0.03

    menu:
        "Hampiri dia":
            jump prolog2_scene4_after_choice1
        "Gk usah deh":
            "Aku melanjutkan langkah pulang, tapi rasa cemas terhadap Fania terus mengganggu pikiranku."
            jump prolog2_scene4_after_choice1

label prolog2_scene4_after_choice1:
    #Suasana Cool dan sedikit romantiss

    "Meskipun agak ragu-ragu aku akhirnya menghampiri Fania dan memanggilnya."
    show raden:
        xalign 0.0
    with moveinright

    show raden kemeja_tersenyum
    raden "\"Fania!\""

    #fania dingin

    voice "audio/vo/fania/prolog2/prolog2_5_ya.flac"
    fania "\"Ya?\""

    #raden canggung
    show raden kemeja_gugup
    raden "\"ummmm…. nama ku Raden… haha….\""

    show raden kemeja_canggung
    voice "audio/vo/fania/prolog2/prolog2_6_iya_aku_udah_liat.flac"
    fania "\"Iya, aku udah liat dari nametag mu\""

    #raden gugup
    show raden kemeja_gugup

    raden "\"Gini…. Fania… kamu…\""

    #fania gugup
    "Fania melihatku dengan bingung, menunggu ku untuk melanjutkan kalimat ku"

    stop music fadeout 2.0

    raden "\"Kamu terlihat berbeda\""

    #fania terkejut
    "Fania terlihat kaget mendengar nya dan hanya berdiri diam."

    raden "\"Gini… kemarin.. kan kamu keliatan kayak rileks banget gitu… dan sekarang ku liat kamu sekarang.. kek kaku banget gitu, kayak kamu nahan sesuatu… jadi aku cuman pengen bilang… menurutku... aku lebih suka kamu yang kemarin…\""

    "Raden menggaruk pipinya dengan canggung."

    #special moment
    scene bg lap_futsal with dissolve:
        zoom 0.5

    scene blank with dissolve

    play music romantic fadein 1.0

    show fania_prolog at pan_up:
        zoom 1.5 xalign 0.45
    with dissolve
    
    pause 4.0

    scene fania_prolog with dissolve:
        zoom 0.75

    pause 1.5

    "Fania membalikkan badan perlahan, memperlihatkan punggungnya. Dia menoleh sebentar ke belakang, terlihat ragu, tapi akhirnya bibirnya bergerak."

    fania "\"*********\""#bipp suara sensor

    "Suaranya sangat pelan, nyaris seperti gumaman yang hanya bisa didengar angin. Aku mencoba memahami apa yang dia katakan, tapi terlalu samar untuk dimengerti."

    scene blank with dissolve

    "Tanpa banyak basa-basi, dia langsung berjalan cepat menjauh. Aku masih terdiam di tempat, tubuhku seakan terkunci oleh kebingungan dan rasa penasaran."

    "Apa yang Fania ingin sampaikan?"

    "Aku juga kenapa..? Kenapa aku tiba-tiba bilang begitu ke dia..?"

    "Aku tidak mengerti…"

    stop music fadeout 2.0

    show black with dissolve
    
    jump prolog_day2_scene5