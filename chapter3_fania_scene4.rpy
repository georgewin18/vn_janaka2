label chapter3_fania_scene4:

    scene bg depan_auditorium with dissolve:
        zoom 0.5

    #raden santo netral
    show raden biasa with dissolve:
        zoom 0.2 xalign 0.2 yalign 0.0
    show santo kemeja_biasa with dissolve:
        zoom 1.0 xalign 1.5 yalign 0.06

    "Aku dan Santo melihat Aisyah dan Fania di perpustakaan."
    
    raden "Lah, ada Fania sama Aisyah tuh."

    menu:
        "Cari tempat duduk aja kali ya.":
            raden "Biar deh, ayo cari tempat duduk."

            "aku langsung mengalihkan perhatianku dari dua perempuan itu dan kembali ke tujuan utamanya."

            santo "Kayaknya mereka kena sesuatu deh, gimana hampiri bentar yuk?"

            show raden bingung

            raden "Lah? Tumben, tapi gak lah, lagian mereka juga sibuk."

            "Hanya melihat dari kejauhan, aku bisa melihat Fania dan Aisyah begitu bersemangat dengan jumlah buku yang mereka baca."

            santo "Ayolah, cuma sebentar doang,"

            raden "Tapi kan nanti ganggu mereka."

            "Aku tetap kukuh. Bagaimanapun, itu adalah ide yang buruk untuk membuat Aisyah marah nanti."

            santo "Nanti ngomong aja kalau aku yang nyuruh"

            jump chapter3_fania_scene4_afterchoice1
        
        "Cek mereka dulu, kayaknya ada sesuatu.":
            raden "Ayo coba kita cek dulu, kayaknya mereka ada sesuatu deh,"

            santo "Oke. Kayaknya mereka lagi sibuk, mungkin kita bisa bantu,"

            "Balasan Santo, yang membuatku terkejut. Aku mengabaikan itu dan langsung menghampiri Aisyah dan Fania."

            raden "Aisyah! Fania!"

            #fania kesal
            show fania kemeja_biasa with dissolve:
                zoom 1.1 xalign 1.0 yalign 0.06
            
            "Tapi melihat ekspresi Fania yang berubah mengkerut kesal, sepertinya itu adalah sebuah kesalahan untuk menghampiri mereka."
            #affection turun
            
            jump chapter3_fania_scene4_afterchoice1

label chapter3_fania_scene4_afterchoice1:

    show raden:
        xalign -0.2
    show santo:
        xalign 0.2
    with moveinright

    show aisyah kemeja_gugup with dissolve:
        zoom 0.34 yalign -1.0 xalign 1.2

    show fania kemeja_biasa:
        zoom 1.1 xalign 1.86 yalign 0.06

    #mulai dari sini agak bingung santo diilanin atau gak, soalnya blm ngomong apa apa tapi masih dinotice raden non dialog
    "..."

    "..."

    "Hanya ada keheningan dan suara ketukan keyboard dari laptop Fania yang terdengar di antara keduanya. Udara canggung itu berasal dari Fania yang jutek dan Aisyah yang nampak khawatir tapi tidak mampu menunjukkannya tanpa mengganggu temannya."

    "Aku mendekat pada Aisyah dan berbisik padanya."

    raden "Aisyah, ini Fania yang ngambil semua bukunya?"

    aisyah "Iya, dia lagi ngerjain tugas katanya,"

    "jawab Aisyah dengan suara pelan yang mengikutiku."

    "Jawabannya itu membuatku dan Santo mau tidak mau melongo dengan jumlahnya."

    #raden kaet
    show raden bingung
    raden "Hah? Tugas? Banyak banget, departemenku aja belum pernah ada yang kayak gini di kelas satu. Kecuali…"

    "Aku memandang buku-buku yang dibaca Fania. Teknik multitasking yang luar biasa."

    aisyah "Kayaknya itu bukan tugas individu deh, Den."

    "Aisyah menjawab dengan khawatir. Dan aku setuju pada Aisyah."

    menu:
        "Fania, ini kamu ngerjain tugas kelompok sendiri?":
            show raden bingung
            raden "Fania, ini kamu ngerjain tugas kelompok sendiri?"

            "Aku bertanya kepada Fania, tapi dia tidak menjawab dan kelihatan semakin malas untuk menjawab atas pertanyaanku. Mungkin, aku terlalu ikut campur."

            #affection turun

            jump chapter3_fania_scene4_afterchoice2
        
        "Fania, ini tugas kelompok kan? Kok bisa kamu ngerjain semuanya sendiri?":
            show raden bingung
            raden "Fania, ini tugas kelompok kan? Kok bisa kamu ngerjain semuanya sendiri?"

            "Aku bertanya kepada Fania, tapi dia tidak menjawab dan kelihatan semakin malas untuk menjawab atas pertanyaanku. Mungkin, aku terlalu ikut campur."

            #affection turun

            jump chapter3_fania_scene4_afterchoice2

