label prolog_day2_scene2:

    #Depan Auditorium
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    show raden kemeja_panik with dissolve:
        zoom 0.48 xalign 0.5 yalign 0.1

    raden "\"Hah… hah… haahh…! Akhirnya sampai!!!\""

    raden "\"Perasaan kemarin ga kerasa deh…\""
    
    "Tenggorokanku sangat kering dan kakiku bergetar hebat setelah naik tangga dari lantai satu ke lantai enam."

    show black with dissolve

    scene bg auditorium with dissolve:
        zoom 0.5

    "Aku masuk ke dalam auditorium dan memeriksa sekeliling mencari Region-ku."

    #Sekar muncul tegass
    show sekar jas_teriak with dissolve:
        zoom 1.25 xalign 0.5 yalign 0.05

    sekar "\"Aldebaran… Aldebaran…\"" #Suara LO kami dari Aldebaran terdengar jelas, itu si kakak berambut hijau, kak Sekar.

    hide sekar with dissolve

    show raden kemeja_biasa with dissolve:
        zoom 0.48 xalign 0.5 yalign 0.1

    raden "\"Nah! Itu dia. Ternyata masih sama seperti kemarin.\""

    "Aku bergegas ke bangku region dan ternyata mendapatkan tempat duduk yang paling pojok dekat dengan jalan dan di depanku ternyata ada Aisyah."

    show raden kemeja_biasa with moveinright:
        xalign 0.0

    show aisyah kemeja_bicara with dissolve:
        zoom 0.35 xalign 0.85 yalign -0.7

    show raden kemeja_tersenyum
    raden "\"Hey! Aisyah!\"" #Aku menyapa perempuan di depanku.

    show aisyah kemeja_senyum

    voice "audio/vo/aisyah/prolog2/prolog2_1_halo_den.flac"
    aisyah "\"Oh! halo Den\"" #Aisyah menyapa ku kembali dengan senyuman.

    #Aisyah hilang
    hide aisyah with dissolve

    show raden kemeja_biasa
    "Aku mengeluarkan botol minum 2 liter milikku dari tas dan menengok ke samping kanan, sembari melihat mahasiswa di Region seberang. Aku melihat id card miliknya dan membaca namanya."

    #di sini karena santo lebih tinggi dari raden jadi kunaikin dikit yalign nya
    show santo kemeja_biasa with dissolve:
        zoom 1.15 xalign 2.7 yalign 0.08
    
    #Raden terkejut
    show raden kemeja_bingung
    raden "\"Santo?\""

    "kataku tanpa sengaja terdengar cukup keras, yang membuat dia tersentak, mungkin dia mendengar suaraku. Aku mengingat teman satu kelas yang namanya sama."

    show raden kemeja_tersenyum
    raden "\"Kebetulan, acara belum mulai, mending aku cek dulu.\""

    show raden kemeja_biasa
    "Aku membuka ponsel dan mentag Santo dari grup obrolan. Ketika aku mengirim pesan, mahasiswa di sampingku membuka ponselnya dan menengok ke arahku."

    show santo kemeja_bicara
    santo "\"Kau Raden dari DTME?\""

    show raden kemeja_tersenyum
    raden "\"Iya, kau Santo dari DTME?\""

    "Santo mengangguk dan mengulurkan tangan. Aku menyambutnya untuk bersalaman."

    raden "\"Gak nyangka bakalan duduk sebelahan begini, hehe.\"" #Aku terkekeh.

    show santo kemeja_biasa
    santo "\"Ya.\""#Santo menjawab singkat dengan senyuman kecil.

    #Aisyah muncul netral 
    #di sini menurutku kayanya mending aisyah cuma ngomong dari background ajh gak usah dimunculin, soalnya dia muncul cuma ngingetin raden trs ilang lagi
    show raden kemeja_biasa:
        xalign 0.4
    show santo kemeja_biasa:
        xalign 3.5
    with moveinleft

    show aisyah kemeja_bicara with dissolve:
        zoom 0.35 xalign -0.05 yalign -0.7
    
    voice "audio/vo/aisyah/prolog2/prolog2_2_udah_mau_mulai.flac"
    aisyah "\"Raden! Udah mau mulai!\""
    
    hide aisyah kemeja_bicara with dissolve
    
    show raden kemeja_biasa:
        xalign 0.0
    show santo kemeja_biasa:
        xalign 2.7
    with moveinleft

    "Aisyah memanggilku sebelum sempat berbicara lebih jauh. Waktu sudah habis, dan aku terpaksa menghentikan percakapan untuk fokus pada acara yang segera dimulai."

    "Di tengah presentasi, perhatianku teralihkan oleh seorang perempuan berambut merah yang duduk di bagian depan, tak jauh dari posisi Santo. Aku mengenalinya, perempuan yang kutemui kemarin sebelum pulang."

    raden "\"Ternyata udah sesi tanya-jawab.\""#Aku ingat gadis itu juga pernah bertanya kemarin, sepertinya dia cukup aktif.
    
    show raden kemeja_tersenyum
    raden "\"Temenmu..?\""# kataku berkomentar kepada santo.

    show raden kemeja_biasa
    show santo kemeja_bicara

    santo "\"Ya, dia keren sih. Sayang yang lain gak seperti dia.\""#Santo setuju dengan kata-kataku dengan anggukan.
    
    show santo kemeja_biasa
    show raden kemeja_tersenyum

    raden "\"Maksud?\""#Aku mendengar rasanya Santo mengeluh tentang keadaan region miliknya.

    show raden kemeja_biasa
    show santo kemeja_bicara

    santo "\"Gimana ya… di kelompok kami, yang bekerja itu cuma sedikit… bahkan bisa dibilang, cuma dia sendiri yang kerja paling banyak.\""#jawab Santo.
    
    show santo kemeja_biasa
    #Raden terkejut
    show raden kemeja_kaget

    menu:
        "Yang kamu maksud kerja paling banyak itu, dia ketua yang bertanggungjawab di banyak hal, kan?":
            jump prolog_day2_scene2_after_choice1
        "Dia beneran kerja sendirian?!":
            jump prolog_day2_scene2_after_choice1

