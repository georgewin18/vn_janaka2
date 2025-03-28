define fania_nvl = Character("Fania", kind=nvl, callback=Phone_ReceiveSound)
define chapter3_fania_scene4_choice1_2_choosen = False

label chapter3_fania_scene4:
    # screen minggu_selanjutnya():
    #     text "Seminggu seanjutnya"

    centered "Seminggu setelahnya.."

    scene bg depan_auditorium with dissolve:
        zoom 0.5

    play music campus fadein 1.0
    #raden santo netral
    show raden kasual_biasa:
        zoom 0.48 xalign 0.0 yalign 0.1
    show santo kemeja_biasa:
        zoom 1.15 xalign 2.7 yalign 0.08
    with dissolve

    "Aku dan Santo melihat Aisyah dan Fania di perpustakaan."
    
    raden "\"Lah, ada Fania sama Aisyah tuh.\""

    menu:
        "Cari tempat duduk aja kali ya.":
            raden "\"Biar deh, ayo cari tempat duduk.\""

            "aku langsung mengalihkan perhatianku dari dua perempuan itu dan kembali ke tujuan utamanya."

            santo "\"Kayaknya mereka kena sesuatu deh, gimana hampiri bentar yuk?\""

            show raden kasual_bingung

            raden "\"Lah? Tumben, tapi gak lah, lagian mereka juga sibuk.\""

            "Hanya melihat dari kejauhan, aku bisa melihat Fania dan Aisyah begitu bersemangat dengan jumlah buku yang mereka baca."

            santo "\"Ayolah, cuma sebentar doang,\""

            raden "\"Tapi kan nanti ganggu mereka.\""

            "Aku tetap kukuh. Bagaimanapun, itu adalah ide yang buruk untuk membuat Aisyah marah nanti."

            santo "\"Nanti ngomong aja kalau aku yang nyuruh\""

            stop music fadeout 2.0

            jump chapter3_fania_scene4_afterchoice1
        
        "Cek mereka dulu, kayaknya ada sesuatu.":
            raden "\"Ayo coba kita cek dulu, kayaknya mereka ada sesuatu deh,\""

            santo "\"Oke. Kayaknya mereka lagi sibuk, mungkin kita bisa bantu,\""

            "Balasan Santo, yang membuatku terkejut. Aku mengabaikan itu dan langsung menghampiri Aisyah dan Fania."

            raden "\"Aisyah! Fania!\""

            $ chapter3_fania_scene4_choice1_2_choosen = True
            #affection turun
            
            stop music fadeout 2.0

            jump chapter3_fania_scene4_afterchoice1

label chapter3_fania_scene4_afterchoice1:

    show raden:
        xalign -0.5
    show santo:
        xalign -0.25
    with moveinright

    show aisyah kemeja_gugup:
        zoom 0.35 xalign 0.78 yalign -0.7
    show fania casual_dingin:
        zoom 1.15 xalign 1.45 yalign -0.02
    with dissolve

    if (chapter3_fania_scene4_choice1_2_choosen == True):
        "Tapi melihat ekspresi Fania yang berubah mengkerut kesal, sepertinya itu adalah sebuah kesalahan untuk menghampiri mereka."

    #mulai dari sini agak bingung santo diilanin atau gak, soalnya blm ngomong apa apa tapi masih dinotice raden non dialog
    "..."

    "..."

    "Hanya ada keheningan dan suara ketukan keyboard dari laptop Fania yang terdengar di antara keduanya. Udara canggung itu berasal dari Fania yang jutek dan Aisyah yang nampak khawatir tapi tidak mampu menunjukkannya tanpa mengganggu temannya."

    "Aku mendekat pada Aisyah dan berbisik padanya."

    show raden kasual_serius

    raden "\"Aisyah, ini Fania yang ngambil semua bukunya?\""

    $ renpy.show("aisyah kemeja_gugup", zorder=1)
    aisyah "\"Iya, dia lagi ngerjain tugas katanya,\""

    "Jawabannya itu membuatku dan Santo mau tidak mau melongo dengan jumlahnya."

    #raden kaet
    show raden kasual_kaget
    raden "\"Hah? Tugas? Banyak banget, departemenku aja belum pernah ada yang kayak gini di kelas satu. Kecuali…\""

    show raden kasual_serius
    "Aku memandang buku-buku yang dibaca Fania. Teknik multitasking yang luar biasa."

    aisyah "\"Kayaknya itu bukan tugas individu deh, Den.\""

    "Aisyah menjawab dengan khawatir. Dan aku setuju pada Aisyah."

    show raden kasual_bingung
    menu:
        "Fania, ini kamu ngerjain tugas kelompok sendiri?":
            raden "\"Fania, ini kamu ngerjain tugas kelompok sendiri?\""

            "Aku bertanya kepada Fania, tapi dia tidak menjawab dan kelihatan semakin malas untuk menjawab atas pertanyaanku. Mungkin, aku terlalu ikut campur."

            #affection turun

            jump chapter3_fania_scene4_afterchoice2
        
        "Fania, ini tugas kelompok kan? Kok bisa kamu ngerjain semuanya sendiri?":
            raden "\"Fania, ini tugas kelompok kan? Kok bisa kamu ngerjain semuanya sendiri?\""

            "Aku bertanya kepada Fania, tapi dia tidak menjawab dan kelihatan semakin malas untuk menjawab atas pertanyaanku. Mungkin, aku terlalu ikut campur."

            #affection turun

            jump chapter3_fania_scene4_afterchoice2

