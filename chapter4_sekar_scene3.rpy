label chapter4_sekar_scene3:
    show raden biasa
    show santo kemeja_biasa
    show sekar jas_normal

    "Semua sudah menyelesaikan makanannya, kemudian Kak Sekar bertanya"

    show sekar jas_bicara

    voice "audio/vo/sekar/chapter4/chapter4_3_1_oh_iya.flac"
    sekar "\"Oh iya, kalian ada waktu nggak?\""

    show sekar jas_normal
    show raden ngomong

    raden "\"Ada sih kak, kenapa emangnya?\""

    show raden biasa
    show sekar jas_bicara

    voice "audio/vo/sekar/chapter4/chapter4_3_2_ini.flac"
    sekar "\"Ini aku butuh bantuan untuk mengangkat-angkat barang, karena pihak kepanitiaan kekurangan anggota. Cuacanya lagi sering hujan, jadi banyak yang sakit dan tidak hadir\""

    pause 1

    voice "audio/vo/sekar/chapter4/chapter4_3_3_ada_konsumsi.flac"
    sekar "\"Ada konsumsinya juga kok\""

    menu:
        "Tugas masih ada yang belum sih, tapi sekali-kali gpp lah ikut ke ginian":
            jump chapter4_sekar_scene2_choice3_1
        "Tugas masih ada yang belum sih, tolak aja deh":
            jump chapter4_sekar_scene2_choice3_2
        "Malas banget aku, tolak aja deh":
            $ chapter4_sekar_choice3_3_choosen = True
            jump chapter4_sekar_scene2_choice3_3

    return

