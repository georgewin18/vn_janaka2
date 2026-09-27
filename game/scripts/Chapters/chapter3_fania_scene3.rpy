label chapter3_fania_scene3:
    #bg perpus pasca
    scene bg depan_auditorium with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    #bgm netral in kampus
    #fania dingin
    show fania casual_dingin with dissolve:
        zoom fania_default.zoom
        xalign 0.0
        yalign fania_default.yalign

    "Aisyah masuk ke perpustakaan dan melihat tiga buah buku yang sama-sama dibuka dengan laptop Fania yang juga membuka tiga buah artikel jurnal."

    show aisyah kemeja_gugup with dissolve:
        xalign 0.9
        yalign aisyah_default.yalign

        zoom aisyah_default.zoom
    voice "audio/vo/aisyah/chapter3/chapter3_1_fa.ogg"
    aisyah "\"Fa- hmm, mendingan jangan deh.\""

    "Aisyah menghentikan niatnya untuk memanggil Fania, melihat dia begitu fokus dan penuh konsentrasi."

    show aisyah:
        xalign 0.7
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    with moveinright
    
    "Aisyah mendekati Fania dan membuat Fania menyadarinya."

    voice "audio/vo/fania/chapter3/chapter3_12_aisyah.ogg"
    fania "\"Aisyah.\""

    "Jumlah kata-kata yang terlampau banyak di layar laptop dalam satu saat membuat Aisyah merasa pusing melihatnya. Dia duduk di bangku di sisi Fania. "

    voice "audio/vo/aisyah/chapter3/chapter3_2_fania.ogg"
    aisyah "\"Fania, itu mau kamu baca semuanya? Kenapa kok ada banyak sekali bukunya?\""

    voice "audio/vo/fania/chapter3/chapter3_13_buat_tugas_aja.ogg"
    fania "\"Buat tugas aja sih.\'"

    "Aisyah menatap Fania dengan kebingungan dan tidak yakin. "

    show aisyah kemeja_bingung:

        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    voice "audio/vo/aisyah/chapter3/chapter3_3_tugas.ogg"
    aisyah "\"Tugas?\""

    voice "audio/vo/aisyah/chapter3/chapter3_4_kayanya.ogg"
    aisyah "\"Kayaknya kebanyakan deh kalau cuma buat tugas.\""

    show black at Transform(xsize=config.screen_width, ysize=config.screen_height, xpos=0, ypos=0) with dissolve

    stop music fadeout 2.0

    jump chapter3_fania_scene4
