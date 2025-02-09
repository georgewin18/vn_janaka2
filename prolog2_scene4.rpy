label prolog2_scene4:
    #bg gang
    scene bg lap_futsal:
        zoom 0.5

    show raden biasa:
        zoom 0.2 xalign -0.2 yalign 0.0
    "Saat itu, aku tiba-tiba berhenti, mengingat pertemuanku dengan Fania kemarin. Fania yang saat itu terlihat begitu santai terasa sangat berbeda dari yang sekarang. Ini mengganggu pikiranku, serasa ingin menghampirinya."

    show fania jas_biasa:
        zoom 1.1 xalign 1.9 yalign 0.0

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
        xalign 0.2
    with moveinright

    raden "Fania!"

    #fania dingin

    fania "Ya?"

    #raden canggung
    raden "ummmm…. nama ku Raden… haha…."

    fania "Iya, aku udah liat dari nametag mu"

    #raden gugup
    raden "Gini…. Fania… kamu…"

    #fania gugup
    "Fania melihatku dengan bingung, menunggu ku untuk melanjutkan kalimat ku"

    raden "Kamu terlihat berbeda"

    #fania terkejut
    "Fania terlihat kaget mendengar nya dan hanya berdiri diam."

    raden "Gini… kemarin.. kan kamu keliatan kayak rileks banget gitu… dan sekarang ku liat kamu sekarang.. kek kaku banget gitu, kayak kamu nahan sesuatu… jadi aku cuman pengen bilang… menurutku... aku lebih suka kamu yang kemarin…"

    "Raden menggaruk pipinya dengan canggung."

    #special moment
    scene bg lap_futsal with dissolve

    "Fania membalikkan badan perlahan, memperlihatkan punggungnya. Dia menoleh sebentar ke belakang, terlihat ragu, tapi akhirnya bibirnya bergerak."

    fania "*********"#bipp suara sensor

    "Suaranya sangat pelan, nyaris seperti gumaman yang hanya bisa didengar angin. Aku mencoba memahami apa yang dia katakan, tapi terlalu samar untuk dimengerti."

    "Tanpa banyak basa-basi, dia langsung berjalan cepat menjauh. Aku masih terdiam di tempat, tubuhku seakan terkunci oleh kebingungan dan rasa penasaran."

    "Apa yang Fania ingin sampaikan?"

    "Aku juga kenapa..? Kenapa aku tiba-tiba bilang begitu ke dia..?"

    "Aku tidak mengerti…"

    show black with dissolve
    jump prolog2_scene5