label chapter4_sekar_scene2_choice3_1:
    show raden ngomong

    raden "\"Aku bisa sih kak, kalau membantu angkat-angkat barang doang\""

    show santo kemeja_bicara

    santo "\"Kalau aku nggak bisa, soalnya tugasku masih menunggu untuk diselesaikan hari ini\""

    show raden biasa
    show santo kemeja_biasa
    show sekar jas_bicara

    voice "audio/vo/sekar/chapter4/chapter4_3_1_1_baiklah.flac"
    sekar "\"Baiklah kalau begitu, oh iya, kalau kalian mau mengunjungi acaranya, kalian bisa langsung datang saja kok\""

    show sekar jas_normal
    show raden ngomong
    show santo kemeja_biasa

    raden "\"Siap kak\""

    show raden biasa
    show sekar jas_bicara

    voice "audio/vo/sekar/chapter4/chapter4_3_1_2_kalau_begitu.flac"
    sekar "\"Kalau begitu ayo langsung ke lapmer den\""

    show raden ngomong

    raden "\"Siap kak\""

    raden "\"Duluan yak, to\""

    show santo kemeja_bicara

    santo "\"Iya den\""

    scene bg lapmer with dissolve:
        zoom 0.5

    show raden biasa:
        zoom 0.23 yalign 0.1 xalign 0.0
    show sekar jas_normal:
        zoom 1.15 yalign 0.03 xalign 2.5
    with dissolve

    show sekar jas_bicara

    voice "audio/vo/sekar/chapter4/chapter4_3_1_3_guys.flac"
    sekar "Guys, aku kembali dengan membawa sukarelawan nih"

    anon "\"Wih, dapet darimana kar?\""

    voice "audio/vo/sekar/chapter4/chapter4_3_1_4_ga_sengaja.flac"
    sekar "\"Nggak sengaja ketemu adik kelas di kantin. Ku ajak, untungnya mau dia. Jadi ini kutitipin ke kamu ya\""

    anon "\"Oke kar\""

    voice "audio/vo/sekar/chapter4/chapter4_3_1_5_sana_den.flac"
    sekar "\"Sana den ikut kating itu\""

    raden "\"Siap kak\""

    hide sekar with dissolve
    show raden with moveinleft:
        xalign 0.5

    anon "\"Jadi... siapa namamu?\""

    show raden ngomong

    raden "\"Raden kak\""

    anon "\"Asal mana?\""

    raden "\"Surabaya\""

    bima "\"Sama nih aku juga dari Surabaya. Oh iya, panggil aja aku Bima\""

    raden "\"Siap Kak Bima\""

    "Setelah berkenalan dengan kating tersebut, Aku membantu sesuai instruksi yang diberikan. Tugas yang diberikan bisa terbilang berat, karena ada sekitar 3 anak yang tidak hadir."

    "Tapi, Aku tetap membantu sekuat tenagaku"

    "Ketika acara sudah selesai, disitulah waktu istirahat untuk para panitia koordinator barang dimulai."

    #malem
    scene bg lapmer with dissolve:
        zoom 0.5

    show raden capek with dissolve:
        zoom 0.23 yalign 0.1 xalign 0.5

    raden "\"Capek banget dah\""

    bima "\"Aman den?\""

    raden "\"Dah, tewas kak\""

    bima "\"Hahaha, nih makan dulu\""

    show raden biasa

    raden "\"Makasih kak. Btw, sudah nggak ada kerjaan lagi kan?\""

    bima "\"Ada sih, cuma mengembalikan barang ke tempatnya\""

    raden "\"Waduh, kalau begitu kubantu aja kak, aku makannya nanti aja\""

    bima "\"Jangan begitu dong den, kamu disini kan cuma membantu, dengan bantuanmu yang sebelumnya itu sudah cukup. Jadi jangan membebani dirimu lagi\""

    raden "\"Nggak apa-apa nih kak? Aku jadi nggak enak kalo nggak ikut membantu\""

    bima "\"Gapapa den, makan aja sana\""

    raden "\"Ok, kak\""

    bima "\"Kalau begitu aku tinggal dulu ya den\""

    stop music fadeout 2.0

    "Aku memilih makan di pinggiran lapmer, karena tempat ini, tempat paling sepi daripada tempat lainnya, aku mendengar suara langkah mendekat"

    #show sekar
    show raden:
        xalign 0.0
    show sekar jas_normal:
        zoom 1.15 yalign 0.03 xalign 2.5
    with moveinright

    play music sekar_bgm fadein 1.0

    "Aku menoleh dan melihat Kak Sekar berdiri di depanku. Wajahnya sedikit terlihat lebih tenang dari biasanya"

    show sekar jas_bicara

    voice "audio/vo/sekar/chapter4/chapter4_3_1_6_gimana_den.flac"
    sekar "\"Gimana den? Masih kuat kan?\""

    show sekar jas_normal
    show raden ngomong

    raden "\"Masih Kak, Apalagi dikasih makan begini, udah semangat lagi ini\""

    show sekar jas_bicara

    voice "audio/vo/sekar/chapter4/chapter4_3_1_7_haha_bisa_aja.flac"
    sekar "\"Haha, bisa aja den\""

    show sekar jas_normal
    show raden biasa

    "Namun, tawanya cepat mereda. Dia terdiam sejenak, kemudian duduk dekat di sebelahku tanpa banyak bicara."

    show sekar jas_bicara

    voice "audio/vo/sekar/chapter4/chapter4_3_1_8_btw.flac"
    sekar "\"Btw makasih ya den, dengan bantuannya. Acaranya berjalan lancar karenamu nih\""

    show sekar jas_normal

    "Aku hanya mengangguk kecil, merasakan kehangatan dalam kata-katanya. Ada sesuatu yang berbeda dari Kak Sekar saat ini, sesuatu yang membuat hatiku berdetak lebih cepat."

    stop music fadeout 2.0

    "Keheningan yang nyaman menyelimuti kami, hanya ditemani suara daun yang berdesir pelan. Tapi keheningan itu tak berlangsung lama."

    show sekar jas_bicara

    voice "audio/vo/sekar/chapter4/chapter4_3_1_9_den.flac"
    sekar "\"Den...\""

    show sekar jas_normal
    show raden ngomong    

    raden "\"Iya, kak?\""

    show raden biasa
    show sekar jas_bicara

    play music dramatic fadein 1.0

    voice "audio/vo/sekar/chapter4/chapter4_3_1_10_kenapa.flac"
    sekar "\"Kenapa kamu kuliah? Apalagi di PENS, ada alasan khusus?\""

    show raden ngomong
    show sekar jas_normal

    raden "\"Aku sih...\""

    raden "\"Nggak ada alasan yang spesial sih kak. Aku cuma ingin menjadi pribadi mapan... dan juga, kurasa berkuliah adalah sebuah kesempatan yang tidak bisa dirasakan semua orang\""

    show sekar jas_bicara
    show raden biasa

    voice "audio/vo/sekar/chapter4/chapter4_3_1_11_terus.flac"
    sekar "\"Terus, kenapa menurutmu penting den?\""

    show sekar jas_normal
    show raden ngomong

    raden "\"Untuk kasus ku sendiri, alasannnya mempersiapkan diri ke dunia yang lebih luas diluar sana...\""

    raden "\"Di saat kita masih SD, SMP, SMA ataupun SMK, kita hanya diajarkan materi dan melatih kedisiplinan kita.\""
    
    raden "\"Yaa, meskipun anak SMK sudah diajarkan dasar sebelum bekerja, tapi aku rasa masih belum cukup\""

    raden "\"Sedangkan, saat kuliah, kita mulai dikenalkan dengan dunia yang lebih luas dan kompleks. Bukan hanya soal teori, tapi juga bagaimana cara berpikir kritis, menyelesaikan masalah, dan beradaptasi dengan berbagai situasi.\""

    raden "\"Kuliah juga mengajarkan untuk lebih mandiri, baik secara akademis maupun dalam kehidupan sehari-hari\""

    raden "\"Setidaknya itu yang kuharapkan\""

    show raden biasa

    "Kak Sekar mendengarkanku dengan seksama, tetapi dengan perlahan ekspresinya berubah. Ada keterkejutan sama di wajahnya, seolah dia tidak menyangka jawaban itu keluar dari raden."

    show raden ngomong

    raden "\"Selain itu, PENS kan terkenal sebagai politeknik terbaik se-Asia Tenggara\""

    raden "\"Aku pikir, kalau aku mau berhasil, ini adalah tempat yang tepat\""

    show raden biasa

    "Kak Sekar tetap diam, tetapi ekspresinya sekarang sedikit serius. Ekspresinya seperti mencoba memahami setiap kata yahng baru saja kuucapkan."

    "Dia tersenyum samar, meskipun matanya masih terlihat serius, seolah ada banyak hal yang sedang dia pikirkan."

    show raden ngomong

    raden "\"Kalau kakak sendiri?\""

    raden "\"Apa alasan Kakak kuliah di PENS?\""

    show raden biasa

    "Dia menundukkan kepala sedikit, seolah mencari jawaban di antara sela-sela dedaunan yang berguguran."

    show sekar jas_bicara

    voice "audio/vo/sekar/chapter4/chapter4_3_1_12_aku_ya.flac"
    sekar "\"Aku ya, hmmm...\""

    show sekar jas_normal

    "Kak Sekar terdiam sejenak, wajahnya sedikit muram seolah memikirkan apa yang harus dijawab, sementara aku menatapnya, berusaha membaca pikirannya yang tampak begitu berat."

    show raden ngomong

    raden "\"Jika kakak masih ragu bagaimana cara menjawabnya, lebih baik dipendam dulu untuk sekarang\""

    show raden biasa
    show sekar jas_bicara

    voice "audio/vo/sekar/chapter4/chapter4_3_1_13_eh_maaf.flac"
    sekar "\"Eh, maaf den. Padahal aku duluan yang memulai percakapan, malah aku juga yang menghentikan percakapan\""

    show raden ngomong
    show sekar jas_normal

    raden "\"Gapapa kak, ini juga salahku sih karena menjawab pertanyaan kaka dengan jawaban yang dalam seperti itu\""

    show raden biasa

    "Aku hanya bisa tersenyum kecil, merasakan sesuatu yang hangat mengalir di dadaku. Kata-katanya terasa seperti meninggalkan jejak yang dalam. Kemudian, dia melangkah pergi, meninggalkan keheningan yang anehnya menenangkan."

    scene black with dissolve
    with Pause(0.2)

    centered "Hari itu, aku tidak hanya melihat sisi lain dari Kak Sekar, tetapi juga merasakan hubungan yang lebih dalam. Seperti ada sesuatu yang tak terucap, namun terasa nyata."

    stop music fadeout 2.0

    jump chapter4_sekar_good_ending

