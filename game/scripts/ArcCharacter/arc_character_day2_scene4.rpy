transform cam_zoom_fania:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    zoom 1.0
    linear 60.0 zoom 2.5 xpos -0.2 ypos 0.9
layeredimage scene_with_chars:
    always "bg perpus_pasca"
    group char:
        attribute raden default
        attribute santo default
        attribute fania default
        attribute aisyah default
transform normal_camera:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    zoom 1.0

label arc_character_day2_scene4:
    camera at normal_camera
    scene bg perpus_pasca

    show raden kasual_biasa:
        xalign -0.8
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kasual_netral:
        xalign 0.8
        zoom santo_default.zoom
    show fania casual_dingin:
        xalign 2.0
        zoom fania_default.zoom
        yalign fania_default.yalign
    show aisyah casual_gugup:
        xalign 0.15

        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    #Backsound Suasana sedikit dramatis

    fania "\"Kenapa kalian pada bantu, padahal aku gak minta?\""
    
    "Aisyah menatap Fania dengan senyuman, tetapi ada ketegasan dalam nada suaranya."

    show aisyah casual_senyum:
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    aisyah "\"Karena kami gak mungkin diam aja lihat kamu kerja kayak gini, Fan. Kita teman kan?\""

    "Fania kembali menatap layar laptopnya, mengetik beberapa baris lagi tanpa menanggapi. Tapi gerakannya sedikit melambat, seperti memikirkan jawaban."

    raden "\"Fania, ini kan tugas kelompok, kita bisa bantu dikit-dikit.\""

    "Fania menghentikan ketikannya, lalu menutup laptop dengan pelan. Dia menatap mereka dengan ekspresi dingin, tetapi ada sedikit kelelahan di matanya."

    show fania casual_menghelanapas:
        zoom fania_default.zoom
        yalign fania_default.yalign
    with Pause(1.0)
    show fania casual_menghelanapas_ada_asap:
    
        zoom fania_default.zoom
        yalign fania_default.yalign
    fania "\"haahhh…\""

    show fania casual_senyum_normal_biasa:

        zoom fania_default.zoom
        yalign fania_default.yalign
    fania "\"Makasih, Aisyah, Santo, Raden.\""

    show fania casual_menghelanapas:

        zoom fania_default.zoom
        yalign fania_default.yalign
    fania "\"Sebenarnya, aku ada masalah sama anggota kelompokku…\""

    show fania casual_gugup:

        zoom fania_default.zoom
        yalign fania_default.yalign
    "Fania bercerita kepada kami, tentang masalah yang dia hadapi."

    "Masalah internal yang diakibatkan hanya karena seseorang memiliki urusan pribadi dan cekcok yang berakhir pada pertengkaran Fania dan salah satu rekan di kelompoknya."

    fania "\"… Jadi kupikir, mending ngerjain sendiri aja, daripada sama rekan yang gak jelas kabarnya.\""

    "Cerita yang Fania beritahukan kepada kita bertiga menjelaskan bahwa sifatnya itu ada bukan tanpa alasan. Dia telah kehilangan kepercayaannya pada orang lain."

    #Backsound sedikit dramatis

    show raden kasual_tersenyum:
        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Aku paham.\""

    "Aku mengangguk dengan tenang tanpa mengalihkan mataku dari buku yang ku baca. Perhatian ketiga temanku tertuju ke arahku ketika aku berhenti membaca dan memandang Fania."

    raden "\"Aku ngerti kenapa kamu susah percaya sama orang lain. Itu wajar kok, apalagi kalau ada alasannya. Tapi, gak ada salahnya coba kasih kesempatan sekali lagi, kan?\""

    "Perasaan kepercayaan yang telah dikhianati ketika masa PKKMB dan cekcok yang dimulai dari perbedaan cara mengerjakan tugas, membuat Fania tidak lagi berniat memberikan kepercayaan yang dalam kepada orang lain."

    show fania casual_sedih:

        zoom fania_default.zoom
        yalign fania_default.yalign
    fania "\"Gak segampang itu Den.\""

    fania "\"Santo, Kamu inget satu orang yang dari DTMK di kelompok kita selain aku?\""

    santo "\"Iya.\""

    santo "\"Sifatnya masih sama-sama tidak bertanggungjawab.\""

    #Santo Serius
    show santo kasual_kesal:

        zoom santo_default.zoom
    "Santo hanya bisa mengerutkan keningnya, membuatku memahami bahwa ada masalah yang cukup serius di antara Fania, Santo, dan kelompok PKKMB mereka."

    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Fania, sekarang kamu lihat kami bertiga.\""

    raden "\"Apakah kamu pikir kita kesini buat main-main?\""

    show fania casual_gugup:

        zoom fania_default.zoom
        yalign fania_default.yalign
    fania "\"Enggaklah, jelas-jelas kalian kesini buat belajar.\""

    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Menurutmu semua orang juga sama kayak kita atau orang yang kamu sebutin?\""

    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Fania, manusia itu rumit. Kamu kira Santo ngerjain tugasnya di sini karena rajin? Bukan, dia malah gabung biar cepet kelar. Malas mikirin tugas sendiri, gitu.\""

    show santo kasual_netral:

        zoom santo_default.zoom
    santo "\"Kamu juga sama aja sih.\""

    raden "\"Waspada itu nggak salah, tapi jangan sampai bikin kamu jadi close-minded, Fania.\""

    raden "\"Menyaring orang itu sih oke, tapi coba deh kasih mereka kesempatan. Siapa tahu mereka punya warna-warni yang bisa ngisi hidup kamu. Hidup ini kan soal saling kenal dan saling terima, kan?\""

    raden "\"Kita ini generasi masa depan, Fania! Dituntut buat open-minded, berpikir kritis, dan jadi agen perubahan!\""

    raden "\"Jadi, kasih aja mereka waktu. Kalau gagal, yaudah, at least kamu udah berusaha sebaik mungkin. Slow aja, dunia nggak akan runtuh cuma karena kamu kasih orang kesempatan, kok!\""

    "Aku berhenti, mengakhiri pidato bijak ku dan memandang Fania."

    #Backsound sedikit romantis

    camera at cam_zoom_fania
    show fania casual_senyum_ceria:

        zoom fania_default.zoom
        yalign fania_default.yalign
    "Tawa halusnya terdengar seperti lonceng yang dihembuskan oleh angin lembut, berpadu dengan senyum yang memancarkan kehangatan seperti siraman mentari pagi. Aku terdiam sesaat, terpaku pada wajahnya yang terlihat begitu bersinar."

    "Aku mengagumi itu. Mungkin lebih dari sekadar kekaguman biasa."

    show raden kasual_canggung:
        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Lah, kenapa ketawa?\""

    raden "{i}Apa yang salah?{i}"

    raden "{i}Apakah aku melakukan kesalahan tadi?{i}"

    raden "\"Kalian sialan, orang bicara malah diketawain.\""

    camera at normal_camera

    show fania casual_senyum_normal_biasa:

        zoom fania_default.zoom
        yalign fania_default.yalign
    fania "\"Ok lah, Den.\""

    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Fania tersenyum dengan cool, ada sesuatu dalam dirinya yang membuatku semakin terpesona. Caranya menatapku—penuh keyakinan, tapi juga penuh penghargaan—seolah mengatakan kalau dia benar-benar mendengarkan setiap kata yang keluar dari mulutku."

    fania "\"Akan ku lakuin sesuai saranmu. Rasanya gak mungkin deh mengabaikan temanku yang udah berkorban untuk mengatakan semua itu.\""

    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Kalau begitu, ayo lakuin sekarang!\""

    raden "\"Semakin banyak ditunda bakalan semakin susah nanti. Mendingan sekarang aja.\""

    raden "\"Karena sejatinya, ini adalah tugas kelompok, bukan tugas individu, jadi, akan lebih baik dan maksimal kalau kalian sendiri yang ngerjain, kan? Dan, kalau bukan sekarang, kapan lagi?\""

    fania "\"Iya sih..\""

    fania "\"Aku {i}call{/i} sekarang.\""

    "Ada sesuatu tentang cara dia mengambil keputusan, tentang caranya menatap dengan keyakinan, yang membuatku tidak bisa berpaling."

    "Aku mungkin baru mengenalnya."

    "Tapi, di momen itu, aku tahu—itulah Fania yang sebenarnya."

    "Akhirnya, Fania bangkit dari kursinya, berjalan keluar perpustakaan, dan menelpon teman satu kelompoknya yang sebelumnya sempat terlibat adu mulut dengannya"

    "Santo berdehem pelan, lalu menyenggol lenganku dengan siku."

    show santo kasual_senyum:
        zoom santo_default.zoom
    santo "\"Den. Barusan pidatonya kayak dosen filsafat yang lagi jatuh cinta.\""

    show raden kasual_canggung:
        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Yah... kadang pencerahan datang di luar jam kuliah.\""

    show aisyah casual_senyum:
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    aisyah "\"Tapi jujur, Den. Keren sih. Kamu ngomong kayak gitu tuh nggak semua orang bisa. Ngena. Dan Fania dengerin beneran.\""

    show santo kasual_netral:
        zoom santo_default.zoom
    santo "\"Setuju. Kita emang nggak bisa bantu banyak di masalah dia, tapi kayaknya… itu udah cukup. Sisanya, biar dia yang hadapi sendiri.\""

    "Aku dan Aisyah menganggukan kepala, setuju dengan Santo."

    "Aku tidak tahu pasti bagaimana percakapan mereka berlangsung. Yang jelas, ketika Fania kembali dan berdiri di depan kami, ia membawa kabar baik."

    show fania casual_senyum_ceria:
        zoom fania_default.zoom
        yalign fania_default.yalign
    fania "\"Kami udah baikan.\""

    show raden kasual_biasa:
        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Bagus. Kamu udah ngelangkah. Sisanya tinggal dijalanin aja, pelan-pelan.\""

    santo "\"Anyway, kita pamit dulu ya.\""

    santo "\"Sudah janji mau datang ke Acaranya Kak Sekar..\""

    raden "\"Iya, udah waktunya juga. Tapi jangan lupa istirahat, Fan.\""

    show fania casual_senyum_normal_biasa:
        zoom fania_default.zoom
        yalign fania_default.yalign
    fania "\"Makasih, kalian berdua. Beneran… makasih.\""

    jump arc_character_day2_scene5
