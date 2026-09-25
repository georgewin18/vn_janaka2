transform kanan_kiri:
    subpixel True
    zoom 1.35 yalign 0.05
    linear 1.0 xalign 0.0
    xzoom -1.0
    linear 1.0 xalign 1.0
    xzoom 1.0
    
    repeat

label arc_character_day2_scene6:
    scene bg jalan_d4_kantin with dissolve:
        zoom 0.5

    show tessa kasual_kesal at tessa_default: #tessa bingung
        xalign 0.8
    show raden kasual_gugup at raden_default: #raden gugup
        xalign 0.0
    #Suasana netral in campus
    "Tessa mengerutkan kening, lalu terdiam sejenak, tampak bingung dengan apa yang baru saja aku katakan."

    tessa "\"Ganggu kamu? Ngapain aku ganggu kamu?\""

    raden "\"E.. enggak tau\""

    tessa "\"Gitu kenapa takut? Nyapa doang.\""

    "Aku menarik napas panjang, mencoba menjelaskan."

    raden "\"Kak Tessa... aku tahu suara kakak memang biasanya galak, walaupun nggak marah.\""

    raden "\"Tapi kali ini... suara kakak beneran bikin aku merinding, seriusan\""

    show tessa kasual_netral

    tessa "\"Beda gimana?\""

    raden "\"Suara Kak Tessa tadi kayak... benar-benar marah. jadi keinget... yang di deket D4 pas itu..\""

    tessa "\"Hmm? yang mana?\""

    raden "\"Waktu Kak Tessa mbentak Kak Dio dan semua nya langsung diam.\""

    "Tessa memutar bola matanya, seolah sedang mengingat kejadian itu."

    tessa "\"Ah, itu. Ya, aku ingat. kenapa emang?\""

    raden "\"Pas itu, Kak Tessa kayak... serem banget. Semua orang pada takut, Santo yang selalu keliatan santai aja kabur duluan\""

    #Tessa senyum tipis(Tessa tertawa kecil)
    show tessa kasual_senyum
    tessa "\"Oh, itu. Yah, aku cuma marah soalnya dia nyelomot aja orang nya.\""

    tessa "\"Kalau nggak ditekan kayak gitu, dia nggak bakal berhenti menyangkal..\""

    tessa "\"Dio emang gitu orang nya, jadinya harus di tegas in dari awal.\""

    show raden kasual_canggung
    
    raden "\"Tapi ya itu… Kak Tessa tadi suaranya sama kek pas mbentak Kak Dio… makanya sempet takut aku…\""

    show tessa kasual_kesal #tessa bingung
    tessa "\"Memangnya aku terlihat seburuk itu?\""

    'Tanyanya sambil tertawa kecil, meskipun aku menangkap sedikit rasa penasaran dalam nadanya.'

    "Aku terdiam sebentar sebelum akhirnya menjawab"

    show raden kasual_biasa

    raden "\"Di pikir pikir Kak Tessa keren sih... tapi… juga menakutkan...\""

    tessa "\"Ya, tapi sekarang ini aku gak marah kok.\""

    show tessa kasual_senyum #Tessa Lega atau senyum(Tessa menghela napas) 

    tessa "\"Suaraku memang jadi lebih keras, soalnya tenggorokanku lagi sakit.\""

    raden "\"Btw makasih ya kak, udah bantu kita waktu itu\""

    tessa "\"iya, sama-sama\""

    "Mendengar jawabanya tessa, aku pun tenang tapi agak bingung kemudian hanya nganguk kepala."

    show raden kasual_biasa

    raden "\"Yaudah kak, aku lanjut ke acara di lapmer ya.\""

    tessa "\"Oi tunggu\"" # (keras dan serak)

    tessa "\"Tas mu kebuka itu\""

    #Raden cemas
    show raden kasual_canggung
    raden "\"Wah, bener\""

    raden "\"Semoga barangku endak ada yang hilang\""

    "Saat Raden memeriksa barang yang ada di tasnya Tessa sempat melihat buku komik yang dibawa oleh Raden"

    show tessa kasual_netral
    tessa "\"Buku itu\""

    tessa "\"Kau juga baca komik itu?\""

    raden "\"Oh...komik ini\""

    "Aku Menunjukkan buku komik yang kutemukan di kamar pagi ini."

    raden "\"Komik ini emang udah aku miliki dari waktu aku masih kecil\""

    raden "\"Seperti tanpa sadar aku masukin komik ini saat tadi pagi aku sedang bersih-bersih kamar\""

    show tessa kasual_senyum
    tessa "\"Ehhh.....Ternyata kau cukup rajin juga untuk seorang laki-laki\""

    raden "\"Ngomong-ngomong, volume terakhir komik ini hilang udah aku cari tapi tidak ketemu\""

    tessa "\"Oh...\""

    tessa "\"Mau pinjam volume terakhir punya ku?\""

    raden "\"Kak Tessa juga baca?\""

    tessa "\"Iya, sama kayak kamu aku baca komik ini dari kecil juga\""

    "Tessa pun langsung mengeluarkan buku komik volume terakhir miliknya"

    tessa "\"Ini.\""

    show raden kasual_tersenyum

    raden "\"Makasih kak Tessa, tapi kenapa kak Tessa bawa buku komik ini?\""

    tessa "\"Sebenarnya komik ini untuk mengisi waktu saat istirahat\""

    tessa "\"Tugas panitia sungguh sibuk kau tau\""

    raden "\"Kalau gitu aku pergi untuk melihat acaranya\""

    tessa "\"Oke, selamat menikmati acaranya\""

    scene black with dissolve

    #Suara Bising/Ramai

    "Aku berjalan lagi, tanpa arah. Sampai aku melihat Santo, amarahku meledak dan aku lari menuju dirinya. Sebelum aku merasakan tatapan yang tidak mengenakkan."

    #Lorong D3 dekat lapmer 
    scene bg lapmer with dissolve:
        zoom 0.5
    #Sekar Mondar Mandir
    show sekar kasual_biasa at kanan_kiri:
        xzoom 1.0
    with dissolve
    "Ketika aku berjalan di lapmer aku sempat melihat Kak Sekar yang mondar-mandir di jalan."

    "Aku pun memanggil Kak Sekar"
    hide sekar kasual_biasa
    show sekar kasual_biasa at sekar_default:
        xalign 1.0 xzoom 1.0
    show raden kasual_biasa at raden_default:
        xalign -0.2
    with dissolve
    
    sekar "\"Ada apa den?\""

    raden "\"Nggak kak, Ngeliat Kak Sekar mondar mandir, jadi kupanggil deh. Siapa tau, butuh bantuan.\""

    sekar "\"Nggak den, cuma lagi mikir saja.\""

    raden "\"Begitu ya kak? Yasudah kalau begitu. Aku pergi dulu ya.\""

    sekar "\"Iya, hati-hati den.\""

    raden "\"Iya kak.\""

    show sekar kasual_biasa at sekar_default:
        xalign 1.0 xzoom -1.0
    hide sekar with moveoutright

    "Seperti tadi pagi, Aku menoleh ke arahnya. Aku berpikir, apa yang seharusnya ku lakukan."

    menu:
        "Tertelan amarah":
            "Aku melupakan tatapan tersebut, dan langsung berlari ke arah Santo."

            show raden kasual_kesal
            raden "\"SANTOO!\""

            show santo kasual_netral at santo_default:
                xalign 1.0
            with dissolve

            santo "\"Sore den.\""

            raden "\"Nggak merasa bersalah nih?\""

            #Santo Gugup
            show santo kasual_senyum_lebar

            santo "\"Hehe, maaf maaf. Masalah hidup dan mati den, salah satu dari kita harus jadi korban\""

            raden "\"Enak banget ngomongnya, ckckck.\""

            show raden kasual_biasa

            "Btw, kamu tadi lihat nggak. Orang dengan tatapan agak aneh."

            #Santo Bingung
            show santo kasual_netral

            santo "\"Aneh gimana?\""

            raden "\"Kayak nggak enak aja gitu, tadi aku ngerasain perasaan kek gitu.\""

            santo "\"Aneh ya….\""

            raden "\"Btw, kamu dari tadi ngapain aja to?\""

            raden "\"....\""

            raden "\"Dih, dikacangin.\""

            "Melihat tidak ada respon dari Santo, aku akhirnya diam dan menikmati acara yang berjalan dengan menyenangkan, semua orang yang mengikuti acara baik panitia dan org lainnya semuanya bersemangat. Meskipun ada beberapa bagian yang bisa dibilang membosankan."

            scene black with dissolve
            jump arc_character_day2_scene7

        "Rasa ingin tahu yang tak tertahankan":
            "Aku pun mencoba berjalan ke arah tatapan tersebut. Melihat orang yang menatapku tadi pergi dengan berlari. Aku pun mengejarnya."

            scene black with dissolve
            pause 1.0
            scene bg kantin with dissolve:
                zoom 0.5
            pause 1.0
            scene black with dissolve
            pause 1.0
            scene bg jalan_d4_kantin with dissolve:
                zoom 0.5
            pause 1.0

            "Ketika masuk menuju D4 tiba-tiba saja ada banyak orang yang keluar secara bersamaan."

            #Crowd keluar dari dalam D4. Ini aku bingung digimanain -Daffa

            "Sebelum akhirnya aku tidak bisa menemukan orang tersebut."

            scene black with dissolve

            #Suara Bising/Ramai

            #D3 dekat Lapmer
            scene bg lapmer with dissolve:
                zoom 0.5

            "Aku kembali ke D3 dekat Lapmer untuk melihat acara nya lagi, semua orang terlihat menikmati nya."
            show raden kasual_biasa at raden_default:
                xalign 0.0
            with dissolve

            "Santo kemudian memanggilku dari belakang"

            santo "\"Raden!\""
            
            show santo kasual_netral at santo_default:
                xalign 1.0
            with dissolve

            raden "\"?\""

            santo "\"Kamu kenapa lari tadi den?\""

            show raden kasual_serius

            raden "\"Bukan apa-apa to.\""

            santo "\"Beneran?\""

            raden "\"Iya sih, cuma ada beberapa hal yang menggangguku tadi.\""

            santo "\"Yasudah kalau begitu.\""

            show raden kasual_tersenyum

            raden "\"Btw, kamu nggak lupa kan?\""

            #Santo Bingung
    
            santo "\"Lupa tentang apa?\""

            show raden kasual_kesal

            raden "\"Siapa tadi yang lari duluan meninggalkanku.\""

            santo "\"Hehe.\""

            raden "\"Sudahlah, lupakan.\""

            show raden kasual_biasa

            raden "\"Btw, apa saja yang kulewatkan pada acara tadi.\""

            santo "\"Dikit sih, cuma penampilan Kak Sekar.\""

            "Setelah itu, kami berbincang-bincang sebentar. Kemudian melihat dan menikmati acara yang berjalan dengan menyenangkan, semua orang yang mengikuti acara baik panitia dan org lainnya semuanya bersemangat. Meskipun ada beberapa bagian yang bisa dibilang membosankan."

            scene black with dissolve

            jump arc_character_day2_scene7