label chapter4_sekar_scene2_choice3_2:
    show raden ngomong
    show sekar jas_normal

    raden "\"Maaf nih kak, tapi aku masih ada tugas\""

    show santo kemeja_bicara

    santo "\"Kalau aku nggak bisa soalnya tugasku masih menunggu untuk diselesaikan hari ini\""

    show sekar jas_bicara
    show santo kemeja_biasa
    show raden biasa
    
    voice "audio/vo/sekar/chapter4/chapter4_3_2_1_baiklah.flac"
    sekar "\"Baiklah kalau begitu\""

    voice "audio/vo/sekar/chapter4/chapter4_3_2_2_oh_iya.flac"
    sekar "\"Oh iya, jika kalian mau mengunjungi acaranya, kalian bisa langsung datang aja kok\""

    show raden ngomong

    raden "\"Siap kak\""

    #hide sekar
    hide sekar with dissolve
    show raden:
        xalign 0.0
    show santo:
        xalign 2.7
    with moveinleft

    raden "\"To\""

    show raden biasa
    show santo kemeja_bicara

    santo "\"Apa den?\""

    show santo kemeja_biasa
    show raden ngomong

    raden "\"Mau bantu aku mengerjakan tugas nggak?\""

    show santo kemeja_bicara
    show raden biasa

    santo "\"Tumben ngajak, biasanya dijawab lagi malas\""

    show santo kemeja_biasa
    show raden ngomong

    raden "\"Iya sih, tapi dipikir-pikir enakan nggak ada beban\""

    show santo kemeja_bicara
    show raden biasa

    santo "\"Yasudah sih gapapa\""

    show santo kemeja_biasa
    show raden ngomong

    raden "\"Memangnya kamu mau ngerjain dimana?\""

    show santo kemeja_bicara
    show raden biasa
    
    santo "\"Terserah sih, perpus pasca aja kali\""

    show santo kemeja_biasa
    show raden ngomong

    raden "\"Okeh aku ikut ya\""

    show santo kemeja_bicara

    santo "\"Ayo aja\""

    hide santo
    hide raden
    with moveoutright

    #perpus
    scene bg auditorium with dissolve:
        zoom 0.5

    show raden biasa:
        zoom 0.23 yalign 0.1 xalign 0.0
    show santo kemeja_biasa:
        zoom 1.15 yalign 0.08 xalign 2.7
    with moveinleft

    "Sesampainya di perpustakaan pasca kami langsung melakukan scan, dan langsung mencari tempat duduk."

    show raden ngomong

    raden "\"Seperti biasa disini dingin\""

    show raden biasa
    show santo kemeja_bicara

    santo "\"Tapi enak disini den, suasananya tenang\""

    show raden ngomong
    show santo kemeja_biasa

    raden "\"Iya sih\""

    show raden biasa
    show santo kemeja_bicara

    santo "\"Jadi kau butuh bantuan seperti apa?\""

    show raden ngomong
    show santo kemeja_biasa

    raden "\"Hampir semua sih...\""

    pause 2

    #show santo kesal

    raden "\"Canda, canda. Aku hanya tidak tahu bagaimana tata letak penulisanmu\""

    show raden biasa
    show santo kemeja_bicara

    santo "\"Bilang dong\""

    show santo kemeja_biasa

    "Dengan bantuan Santo, tugasku akhirnya selesai juga. Setelah mengerjakan tugas, kami bingung mau ngapain"

    menu:
        "Ikut ke acara yang dipanitiai oleh Kak Sekar":
            jump chapter4_sekar_scene2_choice3_2_1
        "Aku sudah lelah, langsung pulang saja":
            jump chapter4_sekar_scene2_choice3_2_2

