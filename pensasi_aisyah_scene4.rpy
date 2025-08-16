init:
    transform pan_left:
        xalign 1.0
        linear 5.0 xalign 0.5

    transform pan_right:
        xalign 0.0
        linear 4.5 xalign 0.5

label pensasi_aisyah_scene4:
    #depan pasca
    scene bg lapmer with dissolve:
        zoom 0.5

    "Waktu sudah menunjukkan sekitar pukul satu siang ketika kami melangkah keluar dari masjid. Udara siang yang panas langsung menyambut, membuat bayangan kami tampak jelas di jalanan kampus."

    show raden kasual_biasa at raden_default:
        xalign -0.2
    show aisyah casual_senyum at aisyah_default:
        xalign 1.0
    with dissolve

    aisyah "\"Sekarang mau kemana?\""

    show raden kasual_tersenyum

    raden "\"Kalau begitu ke booth robotik gimana?\""

    show raden kasual_biasa
    show aisyah casual_senyum2

    aisyah "\"Boleh sih, tapi bukannya kamu udah di lantai 1 tadi?\""

    show aisyah casual_senyum
    show raden kasual_tersenyum

    raden "\"Tadi kan rame, belum sempat eksplor banget di sana.\""

    show aisyah casual_senyum3

    aisyah "\"Yaudah, ayok!\""

    show raden kasual_biasa

    stop music fadeout 2.0

    "Dia langsung berjalan cepat melewatiku, wajahnya berbinar-binar. Antusiasmenya terasa menular, membuatku ikut mempercepat langkah agar tidak tertinggal."

    ## SPECIAL MOMENT

    play music aisyah_bgm fadein 1.0

    scene blank with dissolve

    show aisyah_pensasi at pan_left:
        zoom 1.5
    with dissolve

    pause 3.0

    hide aisyah_pensasi

    show aisyah_pensasi at pan_right:
        zoom 1.0
    with dissolve

    pause 2.0

    scene aisyah_pensasi with dissolve:
        zoom 0.75

    pause 1.5

    aisyah "\"Waahh! Keren!\""

    raden "\"Kok bisa gerak sendiri gitu ya.\""

    aisyah "\"Ajaib mungkin..? hahaha!\""

    raden "\"Hahaha, bisa ngelawak juga kamu..\""

    aisyah "\"Oh ya, FYI, PENS selalu menang kalo lomba robotik.\""

    raden "\"Oh jadi Aisyah pengen ikut kompetisi juga.\""

    aisyah "\"Iya! Aku pengen banget kerja bareng tim, terus belajar lebih banyak soal teknis robotik.\""

    aisyah "\"Tapi sebenarnya...\""

    raden "\"Sebenarnya apa?\""

    aisyah "\"Aku lebih pengen fokus jadi programmer. Aku pengen jadi orang yang bikin otaknya robot, gimana biar robotnya bisa jalan sesuai logika yang aku rancang.\""

    aisyah "\"Kayaknya itu tantangan yang keren banget!\""

    raden "\"Oh iya kamu kan anak IT\""

    aisyah "\"Iya! Aku pengen belajar lebih dalam soal coding, AI.. gimana cara bikin robot bisa 'berpikir.\""

    aisyah "\"Rasanya seru banget kalau aku bisa bikin kode yang bikin robot benar-benar hidup.\""

    "Melihat Aisyah berbicara dengan begitu semangat, aku tidak bisa menahan senyumku. Energinya terasa menular, dan aku merasa ikut bangga meskipun hanya mendengarnya bercerita."

    "Sekali lagi, aku melihat sisi lain dari Aisyah- sisi yang jarang muncul, sisi yang lebih santai, bersemangat dan terbuka."

    aisyah "\"Raden..?\""

    raden "\"Yaa..?\""

    aisyah "\"Kamu tertarik dengan Robotik?\""

    aisyah "\"Kok ngajak aku kesini?\""

    menu:
        "Karena kamu":
            raden "\"Aku hanya nemenin kamu yang suka robot aja\""

            raden "\"Kamu pernah bilang kan..?\""

            raden "\"waktu PKKMB\""

            "Aisyah terdiam. Wajahnya tiba-tiba merona, dia mencoba mengalihkan pandangan sambil menggigit bibir bawahnya, tapi senyum kecil di wajahnya tidak bisa disembunyikan. Mata melirik ke arah samping."

            "..."

            aisyah "\"Ingat aja kamu\""

            "Dia bergumam pelan, nyaris tak terdengar, tapi cukup untuk membuatku tersenyum lebih lebar."

            raden "\"Kata-kata dari orang se-excited kamu emang susah dilupain.\""

            aisyah "\"Kamunya aja yang sok perhatian.\""

            "Tawa kami terus mengisi udara, seolah keramaian di sekitar tidak lagi terasa."

            "Momen sederhana ini, dengan canda yang ringan, membuatku merasa lebih dekat dengannya."

        "Karena anime":
            raden "\"Aku sih tertarik gara-gara dulu sering nonton anime mecha.\""

            aisyah "\"Anime mecha? Jadi kamu kayak suka robot karena anime?\""

            raden "\"Ya, begitulah. Aku suka lihat robot-robot keren yang bisa berubah bentuk atau bertarung,\""

            aisyah "\"Haha, Raden wibu!\""

            raden "\"Biarin..\""

            "Tawa kami terus mengisi udara, seolah keramaian di sekitar tidak lagi terasa."

            "Momen sederhana ini, dengan canda yang ringan, membuatku merasa lebih dekat dengannya."

    stop music fadeout 2.0

    jump pensasi_aisyah_ending

    return