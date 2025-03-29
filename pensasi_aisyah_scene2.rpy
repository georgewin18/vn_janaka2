define pensasi_aisyah_scene2_choice2_1_choosen = False

label pensasi_aisyah_scene2:
    scene bg auditorium with dissolve:
        zoom 0.5

    if (from_sekar_route == True):
        raden "\"Aisyah\""

        aisyah "\"Oh, Raden\""

        aisyah "\"Kamu di depan lihat Fania?\""

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

    aisyah "\"Kenapa kamu malah ngikut aku--?\""

    aisyah "\"Padahal.. kamu gak suka ginian kan?\""

    menu:
        "Karena ingin bersama mu":
            raden "\"Pengen sama kamu..\""

            aisyah "\"Haa?\"" with vpunch

            raden "\"Nggak, maksudku... kamu bilang acara ini bermanfaat..\""

            raden "\"Ya... aku pengen lihat-lihat aja. Siapa tahu... mungkin, ehm...\""

            raden "\"Mungkin acara ini memang akan berguna untukku...\""

            aisyah "\"Hahaha.. Itu alasanmu?\""

            raden "\"Y-ya, kenapa? Nggak boleh?\""

            aisyah "\"Boleh sih, tapi cara ngomongmu barusan... agak...\""

            raden "\"Ya udah, nggak usah dibahas lagi...\""

            aisyah "\"Haha.. iya...\""

            $ pensasi_aisyah_scene2_choice2_1_choosen = True

        "Karena memang tertarik dengan acara ini":
            raden "\"hhhmm..? Kenapa mikir gitu, syah?\""

            aisyah "\"Hahah gak tahu, cuman kayaknya kamu lebih suka kebebasan seperti Fania.\""

            raden "\"Mungkin karena aku emang pengen eksplor.\""

            raden "\"Aku pikir, nggak ada salahnya, kan, belajar sesuatu yang baru?\""

            aisyah "\"Boleh, bagus itu.\""

            raden "\"Karena aku seorang pengelana\""

            aisyah "\"Haha.. iya...\""

    "Dan entah kenapa, meskipun aku merasa seperti orang bodoh, senyumnya membuat semua rasa malu itu sepadan."

    jump pensasi_aisyah_scene3

    return