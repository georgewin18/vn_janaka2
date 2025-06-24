label pensasi_aisyah_scene1:
    scene bg auditorium with dissolve:
        zoom 0.5

    play music campus fadein 1.0

    show raden kasual_biasa:
        zoom 0.48 xalign 0.0 yalign 0.1
    show aisyah kemeja_bicara:
        zoom 0.35 xalign 0.95 yalign -0.7
    with dissolve

    show raden kasual_tersenyum

    raden "\"Ramai juga ternyata\""

    aisyah "\"Iyalah..\""

    show raden kasual_biasa

    "Di panggung, para mahasiswa sudah mulai mempresentasikan perangkat canggih yang mereka kembangkan."

    "Suara riuh rendah diskusi penonton bercampur dengan penjelasan para pembicara di panggung."

    "Aku melihat sekeliling ruangan, mencari tempat duduk yang masih kosong. Hanya ada dua pilihan. Di depan, dekat panggung, atau di belakang."

    "{i}Duduk Dimana enaknya..?{/i}"

    menu:
        "Duduk di depan":
            show raden kasual_tersenyum

            raden "\"Di depan aja gimana?\""

            show aisyah kemeja_bingung

            aisyah "\"Hhmm...?\""

            show raden kasual_bingung

            raden "\"Kenapa?\""

            show aisyah kemeja_bicara

            aisyah "\"Padahal tadi kayak terpaksa..  tapi nggak apa-apa.\""

            "Aku terdiam, sedikit bingung dengan maksudnya. Namun, kami akhirnya melangkah ke depan, memilih kursi yang tersisa."

        "Duduk di belakang":
            show raden kasual_tersenyum

            raden "\"Di belakang aja\""

            show aisyah kemeja_penasaran

            aisyah "\"Eeehh..?\""

            aisyah "\"Kok di belakang?!\""

            show raden kasual_biasa2

            raden "\"Ngapain juga di depan emangnya?\""

            aisyah "\"Di depan aja\""

            show raden kasual_menghela_napas with dissolve

            "Aku terdiam sesaat,menatap Aisyah yang tampak sangat yakin. Akhirnya aku mengalah."

            raden "\"Iya-iya\""

            "Kami akhirnya melangkah ke barisan depan dan duduk di salah satu kursi kosong. Meski awalnya aku enggan, duduk di depan ternyata tidak seburuk yang kubayangkan."

    stop music fadeout 2.0

    jump pensasi_aisyah_scene2

    return