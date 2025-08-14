init:
    transform bottom:
        yalign -2.0

label prolog_day4_scene2:
    #bg jalan kantin-d4
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    play music raden_bgm fadein 1.0

    show raden kemeja_biasa with dissolve:
        zoom 0.54 xalign 0.45 yalign 0.05

    "Setelah prosesi pengukuhan selesai, panitia memberi instruksi agar semua sekelompok berbaris dua banjar. Aku segera mencari posisi bersama kelompokku."

    "Dengan Aisyah di depanku, kami bergerak cepat membentuk barisan"

    "Langkah kami mulai bergerak mengikuti kelompok lain. Jalur menuju area expo cukup ramai dengan kelompok lain yang berbaris, sementara panitia dan senior sibut memberi arahan di sepanjang jalan."

    "Aku berusaha tetap fokus mengikuti langkah teman di depanku."
    
    stop music fadeout 2.0

    hide raden with MoveTransition(0.3, leave=bottom)

    "{i}Bruk!{/i}" with vpunch

    show aisyah kemeja_terkejut with dissolve:
        zoom 0.4 xalign 1.0 yalign 0.1

    play music intense fadein 1.0

    voice "audio/vo/aisyah/prolog4/prolog4_1_den_kamu_gapapa.flac"
    aisyah "\"Den! kamu gapapa?!\""

    show raden kemeja_gugup with moveinbottom:
        zoom 0.54 xalign -0.2 yalign 0.05

    show aisyah kemeja_serius
    voice "audio/vo/aisyah/prolog4/prolog4_2_aduh_gimana_sih.flac"
    aisyah "\"Aduh, gimana sih jalannya?\""

    show raden:
        xalign -0.45
    show aisyah:
        xalign 0.5
    show sekar jas_khawatir:
        zoom 1.25 xalign 1.15 yalign 0.05
    with moveinright

    voice "audio/vo/sekar/prolog4/prolog4_1_raden_kamu.flac"
    sekar "\"Raden, kamu baik-baik saja?\""

    raden "\"Gak apa-apa, Kak. Cuma sedikit kesandung\""

    voice "audio/vo/sekar/prolog4/prolog4_2_jangan_dipaksakan.flac"
    sekar "\"Jangan dipaksakan dulu\""

    voice "audio/vo/sekar/prolog4/prolog4_3_coba_duduk.flac"
    sekar "\"Coba duduk dulu di pinggir jalan. Aku cek lututmu\""

    "Aku mengikuti arahannya meski rasa malu masih terasa. Dengan hati-hati aku duduk di pinggir jalan, dan Kak Sekar berjongkok di depanku menyuruh salah satu panitia lain mengambil kotak P3K"

    "Sementara itu, anggota kelompokku yang lain diserahkan pada LO region kami yang satunya, Kak Ryan, untuk lanjut menuju area expo"

    voice "audio/vo/aisyah/prolog4/prolog4_3_tapi_kak.flac"
    aisyah "Tapi kak, Raden gimana?"

    show sekar jas_tegas

    voice "audio/vo/sekar/prolog4/prolog4_4_tenang.flac"
    sekar "\"Tenang, ku pastikan dia baik-baik saja\""

    hide aisyah with dissolve
    show raden:
        xalign -0.2
    show sekar:
        xalign 1.0
    with moveinright

    "Akhirnya kelompok kami melanjutkan perjalanan, sementara aku tetap duduk di pinggi halan bersama Kak Sekar."

    scene black with dissolve
    with Pause(0.2)

    scene sekar_prolog with dissolve:
        zoom 0.75

    "Dia memeriksa lututku dengan cermat. Namun saat dia melihat lututku yang berdarah, wajahnya mendadak berubah."

    #sekar gugup
    "Tatapan tegasnya seketika memudar, berganti dengan raut bingung dan gugup. Dia tampak menahan diri tetapi tangannya sedikit gemetar."

    "Tak lama panitia lain datang dan memberinya kotak P3K, tapi setelah itu langsung pergi karena banyak yang harus diurus"

    voice "audio/vo/sekar/prolog4/prolog4_5_eh_ini_darah.flac"
    sekar "\"Eh... ini, darahnya...\""

    raden "\"Kak, ga apa-apa?\""

    voice "audio/vo/sekar/prolog4/prolog4_6_eh_gapapa.flac"
    sekar "\"Eh... gapapa kok. Aku... aku cuma gak tahan liat darah...\""

    "Aku menatapnya, heran. Biasanya, Kak Sekar adalah sosok yang selalu terlihat tangguh dan sempurna."

    "Tapi sekarang, dia tampak ragu-ragu. Tidak pernah terpikirkan bahwa Kak Sekar, yang selau terlihat tegas dan kuat, ternyata punya kelemahan seperti ini."

    menu:
        "Membiarkan Kak Sekar lanjut mengobati ku":
            jump prolog_day4_scene2_choice1
        "Melihat keadaannya, aku memutuskan untuk mengambil inisiatif membantu":
            jump prolog_day4_scene2_choice2

    return 