label chapter3_fania_scene4_afterchoice2:
    play music intense fadein 1.0
    #fania kesal

    show raden kasual_serius
    $ renpy.show("fania casual_kesal", zorder=1) 
    fania "\"Kalau kalian punya waktu buat diskusi, minimal jangan ganggu orang ngerjain tugas.\""

    $ renpy.show("aisyah kemeja_gugup", zorder=2)
    aisyah "\"Fania, biar ku bantu!\""

    "Aisyah langsung berkata, menyela Fania dari memarahiku."

    menu:
        "Ikut bantu Fania":
            raden "\"Kalau begitu, aku juga bakalan bantu, Fan. Tapi aku mau kamu kasih tau kita nanti kenapa kamu ngerjain tugasmu sendirian,\""

            #fania dingin
            $ renpy.show("fania casual_dingin", zorder=2) 
            fania "\"Tapi aku gak minta bantuan,\""

            stop music fadeout 2.0

            raden "\"Sh, sh. Abaikan detailnya.\""

            #affection naik
            #Backsound Suasana sedikit dramatis

            play music dramatic fadein 1.0 

            $ renpy.show("santo kemeja_bicara", zorder=2) 
            santo "\"Jadi kamu mau bantuin Fania sekarang? tugas kita gimana?\""

            show santo kemeja_biasa
            "Santo bertanya, saat dia mulai duduk di kursi yang tersisa."#di sini sih santo baru duduk

            raden "\"Tugas kita kan gak sesusah itu, lagian, mana ada orang yang bisa nyelesain tugas sesuai tenggat waktu?\""

            "balasku saat meraih buku dan mulai menyalin kalimat yang Fania butuhkan dan mengirimnya melalui private chat agar dia bisa langsung menyalin."

            santo "\"Seriusan?\""

            show raden kasual_biasa
            raden "\"Duariusan.\""

            show aisyah kemeja_senyum

            "Aisyah terkekeh kecil dan Fania hanya menunjukkan emot batu pada candaanku."

            jump chapter3_fania_scene4_afterchoice3

        "Tidak ikut membantu":
            show fania casual_dingin

            "Aku hanya diam melihat dan membiarkan Aisyah membantu Fania."

            santo "\"Jadi kamu gak punya niat bantu? Biasanya bantuin,\""

            #raden cangung
            show raden kasual_canggung
            raden "\"Tapi kita punya tugas sendiri, gak mungkinlah kita jadi kena hukuman,\""

            santo "\"Tapi kalau diperkirakan, kita bisa nyelesain tugas Fania duluan dan kita masih punya waktu banyak untuk deadline kita. Fania, aku bakalan bantu.\""

            show raden kasual_bingung

            "Balasan Santo membuatku bingung pada sifatnya hari ini yang tiba-tiba unjuk gigi pada orang lain, padahal, biasanya dia hanya akan melihat dari samping."

            "Melihat mereka semua, sayang sekali jika aku tidak membantu. Pada akhirnya, aku tidak bisa menahan diri dan mengikuti arus."

            stop music fadeout 2.0

            show raden kasual_tersenyum
            raden "\"Oke deh, aku bakalan bantu juga!\""

            play music dramatic fadein 1.0

            jump chapter3_fania_scene4_afterchoice3