label prolog_day2_scene2_after_choice1:

    show santo kemeja_bicara

    santo "\"Dia adalah definisi dari \'kerja\', dan yang lain itu definisi dari \'kelompok\'\""

    raden "\"Gila…\""

    "Untuk melihat definisi kerja-kelompok secara pribadi bahkan ketika sudah di masa perkuliahan membuatku sadar kalau tidak semua mahasiswa itu memiliki niat murni berkuliah. Ada yang cuma bersenang-senang, ada juga yang cuma menyetujui perintah orang tuanya."

    "Kasihan sekali, dia tidak cukup beruntung dengan kelompok region-nya, jauh berbeda dengan kelompok Region-ku yang saling bersemangat satu sama lain sampai-sampai aku tidak mendapatkan pekerjaan apapun."

    show raden kemeja_tersenyum
    raden "\"Kalau begitu, gimana kalau ku bantu?\""
    
    #raden terkejut
    show raden kemeja_kaget:
        xalign -0.25
    #santo terkejut, gak ada/blm ada asset nya jadi pake biasa
    show santo kemeja_biasa:
        xalign 3.5
    with moveinleft
    #aisyah muncul senyum
    show aisyah kemeja_senyum with dissolve:
        zoom 0.35 xalign 0.5 yalign -0.7

    voice "audio/vo/aisyah/prolog2/prolog2_3_aku_juga_ikut.flac"
    aisyah "\"Aku juga ikut bantu!\""

    "Kami tersentak saat Aisyah tiba-tiba berbicara dari depan."

    show raden kemeja_tersenyum
    raden "\"Kamu dengerin kita bicara dari tadi?\""#Aku membelalakkan mata karena tidak menyangka bahwa Aisyah yang sedang fokus dengan materi bisa teralihkan perhatiannya untuk bicara dengan kita.

    show raden kemeja_biasa
    show aisyah kemeja_bicara

    voice "audio/vo/aisyah/prolog2/prolog2_4_aku_juga_mau_bantu.flac"
    aisyah "\"Aku juga mau bantu kamu, Santo.. kan ya?\""#Aisyah cuma mengangguk

    show santo kemeja_bicara
    santo "\"Kalian gak usah repot-repot lah.\""

    show santo kemeja_biasa
    show raden kemeja_tersenyum

    raden "\"Gak masalah, aku bakalan ngikutin kamu, jadi mau gak mau kamu bakalan nerima bantuan kami.\""#ujar ku dengan Aisyah mengangguk setuju.

    show santo kemeja_bicara

    santo "\"Yaudahlah, oke kalau begitu.\""#Santo akhirnya menyerah dengan nada pasrah

    show black with dissolve

    jump prolog_day2_scene3