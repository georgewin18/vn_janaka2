init:
    transform bottom:
        yalign -2.0

label prolog_day4_scene2:
    #bg jalan kantin-d4
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    show raden biasa with dissolve:
        zoom 0.23 yalign 0.1 xalign 0.5

    "Setelah prosesi pengukuhan selesai, panitia memberi instruksi agar semua sekelompok berbaris dua banjar. Aku segera mencari posisi bersama kelompokku."

    "Dengan Aisyah di depanku, kami bergerak cepat membentuk barisan"

    "Langkah kami mulai bergerak mengikuti kelompok lain. Jalur menuju area expo cukup ramai dengan kelompok lain yang berbaris, sementara panitia dan senior sibut memberi arahan di sepanjang jalan."

    "Aku berusaha tetap fokus mengikuti langkah teman di depanku."
    
    hide raden with MoveTransition(0.3, leave=bottom)

    "{i}Bruk!{/i}" with vpunch

    show aisyah kemeja_gugup with dissolve:
        zoom 0.34 yalign -1.0 xalign 0.9

    aisyah "\"Den! kamu gapapa?!\""

    show raden capek with moveinbottom:
        zoom 0.23 yalign 0.1 xalign 0.0

    aisyah "\"Aduh, gimana sih jalannya?\""

    show raden:
        xalign -0.2
    show aisyah:
        xalign 0.55
    show sekar jas_teriak:
        zoom 1.15 xalign 3.6 yalign 0.03
    with moveinright

    sekar "\"Raden, kamu baik-baik saja?\""

    raden "\"Gak apa-apa, Kak. Cuma sedikit kesandung\""

    sekar "\"Jangan dipaksakan dulu\""

    sekar "\"Coba duduk dulu di pinggir jalan. Aku cek lututmu\""

    "Aku mengikuti arahannya meski rasa malu masih terasa. Dengan hati-hati aku duduk di pinggir jalan, dan Kak Sekar berjongkok di depanku menyuruh salah satu panitia lain mengambil kotak P3K"

    "Sementara itu, anggota kelompokku yang lain diserahkan pada LO region kami yang satunya, Kak Ryan, untuk lanjut menuju area expo"

    aisyah "Tapi kak, Raden gimana?"

    sekar "\"Tenang, ku pastikan dia baik-baik saja\""

    hide aisyah with dissolve
    show raden:
        xalign 0.0
    show sekar:
        xalign 2.5
    with moveinright

    "Akhirnya kelompok kami melanjutkan perjalanan, sementara aku tetap duduk di pinggi halan bersama Kak Sekar."

    "Dia memeriksa lututku dengan cermat. Namun saat dia melihat lututku yang berdarah, wajahnya mendadak berubah."

    show sekar jas_normal with dissolve
    #sekar gugup
    "Tatapan tegasnya seketika memudar, berganti dengan raut bingung dan gugup. Dia tampak menahan diri tetapi tangannya sedikit gemetar."

    "Tak lama panitia lain datang dan memberinya kotak P3K, tapi setelah itu langsung pergi karena banyak yang harus diurus"

    sekar "\"Eh... ini, darahnya...\""

    show raden bingung with dissolve

    raden "\"Kak, ga apa-apa?\""

    sekar "\"Eh... gapapa kok. Aku... aku hanya gak tahan liat darah...\""

    "Aku menatapnya, heran. Biasanya, Kak Sekar adalah sosok yang selalu terlihat tangguh dan sempurna."

    "Tapi sekarang, dia tampak ragu-ragu. Tidak pernah terpikirkan bahwa Kak Sekar, yang selau terlihat tegas dan kuat, ternyata punya kelemahan seperti ini."

    menu:
        "Membiarkan Kak Sekar lanjut mengobati ku":
            jump prolog_day4_scene2_choice1
        "Melihat keadaannya, aku memutuskan untuk mengambil inisiatif membantu":
            jump prolog_day4_scene2_choice2

    return 

label prolog_day4_scene2_choice1: 
    show raden biasa with dissolve

    "Aku merasa sedikit bersalah sudah membuatnya harus menghadapi rasa takut ini, tetapi aku juga kagum pada usahanya untuk tetap membantu."

    "Dia kembali melanjutkan membersihkan lukaku, meski tangannya terlihat ragu. Aku memperhatikan wajahnya yang sedikit pucat, tetapi dia tetap memaksakan diri untuk menyelesaikan tugasnya."

    "Setelah beberapa saat, kak Sekar akhirnya berhasil membersihkan luka menggunakan kapas antiseptik dan menempelkan perban di atasnya. Dia menghela napas panjang, terlihat sangat lega."

    sekar "\"Maaf ya kalau tadi agak lama.. karena aku.. aku kurang nyaman sama hal-hal seperti ini. Padahal.. Aku ini LO yang harusnya membantu kalian, tapi malah begini...\""

    jump prolog_day4_scene2_after_choice

label prolog_day4_scene2_choice2:
    show raden biasa with dissolve

    raden "\"Kak, gak apa-apa kalau aku yang urus sendiri?\""

    sekar "\"Enggak, enggak. Ini tanggung jawabku. Kamu tenang aja\""

    "Aku tersenyum kecil, merasa sedikit terhibur melihat sisi rapuhnya yang jarang terlihat."

    raden "\"Kalau begitu, aku bantu Kakak, pegang perban ini, ya\""

    sekar "\"Iya...\""

    raden "\"Santai aja, Kak. Aku juga bisa kok bersihin sendiri.\""

    "Dengan hati-hati, aku membersihkan lukaku menggunakan kapas antiseptik yang juga dia siapkan, kemudian menempelkan perban di atasnya."

    raden "\"Lihat... Gampang, kan?\""

    sekar "\"Iya... maaf ya, Raden. Padahal... Aku ini LO yang harusnya membantu kalian, tapi malah begini...\""

label prolog_day4_scene2_after_choice:
    
    raden "\"Gak masalah, Kak. Justru aku baru tahu Kakak ini manusia juga, ternyata bisa gugup,\""

    "Kak Sekar tersenyum anggun, senyumnya terasa hangat, memancarkan kharisma yang membuatku terdiam sejenak dalam kekaguman."

    "Lalu dia tertawa kecil, dan wajahnya mulai kembali ke ekspresi tenang."

    sekar "\"Ya, aku kan juga manusia. Tapi jangan bilang siapa-siapa ya soal ini. Malu kalau ketahuan panitia lain\""

    raden "\"Tenang, aman kok\""

    jump prolog_day4_scene3

    return 