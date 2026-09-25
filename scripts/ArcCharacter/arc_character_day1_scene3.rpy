label arc_character_day1_scene3:
    scene bg kantin with dissolve:
        zoom 0.5

    show raden kasual_biasa at raden_default:
        xalign -0.2
    show santo kasual_netral at santo_default:
        xalign 1.0
    with dissolve

    "Setelah kejadian Aisyah dan si perokok, kami akhirnya benar-benar antre beli makanan. Aku dan Santo berdiri di depan warung nasi goreng yang sudah lumayan ramai. Erin duduk duluan, jagain meja."

    show santo kasual_bicara

    santo "\"Nasi goreng dua ya Bang.\""

    show santo kasual_netral

    "Penjual mengangguk cepat, Wajan mulai berdentang."

    anon "\"Nasi goreng satu...!\""

    hide santo with dissolve
    show fania casual_dingin at fania_default:
        xalign 1.4
    with moveinright

    "Saat aku menoleh, seseorang di sampingku sudah maju mengambil pesanan duluan. Aku nyaris nggak ngeh—tapi ternyata itu Fania"

    menu:
        "Sapa fania":
            show raden kasual_tersenyum

            raden "\"Eh... Fania?\""

            show raden kasual_biasa
            show fania casual_senyum_normal_biasa at fania_default:
                xalign 1.25
            with moveinright

            fania "\"Oh Raden?\""

            show raden kasual_tersenyum

            raden "\"Kamu sering beli nasgor di sini?\""

            show raden kasual_biasa

            fania "\"Iya. Cepet dan enak.\""

            fania "\"Aku duluan ya\""

            show raden kasual_tersenyum

            raden "\"Oh, iya. Sip. Semangat, ya.\""

            show raden kasual_biasa

            fania "\"Makasih.\""

            hide fania with moveoutright

            "Fania menggaguk singkat, dan pergi."

            jump arc_character_day1_scene4

        "Biarkan Saja":
            "Fania mengambil nasi goreng, membayar, dan pergi tanpa menoleh."

            hide fania with moveoutright

            jump arc_character_day1_scene4

    return