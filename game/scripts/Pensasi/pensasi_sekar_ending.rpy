label pensasi_sekar_ending:
    show raden kasual_biasa with dissolve:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show sekar kasual_biasa with dissolve:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    "Hari telah menjelang sore. Langit mulai berwarna jingga keemasan, menciptakan suasana yang tenang di tengah keramaian yang perlahan surut."

    "Kak Sekar menoleh padaku, senyum lembutnya tetap terlihat meskipun ia tampak sedikit lelah."

    show sekar kasual_bicara:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    voice "audio/vo/sekar/pensasi/pensasi_ending_1_menyenangkan.ogg"
    sekar "\"Menyenangkan nggak den?\""

    show raden kasual_ceria:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Sangat menyenangkan kak\"" 

    show sekar kasual_ceria:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    voice "audio/vo/sekar/pensasi/pensasi_ending_2_iya_kan.ogg"
    sekar "\"Iya kan? Nggak nyangka bakal seseru ini\""

    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Btw kak, lain kali mau jalan-jalan bersama nggak kak?\""

    raden "\"Berdua doang\""

    show sekar kasual_bingung:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    "Kak Sekar menghentikan langkahnya sebentar, lalu menatapku dengan alis terangkat"

    show sekar kasual_bicara:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    voice "audio/vo/sekar/pensasi/pensasi_ending_3_kamu.ogg"
    sekar "\"Kamu ngajak ngedate nih?\""

    show raden kasual_gugup:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Cuma main doang sih kak\""

    show sekar kasual_biasa:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    voice "audio/vo/sekar/pensasi/pensasi_ending_4_oh.ogg"
    sekar "\"Oh cuma main\""

    "Nada suaranya terdengar sedikit bercanda. Ia kemudian berjalan lagi, menatap lurus ke depan, sebelum akhirnya menambahkan dengan suara yang lebih lembut."

    show sekar kasual_senyum:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    voice "audio/vo/sekar/pensasi/pensasi_ending_5_kalo.ogg"
    sekar "\"Kalau cuma main mah, kamu chat aja kapan waktu mainnya\""

    voice "audio/vo/sekar/pensasi/pensasi_ending_6_biar.ogg"
    sekar "\"Biar aku bisa enak ngatur jadwal\""

    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Baik kak\""

    show sekar kasual_ceria:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    voice "audio/vo/sekar/pensasi/pensasi_ending_7_kalo_begitu.ogg"
    sekar "\"kalau begitu, aku pergi dulu ya den\""

    voice "audio/vo/sekar/pensasi/pensasi_ending_8_selamat_tinggal.ogg"
    sekar "\"Selamat tinggal\""

    show raden kasual_ceria:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Selamat tinggal kak\""

    stop music fadeout 2.0

    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(0.3)

    return
