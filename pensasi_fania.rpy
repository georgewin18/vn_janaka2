define pensasi_fania_choice1_1_choosen = False
define pensasi_fania_choice2_1_choosen = False
define pensasi_fania_choice2_2_choosen = False
define pensasi_fania_choice3_1_choosen = False
label pensasi_fania:
    #Netral di kampus

    scene bg depan_pasca_ramai with dissolve:
        zoom 0.5

    "Kami berjalan keluar gedung pascasarjana, udara segar langsung menyapa wajah kami setelah beberapa jam berada di dalam keramaian."

    show raden kasual_biasa at raden_default:
        xalign -0.2
    show fania casual_senyum_normal_biasa at fania_default:
        xalign 1.25
    with dissolve
    
    raden "\"Ramai banget ya di dalam.\""

    fania "\"Namanya juga event tahunan.\""

    #fania senyum
    show fania casual_senyum_ceria

    fania "\"Rame banget ya hari ini!\""

    show raden kasual_tersenyum
    raden "\"Iya, ternyata pameran kampus bisa seramai ini.\""

    #fania gugup
    show fania casual_gugup
    fania "\"Den?\""

    show raden kasual_biasa2
    raden "\"Ya?\""

    fania "\"kenapa kamu milih ikut main-main ketimbang dengerin materi sama Aisyah?\""

    menu:
        "Lebih seru main daripada materi.":
            show raden kasual_tersenyum
            show fania casual_senyum_normal_biasa
            raden "\"Hmm… yah, karena pastinya bakalan bosenin dengerin sampai selesai.\""

            raden "\"Aku yakin bakalan ketiduran di tengah acara kalau aku ikut Aisyah.\""

            raden "\"Aku juga lebih suka lihat dan eksplorasi hal-hal baru ketimbang dengerin penjelasan di satu tempat,\""

            raden "\"Ketimbang mendengarkan hal-hal membosankan, aku yakin bakalan ketemu hal-hal yang menyenangkan di luar auditorium.\""

            #fania senyum
            show fania casual_senyum_ceria
            fania "\"Sama dong, aku juga..\""
            $ pensasi_fania_choice1_1_choosen = True

            jump pensasi_fania_afterchoice1

        "Pengen aja sih.":
            show raden kasual_tersenyum
            raden "\"Yah… pengen aja sih, emangnya gak boleh?\""

            show fania casual_dingin
            show raden kasual_canggung
            fania "\"Gak boleh gimana? Ya udah kalau begitu.\""

            "Fania menanggapiku dengan nada sedikit ketus. Meski begitu, aku lega karena dia tidak terlihat benar-benar marah."

            "Aku harus lebih berhati-hati lain kali. Bercanda saat Fania sedang serius ternyata bukan ide yang bagus."

            "Ini memang kesalahanku karena bercanda di waktu yang salah."

            "Aku harus segera mencairkan suasana"

            raden "\"Uuhmm..\""

            jump pensasi_fania_afterchoice1

label pensasi_fania_afterchoice1:

    #raden senyum ceria
    show raden kasual_tersenyum
    raden "\"btw Lihat itu Fania! ada yang naik Go-kart!\""

    #fania senyum ceria
    show fania casual_senyum_ceria

    fania "\"Waah..\""

    fania "\"Tapi kok bisa ada Go-Kart?\""

    show raden kasual_biasa
    
    raden "\"Ya mungkin hemat energi gitu atau—\""

    #raden kaget
    show raden kasual_kaget with vpunch

    raden "\"Lah, ada mobil juga?!\""

    #fania bingung
    show raden kasual_biasa
    show fania casual_terkejut
    fania "\"Buset Mahasiswa PENS sepuh semua isinya.\""

    fania "\"Eh, kita boleh naik juga gak sih?\""

    show fania casual_senyum_ceria
    show raden kasual_biasa2
    if(pensasi_fania_choice1_1_choosen == True): #btw di sini narator bilang wajah fania berubah senang, tapi di perintah gak ada suruh ubah ekspresi jadi mending ditambah kah?
        "Wajah Fania langsung berubah ceria, matanya berbinar penuh semangat. Ia tampak semakin hidup dan bersemangat."
    else:
        "Wajah Fania langsung berubah ceria. Syukurlah, sepertinya pikirannya berhasil teralihkan."    

    raden "\"Harusnya boleh. Coba mampir ke boothnya.\""

    fania "\"Yang mana dulu?\""

    "\"Pergi kemana dulu ya?\""

    menu:
        "Mobil":
            jump pensasi_fania_choice_mobil
        "Go-kart":
            jump pensasi_fania_choice_gokart