label chapter3_fania_scene4_afterchoice3:
    #Backsound Suasana sedikit dramatis

    $ renpy.show("fania casual_dingin", zorder=2) 
    fania "\"Kenapa kalian pada bantu, padahal aku gak minta?\""

    show aisyah kemeja_senyum
    "Aisyah menatap Fania dengan senyuman, tetapi ada ketegasan dalam nada suaranya."

    $ renpy.show("aisyah kemeja_senyum", zorder=3)
    aisyah "\"Karena kami gak mungkin diam aja lihat kamu kerja kayak gini, Fan. Kita teman kan?\""

    "Fania kembali menatap layar laptopnya, mengetik beberapa baris lagi tanpa menanggapi. Tapi gerakannya sedikit melambat, seperti memikirkan jawaban."

    raden "\"Fania, ini kan tugas kelompok, kita bisa bantu dikit-dikit.\""

    "Fania menghentikan ketikannya, lalu menutup laptop dengan pelan. Dia menatap mereka dengan ekspresi dingin, tetapi ada sedikit kelelahan di matanya."

    #fania menghela nafas
    $ renpy.show("fania casual_menghelanapas", zorder=3)
    pause 0.3
    show fania casual_menghelanapas_ada_asap with dissolve
    pause 0.3
    show fania casual_menghelanapas with dissolve
    
    fania "\"haahhh…\""

    #fania senyum
    show fania casual_senyum_normal_biasa
    fania "\"Makasih, Aisyah, Santo, Raden.\""

    show fania casual_dingin
    fania "\"Sebenarnya, aku ada masalah sama anggota kelompokku…\""

    "Fania bercerita kepada kami, tentang masalah yang dia hadapi."

    "Masalah internal yang diakibatkan hanya karena seseorang memiliki urusan pribadi dan cekcok yang berakhir pada pertengkaran Fania dan salah satu rekan di kelompoknya."

    fania "\"… Jadi kupikir, mending ngerjain sendiri aja, daripada sama rekan yang gak jelas kabarnya,\""

    "Cerita yang Fania beritahukan kepada kita bertiga menjelaskan bahwa sifatnya itu ada bukan tanpa alasan. Dia telah kehilangan kepercayaannya pada orang lain."

    menu:
        "Beri saran kepada Fania":
            #Backsound sedikit dramatis
            #spesial momentt
            show raden kasual_biasa
            raden "\"Aku paham.\""

            "Aku mengangguk dengan tenang tanpa mengalihkan mataku dari buku yang ku baca. Perhatian ketiga temanku tertuju ke arahku ketika aku berhenti membaca dan memandang Fania."

            show raden kasual_tersenyum
            raden "\"Aku ngerti kenapa kamu susah percaya sama orang lain. Itu wajar kok, apalagi kalau ada alasannya. Tapi, gak ada salahnya coba kasih kesempatan sekali lagi, kan?\""

            "Perasaan kepercayaan yang telah dikhianati ketika masa PKKMB dan cekcok yang dimulai dari perbedaan cara mengerjakan tugas, membuat Fania tidak lagi berniat memberikan kepercayaan yang dalam kepada orang lain."

            show raden kasual_biasa
            #fania sedih
            show fania casual_sedih with dissolve
            fania "\"Gak segampang itu Den.\""

            fania "\"Santo, Kamu inget satu orang yang dari DTMK di kelompok kita selain aku?\""

            $ renpy.show("santo kemeja_biasa", zorder=3)
            santo "\"Iya.\""

            fania "\"Sifatnya masih sama-sama tidak bertanggungjawab.\""

            #Di bagian ini juga aku bingung masukin aisyah gak, di script sih gak ada suruh tamppilin jadi kupake lokai bertiga ajh
            #santo serius
            #sama sebenernya agak bingung sama spesial moment, kukita itu kaya bg nya diganti kaya fullscreen nampilin karakter(bg full karakter). tapi di sini suruh nampilin karakter(karakter png)

            "Santo hanya bisa mengerutkan keningnya, membuatku memahami bahwa ada masalah yang cukup serius di antara Fania, Santo, dan kelompok PKKMB mereka."

            show raden kasual_tersenyum
            raden "\"Fania, sekarang kamu lihat kami bertiga.\""

            raden "\"Apakah kamu pikir kita kesini buat main-main?\""

            #fania gugup
            show fania casual_dingin
            fania "\"Enggaklah, jelas-jelas kalian kesini buat belajar.\""

            raden "\"Menurutmu semua orang juga sama kayak kita atau orang yang kamu sebutin?\""

            raden "\"Fania, manusia itu rumit. Kamu kira Santo ngerjain tugasnya di sini karena rajin? Bukan, dia malah gabung biar cepet kelar. Malas mikirin tugas sendiri, gitu.\""

            show raden kasual_biasa
            show santo kemeja_bicara
            santo "\"Kamu juga sama aja sih,\""

            show santo kemeja_biasa
            show raden kasual_tersenyum
            raden "\"Waspada itu nggak salah, tapi jangan sampai bikin kamu jadi close-minded, Fania.\""

            raden "\"Menyaring orang itu sih oke, tapi coba deh kasih mereka kesempatan. Siapa tahu mereka punya warna-warni yang bisa ngisi hidup kamu. Hidup ini kan soal saling kenal dan saling terima, kan?\""

            raden "\"Kita ini generasi masa depan, Fania! Dituntut buat open-minded, berpikir kritis, dan jadi agen perubahan!.\""

            raden "\"Jadi, kasih aja mereka waktu. Kalau gagal, yaudah, at least kamu udah berusaha sebaik mungkin. Slow aja, dunia nggak akan runtuh cuma karena kamu kasih orang kesempatan, kok!\""

            stop music fadeout 2.0

            show raden kasual_biasa
            "Aku berhenti, mengakhiri pidato bijak ku dan memandang Fania."

            #Backsound sedikit romantis
            #(Moment) Fania yang tertawa
            #scene bg with dissolve

            play music romantic fadein 1.0

            show fania casual_senyum_ceria
            "Tawa halusnya terdengar seperti lonceng yang dihembuskan oleh angin lembut, berpadu dengan senyum yang memancarkan kehangatan seperti siraman mentari pagi."

            "Aku terdiam sesaat, terpaku pada wajahnya yang terlihat begitu bersinar."

            "Aku mengagumi itu. Mungkin lebih dari sekadar kekaguman biasa."

            show raden kasual_bingung
            raden "\"Lah, kenapa ketawa?\""

            "Apa yang salah?"

            "Apakah aku melakukan kesalahan tadi?"

            raden "\"Kalian sialan, orang bicara malah diketawain.\""

            show fania casual_senyum_normal_biasa
            fania "\"Ok lah, Den.\""

            #(Moment) Fania yang tersenyum dengan cool
            #scene bg with dissolve

            "Fania tersenyum dengan cool, ada sesuatu dalam dirinya yang membuatku semakin terpesona. Caranya menatapku—penuh keyakinan, tapi juga penuh penghargaan—seolah mengatakan kalau dia benar-benar mendengarkan setiap kata yang keluar dari mulutku."

            fania "\"Akan ku lakuin sesuai saranmu. Rasanya gak mungkin deh mengabaikan temanku yang udah berkorban untuk mengatakan semua itu.\""

            show raden kasual_biasa
            raden "\"Kalau begitu, ayo lakuin sekarang!\""

            show fania casual_terkejut
            fania "\"Sekarang?\""

            raden "\"Semakin banyak ditunda bakalan semakin susah nanti. Mendingan sekarang aja.\""

            raden "\"Karena sejatinya, ini adalah tugas kelompok, bukan tugas individu, jadi, akan lebih baik dan maksimal kalau kalian sendiri yang ngerjain, kan? Dan, kalau bukan sekarang, kapan lagi?\""

            show fania casual_dingin
            fania "\"Iya sih..\""

            fania "\"Aku {i}call{i} sekarang.\""

            "Ada sesuatu tentang cara dia mengambil keputusan, tentang caranya menatap dengan keyakinan, yang membuatku tidak bisa berpaling."

            "Aku mungkin baru mengenalnya."

            "Tapi, di momen itu, aku tahu—itulah Fania yang sebenarnya."

            #Transisi Putih
            #di sini aku gak paham maksudnya transisi putih gimana

            "Akhirnya, Fania bangkit dari kursinya, berjalan keluar perpustakaan, dan menelpon teman satu kelompoknya yang sebelumnya sempat terlibat adu mulut dengannya"

            #BG putih
            scene blank with dissolve

            "Di luar, aku membayangkan Fania berbicara dengan tenang namun tegas, meminta maaf atas kata-kata yang sempat menyinggung dan mencela."

            "Di sisi lain, aku juga bisa membayangkan temannya mulai melunak, mengakui kesalahan, dan meminta maaf atas kekeras kepalaannya, serta ide-ide aneh yang sempat ia paksakan."

            "Aku tidak tahu pasti bagaimana percakapan mereka berlangsung. Yang jelas, ketika Fania kembali dan berdiri di depan kami, ia membawa kabar baik."

            scene bg depan_auditorium with dissolve:
                zoom 0.5

            #fania tersenyum
            show fania casual_senyum_normal_biasa:
                zoom 1.15 xalign 0.5 yalign -0.02
            fania "\"Kami udah baikan.\""

            scene black with dissolve

            stop music fadeout 2.0            

            centered "Seminggu setelahnya..."

            #kelasd4
            show bg lap_futsal with dissolve:
                zoom 0.5
            #Backsound Netral suasana kampus
            play music campus fadein 1.0

            #SFX Orang berbincang

            "Di tengah-tengah kelas, aku yang sedang menikmati jam kosong sambil menguap mengantuk merasakan ponselku berbunyi."

            #SFX notifikasi chat

            "Aku mendapatkan sebuah pesan pribadi dari Fania."

            fania_nvl "Makasih Den. Berkat kalian, kami berhasil dapat nilai yang memuaskan dan tidak terdeteksi sebagai buatan AI."
            raden_nvl "Baguslah kalau begitu."

            nvl clear

            scene black with dissolve
            with Pause(0.3)

            stop music fadeout 2.0
            #"CHAPTER 3 (Arc Fania) Ending 1 (+20% affection)."
            jump chapter4_sekar_scene1

        "Buat Fania mengandalkan kita":
            show raden kasual_tersenyum
            raden "\"Kalau begitu, kamu tinggal andalin aja kita sebagai temanmu!\""

            $ renpy.show("aisyah kemeja_senyum", zorder=4)
            aisyah "\"Fania, gimana kalau kamu coba bicara sama teman-teman kelompokmu dan mencoba berbaikan. Pada akhirnya, semua orang punya kekurangan, dan kuyakin mereka juga punya\""

            aisyah '\"Dan kalau mereka tidak menghasilkan apapun, kamu tetap bisa laporkan ke dosen untuk evaluasi lanjutan!\"'

            #fania tersenyum
            $ renpy.show("fania casual_senyum_normal_biasa", zorder=4)
            fania "\"Makasih, Aisyah. Aku bakalan coba hubungi mereka nanti setelah ini selesai.\""

            $ renpy.show("aisyah kemeja_senyum", zorder=4)
            aisyah "\"Baguslah kalau begitu.\""

            scene black with dissolve

            stop music fadeout 2.0
            #Transisi menghitam

            #"Neutral Ending"

            centered "Seminggu setelahnya..."

            #Kelas Raden
            scene bg auditorium with dissolve:
                zoom 0.5

            #Backsound Netral suasana kampus
            play music campus fadein 1.0

            #SFX Orang berbincang

            "Di tengah-tengah kelas, aku yang sedang menikmati jam kosong sambil menguap mengantuk merasakan ponselku berbunyi."

            "Aku mendapatkan sebuah pesan pribadi dari Fania."

            #SFX notifikasi chat

            fania_nvl "\"Makasih Den, walaupun kami gak dapet nilai yang memuaskan, tapi berkat kalian, tugas kami tidak terdeteksi sebagai buatan AI.\""
            raden_nvl "Baguslah kalau begitu."

            nvl clear

            scene black with dissolve
            with Pause(0.3)

            stop music fadeout 2.0
            #CHAPTER 3 (Arc Fania) Ending 2 (+0 affection).
            jump chapter4_sekar_scene1