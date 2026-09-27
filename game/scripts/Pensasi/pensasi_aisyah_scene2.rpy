define pensasi_aisyah_scene2_choice2_1_choosen = False

label pensasi_aisyah_scene2:
    scene bg auditorium with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    play music campus fadein 1.0

    show raden kasual_biasa:
        xalign -0.2
        zoom raden_default.zoom
        yalign raden_default.yalign
    show aisyah casual_senyum:
        xalign 1.0
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    with dissolve

    if (from_sekar_route == True):
        show raden kasual_tersenyum:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"Aisyah\""

        show aisyah casual_terkejut:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        voice "audio/vo/aisyah/pensasi/pensasi_2_1_oh_raden.ogg"
        aisyah "\"Oh, Raden\""

        voice "audio/vo/aisyah/pensasi/pensasi_2_2_kamu.ogg"
        aisyah "\"Kamu di depan lihat Fania?\""

        show raden kasual_biasa:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"Lihat sih, tadi juga diajak jalan-jalan sama dia\""

        show aisyah casual_senyum2:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        voice "audio/vo/aisyah/pensasi/pensasi_2_3_oh.ogg"
        aisyah "\"oh begitu\""

        voice "audio/vo/aisyah/pensasi/pensasi_2_4_karena.ogg"
        aisyah "\"Karena kamu kesini, jadi tawaran Fania kamu tolak?\""

        show aisyah casual_senyum:
            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        show raden kasual_biasa2:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"Iya, kenapa emangnya?\""

        show aisyah casual_senyum3:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        voice "audio/vo/aisyah/pensasi/pensasi_2_5_gpp.ogg"
        aisyah "\"Tidak apa-apa sih..\""

        show aisyah casual_senyum2:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        aisyah "\"Oh iya duduk dulu sini, daripada mengganggu yang di belakang\""

        raden "\"Oh, iya-iya\""
    
    show aisyah casual_senyum:
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Di tengah suasana yang ramai, aku dan Aisyah sudah duduk di kursi barisan depan. Sesekali aku melirik ke arah panggung, mencoba fokus pada presentasi yang sedang berlangsung."

    "Namun, tiba-tiba Aisyah memecah keheningan."

    show aisyah casual_senyum2:
    
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    aisyah "\"Raden...\""

    raden "\"Kenapa?\""

    show aisyah casual_bingung:

        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    aisyah "\"Kenapa kamu malah ngikut aku--?\""

    aisyah "\"Padahal.. kamu gak suka ginian kan?\""

    menu:
        "Karena ingin bersama mu":
            show raden kasual_ceria:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Pengen sama kamu..\""

            show aisyah casual_gugup:

                zoom aisyah_default.zoom
                yalign aisyah_default.yalign
            aisyah "\"Haa???\"" with vpunch

            show raden kasual_gugup:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Nggak, maksudku... kamu bilang acara ini bermanfaat..\""

            raden "\"Ya... aku pengen lihat-lihat aja. Siapa tahu... mungkin, ehm...\""

            raden "\"Mungkin acara ini memang akan berguna untukku...\""

            show raden kasual_canggung:
                zoom raden_default.zoom
                yalign raden_default.yalign
            show aisyah casual_senyum4:

                zoom aisyah_default.zoom
                yalign aisyah_default.yalign
            aisyah "\"Hahaha.. Itu alasanmu?\""

            show raden kasual_gugup:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Y-ya, kenapa? Nggak boleh?\""

            show aisyah casual_gugup:

                zoom aisyah_default.zoom
                yalign aisyah_default.yalign
            aisyah "\"Boleh sih, tapi cara ngomongmu barusan... agak...\""

            show raden kasual_canggung:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Ya udah, nggak usah dibahas lagi...\""

            aisyah "\"Haha.. iya...\""

            $ pensasi_aisyah_scene2_choice2_1_choosen = True

        "Karena memang tertarik dengan acara ini":
            show raden kasual_bingung:
        
                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"hhhmm..? Kenapa mikir gitu, syah?\""

            show aisyah casual_senyum2:

                zoom aisyah_default.zoom
                yalign aisyah_default.yalign
            aisyah "\"Hahah gak tahu, cuman kayaknya kamu lebih suka kebebasan seperti Fania.\""

            show aisyah casual_senyum:
                zoom aisyah_default.zoom
                yalign aisyah_default.yalign
            show raden kasual_tersenyum:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Mungkin karena aku emang pengen eksplor.\""

            raden "\"Aku pikir, nggak ada salahnya, kan, belajar sesuatu yang baru?\""

            show aisyah casual_bersemangat:

                zoom aisyah_default.zoom
                yalign aisyah_default.yalign
            aisyah "\"Boleh, bagus itu.\""

            show raden kasual_hehe:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Karena aku seorang pengelana\""

            show aisyah casual_senyum4:

                zoom aisyah_default.zoom
                yalign aisyah_default.yalign
            aisyah "\"Haha.. iya...\""

    "Dan entah kenapa, meskipun aku merasa seperti orang bodoh, senyumnya membuat semua rasa malu itu sepadan."

    jump pensasi_aisyah_scene3

    return