label chapter4_sekar_scene2_choice3_3:
    show raden ngomong
    show sekar jas_normal

    raden "\"Maaf kak, tapi kurasa aku nggak bisa ikut\""

    show santo kemeja_bicara

    santo "\"Kalau aku nggak bisa soalnya tugasku masih menunggu untuk diselesaikan hari ini\""

    show sekar jas_bicara
    show santo kemeja_biasa
    show raden biasa

    voice "audio/vo/sekar/chapter4/chapter4_3_2_1_baiklah.flac"
    sekar "\"Baiklah kalau begitu\""

    voice "audio/vo/sekar/chapter4/chapter4_3_2_2_oh_iya.flac"
    sekar "\"Oh iya, jika kalian mau mengunjungi acaranya, kalian bisa langsung datang aja kok\""

    show raden ngomong

    raden "\"Siap kak\""

    #hide sekar
    hide sekar with dissolve
    show raden:
        xalign 0.0
    show santo:
        xalign 2.7
    with moveinleft

    raden "\"Yaudah to, pulang dulu ya\""

    hide raden with moveoutleft

    "Santo hanya mengangguk melihatku pergi"

    stop music fadeout 2.0

    if (chapter4_sekar_choice1_2_choosen == True and chapter4_sekar_choice2_2_choosen == True):
        jump chapter4_sekar_bad_ending
    else:
        jump chapter4_sekar_neutral_ending

