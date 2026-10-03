define chapter2_aisyah_scene4_choice1_choosen = False
define chapter2_aisyah_scene4_choice2_choosen = False
define chapter2_aisyah_scene4_choice3_choosen = False

define mahasiswi = Character("Mahasiswi")

label chapter2_aisyah_scene4:
    scene jalan_d4_kantin with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kemeja_biasa:
        zoom raden_default.zoom
        xalign 0.5
        yalign raden_default.yalign
    
    show santo kemeja_netral at flip:
        zoom santo_default.zoom
        xalign 8.7
        yalign 0.08
    
    show aisyah kemeja_bicara:
        zoom aisyah_default.zoom
        xalign 0.2
        yalign aisyah_default.yalign

    show tessa kemeja_kesal: #kesal
        zoom tessa_default.zoom
        xalign 1.2
        yalign tessa_default.yalign
    with dissolve

    tessa "\"HEY! DIEM DULU BISA GAK!!\""

    #Backsound Hening

    #raden terkejut

    raden "\"Kak Tessa?!\""

    anon "\"Tess, lu liat sendiri kan mereka—\""

    "Tessa menatap pria itu dengan aura yang mencekam, membuat seluruh mahasiswa yang ada di ruangan ini tegang dan takut."

    tessa "\"Dio, aku dah bilang untuk diem dulu kan\""

    "Pria perokok itu ternyata bernama Dio, akhirnya menciut, tak berani membalas perkataan Kak Tessa."

    "Tessa melihat sekeliling, dia melihat di antara semua orang di sini, dan melihat dari tadi Santo berdiri diam mengamati dengan kepala dingin."

    tessa "\"Hey gondrong! Coba jelaskan!\""

    #Santo kaget 
    santo "?!!"

    #Santo Netral
    santo "\"Ehm..\""

    "Santo berjalan maju pelan, menghela nafas dengan tangan menggaruk bagian belakang lehernya."

    santo "\"Kak Dio ini. Tadi di Kantin sempat merokok dan membuangnya sembarang, salah satu teman ku mencoba memperingati nya, dan yah—\""

    "Santo mengangkat kedua bahunya. Lalu melihat Kak Dio dengan tatapan tajam."

    #santo serius
    #Kak Dio gugup, menelan ludahnya sendiri.

    santo "\"Inilah hasilnya\""

    dio "\"Hei, jangan fitnah! Gue ngerokok di luar kantin tadi, cuma mampir ke sana buat beli minum!\""

    santo "\"Mungkin Kak Tessa bisa tanya Kak Sekar. Dia tadi ada di sana waktu semuanya mulai.\""

    "Tessa mengangguk, tanpa berkata apa-apa. Dia langsung mengambil ponselnya dan menekan nomor."

    tessa "\"Gimana Dio? Benar kah? Perlu kah ku telfon Sekar buat memastikan?\""

    dio "\"I…itu.. Aku…\""

    #Tessa menghela nafas
    #(Tessa menghela nafas: hhaaahhh)

    tessa "\"Maaf, karena dia telah merepotkan kalian, sisanya biar aku urus.\""

    "Akhirnya, Tessa mencengkram bahu Kak Dio dan membawa nya pergi dengan langkah berat, mulutnya masih menggumamkan ketidakpuasan."

    "Kami hanya bisa mengangguk dan berterima kasih pada Kak Tessa."

    #Tessa hilang

    #Suasana dramatis sedih

    hide tessa

    show raden kemeja_canggung at flip:
        zoom raden_default.zoom
        xalign 1.3
        yalign raden_default.yalign
    
    show santo kemeja_netral at flip:
        zoom santo_default.zoom
        xalign 8.0
        yalign 0.08
    
    show aisyah kemeja_gugup:
        zoom aisyah_default.zoom
        xalign 0.5
        yalign aisyah_default.yalign
    with moveinleft

    aisyah "\"Raden, Santo, sekali lagi terima kasih ya.. sudah membantu.\""

    "Aisyah tersenyum. Bibirnya melengkung tipis, seolah berusaha meyakinkan dunia bahwa semuanya baik-baik saja, tetapi matanya berbicara sebaliknya. Ada kehangatan yang tertahan, seperti api kecil yang mencoba bertahan di tengah badai."

    aisyah "\"Dan maaf ya sudah merepotkan tadi.\""

    "Itu bukan senyuman keceriaan dan percaya diri yang biasa dia berikan, melainkan seperti seseorang yang menerima luka dari masa lalu yang dia coba sembunyikan."

    aisyah "\"Maaf, aku emang dari dulu susah banget buat nggak negur kalau ada yang salah...\""

    aisyah "\"..dan kadang suka kebablasan. Kayak hari ini juga, sih—\""

    "Aisyah menunduk, dengan kesedihan dan penyesalan yang tergambar di wajahnya."

    raden "{i}…Apa yang harus kukatakan untuk menghiburnya?{/i}"

    menu:
        "Menghibur Aisyah":
            $ chapter2_aisyah_scene4_choice1_choosen = True

        "Kritik Aisyah":
            $ chapter2_aisyah_scene4_choice1_choosen = False

    if (chapter2_aisyah_scene4_choice1_choosen == True):
        #Raden canggung
        #Aku menggelengkan kepala, tersenyum kecil, mencoba membuat suasana lebih ringan.

        raden "\"—Oh, nggak apa kok, Aisyah. Lagipula Mas tadi memang salah.\""

        #Aisyah mengangguk dan memberi senyuman yang tak biasa itu lagi.

        aisyah "\"Terimakasih—- Raden.\""

        "Saat aku menatap matanya, aku bisa merasakan bahwa itu sama sekali tidak menenangkannya. Seperti dia menjawab dengan template dari situasi yang telah dia rasakan berulangkali sebelumnya."

        raden "{i}Apakah.. Aku telah mengatakan hal yang salah…{/i}"

        #Aisyah, Santo hilang

        scene black with dissolve:
            size (config.screen_width, config.screen_height)
            truecenter
        with Pause(0.2)

        scene perjalanan_pulang with dissolve:
            size (config.screen_width, config.screen_height)
            truecenter

        show raden kemeja_biasa:
            zoom raden_default.zoom
            xalign 0.5
            yalign raden_default.yalign

        #Suasana netral di kampus saat malam
        
        "Setelah kejadian tersebut. Aku mengikuti UKM hari ini, itu berlangsung sampai malam. Sepulangnya aku menaiki motor dan berkendara menuju gerbang keluar kampus. Dalam perjalanan aku melihat Aisyah berjalan, sibuk dengan ponselnya."

        show raden:
            xalign 0.0
            zoom raden_default.zoom
            yalign raden_default.yalign
        with moveinright

        show aisyah kemeja_bicara with dissolve:
            zoom aisyah_default.zoom
            xalign 0.9
            yalign aisyah_default.yalign
        
        #Aisyah muncul netral
        raden "\"Aisyah, pulang sekarang?\""

        aisyah "\"Iya, mau balik ke kost. Kenapa?\""

        raden "\"Mau kuantar aja? kan kost-mu searah rumahku.\""

        #Aisyah Serius
        show aisyah kemeja_penasaran:
            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        aisyah "\"Maaf, Raden, nggak perlu. Cowok sama cewek nggak seharusnya jalan bareng malem-malem.\""

        raden "\"Tapi aku cuma mau bantu\""

        aisyah "\"Terima kasih, tapi aku bisa sendiri,\""

        raden "\"Oke, hati-hati ya.\""

        aisyah "\"Hati-hati juga,\""

        #Raden, Aisyah hilang

        scene black with dissolve:
            size (config.screen_width, config.screen_height)
            truecenter
        with Pause(0.2)

        scene tengah_jalan with dissolve:
            size (config.screen_width, config.screen_height)
            truecenter

        show aisyah kemeja_penasaran at flip:
            zoom aisyah_default.zoom
            xalign 0.9
            yalign aisyah_default.yalign
        with dissolve

        "Kota Surabaya memang dikenal ramai, namun di gang-gang rumah, suasana cenderung lebih sepi. Saat itu, aku sedang mengendarai motor dan melaju di jalanan. Tiba-tiba, aku melihat Aisyah tengah terlibat perkelahian dengan dua pria asing di tengah jalan. Kedua pria itu jelas begal yang sedang mencoba mencuri sesuatu."

        show raden kemeja_biasa2:
            zoom raden_default.zoom
            xalign 0.0
            yalign raden_default.yalign

        "Tanpa berpikir panjang, aku segera menginjak rem dan berhenti. Langsung turun dari motor, aku berlari menghampiri Aisyah untuk membantu."

        raden "\"Aisyah!\""

        "Aisyah yang sudah berada dalam posisi bertahan memberi isyarat dengan matanya agar aku berhati-hati. Aku langsung masuk ke posisi siap, mengingat latihan bela diri yang pernah kupelajari."

        #sfx suara serangan bogem

        "Dengan gerakan cepat, aku membantu Aisyah melawan kedua begal itu. Serangan kami yang terkoordinasi akhirnya membuat para begal tersebut melarikan diri tanpa hasil."

        #scene dramatis

        "Seorang mahasiswi yang tadi nyaris menjadi korban datang menghampiri kami dengan wajah penuh rasa terima kasih."

        mahasiswi "\"Terima kasih banyak, Kak. Kalau nggak ada kalian, aku nggak tahu apa yang bakal terjadi,\""

        raden "\"Hati-hati ya, lain kali jangan jalan sendirian di tempat sepi,\""

        "Setelah mahasiswi itu pergi, aku menoleh ke arah Aisyah. Wajahnya tampak tenang, tapi aku melihat ada sesuatu yang tidak beres."

        #Raden gugup

        show raden kemeja_gugup:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"Aisyah, kamu nggak apa-apa?\""

        "Mataku tertuju pada bahunya. Ada goresan kecil yang tampak mengeluarkan darah tipis."

        "Aisyah melirik ke pundaknya lalu mendengus kecil."

        #Aisyah canggung
        show aisyah kemeja_canggung:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        aisyah "\"Ah, ini cuma lecet kok, nggak serius,\""

        raden "\"Yakin nggak perlu diobati? Kita bisa ke klinik, lho.\""

        show aisyah kemeja_gugup:
            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        "Dia hanya menggeleng dengan senyuman tipis."

        aisyah "\"Aku baik-baik aja, Raden. Tapi makasih ya... udah bantu tadi,\""

        menu:
            "Jaga dirimu dulu sebelum bantu orang lain.":
                $ chapter2_aisyah_scene4_choice2_choosen = True
                #Bad End

            "Tolong, jangan ceroboh lagi!":
                $ chapter2_aisyah_scene4_choice2_choosen = False
                #to Good End

    else:
        #[kritik aisyah]
        
        #Raden canggung
        show raden kemeja_canggung:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"—Oh, nggak apa kok, Aisyah. Lagipula Mas tadi memang salah.\""

        #Tapi aku melanjutkan, mencoba memberi nasihat tanpa menyakiti perasaannya.
        #Raden netral
        show raden kemeja_biasa:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"Tapi ya, Syah… Lain kali hati-hati, ya. Banyak orang di luar sana kayak Mas perokok tadi. Sudah salah, nggak mau mengaku, malah bikin ribut.\""

        #Aisyah netral
        show aisyah kemeja_bicara:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        aisyah "\"Aku ngerti, Raden. Makasih udah ngingetin.\""

        raden "Ya, sama-sama."

        raden "Kita semua belajar, kan?"

        #Aisyah senyum
        show aisyah kemeja_senyum:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        aisyah "\"Iya, makasih banget, Raden, Santo.\""

        #Aisyah, Santo hilang

        scene black with dissolve:
            size (config.screen_width, config.screen_height)
            truecenter
        with Pause(0.2)

        scene perjalanan_pulang with dissolve:
            size (config.screen_width, config.screen_height)
            truecenter

        show raden kemeja_biasa with dissolve:
            zoom raden_default.zoom
            xalign 0.0
            yalign raden_default.yalign

        show aisyah kemeja_bicara with dissolve:
            zoom aisyah_default.zoom
            xalign 0.9
            yalign aisyah_default.yalign
        
        raden "\"Aisyah, pulang sekarang?\""

        aisyah "\"Iya, mau balik ke kost. Kenapa?\""

        raden "\"Mau kuantar aja? kan kost-mu searah rumahku.\""

        aisyah "\"Maaf, Raden, nggak usah. Laki-laki dan perempuan nggak seharusnya jalan berduaan malam-malam. Nggak pantas.\""

        raden "\"Tapi aku cuma mau bantu\""

        aisyah "\"Terima kasih, tapi aku bisa sendiri,\""

        raden "\"Oke, hati-hati ya.\""

        aisyah "\"Hati-hati juga,\""

        #Aisyah hilang

        scene black with dissolve:
            size (config.screen_width, config.screen_height)
            truecenter
        with Pause(0.2)

        scene tengah_jalan with dissolve:
            size (config.screen_width, config.screen_height)
            truecenter

        show raden kemeja_biasa:
            zoom raden_default.zoom
            xalign 0.5
            yalign raden_default.yalign

        #telfon berdering

        raden "{i}Aku sedang bersantai di depan supermarket, menikmati waktu luangku sambil menyesap minuman dingin. Tiba-tiba ponselku bergetar, panggilan masuk muncul di layar. Nama yang terpampang di sana membuatku sedikit terkejut.{/i}"

        raden "\"Hmmm, Aisyah?\""

        raden "{i}Bukankah tadi dia menolak untuk pulang bersamaku? Apa terjadi sesuatu padanya?{/i}"

        #sfx intens

        #HP telfon dengan Aisyah

        aisyah "\"Raden..., boleh minta tolong, kamu bisa bela diri 'kan? Di sini, di daerah XXXXX, ada begal—\""

        raden "\"Apa? Begal?\""

        aisyah "\"Iya, tadi aku...\""

        "Ternyata ini bukan urusan sepele. Dari suaranya, aku bisa mendengar ketakutan yang ia coba sembunyikan. Ini lebih dari sekadar barang yang tertinggal—alasan yang biasa ia gunakan untuk meminta bantuanku."

        "Daerah gang sekitar kampus memang rawan pembegalan. Para pelaku biasanya membawa senjata tajam, dan kemungkinan besar Aisyah benar-benar terlibat. Entah dia mencoba membantu orang lain atau justru dia sendiri yang jadi korban."

        #Aku mengencangkan cengkeraman pada ponselku.

        raden "\"Share loc, aku datang.\""

        #HP telfon dengan Aisyah selesai

        "Aku tidak bisa berpikir panjang. Ini Aisyah—aku tidak akan membiarkannya dalam bahaya. Aku tahu aku harus bertindak cepat."

        "Meneguk sisa minumanku, aku langsung bergegas menuju motorku. Ada ketegangan dalam dadaku, tapi aku mencoba tetap tenang. Dia membutuhkan bantuanku, dan aku tidak akan mengecewakannya."

        scene black with dissolve:
            size (config.screen_width, config.screen_height)
            truecenter
        with Pause(0.2)

        scene tengah_jalan with dissolve:
            size (config.screen_width, config.screen_height)
            truecenter

        show aisyah kemeja_penasaran at flip:
            zoom aisyah_default.zoom
            xalign 0.9
            yalign aisyah_default.yalign
        with dissolve

        "Sesampainya, aku melihat Aisyah tengah terlibat perkelahian dengan dua pria asing di tengah jalan. Kedua pria itu jelas begal yang sedang mencoba mencuri sesuatu."

        show raden kemeja_biasa2:
            zoom raden_default.zoom
            xalign 0.0
            yalign raden_default.yalign
        
        "Tanpa berpikir panjang, aku segera menginjak rem dan berhenti. Langsung turun dari motor, aku berlari menghampiri Aisyah untuk membantu."

        #sfx suara serangan bogem

        "Dengan gerakan cepat, aku membantu Aisyah melawan kedua begal itu. Serangan kami yang terkoordinasi akhirnya membuat para begal tersebut melarikan diri tanpa hasil."

        #scene dramatis

        "Seorang mahasiswi yang tadi nyaris menjadi korban datang menghampiri kami dengan wajah penuh rasa terima kasih."

        mahasiswi "\"Terima kasih banyak, Kak. Kalau nggak ada kalian, aku nggak tahu apa yang bakal terjadi,\""

        raden "\"Hati-hati ya, lain kali jangan jalan sendirian di tempat sepi,\""

        "Setelah mahasiswi itu pergi, aku menoleh ke arah Aisyah. Wajahnya tampak tenang, tapi aku melihat ada sesuatu yang tidak beres."

        #Raden gugup
        show raden kemeja_gugup:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"Aisyah, kamu nggak apa-apa?\""

        "Mataku tertuju pada bahunya. Ada goresan kecil yang tampak mengeluarkan darah tipis."

        "Aisyah melirik ke pundaknya lalu mendengus kecil."

        #Aisyah canggung
        show aisyah kemeja_canggung:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        aisyah "\"Ah, ini cuma lecet kok, nggak serius,\""

        raden "\"Yakin nggak perlu diobati? Kita bisa ke klinik, lho.\""

        show aisyah kemeja_gugup:
            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        "Dia hanya menggeleng dengan senyuman tipis."

        aisyah "\"Aku baik-baik aja, Raden. Tapi makasih ya... udah bantu tadi,\""

        menu:
            "Seharusnya jangan gegabah dan tunggu aku saja":
                $ chapter2_aisyah_scene4_choice3_choosen = True

            "Tolong, jangan ceroboh lagi!":
                $ chapter2_aisyah_scene4_choice3_choosen = False


    if (chapter2_aisyah_scene4_choice2_choosen == True):
        #Raden serius
        show raden kemeja_kesal:
        
            zoom raden_default.zoom
            yalign raden_default.yalign
        "\"Aku menatap Aisyah yang berdiri di depanku dengan wajah keras kepala. Jujur, aku tidak tahu harus bagaimana lagi.\""

        raden "\"Aisyah.!”"

        raden "\"Apa yang kamu pikirin sampai mencoba melawan mereka sendirian?!\""

        #Aisyah gugup
        show aisyah kemeja_gugup:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        aisyah "\"Aku… mana mungkin aku bisa diam, Den. Mereka…\""

        "Aisyah menghindari tatapan ku, aku melihat dia mengepalkan tangannya, ragu untuk melanjutkan."

        "Lalu akhirnya dia berdiri dan menatapku dengan tegas."

        #Aisyah serius
        show aisyah kemeja_penasaran:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        aisyah "\"Mereka hampir menyakiti dia! Aku gak mungkin cuma diam dan liat itu terjadi..\""

        raden "\"Kamu harus lebih peduli sama dirimu sendiri. Kalau kondisimu nggak memungkinkan, jangan paksakan diri membantu orang lain!\""

        aisyah "\"Aku baik-baik saja, Raden. Aku tahu apa yang aku lakukan.\""

        "Aisyah berdiri tegas, dan melihatku dengan serius. Merasa benar dengan aksinya."

        raden "\"Baik-baik saja?! Aisyah, kamu harus sadar sama kemampuan diri sendiri. Apa kamu mau masalah ini berakhir dengan kamu yang terluka, atau lebih buruk lagi?\""

        jump chapter2_aisyah_bad_ending

    elif (chapter2_aisyah_scene4_choice3_choosen == True):
        #Raden serius
        show raden kemeja_serius:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"Aisyah, Apa yang kamu pikirin sampai mencoba melawan mereka sendirian?!\""

        "Dia menggelengkan kepala ringan, dan tersenyum tipis padaku."

        aisyah "\"Engga kok, aku percaya kamu pasti datang buat bantu.\""

        show raden kemeja_gugup:
            zoom raden_default.zoom
            yalign raden_default.yalign
        "Aku terkejut dengan kepercayaannya, tapi aku tahu dia tetap salah."

        show raden kemeja_serius:
            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"Tapi kan kamu bisa nunggu aku sampai dulu!\""

        #Aisyah gugup
        show aisyah kemeja_gugup:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        aisyah "\"Aku… mana mungkin aku bisa diam, Den. Mereka…\""

        "Aisyah menghindari tatapan ku, aku melihat dia mengepalkan tangannya, ragu untuk melanjutkan."

        "Lalu akhirnya dia berdiri dan menatapku dengan tegas."

        #Aisyah serius
        show aisyah kemeja_penasaran:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        aisyah "\"Mereka hampir menyakiti dia! Aku gak mungkin cuma diam dan liat itu terjadi..\""

        #Raden sedih
        show raden kemeja_sedih:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"Kamu harus lebih peduli sama dirimu sendiri. Gimana kalau aku tidak datang tepat waktu— aku…\""

        jump chapter2_aisyah_good_ending

    else:
        #Raden serius
        show raden kemeja_serius:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"Aisyah, yang kamu lakukan tadi sangat ceroboh!\""

        #Raden sedih
        show raden kemeja_sedih:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"...Kalau aku tidak datang tepat waktu—tidak tahu, Aku khawatir ama kamu!!\""

        #Aisyah terkejut
        show aisyah kemeja_gugup:

            zoom aisyah_default.zoom
            yalign aisyah_default.yalign
        "Aisyah sesaat terkejut dengan ucapanku. Aku tahu, perempuan seperti dia sebenarnya sadar akan kesalahannya ini."

        jump chapter2_aisyah_good_ending

    
    return
