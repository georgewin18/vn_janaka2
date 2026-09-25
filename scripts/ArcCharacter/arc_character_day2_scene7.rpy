label arc_character_day2_scene7:
    scene black with dissolve
    pause 0.5

    scene bg lapmer with dissolve:
        zoom 0.5

    show raden kasual_biasa at raden_default:
        xalign 0.0
    raden "\"…\""

    show sekar kasual_biasa at sekar_default:
        xalign 1.0

    sekar "\"Belum pulang den?\""

    show raden kasual_tersenyum
    raden "\"Bentar lagi kak.\""

    show sekar kasual_senyum
    sekar "\"Jangan pulang terlalu malam loh. Kesehatan perlu dijaga.\""

    show sekar kasual_senyum at sekar_default with moveinleft:
        xalign 0.8
    
    sekar "\"Btw makasih ya Den, sudah datang ke acara ini.\""

    raden "\". . . \""

    "Aku hanya mengangguk kecil, kata-katanya terasa hangat. Ada sesuatu yang berbeda dari Kak Sekar saat ini, sesuatu yang membuat hatiku berdetak lebih cepat."

    sekar "\"Den\""

    raden "\"Iya, Kak?\""

    sekar "\"Boleh tanya sebentar nggak?\""

    show raden kasual_bingung

    raden "\"Tanya apa kak?\""

    show sekar kasual_biasa

    sekar "\"Kenapa kamu kuliah? Apalagi di PENS? Ada alasan khusus?\""

    raden "\"…\""

    show raden kasual_biasa
    raden "\"Aku sih…\""

    raden "\"Nggak ada alasan spesial sih kak. Aku cuman ingin menjadi pribadi mapan.. dan juga, kurasa berkuliah adalah kesempatan yang tidak didapatkan semua orang\""

    sekar "\"Terus, kenapa menurutmu penting, Den?\""

    raden "\"Kalau aku sendiri, supaya lebih siap ke dunia yang lebih luas di luar sana... \""

    raden "\"Maksudku, dari SD, SMP, SMA, kita hanya diajarkan materi dan melatih disiplin.\""

    raden "\"Yaaa, meskipun kalau SMK sudah diajarkan dasar sebelum bekerja. Tapi aku rasa masih belum cukup\""

    raden "\"Sedangkan, di sini, harusnya kita dikenalkan ke level yang berbeda.\""

    raden "\"Bukan lagi hanya teori, tapi juga cara berpikir kritis, menyelesaikan masalah, dan beradaptasi dengan berbagai situasi.\""

    raden "\"Disini, aku pengen jadi lebih mandiri, dari akademis maupun dalam kehidupan sehari-hari.\""

    raden "\"Setidaknya itu yang kuharapkan.\""

    raden "\"Di luar itu, PENS kan terkenal sebagai politeknik terbaik se-Asia Tenggara,\""

    raden "\"Aku pikir, kalau aku mau berhasil, ini adalah tempat yang tepat.\""

    show sekar kasual_tegas #serius

    sekar "\"…\""

    show sekar kasual_senyum

    raden "\"Kalau Kakak sendiri?\""

    raden "\"Kenapa kuliah di PENS?\""
    
    show sekar kasual_gugup #Sekar menunduk
    sekar "\"Aku ya, hmm....\""

    sekar "\"Kalau mau jawaban. Jawabku pasti akan sama seperti jawabanmu. Mendapat koneksi lah, menjadi mandiri, menjadi terdorong untuk improve karena masuk ke kampus ternama lah, dan lainnya\""

    raden "\"Memangnya kakak punya alasan lain?\""

    sekar "\"...\""

    "Sekar tampak terdiam, bak mencari jawaban di sela dedaunan."

    show raden kasual_panik
    raden "\"Nggak usah dijawab juga nggak papa, kak. Disimpan saja topiknya buat besok.\""

    sekar "\"Eh, maaf den. Padahal aku duluan yang mulai, malah aku juga yang nutup.\""

    show raden kasual_tersenyum #senyum garing
    raden "\"Nggak papa, Kak. Akunya juga sih, malah tanya ngelantur kayak gitu.\""

    "Setelah perbincangan antara aku dan Kak Sekar selesai. Kak Sekar dipanggil oleh temannya."

    npcP "\"Sekar, ayo. Daripada pulang terlalu malam nanti.\""

    sekar "\"Iya, sebentar. Aku akan kesana.\""

    sekar "\"Aku pergi duluan ya den.\""

    raden "\"Iya kak.\""

    show sekar kasual_biasa at sekar_default:
        xzoom -1.0
    hide sekar kasual_biasa with moveoutright

    "Setelah Kak Sekar pergi ke arah temannya, Santo tiba-tiba datang dari belakang."

    show santo kasual_netral at santo_default:
        xalign 1.0 xzoom -1.0
    with moveinleft

    show santo kasual_netral at santo_default:
        xalign 1.0 xzoom 1.0

    santo "\"Bicarain apa tadi den.\""

    raden "\"Nggak apa-apa to.\""

    raden "\"Btw, To, habis ini kamu mau kemana?\""

    santo "\"Ke kantin. Kenapa den?\""

    raden "\"Nggak, aku cuma nanya doang. Karena aku mau pulang.\""

    santo "\"Oh, kalau begitu. Hati-hati dalam perjalanan pulangnya ya den.\""

    raden "\"Iya to.\""

    "Setelah berpamitan dengan Santo, aku meneruskan perjalananku menuju parkiran."

    #Sfx telfon berdering

    scene bg parkir_d3_sore with dissolve:
        zoom 0.5
    
    show raden kasual_biasa at raden_default:
        xalign 0.0
    raden "\"Hmmm, Aisyah?\""

    #HP telfon dengan Aisyah

    aisyah "\"Raden..., boleh minta tolong, kamu bisa bela diri 'kan? Di sini, di daerah XXXXX, ada begal—\""

    show raden kasual_kaget
    raden "\"Apa? Begal?\""

    aisyah "\"Iya, tadi aku..\""

    "Ternyata ini bukan urusan sepele. Dari suaranya, aku bisa mendengar ketakutan yang ia coba sembunyikan. Ini lebih dari sekadar barang yang tertinggal—alasan yang biasa ia gunakan untuk meminta bantuanku."

    "Daerah gang sekitar kampus memang rawan pembegalan. Para pelaku biasanya membawa senjata tajam, dan kemungkinan besar Aisyah benar-benar terlibat. Entah dia mencoba membantu orang lain atau justru dia sendiri yang jadi korban."

    "Aku mengencangkan cengkeraman pada ponselku."

    show raden kasual_serius
    raden "\"Share loc, aku datang.\""

    #HP telfon dengan Aisyah selesai

    "Aku tidak bisa berpikir panjang. Ini Aisyah—aku tidak akan membiarkannya dalam bahaya. Aku tahu aku harus bertindak cepat."

    "Meneguk sisa minumanku, aku langsung bergegas menuju motorku. Ada ketegangan dalam dadaku, tapi aku mencoba tetap tenang. Dia membutuhkan bantuanku, dan aku tidak akan mengecewakannya."

    scene black with dissolve
    pause 1.0

    #Jalan gang
    scene bg jalan_gang with dissolve:
        zoom 0.5
    #Suasana intens

    "Sampai di gang belakang kampus, aku lihat Aisyah berdiri sigap, siap melawan dua pria mencurigakan. Di sampingnya, seorang mahasiswi terjatuh—aku kenal, Erin."

    "Tanpa berpikir panjang, aku segera menginjak rem dan berhenti. Langsung turun dari motor, aku berlari menghampiri Aisyah untuk membantu."

    show raden kasual_serius at raden_default:
        xalign -0.4
    show aisyah casual_serius at aisyah_default:
        xalign 0.6
    with dissolve

    raden "\"Aisyah!\""

    "Aisyah yang sudah berada dalam posisi bertahan memberi isyarat dengan matanya agar aku berhati-hati. Aku langsung masuk ke posisi siap, mengingat latihan bela diri yang pernah kupelajari. "

    #Sfx suara serangan bogem

    "Dengan gerakan cepat, aku membantu Aisyah melawan kedua begal itu. Serangan kami yang terkoordinasi akhirnya membuat para begal tersebut melarikan diri tanpa hasil."

    #Suasana agak dramatis

    "Erin bangkit, wajahnya pucat, tangannya sedikit gemetar, tapi dia tetap tersenyum tipis. Matanya melirik singkat ke bekas arah begal lari, lalu ke arah kami."

    show erin kasual_netral at erin_default:
        xalign 1.2
    
    erin "\"Terima kasih… kalian cepat sekali.\""

    "Sekilas kayak biasa aja, tapi aku ngerasa… entah kenapa nadanya terlalu datar buat orang habis hampir dibegal. Sepertinya dia cuma sok kuat."

    show raden kasual_bingung 

    raden "\"Hati-hati, Rin… sendirian di tempat sepi kayak gini bahaya.\""

    "Aisyah melangkah mendekat, sikapnya tegas."

    show aisyah casual_serius at aisyah_default:
        xalign 0.6 xzoom -1.0
    aisyah "\"Kamu luka? Mereka nyakitin kamu?\""

    "Erin geleng pelan, senyumnya tetap sopan, tangannya merapikan anak rambut yang berantakan."

    erin "\"Nggak kok… cuma… kaget aja.\""

    "Dia berusaha ketawa kecil, tapi matanya nggak sepenuhnya mengikuti senyumnya. Kayak ada sesuatu yang dia tahan."

    "Saat Aisyah mendekat ke Erin, Mataku tertuju pada bahunya. Ada goresan kecil yang tampak mengeluarkan darah tipis."

    show raden kasual_gugup

    raden "\"Aisyah, kamu nggak apa-apa?\""

    "Aisyah melirik ke pundaknya lalu mendengus kecil."

    show aisyah casual_gugup at aisyah_default:
        xzoom 1.0#canggung

    aisyah "\"Ah, ini cuma lecet kok, nggak serius,\""

    raden "\"Yakin nggak perlu diobati? Kita bisa ke klinik, lho.\""

    "Dia hanya menggeleng dengan senyuman tipis. "

    aisyah "\"Aku baik-baik aja, Raden. Tapi makasih ya... udah bantu tadi,\""

    menu:
        "Seharusnya jangan gegabah dan tunggu aku saja":
            show raden kasual_serius
            "Aku menatap Aisyah yang berdiri di depanku dengan wajah keras kepala. Jujur, aku tidak tahu harus bagaimana lagi."

            raden "\"Aisyah, Apa yang kamu pikirin sampai mencoba melawan mereka sendirian?!\""

            "Dia menggelengkan kepala ringan, dan tersenyum tipis padaku."

            show aisyah casual_senyum #netral
            aisyah "\"Engga kok, aku percaya kamu pasti datang buat bantu.\""

            "Aku terkejut dengan kepercayaan nya, tapi aku tau dia tetap salah."

            raden "\"Tapi kan kamu bisa nunggu aku sampai dulu!\""

            show aisyah casual_gugup

            aisyah "\"Aku… mana mungkin aku bisa diam, Den. Mereka…\""

            "Aisyah menghindari tatapan ku, aku melihat dia mengepalkan tangannya, ragu untuk melanjutkan."

            "Lalu akhirnya dia berdiri dan menatapku dengan tegas."

            show aisyah casual_serius

            aisyah "\"mereka hampir menyakiti Erin!. Aku gak mungkin cuma diam dan liat itu terjadi..\""

            show raden kasual_sedih

            raden "\"kamu harus lebih peduli sama dirimu sendiri. Gimana kalau aku tidak datang tepat waktu— aku…\""

            jump arc_character_day2_scene8
        "Tolong, jangan ceroboh lagi!":
            show raden kasual_serius
            raden "\"Aisyah, yang kamu lakukan tadi sangat ceroboh!\""

            show raden kasual_sedih
            raden "\"...Kalau aku tidak datang tepat waktu—tidak tahu, Aku khawatir ama kamu!!\""

            show aisyah casual_terkejut

            "Aisyah sesaat terkejut dengan ucapanku. Aku tahu, perempuan seperti dia sebenarnya sadar akan kesalahannya ini."

            jump arc_character_day2_scene8