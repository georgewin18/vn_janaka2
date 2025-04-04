init:
    transform shake:
        linear 0.02 xoffset -25
        linear 0.02 xoffset 25
        linear 0.02 xoffset -15
        linear 0.02 xoffset 15
        linear 0.02 xoffset 0

label chapter3_fania_scene2:
    
    #bg perpus pasca
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    "Fania dan Sasa telah berada di dalam perpustakaan gedung Pascasarjana menyiapkan buku di atas meja yang sesuai dengan topik yang akan dibahas dan siap untuk mulai mereview dan meringkas."

    show fania casual_dingin with dissolve:
        zoom 1.15 xalign 0.5 yalign -0.02

    voice "audio/vo/fania/chapter3/chapter3_3_jadi_gimana.flac"
    fania "\"Jadi gimana kabar Tina, dia jadi dateng gak?\""

    "Sasa, yang masih bermain HP dan menghubungi Tina, sementara Fania telah mencari jurnal untuk diringkas di laptopnya."

    "\"Katanya dia ada urusan mendadak buat bantuin pacarnya pindahan.\”"

    #fania kesal
    show fania casual_kesal with dissolve

    stop music fadeout 2.0

    "Jawaban Sasa membuat Fania mengerutkan keningnya."

    voice "audio/vo/fania/chapter3/chapter3_4_pacar.flac"
    fania "{i}Pacar? Kenapa malah minta bantuan perempuan dan bukan teman laki-laki yang lebih mampu secara fisik?{/i}"

    show fania casual_dingin with dissolve
    voice "audio/vo/fania/chapter3/chapter3_5_kalo_begitu.flac"
    fania "\"Kalau begitu, ayo kita mulai dulu deh.\""

    "Fania mulai meringkas tiap bab di dalam buku dan mengambil setiap poin penting di dalamnya."

    #fania bingung
    show fania casual_bingung with dissolve

    voice "audio/vo/fania/chapter3/chapter3_6_kamu_ngga_ngerjain.flac"
    fania "\"Kamu gak ngerjain?\""

    "\“Gak apa-apa, deadline-nya masih lima hari lagi, Masih punya banyak waktu kita. Yakin deh, paling juga dosennya gak bakalan baca.\”"

    "Sasa membalas dengan santai dan tanpa beban sembari terus bermain dan menggulir halaman TokTok nya"

    #fania menghela nafas
    show fania casual_menghelanapas
    pause 0.3

    voice "audio/vo/fania/chapter3/chapter3_menghela2.flac"
    show fania casual_menghelanapas_ada_asap with dissolve
    pause 0.3

    show fania casual_menghelanapas with dissolve

    fania "\"... Huh…\""

    "Fania hanya bisa menghela nafas dengan ketidak bertanggung jawabnya temannya itu."
    
    "Padahal, ini adalah bentuk evaluasi dari dosen kepada mahasiswa untuk menunjukkan seberapa kompeten mahasiswa dalam mengambil kesimpulan, mencari tahu informasi, dan membuat ringkasan yang masih sesuai dengan topik di dalam buku dan jurnal yang berhubungan dengan mata kuliah mereka."

    #fania dingin
    show fania casual_dingin with dissolve
    voice "audio/vo/fania/chapter3/chapter3_7_itu_kesalahan.flac"
    fania "\"Itu kesalahan berpikir.\""

    fania "\"Dosen itu bukan orang yang cuma bisa meluluskan murid kayak guru sekolah umum yang dibawahnya. Mereka itu orang yang terbaik di bidangnya yang berpengalaman dan tahu karakter mahasiswa\""

    voice "audio/vo/fania/chapter3/chapter3_8_kalau_kamu.flac"
    fania "\"Kalau kamu bilang begitu, kamu terlalu meremehkan dosen.\""

    "\"Yah, kalau begitu tinggal minta bantuan AI kayak METAL dan chatGaBuT.\""

    show fania casual_bingung with dissolve
    voice "audio/vo/fania/chapter3/chapter3_9_tapi_kan.flac"
    fania "\"Tapi kan nanti kelihatan kalau itu buatan AI\""

    "\"Tinggal di revisi sama AI-nya aja terus-terusan sampai gak kelihatan buatan AI dong. Itu lebih cepet dan gampang daripada ngerjain sendiri dan malah dianggap pakai AI.\""

    "Sasa tersenyum dengan percaya diri seolah-olah percaya bahwa itu adalah rencana yang brilian dan sangat berotak Senku."

    "\"Udahlah Fan, pakai cara yang gampang aja.\""

    "\"Hasilnya juga gak jauh beda kok, dan kalau kamu mau, ada kok cara pake AI yang lebih minimal untuk perbaikin typo doang.\""

    #backsound agak intens

    #layar bergetar
    show fania casual_kesal with hpunch

    play music intense fadein 1.0

    voice "audio/vo/fania/chapter3/chapter3_10_mana_mungkin.flac"
    fania "\"Mana mungkin aku pakai cara instan kayak gitu yang malah bikin aku bodoh. Aku gak mau pakai cara mudah buat bikin tugasku.\""

    voice "audio/vo/fania/chapter3/chapter3_11_lagian.flac"
    fania "\"Lagian, kerja cepat bukan berarti kamu paham sama apa yang ada di dalam tugasmu ‘kan? Kalau kamu mau pakai cara yang bisa bikin sel otakku berkurang itu, kamu pakai sendiri aja, dan aku tahu soal yang terakhir,\""
    
    "Fania meninggikan suaranya, cukup untuk membuat orang asing di bangku samping menoleh ke arah Fania"

    "Sasa mengerutkan keningnya merasa tersinggung dengan kata-kata Fania."

    "\"Fania, aku tahu kamu itu pintar dan kamu gak mau pakai caraku, tapi bukan berarti kamu bisa bicara kayak begitu! Mentang-mentang kamu lebih pintar dan hidupmu lebih mewah dari kita! Kamu gak tau apa-apa diam aja!\""

    "Fania hanya menatap ke arah Sasa tanpa mengatakan apapun untuk sesaat dan pergi."

    show black with dissolve

    jump chapter3_fania_scene3