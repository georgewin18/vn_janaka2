label pensasi_aisyah_scene1:
    scene bg auditorium with dissolve:
        zoom 0.5

    play music campus fadein 1.0

    show raden kasual_biasa at raden_default:
        xalign -0.2
    show aisyah casual_senyum at aisyah_default:
        xalign 1.0
    with dissolve

    show raden kasual_tersenyum

    raden "\"Ramai juga ternyata\""

    show aisyah casual_senyum2

    voice "audio/vo/aisyah/pensasi/pensasi_1_iyalah.mp3"
    aisyah "\"Iyalah..\""

    show raden kasual_biasa
    show aisyah casual_senyum

    "Di panggung, para mahasiswa sudah mulai mempresentasikan perangkat canggih yang mereka kembangkan."

    "Suara riuh rendah diskusi penonton bercampur dengan penjelasan para pembicara di panggung."

    "Aku melihat sekeliling ruangan, mencari tempat duduk yang masih kosong. Hanya ada dua pilihan. Di depan, dekat panggung, atau di belakang."

    "{i}Duduk Dimana enaknya..?{/i}"

    menu:
        "Duduk di depan":
            show raden kasual_tersenyum

            raden "\"Di depan aja gimana?\""

            show aisyah casual_bingung

            voice "audio/vo/aisyah/pensasi/pensasi_1_1_1_hmm.mp3"
            aisyah "\"Hhmm...?\""

            show raden kasual_bingung

            raden "\"Kenapa?\""

            show aisyah casual_senyum4

            voice "audio/vo/aisyah/pensasi/pensasi_1_1_2_padahal.mp3"
            aisyah "\"Padahal tadi kayak terpaksa..  tapi nggak apa-apa.\""

            "Aku terdiam, sedikit bingung dengan maksudnya. Namun, kami akhirnya melangkah ke depan, memilih kursi yang tersisa."

        "Duduk di belakang":
            show raden kasual_tersenyum

            raden "\"Di belakang aja\""

            show aisyah casual_serius

            voice "audio/vo/aisyah/pensasi/pensasi_1_2_1_ehh.mp3"
            aisyah "\"Eeehh..?\""

            voice sustain

            aisyah "\"Kok di belakang?!\""

            show raden kasual_biasa2

            raden "\"Ngapain juga di depan emangnya?\""

            voice "audio/vo/aisyah/pensasi/pensasi_1_2_2_di_depan_aja.mp3"
            aisyah "\"Di depan aja\""

            show raden kasual_menghela_napas with dissolve

            "Aku terdiam sesaat,menatap Aisyah yang tampak sangat yakin. Akhirnya aku mengalah."

            raden "\"Iya-iya\""

            "Kami akhirnya melangkah ke barisan depan dan duduk di salah satu kursi kosong. Meski awalnya aku enggan, duduk di depan ternyata tidak seburuk yang kubayangkan."

    stop music fadeout 2.0

    jump pensasi_aisyah_scene2

    return