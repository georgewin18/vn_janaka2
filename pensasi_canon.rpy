define raden_nvl = Character("Raden", kind=nvl, callback=Phone_SendSound)
define santo_nvl = Character("Santo", kind=nvl, callback=Phone_ReceiveSound)
define fania_nvl = Character("Fania", kind=nvl, callback=Phone_ReceiveSound)
define aisyah_nvl = Character("Aisyah", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

label pensasi_canon:
    #kelas d4
    #suasana netral in campus
    
    scene bg lap_futsal with dissolve:
        zoom 0.5

    play music campus fadein 1.0

    "Minggu ke-15 perkuliahan akhirnya tiba, saat para mahasiswa tenggelam dalam kesibukan menyelesaikan Ujian Akhir Semester."

    "Suasana kampus dipenuhi wajah-wajah lelah namun lega, tanda perjuangan panjang hampir mencapai garis akhir. Satu semester berlalu begitu cepat, seolah hanya berkedip dalam perjalanan waktu."

    "Aku tersenyum lega sambil meregangkan badan."

    show raden kasual_biasa with dissolve:
        zoom 0.48 xalign 0.2 yalign 0.1

    raden "\"Akhirnya kelar juga semua ujian teori,\""

    show santo kemeja_biasa with dissolve:
        zoom 1.0 xalign 1.5 yalign 0.06

    santo "\"Jangan senang dulu, gimana dengan projectmu?\""

    raden "\"Aman, tinggal acc dari dosen.\""

    santo "\"Yakin gak revisi?\""

    raden "\"Hahaha, penting yakin aja.\""

    santo "\"Terserah kamu lah.\""

    raden "\"Oh iya, kira-kira di jurusan Multimedia sama Informatika ujiannya gimana ya?\""

    santo "\"Aku udah tanya di grup, tapi kayaknya belum—\""

    santo "\"Oh! barusan dibalas\""

    #kurang icon hp fania sama aisyah
    window hide
    santo_nvl "Gimana ujian kalian?"(interact = False)
    
    window show
    fania_nvl "Multimedia mah gampang."(interact = False)
    aisyah_nvl "Aku dapet info menarik nih" 
    aisyah_nvl "Besok ada acara PENSASI"
    #ini bener kah
    #aisyah_nvl "*attach foto"
    #aisyah_nvl "➀  Foto" #ini gak bisa
    nvl_narrator "Aisyah mengirim foto"
    raden_nvl "Apaan PENSASI?"
    aisyah_nvl "Pameran penelitian gitu"
    aisyah_nvl "Pokoknya ayo hadir"
    raden_nvl "Gass"
    fania_nvl "Apa serunya"
    aisyah_nvl "Pasti seru bisa lihat” karya"
    santo_nvl "Aku ada turnamen Esport besok"
    aisyah_nvl "Yah.."
    raden_nvl "Kamu gimana Fan? ikut aja daripada gak ngapa”in, UAS juga udah selesai."
    fania_nvl "iyadah kalau mood"
    aisyah_nvl "Oh iya, aku sama Fania lagi di perpus, mau kesini?"
    raden_nvl "Otw"

    nvl clear

    #Santo Kesal (Di sini raden tidak menyadari ekspresi sinis jadi gak dideskripsikan)
    show santo kemeja_biasa
    santo "\"Aku balik dulu kalau gitu, den\""

    raden "\"Ga ikut ke perpus?\""

    santo "\"Ga, ada latihan buat tourney besok\""

    raden "\"Oh.. ya, hati-hati!\""

    hide santo with dissolve
    hide raden with dissolve

    pause 0.5

    #Pasca lt atas
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    "Sambil berjalan pergi juga, aku melanjutkan chat untuk merencanakan pertemuan untuk acara besok. terlalu fokus dengan HP hingga nyaris menabrak seseorang—"

    show sekar kemeja_biasa with dissolve:
        zoom 1.15 xalign 1.1 yalign 0.05

    sekar "\"Uh..\""

    show raden kasual_biasa with dissolve:
        zoom 0.48 xalign 0.2 yalign 0.1

    raden "\"Oh maaf Kak—\""

    #raden kaget
    show raden kasual_kaget
    raden "\"Kak Sekar?!!\""

    show sekar kemeja_lelah_kantung_mata
    sekar "\"Oh. Raden ya..\"" #Sekar (kantung mata) lelah  (nada perlahan, kecapekan.)

    #raden gugup
    show raden kasual_biasa

    "Ekspresi Kak Sekar terlihat berbeda hari ini. Biasanya, dia selalu tampil tegas dan penuh semangat. Namun, kali ini matanya tampak lebih lelah, dengan raut wajah yang menunjukkan tanda-tanda kurang tidur."
    
    "Seperti ada beban yang menekan, membuatnya tampak kurang bertenaga."

    sekar "Maaf ya… aku lagi buru-buru ini."

    "Nafas Kak Sekar terdengar terengah-engah, seperti baru saja dikejar sesuatu atau terburu-buru."

    menu:
        "Sarankan untuk menenangkan diri terlebih dahulu.":
            raden "\"Tenang dulu kak.. nafas dulu pelan-pelan\""

            "Dia mengikuti saranku, menarik napas dalam-dalam dan menghembuskannya perlahan. "

            sekar "\"Haahh… hah…\""

            sekar "\"Terima kasih ya, Den\""

            raden "\"Kak Sekar beneran gapapa? Kak Sekar keliatan lelah banget loh.\""

            "Dia mengangguk pelan, meski masih terlihat lelah."

            sekar "\"UAS, PENSASI, semuanya barengan. Bikin pusing.\""

            raden "\"Oh, Pantes. Jangan maksain diri, Semangat ya Kak Sekar.\""

            show sekar kemeja_lelah_kantung_mata
            #Sekar (kantung mata) senyum 
            "Dia tersenyum lemah sambil mengangguk lagi."

            sekar "\"Udah biasa kok multitasking gini.\""
            
            sekar "\"Aku pergi dulu ya, masih banyak yang harus kusiapkan.\""

            "Tanpa menunggu jawaban dariku, Kak Sekar perlahan pergi, langkahnya tetap terburu-buru."

            jump pensasi_canon_afterchoice1

        "Tanyakan masalah apa yang menimpanya.":
            raden "\"Buru-buru mau kemana, Kak?\""

            sekar "\"Besok PENSASI, terus UAS juga\""

            sekar "\"Rasanya kepala mau pecah ngurus semuanya.\""

            raden "\"Oh, Pantes. Jangan maksain diri, Semangat ya Kak Sekar.\""

            #Sekar (kantung mata) senyum
            show sekar kemeja_lelah_kantung_mata

            "Dia hanya tersenyum lemah singkat sebelum langsung berbalik, langkahnya cepat menuruni tangga."

            sekar "\"Makasih Den. Aku pergi dulu ya!\""

            jump pensasi_canon_afterchoice1

label pensasi_canon_afterchoice1:

    "{i}Sebaiknya aku juga segera pergi. Aisyah dan Fania sedang menungguku di perpustakaan.{i}"

    #Perpustakaan
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    #suara scan ktm

    "Di perpustakaan, mataku langsung tertuju pada dua temanku, Aisyah dan Fania, yang sudah menemukan tempat duduk nyaman di sudut ruangan."

    "Mereka tampak asyik dengan masing-masing kegiatan—Aisyah sibuk mencatat sesuatu di buku, sementara Fania terlihat fokus membaca layar laptopnya."

    "Setelah meletakkan tas di loker, aku langsung menghampiri mereka."

    show raden kasual_biasa with dissolve:
        zoom 0.48 xalign 0.5 yalign 0.1

    raden "\"Udah dari tadi, ya?\""

    "Aku menarik kursi untuk duduk di samping Fania. Sedangkan Aisyah duduk di sisi lain Fania."

    #Aisyah Serius, Fania Kesal Muncul
    show raden with moveinright:
        xalign -0.25

    show aisyah kemeja_gugup:
        zoom 0.35 yalign -0.7 xalign 1.15

    show fania casual_kesal:
        zoom 1.15 xalign 0.6 yalign -0.02

    with dissolve

    fania "\"Dari pagi aku mah,\""

    aisyah "\"Kalo aku barusan selesai ujian.\'"

    "jawab Aisyah sambil tetap mencatat sesuatu di bukunya."

    raden "\"Ngapain Fan dari pagi di perpus?\""

    fania "\"Sebenarnya ada kelas pagi, tapi di cancel... terus habis ini ada kelas juga,\""

    #(menghela nafas) 
    show fania casual_menghelanapas
    pause 0.3

    show fania casual_menghelanapas_ada_asap with dissolve
    pause 0.3

    show fania casual_menghelanapas with dissolve
    
    "Fania menghela napas berat. Ekspresinya tampak lesu."

    show fania casual_kesal

    #(Suara meninggi sedikit) 
    
    fania "\"Kapan ini demo projectnya?\""

    aisyah "\"Katamu gampang,\""

    #(Suara meninggi lagi) 
    fania "\"Teorinya mah easy-peasy... project juga gampang sebenarnya, tapi gatau dah maunya dosen gimana,\""

    aisyah "\"Fan..! suaramu kekencengan,\""

    #fania canggung
    show fania casual_canggung
    fania "\"Ah, sorry!\""

    "Fania langsung menurunkan nada suaranya, memasang wajah kesal."

    show fania casual_kesal

    #raden canggung
    show raden kasual_canggung
    raden "\"Hahaha…\""

    "Aku tertawa kecil melihat reaksinya."

    "Kemudian, aku menoleh ke Aisyah yang sedang melanjutkan menulis dengan serius di buku kecilnya."

    #Aisyah serius
    show aisyah kemeja_bingung

    raden "\"Ngerjain apa, Syah?\""

    aisyah "\"Flowchart pemrograman,\""

    "Dia menjawab tanpa mengalihkan pandangan dari bukunya."

    raden "\"Flowchart...? Coba lihat,\""

    "Aku berjalan dan berdiri di belakangnya. Aku mengamati dengan seksama diagram yang sedang dia buat."

    raden "\"Hmm... desain sistem ya?\""

    aisyah "\"Iya. Buat aplikasi,\""

    raden "\"Mirip ama jaringan..\""

    raden "\"Ini tugas?\""

    aisyah "\"Bisa dibilang tugas buat UAS,\""

    "Balas Aisyah sambil tetap fokus pada gambarnya."

    raden "\"Emang bisa gitu...? UAS dan tugas kan beda,\""

    aisyah "\"Suka-suka dosen lah..\""

    #fania biasa
    show fania casual_senyum_normal_biasa

    fania "\"Aku juga ada yang tugas buat UAS.\""

    raden "\"Enak banget kalau kayak gitu,\""

    "Aku berjalan kembali ke kursiku."

    "Beberapa menit berikutnya, kami sibuk dengan urusan masing-masing. Hening hanya diisi oleh suara keyboard dan kertas yang bergesekan. Hingga tiba-tiba aku teringat sesuatu."

    raden "\"Eh, ngomong-ngomong soal PENSASI.. ternyata kak Sekar jadi panitia.. Tadi aku ketemu dia kelihatan capek banget.\""

    "Aisyah menatapku sekilas sebelum kembali fokus ke flowchart-nya."

    aisyah "\"Ya wajar sih, event sebesar itu. Apalagi waktu ujian gini.\""

    raden "\"Tapi emang PENSASI itu apa sih?\""

    aisyah "\"Pameran Inovasi dan Teknologi Vokasi atau yang biasa disebut PENSasi adalah kegiatan pameran edukasi teknologi yang dihelat langsung oleh Politeknik Elektronika Negeri Surabaya.\""

    aisyah "\"kegiatan tersebut menghadirkan berbagai teknologi hasil karya dosen dan mahasiswa PENS, siswa SMA/SMK sederajat, serta pihak industri.\""

    raden "\"Emangnya kamu robot..?\""

    "Fania menoleh ke arahku."

    fania "\"Intinya, acara ini showcase produk. Acaranya di Pasca, ada tiga bagian: booth, workshop, dan pitching produk di auditorium.\""

    fania "\"Oh iya, katanya Kak Tessa jaga booth penelitian juga di sana.\""

    "{i}Kak Tessa? Apa dia bisa menjaga booth dan bertemu orang asing. Takutnya bakal…{i}"

    #Flashback prolog if needed

    raden "\"Penelitian apa?\""

    fania "\"Gak tahu, pokoknya sama dosen,\""

    "Fania menutup laptopnya dan membereskan barang-barangnya."

    raden "\"Besok mau liat-liat PENSasi bareng?\""

    aisyah "\"Boleh\""

    fania "\"ummmm…\""

    aisyah "\"Ayo Fan, besok udah ga ada ujian lagi kan kamu?\""

    fania "\"Yauda deh, aku ikut\""

    fania "\"Eh, duluan ya, ada kelas nih... bye-bye.\""

    hide fania with dissolve

    "Fania segera bangkit dan pergi."

    "Setelah Fania pergi, aku dan Aisyah melanjutkan aktivitas masing-masing. Aisyah masih sibuk dengan flowchart-nya, sementara meneliti kembali project UAS."

    "Waktu berlalu dengan cepat, dan tak terasa sudah sore."

    "Aku pun akhirnya menutup laptop, merasa cukup lega dengan hasil akhir. Aisyah sudah terlihat lebih santai, mungkin juga sudah selesai dengan tugasnya."

    "Kami saling menatap sebentar, lalu aku berdiri dan membereskan barang-barangku."

    "Kampus mulai sepi, Setelah berpamitan dengan Aisyah aku melangkah keluar dengan tenang, menikmati udara sore yang menenangkan."

    hide aisyah with dissolve
    hide raden with dissolve

    scene black with dissolve
    pause (0.3)

    jump pembukaan_pensasi

#[Scene - Pembukaan PENSASI]
label pembukaan_pensasi:
    #Depan Pasca
    scene bg masjid with dissolve:
        zoom 0.5

    "Sekitar pukul jam 8 lebih aku sampai di kampus dan berjalan menuju gedung Pascasarjana, tempat acara PENSASI digelar."

    "Suasana di depan gedung mulai mencair setelah upacara pembukaan yang baru saja selesai."

    "Beberapa kelompok orang terlihat bergerombol, berbincang, atau sekadar berjalan santai menuju bagian dalam gedung."

    "\"\—Dengan penelitian yang dilakukan, diharapkan para mahasiswa ikut berkontribusi dalam kemajuan negara…\""

    "Kalimat terakhir dari sambutan Direktur kampus masih terngiang di pikiranku."

    "Sambil melangkah ke arah keramaian, mataku sibuk memindai wajah-wajah di sekitar, mencari keberadaan Aisyah dan Fania. Namun, sejauh ini, tak satu pun dari mereka tampak."

    "\"{i}Mungkin saja mereka sudah masuk duluan,{i}\""

    scene black with dissolve

    scene bg depan_auditorium with dissolve:
        zoom 0.5
    
    "Aku terus menaiki tangga, berharap menemukan mereka di setiap lantai. Tetapi sampai di lantai enam pun, aku tetap tidak melihat mereka."

    "Aku mencoba mengirim pesan kepada mereka, tetapi tidak ada balasan."

    "\"{i}Ngapain sekarang...?{i}\""

    menu:
        "Menyapa Sekar":#sekar route
            jump pensasi_sekar_scene1

        "Menunggu Aisyah dan Fania":
            "Aku memutuskan mencari tempat duduk untuk menunggu Aisyah dan Fania datang. Suasana di sekitar masih cukup ramai, tapi aku berhasil menemukan bangku kosong di dekat jendela."

            scene black with dissolve
            pause(0.3)

            scene bg depan_auditorium with dissolve

            #notif hp

            "Notifikasi ponselku berbunyi, mengusik keheningan sejenak. Aku membuka layar, membaca pesan yang baru saja masuk."

            "\"{i}Sepertinya mereka berdua sudah datang.{i}\""

            jump pembukaan_pensasi_afterchoice1

        "Pergi menyapa Tessa sebentar":#tessa route
            jump pensasi_tessa_scene1

label pembukaan_pensasi_afterchoice1:
    #Pasca lt 6 zoom out
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    "Aku berjalan menuju pintu lift untuk menjemput mereka."

    "Begitu pintu terbuka, dua wajah familiar muncul—Aisyah dengan senyumnya yang canggung, dan Fania yang memasang ekspresi santai seperti biasa."

    show raden kasual_biasa:
        zoom 0.48 xalign -0.25 yalign 0.1

    show aisyah kemeja_gugup:
        zoom 0.34 yalign -1.0 xalign 1.15

    show fania casual_senyum_normal_biasa:
        zoom 1.15 xalign 0.6 yalign -0.02

    with dissolve

    raden "Lama kalian…?"

    aisyah "\"Maaf ya,\""

    fania "\"Kamunya aja yang kepagian,\""

    raden "\"Oke ayok lihat-lihat.\""

    "Kami berjalan menyusuri deretan booth wirausaha mahasiswa yang berada di lantai 6. Ada berbagai jenis usaha yang dipamerkan, mulai dari kuliner, kerajinan, hingga teknologi."

    "Salah satu booth yang menarik perhatian adalah booth kerupuk gurami. Aroma gurih menggoda dari sampel yang mereka tawarkan berhasil membuat kami berhenti sejenak."

    "Salah satu booth yang menarik perhatian adalah booth kerupuk gurami. Aroma gurih menggoda dari sampel yang mereka tawarkan berhasil membuat kami berhenti sejenak."

    "Aisyah mengamati dengan serius brosur yang diberikan penjaga booth, sementara Fania hanya mencicipi sampel kerupuk sambil bersandar di meja."

    raden "\"Kerupuk gurami ya, lumayan nih,\""

    "Fania tertawa kecil sambil melahap potongan kerupuk terakhirnya" #fania tertara

    fania "\"Bagus buat apa? Kalau aku sih nggak kebayang kerja jualan kerupuk kayak gini. Keliatannya boring.\""

    #aisyah serius
    show aisyah kemeja_senyum
    aisyah "\"Boring? Ini kan soal uang, Fan. Bisnis itu soal gimana kamu dapet profit!\""
    #(Aisyah nada suaranya naik sedikit)

    show fania casual_senyum_normal_biasa
    fania "\"Nggak semuanya soal duit, Ais. Kalau nggak enjoy, mending nggak usah.\""

    fania "\"Yang penting passion dan kesenangan.\""

    aisyah "\"Fan, nggak realistis kalau kamu cuma mikirin passion tanpa mikir untung\""
    
    aisyah "\"..Hidup tuh butuh duit, tau!\""

    fania "\"Ya, tapi aku nggak mau kerja sambil menderita karena nggak suka sama apa yang aku kerjain. Uang aja nggak cukup buat bikin hidup berarti,\""

    "Aku hanya berdiri di tengah mereka, memandang argumen yang tiba-tiba muncul entah dari mana ini."

    "Sesekali aku mencoba mengalihkan perhatian dengan menunjuk booth lain, tapi keduanya sudah terlanjur terlibat debat kecil."

    aisyah "\"Raden setuju sama aku, kan?\""

    "Aisyah menatapku dengan penuh keyakinan."

    fania "\"Ah, nggak mungkin. Raden pasti lebih mendukung soal passion.\""

    "Timpal Fania, menatapku dengan senyum percaya diri."
    menu:
        "Setuju dengan Aisyah":
            raden "\"Aku rasa Aisyah ada benarnya, Fan. Passion itu penting, tapi kalau nggak ada uang, sulit juga bertahan hidup.\""

            raden "\"Apalagi zaman sekarang hampir semuanya diatur dengan uang.\""

            "Fania menghela napas, jelas kurang setuju dengan pendapatku."

            #fania kesal
            show fania casual_kesal
            fania "\"Jadi kamu lebih milih kerja yang nggak kamu suka asal dapet duit, gitu?\""

            raden "\"Bukan soal suka atau nggak suka, tapi gimana kita bisa cari keseimbangan.\""

            raden "\"Kalau kita bisa nemu bisnis yang kita enjoy dan menguntungkan, itu ideal. Tapi kalau nggak, kadang kita harus kompromi sedikit.\""

            "Aisyah tersenyum puas, sementara Fania hanya mengedikkan bahu, terlihat belum sepenuhnya setuju."

            fania "\"Ya udah, terserah deh,\""

            aisyah "\"Udahlah jangan terlalu dibawa serius.. nanti juga tahu mana yang terbaik\""

            "Aku mengangguk kecil, sementara Fania hanya menghela napas kecil, memilih mengalihkan pandangannya ke booth lain."

            jump pembukaan_pensasi_afterchoice2

        "Setuju dengan Fania":
            raden "\"Kalau aku sih lebih setuju sama Fania. Passion itu penting banget, Ais.\""

            raden "\"Kalau kita nggak suka sama apa yang kita kerjain, seberapa pun besarnya profit, tetap aja bakal ngerasa capek terus.\""

            "Aisyah melipat brosurnya dengan sedikit kesal, menatapku dengan nada protes."
            #aisyah keasal
            show aisyah kemeja_bertekad

            aisyah "\"Raden, bisnis itu nggak sesimpel soal suka atau nggak suka. Kamu butuh profit biar bisnis bisa jalan terus. Passion nggak bakal bayar tagihan!\""

            raden "\"Setuju, Syah. Tapi kalau nggak ada passion, bisnis juga nggak bakal bertahan lama. Kita bakal burn out sebelum bisa benar-benar sukses.\""

            fania "\"Tuh, Aisyah. Raden juga tahu kalau hidup itu nggak cuma soal duit.\""

            aisyah "\"Ya udah, terserah kalian. Tapi jangan salahkan aku kalau nanti susah cari uang,\""

            "Fania tertawa kecil, merasa puas, sementara aku hanya bisa menghela napas lega karena perdebatan kecil ini akhirnya selesai."

            "Aisyah masih tampak memendam ketidaksetujuannya, tetapi suasana mulai mencair."

            jump pembukaan_pensasi_afterchoice2

label pembukaan_pensasi_afterchoice2:

    "..."

    "Aku mulai merasa jenuh dan bingung, nggak tahu harus ngapain selanjutnya."

    raden "\"Terus.. Ngapain sekarang?\""

    aisyah "\"Masuk ke Auditorium aja yuk!\""

    fania "\"Ngapain juga kesana?\""

    aisyah "\"Ada pitch produk di sana, bisa dapet insight baru.\""

    fania "\"Gak tertarik aku, mau turun aja.\""

    menu:
        "Ikut Fania":#fania route
            "Aku memutuskan untuk mengikuti Fania yang tampaknya lebih santai"

            raden "\"Ya udah, kalau gitu kita turun aja, Fan.\""

            fania "\"Okey!!.\""

            jump pensasi_fania
        
        "Ikut Aisyah":#aisyah route
            raden "\"Ya udah, aku ikut Aisyah aja,\""

            show aisyah kemeja_senyum

            aisyah "\"Yuk, bisa dapat banyak hal baru kita Den.\""

            "Kami menuju ke Auditorium dengan langkah cepat, Aisyah tampak antusias, sementara aku agak ragu. Tapi, siapa tahu aku bisa mendapatkan sesuatu yang menarik dari acara ini."

            "{i}jump route aisyah{/i}"
            jump pensasi_aisyah_scene1z