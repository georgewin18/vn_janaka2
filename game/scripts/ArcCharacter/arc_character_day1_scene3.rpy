label arc_character_day1_scene3:
    scene bg kantin with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kasual_biasa:
        xalign -0.2
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kasual_netral:
        xalign 1.0
        zoom santo_default.zoom
    with dissolve

    "Setelah kejadian Aisyah dan si perokok, kami akhirnya benar-benar antre beli makanan. Aku dan Santo berdiri di depan warung nasi goreng yang sudah lumayan ramai. Erin duduk duluan, jagain meja."

    show santo kasual_bicara:

        zoom santo_default.zoom
    santo "\"Nasi goreng dua ya Bang.\""

    show santo kasual_netral:

        zoom santo_default.zoom
    "Penjual mengangguk cepat, Wajan mulai berdentang."

    anon "\"Nasi goreng satu...!\""

    hide santo with dissolve
    show fania casual_dingin:
        xalign 1.4
        zoom fania_default.zoom
        yalign fania_default.yalign
    with moveinright

    "Saat aku menoleh, seseorang di sampingku sudah maju mengambil pesanan duluan. Aku nyaris nggak ngeh—tapi ternyata itu Fania"

    menu:
        "Sapa fania":
            show raden kasual_tersenyum:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Eh... Fania?\""

            show raden kasual_biasa:
                zoom raden_default.zoom
                yalign raden_default.yalign
            show fania casual_senyum_normal_biasa:
                xalign 1.25
                zoom fania_default.zoom
                yalign fania_default.yalign
            with moveinright

            fania "\"Oh Raden?\""

            show raden kasual_tersenyum:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Kamu sering beli nasgor di sini?\""

            show raden kasual_biasa:

                zoom raden_default.zoom
                yalign raden_default.yalign
            fania "\"Iya. Cepet dan enak.\""

            fania "\"Aku duluan ya\""

            show raden kasual_tersenyum:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Oh, iya. Sip. Semangat, ya.\""

            show raden kasual_biasa:

                zoom raden_default.zoom
                yalign raden_default.yalign
            fania "\"Makasih.\""

            hide fania with moveoutright

            "Fania menggaguk singkat, dan pergi."

            jump arc_character_day1_scene4

        "Biarkan Saja":
            "Fania mengambil nasi goreng, membayar, dan pergi tanpa menoleh."

            hide fania with moveoutright

            jump arc_character_day1_scene4

    return
