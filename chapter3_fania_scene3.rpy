label chapter3_fania_scene3:
    #bg perpus pasca
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    #bgm netral in kampus
    #fania dingin
    show fania casual_dingin with dissolve:
        zoom 1.15 xalign 0.0 yalign -0.02 

    "Aisyah masuk ke perpustakaan dan melihat tiga buah buku yang sama-sama dibuka dengan laptop Fania yang juga membuka tiga buah artikel jurnal."

    show aisyah kemeja_gugup with dissolve:
        zoom 0.35 xalign 0.9 yalign -0.7

    voice "audio/vo/aisyah/chapter3/chapter3_1_fa.flac"
    aisyah "\"Fa- hmm, mendingan jangan deh.\""

    "Aisyah menghentikan niatnya untuk memanggil Fania, melihat dia begitu fokus dan penuh konsentrasi."

    show aisyah:
        xalign 0.7
    with moveinright
    
    "Aisyah mendekati Fania dan membuat Fania menyadarinya."

    voice "audio/vo/fania/chapter3/chapter3_12_aisyah.flac"
    fania "\"Aisyah.\""

    "Jumlah kata-kata yang terlampau banyak di layar laptop dalam satu saat membuat Aisyah merasa pusing melihatnya. Dia duduk di bangku di sisi Fania. "

    voice "audio/vo/aisyah/chapter3/chapter3_2_fania.flac"
    aisyah "\"Fania, itu mau kamu baca semuanya? Kenapa kok ada banyak sekali bukunya?\""

    voice "audio/vo/fania/chapter3/chapter3_13_buat_tugas_aja.flac"
    fania "\"Buat tugas aja sih.\'"

    "Aisyah menatap Fania dengan kebingungan dan tidak yakin. "

    show aisyah kemeja_bingung

    voice "audio/vo/aisyah/chapter3/chapter3_3_tugas.flac"
    aisyah "\"Tugas?\""

    voice "audio/vo/aisyah/chapter3/chapter3_4_kayanya.flac"
    aisyah "\"Kayaknya kebanyakan deh kalau cuma buat tugas.\""

    show black with dissolve

    stop music fadeout 2.0

    jump chapter3_fania_scene4