label chapter3_fania_scene4_afterchoice2:
    #fania kesal
    show fania jas_bicara
    fania "Kalau kalian punya waktu buat diskusi, minimal jangan ganggu orang ngerjain tugas."

    show aisyah kemeja_gugup
    aisyah "Fania, biar ku bantu!"

    "Aisyah langsung berkata, menyela Fania dari memarahiku."

    menu:
        "Ikut bantu Fania":
            raden "Kalau begitu, aku juga bakalan bantu, Fan. Tapi aku mau kamu kasih tau kita nanti kenapa kamu ngerjain tugasmu sendirian,"

            #fania dingin
            show fania kemeja_biasa
            fania "Tapi aku gak minta bantuan,"

            raden "Sh, sh. Abaikan detailnya."

            #affection naik
            #Backsound Suasana sedikit dramatis

            santo "Jadi kamu mau bantuin Fania sekarang? tugas kita gimana?"

            "Santo bertanya, saat dia mulai duduk di kursi yang tersisa."#di sini sih santo baru duduk

            raden "Tugas kita kan gak sesusah itu, lagian, mana ada orang yang bisa nyelesain tugas sesuai tenggat waktu?"

            "balasku saat meraih buku dan mulai menyalin kalimat yang Fania butuhkan dan mengirimnya melalui private chat agar dia bisa langsung menyalin."

            santo "Seriusan?"

            show raden senyum sadar
            raden "Duariusan."

            show aisyah kemeja_senyum

            "Aisyah terkekeh kecil dan Fania hanya menunjukkan emot batu pada candaanku."

            jump chapter3_fania_scene4_afterchoice3

        "Tidak ikut membantu":

            "Aku hanya diam melihat dan membiarkan Aisyah membantu Fania."

            santo "Jadi kamu gak punya niat bantu? Biasanya bantuin,"

            #raden cangung
            show raden ngomong
            raden "Tapi kita punya tugas sendiri, gak mungkinlah kita jadi kena hukuman,"

            santo "Tapi kalau diperkirakan, kita bisa nyelesain tugas Fania duluan dan kita masih punya waktu banyak untuk deadline kita. Fania, aku bakalan bantu."

            show raden bingung

            "Balasan Santo membuatku bingung pada sifatnya hari ini yang tiba-tiba unjuk gigi pada orang lain, padahal, biasanya dia hanya akan melihat dari samping."

            "Melihat mereka semua, sayang sekali jika aku tidak membantu. Pada akhirnya, aku tidak bisa menahan diri dan mengikuti arus."

            show raden biasa
            raden "Oke deh, aku bakalan bantu juga!"

            jump chapter3_fania_scene4_afterchoice3

label chapter3_fania_scene4_afterchoice3:
    #Backsound Suasana sedikit dramatis

    fania "Kenapa kalian pada bantu, padahal aku gak minta?"

    "Aisyah menatap Fania dengan senyuman, tetapi ada ketegasan dalam nada suaranya."

    aisyah "Karena kami gak mungkin diam aja lihat kamu kerja kayak gini, Fan. Kita teman kan?"

    "Fania kembali menatap layar laptopnya, mengetik beberapa baris lagi tanpa menanggapi. Tapi gerakannya sedikit melambat, seperti memikirkan jawaban."

    raden "Fania, ini kan tugas kelompok, kita bisa bantu dikit-dikit."

    "Fania menghentikan ketikannya, lalu menutup laptop dengan pelan. Dia menatap mereka dengan ekspresi dingin, tetapi ada sedikit kelelahan di matanya."

    #fania menghela nafas
    show fania kemeja_biasa
    "haahhh…"

    #fania senyum
    show fania kemeja_bicara
    fania "Makasih, Aisyah, Santo, Raden."

    fania "Sebenarnya, aku ada masalah sama anggota kelompokku…"

    "Fania bercerita kepada kami, tentang masalah yang dia hadapi."

    "Masalah internal yang diakibatkan hanya karena seseorang memiliki urusan pribadi dan cekcok yang berakhir pada pertengkaran Fania dan salah satu rekan di kelompoknya."

    fania "… Jadi kupikir, mending ngerjain sendiri aja, daripada sama rekan yang gak jelas kabarnya,"

    "Cerita yang Fania beritahukan kepada kita bertiga menjelaskan bahwa sifatnya itu ada bukan tanpa alasan. Dia telah kehilangan kepercayaannya pada orang lain."






    