label pensasi_fania_choice_mobil:
    if(pensasi_fania_choice2_2_choosen == False):
        raden "\"Gimana kalau kita lihat mobil listrik?\""

        voice "audio/vo/fania/pensasi/pensasi_1_boleh.mp3"
        fania "\"Boleh.\""

        scene bg depan_perpus_d3_ramai with dissolve:
            zoom 0.5

        "Booth mobil itu sudah dipenuhi pengunjung yang antusias. Penjaga booth tampak menjelaskan dengan penuh percaya diri mengenai mobil yang timnya kembangkan."

        "Mobil tersebut menggunakan tenaga listrik sebagai sumber energinya dan telah meraih beberapa penghargaan dalam kompetisi bergengsi."

        show raden kasual_biasa at raden_default:
            xalign -0.2
        show fania casual_senyum_normal_biasa at fania_default:
            xalign 1.25
        with dissolve

        raden "\"Kelihatannya pada antre naik mobil deh semuanya.\""

        fania "\"Yahh antre panjang ya..\""

        fania "\"Kayaknya kita gak bisa cobain mobilnya sekarang deh,\""

        raden "\"Nyoba Go-Kart?\""

        fania "\"Di sana ramai juga gak sih, atau istirahat dulu?\""

        "Hmm…"

        $ pensasi_fania_choice2_1_choosen = True

        menu:
            "Go-kart":
                jump pensasi_fania_choice_gokart
            "Istirahat":
                jump pensasi_fania_afterchoice2
    else:
        raden "\"Coba cek dulu Ayo ke mobil listrik deh,\""

        "Kami berdua memeriksa booth yang hanya beberapa meter di sebelah booth go kart."

        fania "\"Ternyata deket ya.\""

        "Booth mobil itu sudah dipenuhi pengunjung yang antusias. Penjaga booth tampak menjelaskan dengan penuh percaya diri mengenai mobil yang timnya kembangkan."

        "Mobil tersebut menggunakan tenaga listrik sebagai sumber energinya dan telah meraih beberapa penghargaan dalam kompetisi bergengsi."

        raden "\"Kelihatannya pada antre naik mobil deh semuanya.\""

        fania "\"Yahh antre panjang ya..\""

        fania "\"Kayaknya kita gak bisa cobain mobilnya sekarang deh,\""

        raden "\"Haahh yaudahlah..\""

        fania "\"Istirahat dulu dah\""

        jump pensasi_fania_afterchoice2

label pensasi_fania_choice_gokart:
    if(pensasi_fania_choice2_1_choosen == False):
        
        raden "\"Mau cobain Go-kart?\""

        #fania senyum
        show fania casual_senyum_ceria

        fania "\"Kayaknya seru.\""

        #depan perpus d3
        scene bg depan_perpus_d3_ramai with dissolve:
            zoom 0.5
        
        "Namun, ketika kami tiba di arena, tempat itu sudah penuh dengan antrean panjang orang-orang yang tak sabar menunggu giliran mereka."

        show raden kasual_biasa at raden_default:
            xalign -0.2
        show fania casual_senyum_normal_biasa at fania_default:
            xalign 1.25
        with dissolve

        raden "\"Kayaknya kita gak bisa naik deh.\""

        "Walaupun wajahnya tampak biasa saja, aku bisa mengira-ngira ada ketidaksenangan dalam suaranya."

        raden "\"Kalau begitu ayo kita lihat yang lain,\""

        voice "audio/vo/fania/pensasi/pensasi_istirahat_aja.mp3"
        fania "\"Istirahat aja dah? pasti yang lain juga ramai\""

        $ pensasi_fania_choice2_2_choosen = True

        menu:
            "Istirahat":
                jump pensasi_fania_afterchoice2
            "Mobil":
                jump pensasi_fania_choice_mobil

    else:
        raden "\"Ayo pergi ke Go-kart!\""

        voice "audio/vo/fania/pensasi/pensasi_1_boleh.mp3"
        fania "\"Boleh.\""

        "Dengan persetujuan, Kami berjalan dan sampai di booth go kart."

        voice "audio/vo/fania/pensasi/pensasi_2_deket_banget.mp3"
        fania "\"Deket banget, kukira bakalan ke booth yang jauh.\""

        "Ternyata tempatnya juga sudah ramai orang yang ingin mencoba Go-kart."

        voice "audio/vo/fania/pensasi/pensasi_3_hmm.mp3"
        fania "\"Hmm…\""

        fania "\"Rasanya gak etis kalau kita tiba-tiba motong di tengah antrian, ayo pergi aja.\""
        
        "Pada akhirnya Fania menarikku pergi."

        jump pensasi_fania_afterchoice2