label chapter4_sekar_scene2_choice3_2_1:
    "Aku terpikirkan undangan dari Kak Sekar, jadi aku mengajak Santo untuk datang bersamaku. Sayangnya dia menolak ajakanku dan langsung pergi untuk pulang."

    stop music fadeout 2.0

    scene bg lapmer with dissolve:
        zoom 0.5

    show raden biasa with dissolve:
        zoom 0.23 yalign 0.1 xalign 0.5

    "Jadi aku memutuskan untuk pergi ke sana sendirian."

    raden "\"Acaranya mungkin udah mau selesai. Tapi gapapa deh, aku masih bisa lihat-lihat sebentar. Lagian, Kak Sekar tadi bilang bisa langsung dateng kalu mau ngunjungi acaranya\""

    "Saat aku sampai, lampu-lampu hias yang sebelumnya terang kini mulai diredupkan, dan beberapa stand terlihat sudah ditutup. Hanya ada beberapa mahasiswa yang masih berbincang, sementara panitia sibuk membereskan dekorasi dan perlengkapan."

    raden "\"Wah, keknya aku telat banget deh...\""

    "Dari kejauhan, terlihat Kak Sekar sedang mengatur beberapa panitia yang mengangkat kotak-kotak besar ke mobil pickup. Wajahnya terlihat lelah, tetapi dia tetap memberikan arahan dengan tegas."

    "Aku berjalan mendekati Kak Sekar dengan sedikit ragu. Ketika aku mendekat, Sekar menoleh dan melihatku."

    show raden with moveinright:
        xalign 0.0
    show sekar jas_bicara with dissolve:
        zoom 1.15 xalign 2.5 yalign 0.03

    play music sekar_bgm fadein 1.0

    voice "audio/vo/sekar/chapter4/chapter4_3_2_1_1_oh_raden.flac"
    sekar "\"Oh, Raden. Kamu datang juga ya?\""

    show sekar jas_normal
    show raden ngomong

    raden "\"Iya, Kak. Tapi... kayaknya udah telat banget ya?\""

    show sekar jas_bicara
    show raden biasa

    voice "audio/vo/sekar/chapter4/chapter4_3_2_1_2_bisa_dibilang.flac"
    sekar "\"Bisa dibilang begitu, gimana tugasmu? Beres?\""
    
    show sekar jas_normal
    show raden ngomong
    
    raden "\"Iya, Kak. Baru selesai, makanya aku baru bisa ke sini\""

    show sekar jas_bicara
    show raden biasa

    voice "audio/vo/sekar/chapter4/chapter4_3_2_1_3_baguslah.flac"
    sekar "\"Baguslah kalau selesai. Tapi lain kali, coba atur waktumu lebih baik, ya\""

    show sekar jas_normal
    show raden ngomong

    raden "\"Iya, Kak. Maaf banget gak bisa bantu tadi\""

    show sekar jas_bicara
    show raden biasa

    voice "audio/vo/sekar/chapter4/chapter4_3_2_1_4_gapapa.flac"
    sekar "\"Gak apa-apa. Setiap orang punya prioritas kok\""

    menu:
        "Bantu Kak Sekar":
            jump chapter4_sekar_scene2_choice3_2_1_1
        "Lihat-lihat acara":
            jump chapter4_sekar_scene2_choice3_2_1_2

label chapter4_sekar_scene2_choice3_2_2:
    raden "Aku dah lelah banget, langsung pulang aja"

    stop music fadeout 2.0

    jump chapter4_sekar_neutral_ending

label chapter4_sekar_scene2_choice3_2_1_1:
    show sekar jas_normal
    show raden ngomong

    raden "\"Kak Sekar, sekarang lagi ngembaliin perlengkapan ya? Biar kubantu kak\""

    show sekar jas_bicara
    show raden biasa

    voice "audio/vo/sekar/chapter4/chapter4_3_2_1_5_gausah.flac"
    sekar "\"Nggak usah den, udah mau selesai kok\""

    show sekar jas_normal
    show raden ngomong

    raden "\"Gapapa kak, anggap aja permintaan maafku, gabisa bantu tadi\""

    show raden biasa

    "Barang-barang sudah dimasukkan ke mobil pickup, dan lokasi acara mulai kosong. Aku dan Kak Sekar berdiri di pinggir lokasi, mengawasi panitia lain yang berkemas."

    show raden ngomong

    raden "\"Akhirnya selesai juga\""

    show sekar jas_bicara
    show raden biasa

    voice "audio/vo/sekar/chapter4/chapter4_3_2_1_6_makasih.flac"
    sekar "\"Makasih ya den, udah nyempetin bantu\""

    show sekar jas_normal
    show raden ngomong

    raden "\"Aman kak, sama-sama\""

    "Setelah itu kami berpamitan dan pulang."

    stop music fadeout 2.0

    jump chapter4_sekar_neutral_ending

label chapter4_sekar_scene2_choice3_2_1_2:
    show sekar jas_normal
    show raden ngomong

    raden "\"yaudah, aku mau lihat sisa-sisa acaranya kak\""

    "Sekar hanya mengangguk lalu kembali membereskan dekorasi dan perlengkapan bersama panitia lain. Karena tidak banyak yang tersisa, aku pulang saja karena bosan"

    stop music fadeout 2.0

    jump chapter4_sekar_neutral_ending