label prolog_day4_scene2_choice1: 
    stop music fadeout 2.0
    play music sekar_bgm fadein 1.0

    "Aku merasa sedikit bersalah sudah membuatnya harus menghadapi rasa takut ini, tetapi aku juga kagum pada usahanya untuk tetap membantu."

    "Dia kembali melanjutkan membersihkan lukaku, meski tangannya terlihat ragu. Aku memperhatikan wajahnya yang sedikit pucat, tetapi dia tetap memaksakan diri untuk menyelesaikan tugasnya."

    "Setelah beberapa saat, kak Sekar akhirnya berhasil membersihkan luka menggunakan kapas antiseptik dan menempelkan perban di atasnya. Dia menghela napas panjang, terlihat sangat lega."

    scene bg depan_auditorium with dissolve:
        zoom 0.5

    show raden kemeja_biasa:
        zoom 0.54 xalign -0.2 yalign 0.05
    show sekar jas_gugup:
        zoom 1.25 xalign 1.0 yalign 0.05
    with dissolve

    voice "audio/vo/sekar/prolog4/prolog4_7_maaf_ya_lama.flac"
    sekar "\"Maaf ya kalau tadi agak lama.. karena aku.. aku kurang nyaman sama hal-hal seperti ini. Padahal.. Aku ini LO yang harusnya membantu kalian, tapi malah begini...\""

    jump prolog_day4_scene2_after_choice

label prolog_day4_scene2_choice2:
    stop music fadeout 2.0
    play music sekar_bgm fadein 1.0

    raden "\"Kak, gak apa-apa kalau aku yang urus sendiri?\""

    voice "audio/vo/sekar/prolog4/prolog4_8_enggak.flac"
    sekar "\"Enggak, enggak. Ini tanggung jawabku. Kamu tenang aja\""

    "Aku tersenyum kecil, merasa sedikit terhibur melihat sisi rapuhnya yang jarang terlihat."

    raden "\"Kalau begitu, aku bantu Kakak, pegang perban ini, ya\""

    voice "audio/vo/sekar/prolog4/prolog4_9_iya.flac"
    sekar "\"Iya...\""

    raden "\"Santai aja, Kak. Aku juga bisa kok bersihin sendiri.\""

    "Dengan hati-hati, aku membersihkan lukaku menggunakan kapas antiseptik yang juga dia siapkan, kemudian menempelkan perban di atasnya."

    raden "\"Lihat... Gampang, kan?\""

    scene bg depan_auditorium with dissolve:
        zoom 0.5

    show raden kemeja_biasa:
        zoom 0.54 xalign -0.2 yalign 0.05
    show sekar jas_gugup:
        zoom 1.25 xalign 1.0 yalign 0.05
    with dissolve

    voice "audio/vo/sekar/prolog4/prolog4_10_iya_maaf_ya.flac"
    sekar "\"Iya... maaf ya, Raden. Padahal... Aku ini LO yang harusnya membantu kalian, tapi malah begini...\""

label prolog_day4_scene2_after_choice:
    show raden kemeja_tersenyum
    raden "\"Gak masalah, Kak. Justru aku baru tahu Kakak ini manusia juga, ternyata bisa gugup,\""

    show raden kemeja_biasa
    show sekar jas_ceria with dissolve
    "Kak Sekar tersenyum anggun, senyumnya terasa hangat, memancarkan kharisma yang membuatku terdiam sejenak dalam kekaguman."

    "Lalu dia tertawa kecil, dan wajahnya mulai kembali ke ekspresi tenang."

    voice "audio/vo/sekar/prolog4/prolog4_11_aku_juga_manusia.flac"
    sekar "\"Ya, aku kan juga manusia. Tapi jangan bilang siapa-siapa ya soal ini. Malu kalau ketahuan panitia lain\""

    raden "\"Tenang, aman kok\""

    jump prolog_day4_scene3

    return 