label pensasi_fania_afterchoice2:

    scene bg depan_perpus_d3:
        zoom 0.5

    show raden kasual_biasa at raden_default:
        xalign -0.2
    show fania casual_menghelanapas at fania_default:
        xalign 1.25
    with dissolve
    
    
    voice "audio/vo/fania/pensasi/pensasi_4_hahh_capek.mp3"
    fania "\"Haahh capek juga ya, muter-muter doang.\""

    show raden kasual_ceria
    raden "\"Hahaha kerasanya pas berhenti\""

    show raden kasual_biasa
    show fania casual_senyum_normal_biasa
    "Kami berdua bersantai di pojok bagian depan gedung pasca sarjana. Di sisi lainnya, terdapat live music yang mengalun untuk mengiringi acara."

    voice "audio/vo/fania/pensasi/pensasi_5_kamu_bisa_nyanyi.mp3"
    fania "\"Kamu bisa nyanyi, den?\""

    raden "\"Ya mungkin, belajar gitar\""

    "Fania menoleh ke arahku dan melambaikan tangannya. Aku mendekatinya dan mendapatkan sebuah pertanyaan yang mengejutkan."

    voice "audio/vo/fania/pensasi/pensasi_6_kamu_mau.mp3"
    fania "\"Kamu mau jadi gitarisku?\""

    #raden kaget
    show raden kasual_kaget
    raden "\"Hah!? Gitaris?!\""

    voice "audio/vo/fania/pensasi/pensasi_7_iya.mp3"
    fania "\"Iya. Gimana?\""

    menu:
        "Ayo":
            show raden kasual_biasa
            "Walaupun aku tidak bisa memakai gitar, rasanya tidak enak untuk menolak Fania. Apalagi, dia kelihatan sangat bersemangat."

            "\"{i}Ya sudahlah, ayo pergi. Mau itu berhasil atau gak, coba dulu deh!{i}\""

            raden "\"Oke.\""

            stop music fadeout 2.0

            play music romantic fadein 1.0

            #Special moment start
            scene fania_pensasi at pan_up:
                zoom 1.5 xalign 0.45
            with dissolve

            pause 4.0

            scene fania_pensasi with dissolve:
                zoom 0.75

            pause 1.5

            "Jantungku berdegup kencang saat tanganku bergetar dengan gugup memegang gitar."

            "Fania melirikku sebentar, lalu mulai bernyanyi."

            "Suaranya lembut, mengalun merdu memenuhi aula seperti diva."

            "Aula yang tadinya riuh perlahan menjadi hening."

            "Semua perhatian tertuju padanya."

            "Bahkan cahaya lampu yang terang terasa seolah memusatkan fokus pada sosoknya di atas panggung"

            "Tapi aku? Aku bahkan tidak bisa menyentuh satu senar pun. Jemariku kaku, dan tubuhku seolah terkunci di tempat."

            raden "\"Ah, sudahlah!\""

            "Aku meraih mic dari stand yang digunakan untuk gitar, ingin bergabung dalam lagunya."

            "Namun melihat ekspresi penonton yang terpukau, aku hanya bisa diam, mencoba menenangkan diri."

            "Saat itu, Fania menoleh ke arahku sejenak sambil tersenyum kecil, memberi tanda agar aku ikut masuk ke dalam irama lagu."

            "Mengabaikan gitar yang sudah tergantung di leher, aku mengambil mic dan mulai menyanyi bersamanya."

            "Suaraku sedikit gemetar di awal, namun perlahan menyatu dengan suaranya yang stabil. Harmoni kami terasa aneh pada awalnya, seperti sebuah eksperimen."

            "Tapi Fania, dengan caranya yang tenang dan percaya diri, membuat suasana menjadi lebih nyaman. Ia membimbing tempo dan nada, membuat lagu itu terdengar seolah-olah memang dirancang untuk dinyanyikan bersama."

            #special moment end

            stop music fadeout 2.0

            show black with dissolve

            #fania terrawa kecil

            scene bg depan_pasca_ramai with dissolve:
                zoom 0.5

            play music campus fadein 1.0

            show raden kasual_canggung at raden_default:
                xalign -0.2
            show fania casual_senyum_ceria at fania_default:
                xalign 1.25
            with dissolve

            voice "audio/vo/fania/pensasi/pensasi_8_pfft.mp3"
            fania "\"Pfftt, hahaha... padahal gak bisa gitar tapi kamu sok banget. Jadi kelihatan lucu,\""

            "Fania tertawa dengan sangat manis saat dia menjauhkan mic-nya."

            show raden kasual_kesal
            raden "\"Diem, lagian aku gak mungkin nolak kamu yang udah kelihatan excited…\""

            "Rasanya sangat memalukan dan canggung. Wajahku terasa panas. Aku yakin Fania bisa melihat pipiku yang merah."

            $ pensasi_fania_choice3_1_choosen = True

            jump pensasi_fania_afterchoice3

        "Aku gak bisa main gitar.":
            show raden kasual_gugup
            "Walaupun rasanya tidak enak, tapi aku tidak bisa mempermalukan diri sendiri karena gak bisa main gitar."

            raden "\"Ah, maaf Fania, aku gak bisa main gitar!\""

            show raden kasual_canggung
            "Rasanya sangat tidak enak saat dia begitu bersemangat tetapi aku tidak bisa memberikannya harapan"

            voice "audio/vo/fania/pensasi/pensasi_9_yah.mp3"
            fania "\"Yah… sayang banget. Kalau begitu kamu harus saksikan ini dengan baik.\""

            show raden kasual_biasa
            "Aku menunjukkan senyuman khas seorang karakter berambut putih bermata biru tertentu yang bersiap melawan musuh bermata empat yang merasuki muridnya"

            raden "\"Tentu saja!\""

            #special moment start
            stop music fadeout 2.0

            play music romantic fadein 1.0

            scene fania_pensasi at pan_up:
                zoom 1.5 xalign 0.45
            with dissolve

            pause 4.0

            scene fania_pensasi with dissolve:
                zoom 0.75

            pause 1.5

            "Sifatnya yang tenang dan elegan berubah, membuatnya terdengar seperti anak kecil ketika dia sangat bersemangat."

            "Fania melirikku sebentar, lalu mulai bernyanyi."

            "Suaranya lembut, mengalun merdu memenuhi aula seperti diva."

            "Aula yang tadinya riuh perlahan menjadi hening. Semua perhatian tertuju padanya. Bahkan cahaya lampu yang terang terasa seolah memusatkan fokus pada sosoknya di atas panggung."

            "Mata kami saling bertemu. Matanya yang memancarkan cahaya kecemerlangan seperti bintang bertemu dengan pandanganku yang sederhana."

            "Detik itu, aku menyadari bahwa dia benar-benar berbeda. "

            "Fania, dengan segala keanggunannya, bukan hanya seorang teman yang pandai menyanyi."

            "Dia seperti bintang yang bersinar terang di langit malam, menonjol di antara gelapnya dunia."

            $ pensasi_fania_choice3_1_choosen = False

            #spesial moment end

            stop music fadeout 2.0

            show black with dissolve

            jump pensasi_fania_afterchoice3

