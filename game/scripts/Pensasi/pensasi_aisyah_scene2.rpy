define pensasi_aisyah_scene2_choice2_1_choosen = False

label pensasi_aisyah_scene2:
    scene bg auditorium with dissolve:
        zoom 0.5

    play music campus fadein 1.0

    show raden kasual_biasa at raden_default:
        xalign -0.2
    show aisyah casual_senyum at aisyah_default:
        xalign 1.0
    with dissolve

    if (from_sekar_route == True):
        show raden kasual_tersenyum

        raden "\"Aisyah\""

        show aisyah casual_terkejut

        voice "audio/vo/aisyah/pensasi/pensasi_2_1_oh_raden.ogg"
        aisyah "\"Oh, Raden\""

        voice "audio/vo/aisyah/pensasi/pensasi_2_2_kamu.ogg"
        aisyah "\"Kamu di depan lihat Fania?\""

        show raden kasual_biasa

        raden "\"Lihat sih, tadi juga diajak jalan-jalan sama dia\""

        show aisyah casual_senyum2

        voice "audio/vo/aisyah/pensasi/pensasi_2_3_oh.ogg"
        aisyah "\"oh begitu\""

        voice "audio/vo/aisyah/pensasi/pensasi_2_4_karena.ogg"
        aisyah "\"Karena kamu kesini, jadi tawaran Fania kamu tolak?\""

        show aisyah casual_senyum
        show raden kasual_biasa2

        raden "\"Iya, kenapa emangnya?\""

        show aisyah casual_senyum3

        voice "audio/vo/aisyah/pensasi/pensasi_2_5_gpp.ogg"
        aisyah "\"Tidak apa-apa sih..\""

        show aisyah casual_senyum2

        aisyah "\"Oh iya duduk dulu sini, daripada mengganggu yang di belakang\""

        raden "\"Oh, iya-iya\""
    
    show aisyah casual_senyum
    show raden kasual_biasa

    "Di tengah suasana yang ramai, aku dan Aisyah sudah duduk di kursi barisan depan. Sesekali aku melirik ke arah panggung, mencoba fokus pada presentasi yang sedang berlangsung."

    "Namun, tiba-tiba Aisyah memecah keheningan."

    show aisyah casual_senyum2
    
    aisyah "\"Raden...\""

    raden "\"Kenapa?\""

    show aisyah casual_bingung

    aisyah "\"Kenapa kamu malah ngikut aku--?\""

    aisyah "\"Padahal.. kamu gak suka ginian kan?\""

    menu:
        "Karena ingin bersama mu":
            show raden kasual_ceria

            raden "\"Pengen sama kamu..\""

            show aisyah casual_gugup

            aisyah "\"Haa???\"" with vpunch

            show raden kasual_gugup

            raden "\"Nggak, maksudku... kamu bilang acara ini bermanfaat..\""

            raden "\"Ya... aku pengen lihat-lihat aja. Siapa tahu... mungkin, ehm...\""

            raden "\"Mungkin acara ini memang akan berguna untukku...\""

            show raden kasual_canggung
            show aisyah casual_senyum4

            aisyah "\"Hahaha.. Itu alasanmu?\""

            show raden kasual_gugup

            raden "\"Y-ya, kenapa? Nggak boleh?\""

            show aisyah casual_gugup

            aisyah "\"Boleh sih, tapi cara ngomongmu barusan... agak...\""

            show raden kasual_canggung

            raden "\"Ya udah, nggak usah dibahas lagi...\""

            aisyah "\"Haha.. iya...\""

            $ pensasi_aisyah_scene2_choice2_1_choosen = True

        "Karena memang tertarik dengan acara ini":
            show raden kasual_bingung
        
            raden "\"hhhmm..? Kenapa mikir gitu, syah?\""

            show aisyah casual_senyum2

            aisyah "\"Hahah gak tahu, cuman kayaknya kamu lebih suka kebebasan seperti Fania.\""

            show aisyah casual_senyum
            show raden kasual_tersenyum

            raden "\"Mungkin karena aku emang pengen eksplor.\""

            raden "\"Aku pikir, nggak ada salahnya, kan, belajar sesuatu yang baru?\""

            show aisyah casual_bersemangat

            aisyah "\"Boleh, bagus itu.\""

            show raden kasual_hehe

            raden "\"Karena aku seorang pengelana\""

            show aisyah casual_senyum4

            aisyah "\"Haha.. iya...\""

    "Dan entah kenapa, meskipun aku merasa seperti orang bodoh, senyumnya membuat semua rasa malu itu sepadan."

    jump pensasi_aisyah_scene3

    return