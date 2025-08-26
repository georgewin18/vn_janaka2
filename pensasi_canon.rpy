define raden_nvl = Character("Raden", kind=nvl, callback=Phone_SendSound)
define santo_nvl = Character("Santo", kind=nvl, callback=Phone_ReceiveSound)
define fania_nvl = Character("Fania", kind=nvl, callback=Phone_ReceiveSound)
define aisyah_nvl = Character("Aisyah", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

label pensasi_canon:
    #kelas d4
    #suasana netral in campus
    
    scene bg kelas_d4 with dissolve

    play music campus fadein 1.0

    "Minggu ke-15 perkuliahan akhirnya tiba, saat para mahasiswa tenggelam dalam kesibukan menyelesaikan Ujian Akhir Semester."

    "Suasana kampus dipenuhi wajah-wajah lelah namun lega, tanda perjuangan panjang hampir mencapai garis akhir. Satu semester berlalu begitu cepat, seolah hanya berkedip dalam perjalanan waktu."

    "Aku tersenyum lega sambil meregangkan badan."

    show raden kasual_ceria at raden_default:
        xalign -0.2
    with dissolve

    raden "\"Akhirnya kelar juga semua ujian teori,\""

    show santo kasual_bicara at santo_default:
        xalign 1.0
    with dissolve
    show raden kasual_biasa

    santo "\"Jangan senang dulu, gimana dengan projectmu?\""

    show raden kasual_tersenyum
    show santo kasual_netral

    raden "\"Aman, tinggal acc dari dosen.\""

    show santo kasual_senyum

    santo "\"Yakin gak revisi?\""

    show raden kasual_ceria

    raden "\"Hahaha, penting yakin aja.\""

    santo "\"Terserah kamu lah.\""

    show raden kasual_tersenyum

    raden "\"Oh iya, kira-kira di jurusan Multimedia sama Informatika ujiannya gimana ya?\""

    santo "\"Aku udah tanya di grup, tapi kayaknya belum—\""

    show santo kasual_terkejut

    santo "\"Oh! barusan dibalas\""

    show raden kasual_biasa
    show santo kasual_netral

    #kurang icon hp fania sama aisyah
    santo_nvl "Gimana ujian kalian?"(interact = False)
    
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
    show santo kasual_kesal with dissolve
    santo "\"Aku balik dulu kalau gitu, den\""

    raden "\"Ga ikut ke perpus?\""

    santo "\"Ga, ada latihan buat tourney besok\""

    raden "\"Oh.. ya, hati-hati!\""

    hide santo
    hide raden
    with dissolve

    pause 0.5

    #Pasca lt atas
    scene bg lt_6_pasca with dissolve:
        zoom 0.5

    "Sambil berjalan pergi juga, aku melanjutkan chat untuk merencanakan pertemuan untuk acara besok. terlalu fokus dengan HP hingga nyaris menabrak seseorang—"

    show sekar kasual_lelah_kantung_mata at sekar_default:
        xalign 1.0
    with dissolve

    voice "audio/vo/sekar/pensasi_canon/pensasi_1_uhh.flac"
    sekar "\"Uh..\""

    show raden kasual_biasa at raden_default:
        xalign -0.2
    with dissolve

    raden "\"Oh maaf Kak—\""

    #raden kaget
    show raden kasual_kaget
    raden "\"Kak Sekar?!!\""

    voice "audio/vo/sekar/pensasi_canon/pensasi_2_ohh.flac"
    sekar "\"Oh. Raden ya..\"" #Sekar (kantung mata) lelah  (nada perlahan, kecapekan.)

    #raden gugup
    show raden kasual_canggung

    "Ekspresi Kak Sekar terlihat berbeda hari ini. Biasanya, dia selalu tampil tegas dan penuh semangat. Namun, kali ini matanya tampak lebih lelah, dengan raut wajah yang menunjukkan tanda-tanda kurang tidur."
    
    "Seperti ada beban yang menekan, membuatnya tampak kurang bertenaga."

    voice "audio/vo/sekar/pensasi_canon/pensasi_3_maaf.flac"
    sekar "Maaf ya… aku lagi buru-buru ini."

    "Nafas Kak Sekar terdengar terengah-engah, seperti baru saja dikejar sesuatu atau terburu-buru."

    menu:
        "Sarankan untuk menenangkan diri terlebih dahulu.":
            show raden kasual_biasa2
            raden "\"Tenang dulu kak.. nafas dulu pelan-pelan\""

            "Dia mengikuti saranku, menarik napas dalam-dalam dan menghembuskannya perlahan. "

            show sekar kasual_hembus_nafas_kantung_mata

            pause 0.2

            show sekar kasual_hembus_nafas with dissolve

            pause 0.2

            show sekar kasual_hembus_nafas_kantung_mata with dissolve

            voice "audio/vo/sekar/pensasi_canon/pensasi_4_huft.flac"
            sekar "\"Haahh… hah…\""

            voice "audio/vo/sekar/pensasi_canon/pensasi_5_terima_kasih.flac"
            sekar "\"Terima kasih ya, Den\""

            raden "\"Kak Sekar beneran gapapa? Kak Sekar keliatan lelah banget loh.\""

            show sekar kasual_lelah_kantung_mata
            "Dia mengangguk pelan, meski masih terlihat lelah."

            voice "audio/vo/sekar/pensasi_canon/pensasi_6_uas.flac"
            sekar "\"UAS, PENSASI, semuanya barengan. Bikin pusing.\""

            show raden kasual_tersenyum
            raden "\"Oh, Pantes. Jangan maksain diri, Semangat ya Kak Sekar.\""

            show raden kasual_biasa
            show sekar kasual_senyum_kurang_tidur
            #Sekar (kantung mata) senyum 
            "Dia tersenyum lemah sambil mengangguk lagi."

            voice "audio/vo/sekar/pensasi_canon/pensasi_7_udah_biasa.flac"
            sekar "\"Udah biasa kok multitasking gini.\""
            
            voice "audio/vo/sekar/pensasi_canon/pensasi_8_aku.flac"
            sekar "\"Aku pergi dulu ya, masih banyak yang harus kusiapkan.\""

            "Tanpa menunggu jawaban dariku, Kak Sekar perlahan pergi, langkahnya tetap terburu-buru."

            jump pensasi_canon_afterchoice1

        "Tanyakan masalah apa yang menimpanya.":
            show raden kasual_biasa2
            raden "\"Buru-buru mau kemana, Kak?\""

            voice "audio/vo/sekar/pensasi_canon/pensasi_9_besok.flac"
            sekar "\"Besok PENSASI, terus UAS juga\""

            voice sustain

            sekar "\"Rasanya kepala mau pecah ngurus semuanya.\""

            show raden kasual_tersenyum
            raden "\"Oh, Pantes. Jangan maksain diri, Semangat ya Kak Sekar.\""

            #Sekar (kantung mata) senyum
            show raden kasual_biasa
            show sekar kasual_senyum_kurang_tidur

            "Dia hanya tersenyum lemah singkat sebelum langsung berbalik, langkahnya cepat menuruni tangga."

            voice "audio/vo/sekar/pensasi_canon/pensasi_10_makasih.flac"
            sekar "\"Makasih Den. Aku pergi dulu ya!\""

            jump pensasi_canon_afterchoice1

label pensasi_canon_afterchoice1:

    "{i}Sebaiknya aku juga segera pergi. Aisyah dan Fania sedang menungguku di perpustakaan.{i}"

    #Perpustakaan
    scene bg perpus_pasca with dissolve

    #suara scan ktm

    "Di perpustakaan, mataku langsung tertuju pada dua temanku, Aisyah dan Fania, yang sudah menemukan tempat duduk nyaman di sudut ruangan."

    "Mereka tampak asyik dengan masing-masing kegiatan—Aisyah sibuk mencatat sesuatu di buku, sementara Fania terlihat fokus membaca layar laptopnya."

    "Setelah meletakkan tas di loker, aku langsung menghampiri mereka."

    show raden kasual_biasa at raden_default:
        xalign 0.45
    with dissolve

    raden "\"Udah dari tadi, ya?\""

    "Aku menarik kursi untuk duduk di samping Fania. Sedangkan Aisyah duduk di sisi lain Fania."

    #Aisyah Serius, Fania Kesal Muncul
    show raden at raden_default:
        xalign -0.5
    with moveinright

    show aisyah casual_serius at aisyah_default:
        xalign 1.35

    show fania casual_dingin at fania_default:
        xalign 0.6

    with dissolve

    voice "audio/vo/fania/pensasi_canon/pensasi_1_dari_pagi.flac"
    fania "\"Dari pagi aku mah,\""

    aisyah "\"Kalo aku barusan selesai ujian.\'"

    "jawab Aisyah sambil tetap mencatat sesuatu di bukunya."

    show raden kasual_tersenyum

    raden "\"Ngapain Fan dari pagi di perpus?\""

    show raden kasual_biasa

    voice "audio/vo/fania/pensasi_canon/pensasi_2_sebenernya.flac"
    fania "\"Sebenarnya ada kelas pagi, tapi di cancel... terus habis ini ada kelas juga,\""

    #(menghela nafas) 
    voice "audio/vo/fania/pensasi_canon/pensasi_3_menghela.flac"
    
    show fania casual_menghelanapas
    pause 0.3

    voice sustain

    show fania casual_menghelanapas_ada_asap with dissolve
    pause 0.3

    voice sustain

    show fania casual_menghelanapas with dissolve
    
    "Fania menghela napas berat. Ekspresinya tampak lesu."

    show fania casual_kesal

    #(Suara meninggi sedikit) 
    
    voice "audio/vo/fania/pensasi_canon/pensasi_4_kapan_ini.flac"
    fania "\"Kapan ini demo projectnya?\""

    aisyah "\"Katamu gampang,\""

    #(Suara meninggi lagi) 
    voice "audio/vo/fania/pensasi_canon/pensasi_5_teorinya.flac"
    fania "\"Teorinya mah easy-peasy... project juga gampang sebenarnya, tapi gatau dah maunya dosen gimana,\""

    aisyah "\"Fan..! suaramu kekencengan,\""

    #fania canggung
    show fania casual_canggung
    voice "audio/vo/fania/pensasi_canon/pensasi_6_sorry.flac"
    fania "\"Ah, sorry!\""

    "Fania langsung menurunkan nada suaranya, memasang wajah kesal."

    show fania casual_kesal

    #raden canggung
    show raden kasual_canggung
    raden "\"Hahaha…\""

    "Aku tertawa kecil melihat reaksinya."

    show fania casual_dingin

    "Kemudian, aku menoleh ke Aisyah yang sedang melanjutkan menulis dengan serius di buku kecilnya."

    #Aisyah serius
    show raden kasual_tersenyum

    raden "\"Ngerjain apa, Syah?\""

    show raden kasual_biasa

    aisyah "\"Flowchart pemrograman,\""

    "Dia menjawab tanpa mengalihkan pandangan dari bukunya."

    show raden kasual_tersenyum

    raden "\"Flowchart...? Coba lihat,\""

    show raden kasual_biasa at raden_default:
        xalign 0.55
    show fania at fania_default:
        xalign -0.6
    with moveinleft
    
    "Aku berjalan dan berdiri di belakangnya. Aku mengamati dengan seksama diagram yang sedang dia buat."

    show raden kasual_tersenyum

    raden "\"Hmm... desain sistem ya?\""

    show raden kasual_biasa
    
    aisyah "\"Iya. Buat aplikasi,\""

    show raden kasual_tersenyum
    
    raden "\"Mirip ama jaringan..\""

    raden "\"Ini tugas?\""

    show raden kasual_biasa
    
    aisyah "\"Bisa dibilang tugas buat UAS,\""

    "Balas Aisyah sambil tetap fokus pada gambarnya."

    show raden kasual_bingung
    
    raden "\"Emang bisa gitu...? UAS dan tugas kan beda,\""

    show aisyah casual_kesal

    aisyah "\"Suka-suka dosen lah..\""

    #fania biasa
    show fania casual_senyum_normal_biasa

    voice "audio/vo/fania/pensasi_canon/pensasi_7_aku_juga.flac"
    fania "\"Aku juga ada yang tugas buat UAS.\""

    show aisyah casual_serius
    show raden kasual_biasa
    
    raden "\"Enak banget kalau kayak gitu,\""

    "Aku berjalan kembali ke kursiku."

    show raden kasual_biasa at raden_default:
        xalign -0.5
    show fania at fania_default:
        xalign 0.6
    with moveinleft

    "Beberapa menit berikutnya, kami sibuk dengan urusan masing-masing. Hening hanya diisi oleh suara keyboard dan kertas yang bergesekan. Hingga tiba-tiba aku teringat sesuatu."

    show raden kasual_tersenyum

    raden "\"Eh, ngomong-ngomong soal PENSASI.. ternyata kak Sekar jadi panitia.. Tadi aku ketemu dia kelihatan capek banget.\""

    show raden kasual_biasa

    "Aisyah menatapku sekilas sebelum kembali fokus ke flowchart-nya."

    aisyah "\"Ya wajar sih, event sebesar itu. Apalagi waktu ujian gini.\""

    show raden kasual_bingung

    raden "\"Tapi emang PENSASI itu apa sih?\""

    aisyah "\"Pameran Inovasi dan Teknologi Vokasi atau yang biasa disebut PENSasi adalah kegiatan pameran edukasi teknologi yang dihelat langsung oleh Politeknik Elektronika Negeri Surabaya.\""

    aisyah "\"kegiatan tersebut menghadirkan berbagai teknologi hasil karya dosen dan mahasiswa PENS, siswa SMA/SMK sederajat, serta pihak industri.\""

    show raden kasual_biasa2

    raden "\"Emangnya kamu robot..?\""

    "Fania menoleh ke arahku."

    voice "audio/vo/fania/pensasi_canon/pensasi_8_intinya.flac"
    fania "\"Intinya, acara ini showcase produk. Acaranya di Pasca, ada tiga bagian: booth, workshop, dan pitching produk di auditorium.\""

    voice "audio/vo/fania/pensasi_canon/pensasi_9_ohiya.flac"
    fania "\"Oh iya, katanya Kak Tessa jaga booth penelitian juga di sana.\""

    "{i}Kak Tessa? Apa dia bisa menjaga booth dan bertemu orang asing. Takutnya bakal…{i}"

    #Flashback prolog if needed

    raden "\"Penelitian apa?\""

    voice "audio/vo/fania/pensasi_canon/pensasi_10_gatau.flac"
    fania "\"Gak tahu, pokoknya sama dosen,\""

    "Fania menutup laptopnya dan membereskan barang-barangnya."

    show raden kasual_tersenyum

    raden "\"Besok mau liat-liat PENSasi bareng?\""

    show raden kasual_biasa
    show aisyah casual_senyum

    aisyah "\"Boleh\""

    show fania casual_dingin

    voice "audio/vo/fania/pensasi_canon/pensasi_11_umm.flac"
    fania "\"ummmm…\""

    show aisyah casual_senyum2

    aisyah "\"Ayo Fan, besok udah ga ada ujian lagi kan kamu?\""

    show aisyah casual_senyum
    show fania casual_senyum_normal_biasa

    voice "audio/vo/fania/pensasi_canon/pensasi_12_yaudah.flac"
    fania "\"Yauda deh, aku ikut\""

    voice "audio/vo/fania/pensasi_canon/pensasi_13_eh_duluan_ya.flac"
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
    scene bg depan_pasca_ramai with dissolve:
        zoom 0.5

    "Sekitar pukul jam 8 lebih aku sampai di kampus dan berjalan menuju gedung Pascasarjana, tempat acara PENSASI digelar."

    "Suasana di depan gedung mulai mencair setelah upacara pembukaan yang baru saja selesai."

    "Beberapa kelompok orang terlihat bergerombol, berbincang, atau sekadar berjalan santai menuju bagian dalam gedung."

    "\"\—Dengan penelitian yang dilakukan, diharapkan para mahasiswa ikut berkontribusi dalam kemajuan negara…\""

    "Kalimat terakhir dari sambutan Direktur kampus masih terngiang di pikiranku."

    "Sambil melangkah ke arah keramaian, mataku sibuk memindai wajah-wajah di sekitar, mencari keberadaan Aisyah dan Fania. Namun, sejauh ini, tak satu pun dari mereka tampak."

    "\"{i}Mungkin saja mereka sudah masuk duluan,{i}\""

    scene black with dissolve

    scene bg lt_6_pasca_ramai with dissolve:
        zoom 0.5
    
    "Aku terus menaiki tangga, berharap menemukan mereka di setiap lantai. Tetapi sampai di lantai enam pun, aku tetap tidak melihat mereka."

    "Aku mencoba mengirim pesan kepada mereka, tetapi tidak ada balasan."

    "Baru saja aku hendak mencari tempat duduk, aku mendengar suara pelan dari arah samping."

    show raden kasual_biasa at raden_default:
        xalign -0.2
    show erin kasual_netral at erin_default:
        xalign 1.0
    with dissolve

    erin "\"Eh... Raden?\""

    "Aku menoleh. Di dekat salah satu pilar, berdiri sosok yang langsung kukenal. Erin, di tangannya tergenggam brosur lipat dari salah satu booth."

    show raden kasual_tersenyum

    raden "\"Erin? Kamu di sini juga?\""

    show raden kasual_biasa

    erin "\"Iya, iseng aja keliling. Katanya acaranya bagus, jadi aku mampir sendiri.\""

    "Erin menatap sekeliling sebentar, lalu kembali padaku"

    erin "\"Kamu sendirian?\""

    show raden kasual_tersenyum

    raden "\"Iya, lagi nyariin Aisyah sama Fania. Tapi belum kelihatan…\""

    show raden kasual_biasa

    erin "\"Kalau begitu… sambil nunggu mereka, mau jalan bareng aku sebentar? Aku belum sempat lihat sisi yang bagian barat.\""

    show raden kasual_tersenyum

    raden "\"Wah, maaf ya, Rin. Aku udah janji buat muter bareng Aisyah sama Fania. Nanti malah mereka nyariin.\""

    show raden kasual_biasa

    erin "\"Oh, tentu. Aku paham kok. Maaf ya, tiba-tiba ngajak.\""

    erin "\"Kalau begitu, semoga acaranya menyenangkan, ya. Sampai ketemu lagi, Den.\""

    "Ia melangkah pergi ke arah koridor kanan."

    hide erin with moveoutright
    show raden at raden_default:
        xalign 0.45
    with moveinright

    "\"{i}Ngapain sekarang...?{i}\""

    menu:
        "Menyapa Sekar":#sekar route
            jump pensasi_sekar_scene1

        "Menunggu Aisyah dan Fania":
            "Aku memutuskan mencari tempat duduk untuk menunggu Aisyah dan Fania datang. Suasana di sekitar masih cukup ramai, tapi aku berhasil menemukan bangku kosong di dekat jendela."

            scene black with dissolve
            pause(0.3)

            #notif hp

            "Notifikasi ponselku berbunyi, mengusik keheningan sejenak. Aku membuka layar, membaca pesan yang baru saja masuk."

            "\"{i}Sepertinya mereka berdua sudah datang.{i}\""

            jump pembukaan_pensasi_afterchoice1

        "Pergi menyapa Tessa sebentar":#tessa route
            jump pensasi_tessa_scene1

label pembukaan_pensasi_afterchoice1:
    #Pasca lt 6 zoom out
    scene bg lt_6_pasca_ramai with dissolve:
        zoom 0.5

    "Aku berjalan menuju pintu lift untuk menjemput mereka."

    "Begitu pintu terbuka, dua wajah familiar muncul—Aisyah dengan senyumnya yang canggung, dan Fania yang memasang ekspresi santai seperti biasa."

    show raden kasual_biasa at raden_default:
        xalign -0.5
    show aisyah casual_senyum at aisyah_default:
        xalign 1.35
    show fania casual_senyum_normal_biasa at fania_default:
        xalign 0.6
    with dissolve

    show raden kasual_tersenyum

    raden "Lama kalian…?"

    show aisyah casual_senyum3

    aisyah "\"Maaf ya,\""

    voice "audio/vo/fania/pensasi_canon/pensasi_14_kamunya.flac"
    fania "\"Kamunya aja yang kepagian,\""

    show raden kasual_biasa

    raden "\"Oke ayok lihat-lihat.\""

    show aisyah casual_senyum

    "Kami berjalan menyusuri deretan booth wirausaha mahasiswa yang berada di lantai 6. Ada berbagai jenis usaha yang dipamerkan, mulai dari kuliner, kerajinan, hingga teknologi."

    "Salah satu booth yang menarik perhatian adalah booth kerupuk gurami. Aroma gurih menggoda dari sampel yang mereka tawarkan berhasil membuat kami berhenti sejenak."

    "Salah satu booth yang menarik perhatian adalah booth kerupuk gurami. Aroma gurih menggoda dari sampel yang mereka tawarkan berhasil membuat kami berhenti sejenak."

    "Aisyah mengamati dengan serius brosur yang diberikan penjaga booth, sementara Fania hanya mencicipi sampel kerupuk sambil bersandar di meja."

    show raden kasual_tersenyum

    raden "\"Kerupuk gurami ya, lumayan nih,\""

    show fania casual_senyum_ceria

    voice "audio/vo/fania/pensasi_canon/pensasi_tertawa.flac"
    "Fania tertawa kecil sambil melahap potongan kerupuk terakhirnya" #fania tertara

    show fania casual_senyum_normal_biasa

    voice "audio/vo/fania/pensasi_canon/pensasi_15_bagus.flac"
    fania "\"Bagus buat apa? Kalau aku sih nggak kebayang kerja jualan kerupuk kayak gini. Keliatannya boring.\""

    #aisyah serius
    show aisyah casual_serius
    aisyah "\"Boring? Ini kan soal uang, Fan. Bisnis itu soal gimana kamu dapet profit!\""
    #(Aisyah nada suaranya naik sedikit)

    show fania casual_dingin
    voice "audio/vo/fania/pensasi_canon/pensasi_16_ga_semuanya.flac"
    fania "\"Nggak semuanya soal duit, Ais. Kalau nggak enjoy, mending nggak usah.\""

    voice "audio/vo/fania/pensasi_canon/pensasi_17_yang_penting.flac"
    fania "\"Yang penting passion dan kesenangan.\""

    aisyah "\"Fan, nggak realistis kalau kamu cuma mikirin passion tanpa mikir untung\""
    
    aisyah "\"..Hidup tuh butuh duit, tau!\""

    show fania casual_kesal

    voice "audio/vo/fania/pensasi_canon/pensasi_18_ya_tapi.flac"
    fania "\"Ya, tapi aku nggak mau kerja sambil menderita karena nggak suka sama apa yang aku kerjain. Uang aja nggak cukup buat bikin hidup berarti,\""

    show raden kasual_canggung

    "Aku hanya berdiri di tengah mereka, memandang argumen yang tiba-tiba muncul entah dari mana ini."

    "Sesekali aku mencoba mengalihkan perhatian dengan menunjuk booth lain, tapi keduanya sudah terlanjur terlibat debat kecil."

    aisyah "\"Raden setuju sama aku, kan?\""

    "Aisyah menatapku dengan penuh keyakinan."

    show fania casual_dingin
    voice "audio/vo/fania/pensasi_canon/pensasi_19_ah_gamungkin.flac"
    fania "\"Ah, nggak mungkin. Raden pasti lebih mendukung soal passion.\""

    "Timpal Fania, menatapku dengan senyum percaya diri."
    menu:
        "Setuju dengan Aisyah":
            show raden kasual_gugup
            raden "\"Aku rasa Aisyah ada benarnya, Fan. Passion itu penting, tapi kalau nggak ada uang, sulit juga bertahan hidup.\""

            raden "\"Apalagi zaman sekarang hampir semuanya diatur dengan uang.\""

            show raden kasual_canggung

            show fania casual_menghelanapas
            pause 0.3

            show fania casual_menghelanapas_ada_asap with dissolve
            pause 0.3

            show fania casual_menghelanapas with dissolve

            "Fania menghela napas, jelas kurang setuju dengan pendapatku."

            #fania kesal
            show fania casual_kesal
            voice "audio/vo/fania/pensasi_canon/pensasi_20_jadi.flac"
            fania "\"Jadi kamu lebih milih kerja yang nggak kamu suka asal dapet duit, gitu?\""

            show raden kasual_gugup
            
            raden "\"Bukan soal suka atau nggak suka, tapi gimana kita bisa cari keseimbangan.\""

            raden "\"Kalau kita bisa nemu bisnis yang kita enjoy dan menguntungkan, itu ideal. Tapi kalau nggak, kadang kita harus kompromi sedikit.\""

            show raden kasual_canggung
            show fania casual_menghelanapas
            show aisyah casual_bersemangat
            
            "Aisyah tersenyum puas, sementara Fania hanya mengedikkan bahu, terlihat belum sepenuhnya setuju."

            voice "audio/vo/fania/pensasi_canon/pensasi_21_yaudah.flac"
            fania "\"Ya udah, terserah deh,\""

            show aisyah casual_senyum4

            aisyah "\"Udahlah jangan terlalu dibawa serius.. nanti juga tahu mana yang terbaik\""

            show raden kasual_biasa

            "Aku mengangguk kecil, sementara Fania hanya menghela napas kecil, memilih mengalihkan pandangannya ke booth lain."

            jump pembukaan_pensasi_afterchoice2

        "Setuju dengan Fania":
            show fania casual_dingin
            show raden kasual_gugup
            raden "\"Kalau aku sih lebih setuju sama Fania. Passion itu penting banget, Ais.\""

            raden "\"Kalau kita nggak suka sama apa yang kita kerjain, seberapa pun besarnya profit, tetap aja bakal ngerasa capek terus.\""

            show raden kasual_canggung
            "Aisyah melipat brosurnya dengan sedikit kesal, menatapku dengan nada protes."
            #aisyah keasal
            show aisyah casual_kesal

            aisyah "\"Raden, bisnis itu nggak sesimpel soal suka atau nggak suka. Kamu butuh profit biar bisnis bisa jalan terus. Passion nggak bakal bayar tagihan!\""

            show raden kasual_gugup
            raden "\"Setuju, Syah. Tapi kalau nggak ada passion, bisnis juga nggak bakal bertahan lama. Kita bakal burn out sebelum bisa benar-benar sukses.\""

            show raden kasual_canggung
            voice "audio/vo/fania/pensasi_canon/pensasi_22_tuh.flac"
            fania "\"Tuh, Aisyah. Raden juga tahu kalau hidup itu nggak cuma soal duit.\""

            aisyah "\"Ya udah, terserah kalian. Tapi jangan salahkan aku kalau nanti susah cari uang,\""

            show fania casual_senyum_normal_biasa
            "Fania tertawa kecil, merasa puas, sementara aku hanya bisa menghela napas lega karena perdebatan kecil ini akhirnya selesai."

            show aisyah casual_serius
            "Aisyah masih tampak memendam ketidaksetujuannya, tetapi suasana mulai mencair."

            jump pembukaan_pensasi_afterchoice2

label pembukaan_pensasi_afterchoice2:

    "..."

    "Aku mulai merasa jenuh dan bingung, nggak tahu harus ngapain selanjutnya."

    show fania casual_dingin
    show aisyah casual_senyum
    show raden kasual_tersenyum

    raden "\"Terus.. Ngapain sekarang?\""

    show aisyah casual_senyum2

    aisyah "\"Masuk ke Auditorium aja yuk!\""

    show raden kasual_biasa
    voice "audio/vo/fania/pensasi_canon/pensasi_23_ngapain.flac"
    fania "\"Ngapain juga kesana?\""

    aisyah "\"Ada pitch produk di sana, bisa dapet insight baru.\""

    show fania casual_menghelanapas
    voice "audio/vo/fania/pensasi_canon/pensasi_24_ga_tertarik.flac"
    fania "\"Gak tertarik aku, mau turun aja.\""

    menu:
        "Ikut Fania":#fania route
            show aisyah casual_senyum
            show fania casual_dingin
            "Aku memutuskan untuk mengikuti Fania yang tampaknya lebih santai"

            show raden kasual_tersenyum
            raden "\"Ya udah, kalau gitu kita turun aja, Fan.\""

            voice "audio/vo/fania/pensasi_canon/pensasi_25_oke.flac"
            fania "\"Okey!!.\""

            jump pensasi_fania
        
        "Ikut Aisyah":#aisyah route
            show fania casual_dingin
            show raden kasual_tersenyum
            raden "\"Ya udah, aku ikut Aisyah aja,\""

            show aisyah casual_senyum4
            aisyah "\"Yuk, bisa dapat banyak hal baru kita Den.\""

            "Kami menuju ke Auditorium dengan langkah cepat, Aisyah tampak antusias, sementara aku agak ragu. Tapi, siapa tahu aku bisa mendapatkan sesuatu yang menarik dari acara ini."

            #"{i}jump route aisyah{/i}"
            jump pensasi_aisyah_scene1