label pensasi_fania_afterchoice3:
    if(pensasi_fania_choice3_1_choosen == False):
        play music campus fadein 1.0

    #depan pasca
    scene bg depan_pasca_ramai with dissolve:
        zoom 0.5
    show raden kasual_biasa at raden_default:
        xalign -0.2
    show fania casual_menghelanapas at fania_default:
        xalign 1.25
    with dissolve
    
    voice "audio/vo/fania/pensasi/pensasi_10_hahh.mp3"
    fania "\"Ha… rasanya capek banget\""

    "Fania meregangkan tubuhnya saat kita keluar dari konser dadakan Fania."

    show raden kasual_tersenyum
    show fania casual_senyum_normal_biasa
    raden "\"Iya sih, lagian kamu semangat banget waktu nyanyi tadi,\""

    if(pensasi_fania_choice3_1_choosen == True):
        show raden kasual_biasa
        "Dia menahan dagunya dengan tangan yang diletakkan di meja."

        #fania tertawa kecil
        show fania casual_tertawa_kecil
        voice "audio/vo/fania/pensasi/pensasi_11_kamu_juga.mp3"
        fania "\"Kamu juga lucu waktu bingung sama gitarnya tadi.\""

        show raden kasual_tersenyum
        raden "\"Siapa tahu aku tiba-tiba dapet skill dadakan gitu,\""

        #(VO tertawa)
        voice "audio/vo/fania/pensasi/pensasi_12_tertawa.mp3"
        "Fania tertawa mendengar komentarku."
    else:
        #fania senyum ceria
        show fania casual_senyum_normal_biasa
        show raden kasual_biasa
        voice "audio/vo/fania/pensasi/pensasi_13_sayang.mp3"
        fania "\"Sayang sih kamu gak ikut tadi. Aku yakin bakalan lebih seru kalau kamu ikut tadi.\""

        show raden kasual_tersenyum
        raden "\"Yah kalau begitu aku bakalan latihan main gitar biar kita bisa duet lain kali,\""

        voice "audio/vo/fania/pensasi/pensasi_14_kalau_begitu.mp3"
        fania "\"Kalau begitu aku tunggu den.\""

    
    #fania senyum
    show fania casual_senyum_ceria

    voice "audio/vo/fania/pensasi/pensasi_15_den.mp3"
    fania "\"Den, gimana hari ini? seru banget kan?\""

    show raden kasual_biasa
    "Pertanyaan Fania membuatku mengingat kembali apa saja yang terjadi hari ini."

    "Mulai dari kita yang berpisah dengan Aisyah hingga mengalami masalah karena acara yang terlalu padat."

    "Sekali lagi, mempertimbangkan pertanyaan Fania,"

    "\"{i}apakah aku menikmati hari ini?\"{/i}"

    menu:
        "Lain kali lagi":
            "Aku menunjukkan senyuman tipis dan mengangguk sebagai jawaban."

            show raden kasual_tersenyum
            raden "\"Ya, rasanya sangat menyenangkan. Gimana kalau kita kencan lagi lain kali?\""

            show raden kasual_biasa
            "Aku menatapnya. Menemukan Fania telah mengalihkan pandangannya dariku, tetapi aku bisa melihat telinganya memerah."

            show fania casual_kesal
            voice "audio/vo/fania/pensasi/pensasi_16_kamu_pinter.mp3"
            fania "\"Kamu… pinter ya, mulutmu itu.\""#suara jengkel

            "Tetapi aku tertawa kecil melihat Fania yang bertingkah malu-malu"

            #raden senyum hehe
            show raden kasual_hehe

            raden "\"Kalau begitu, gimana jawabanmu?\""

            show fania casual_senyum_normal_biasa
            voice "audio/vo/fania/pensasi/pensasi_17_boleh_deh.mp3"
            fania "\"… Boleh deh, lain kali.\""

            show black with dissolve

            #END

        "Lumayan lah.":
            show raden kasual_tersenyum
            raden "\"Yah… lumayanlah, gak buruk. Sayang kita gak bisa cobain mobil listrik sama gokart karena terlalu ramai. Pasti bakalan lebih menyenangkan\""
            
            #menghela nafas
            voice "audio/vo/fania/pensasi/pensasi_18_mau_gimana_lagi.mp3"

            show fania casual_menghelanapas_ada_asap with dissolve
            pause 0.2

            voice sustain

            show fania casual_menghelanapas with dissolve

            voice sustain

            fania "\"Mau gimana lagi. Yang penasaran bukan cuma kita. Semoga tahun depan kita bisa cobain gokart sama mobil listriknya,\""

            show raden kasual_tersenyum
            raden "\"Boleh deh, kalau begitu, ayo jalan bareng lagi lain kali.\""

            show fania casual_senyum_ceria
            voice "audio/vo/fania/pensasi/pensasi_19_oke.mp3"
            fania "\"Oke!\""

            show black with dissolve

            #END
