label prolog_day2_scene5:
    #bg gang
    scene bg jalan_gang:
        size (config.screen_width, config.screen_height)
        truecenter

    play music santo_bgm fadein 1.0

    show raden kemeja_biasa:
        zoom raden_default.zoom
        xalign -0.2
        yalign raden_default.yalign
    show santo kemeja_netral:
        zoom santo_default.zoom
        xalign 1.0
    with dissolve

    show santo kemeja_bicara:
        zoom santo_default.zoom
    santo "\"Den\""

    show santo kemeja_netral:
        zoom santo_default.zoom
    show raden kemeja_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Santo?! Kamu belum pulang\""

    show raden kemeja_biasa:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kemeja_bicara:

        zoom santo_default.zoom
    santo "\"Bentar lagi mau pulang, capek deh, pengen segera rebahan, tapi besok masih masuk pagi lagi\""

    #Raden senyumm
    show santo kemeja_netral:
        zoom santo_default.zoom
    show raden kemeja_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Santo, kupikir kamu tipe orang yang mageran.\""

    show raden kemeja_biasa:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kemeja_senyum:

        zoom santo_default.zoom
    santo "\"Hm? Kamu gak salah kok.\""

    show raden kemeja_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Loh, tapi kok hari ini kelihatannya kamu kayak serius dan niat banget gitu ngerjain tugas PKKMB ini?\""

    show raden kemeja_biasa:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kemeja_netral:

        zoom santo_default.zoom
    "Santo tidak merespon, dan menengok ke arah Fania yang siluetnya masih terlihat dari kejauhan. Lalu kembali menengok pada ku sambil menggaruk bagian belakang leher nya."

    show santo kemeja_bicara:

        zoom santo_default.zoom
    santo "\"Ya… kalau tiba-tiba kelompok ku disuruh ngulang PKKMB kan lebih malesin.\""

    show santo kemeja_netral:
        zoom santo_default.zoom
    show raden kemeja_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Loh, emang nya bisa?\""

    show raden kemeja_biasa:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kemeja_bicara:

        zoom santo_default.zoom
    santo "\"Siapa tahu, Jaga-jaga aja, Duluan ya.\""

    show raden kemeja_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(0.3)

    centered "Aku hanya mengangguk pelan, tubuh terasa lelah setelah seharian penuh aktivitas. Aku melangkah pulang, membiarkan keheningan menyelimuti pikiranku."

    stop music fadeout 2.0

    jump prolog_day3_scene1
