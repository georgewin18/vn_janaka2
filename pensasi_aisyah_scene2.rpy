define pensasi_aisyah_scene2_choice2_1_choosen = False

label pensasi_aisyah_scene2:
    scene bg auditorium with dissolve:
        zoom 0.5

    play music campus fadein 1.0

    show raden kasual_biasa:
        zoom 0.48 xalign 0.0 yalign 0.1
    show aisyah kemeja_bicara:
        zoom 0.35 xalign 0.95 yalign -0.7
    with dissolve

    if (from_sekar_route == True):
        show raden kasual_tersenyum

        raden "\"Aisyah\""

        aisyah "\"Oh, Raden\""

        aisyah "\"Kamu di depan lihat Fania?\""

        show raden kasual_biasa

        raden "\"Lihat sih, tadi juga diajak jalan-jalan sama dia\""

        aisyah "\"oh begitu\""

        aisyah "\"Karena kamu kesini, jadi tawaran Fania kamu tolak?\""

        raden "\"Iya, kenapa emangnya?\""

        aisyah "\"Tidak apa-apa sih..\""

        aisyah "\"Oh iya duduk dulu sini, daripada mengganggu yang di belakang\""

        raden "\"Oh, iya-iya\""
    
    "Di tengah suasana yang ramai, aku dan Aisyah sudah duduk di kursi barisan depan. Sesekali aku melirik ke arah panggung, mencoba fokus pada presentasi yang sedang berlangsung."

    "Namun, tiba-tiba Aisyah memecah keheningan."

    aisyah "\"Raden...\""

    raden "\"Kenapa?\""

    show aisyah kemeja_bingung

    aisyah "\"Kenapa kamu malah ngikut aku--?\""

    aisyah "\"Padahal.. kamu gak suka ginian kan?\""

    menu:
        "Karena ingin bersama mu":
            show raden kasual_ceria

            raden "\"Pengen sama kamu..\""

            show aisyah kemeja_canggung

            aisyah "\"Haa???\"" with vpunch

            show raden kasual_gugup

            raden "\"Nggak, maksudku... kamu bilang acara ini bermanfaat..\""

            raden "\"Ya... aku pengen lihat-lihat aja. Siapa tahu... mungkin, ehm...\""

            raden "\"Mungkin acara ini memang akan berguna untukku...\""

            show raden kasual_canggung
            show aisyah kemeja_senyum

            aisyah "\"Hahaha.. Itu alasanmu?\""

            show raden kasual_gugup

            raden "\"Y-ya, kenapa? Nggak boleh?\""

            show aisyah kemeja_canggung

            aisyah "\"Boleh sih, tapi cara ngomongmu barusan... agak...\""

            show raden kasual_canggung

            raden "\"Ya udah, nggak usah dibahas lagi...\""

            aisyah "\"Haha.. iya...\""

            $ pensasi_aisyah_scene2_choice2_1_choosen = True

        "Karena memang tertarik dengan acara ini":
            show raden kasual_bingung
        
            raden "\"hhhmm..? Kenapa mikir gitu, syah?\""

            show aisyah kemeja_bicara

            aisyah "\"Hahah gak tahu, cuman kayaknya kamu lebih suka kebebasan seperti Fania.\""

            show raden kasual_tersenyum

            raden "\"Mungkin karena aku emang pengen eksplor.\""

            raden "\"Aku pikir, nggak ada salahnya, kan, belajar sesuatu yang baru?\""

            show aisyah kemeja_bertekad

            aisyah "\"Boleh, bagus itu.\""

            show raden kasual_biasa

            raden "\"Karena aku seorang pengelana\""

            aisyah "\"Haha.. iya...\""

    "Dan entah kenapa, meskipun aku merasa seperti orang bodoh, senyumnya membuat semua rasa malu itu sepadan."

    jump pensasi_aisyah_scene3

    return