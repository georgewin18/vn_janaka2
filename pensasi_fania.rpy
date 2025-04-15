define pensasi_fania_choice1_1_choosen = False
define pensasi_fania_choice2_1_choosen = False
define pensasi_fania_choice2_2_choosen = False
define pensasi_fania_choice3_1_choosen = False
label pensasi_fania:
    #Netral di kampus

    scene bg masjid with dissolve:
        zoom 0.5

    "Kami berjalan keluar gedung pascasarjana, udara segar langsung menyapa wajah kami setelah beberapa jam berada di dalam keramaian."

    show raden kasual_biasa:
        zoom 0.48 xalign 0.0 yalign 0.1
    show fania casual_senyum_normal_biasa:
        zoom 1.15 xalign 1.0 yalign -0.02
    with dissolve
    
    raden "\"Ramai banget ya di dalam.\""

    fania "\"Namanya juga event tahunan.\""

    #fania senyum
    show fania casual_senyum_ceria

    fania "\"Rame banget ya hari ini!\""

    show raden kasual_biasa2
    raden "\"Iya, ternyata pameran kampus bisa seramai ini.\""

    #fania gugup
    show fania casual_gugup
    fania "\"Den?\""

    raden "\"Ya?\""

    fania "\"kenapa kamu milih ikut main-main ketimbang dengerin materi sama Aisyah?\""

    menu:
        "Lebih seru main daripada materi.":
            raden "\"Hmm… yah, karena pastinya bakalan bosenin dengerin sampai selesai.\""

            raden "\"Aku yakin bakalan ketiduran di tengah acara kalau aku ikut Aisyah.\""

            raden "\"Aku juga lebih suka lihat dan eksplorasi hal-hal baru ketimbang dengerin penjelasan di satu tempat,\""

            "Ketimbang mendengarkan hal-hal membosankan, aku yakin bakalan ketemu hal-hal yang menyenangkan di luar auditorium."

            #fania senyum
            show fania casual_senyum_ceria
            fania "\"Sama dong, aku juga..\""
            $ pensasi_fania_choice1_1_choosen = True

            jump pensasi_fania_afterchoice1

        "Pengen aja sih.":
            show raden kasual_tersenyum
            raden "\"Yah… pengen aja sih, emangnya gak boleh?\""

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
    show raden kasual_kaget

    raden "\"Lah, ada mobil juga?!\""

    #fania bingung
    show fania casual_bingung
    fania "\"Buset Mahasiswa PENS sepuh semua isinya.\""

    fania "\"Eh, kita boleh naik juga gak sih?\""

    if(pensasi_fania_choice1_1_choosen == True): #btw di sini narator bilang wajah fania berubah senang, tapi di perintah gak ada suruh ubah ekspresi jadi mending ditambah kah?
        "Wajah Fania langsung berubah ceria, matanya berbinar penuh semangat. Ia tampak semakin hidup dan bersemangat."
    else:
        "Wajah Fania langsung berubah ceria. Syukurlah, sepertinya pikirannya berhasil teralihkan."
    show fania casual_senyum_ceria
    show raden kasual_biasa2

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

        fania "\"Boleh.\""

        scene bg masjid with dissolve:
            zoom 0.5

        "Booth mobil itu sudah dipenuhi pengunjung yang antusias. Penjaga booth tampak menjelaskan dengan penuh percaya diri mengenai mobil yang timnya kembangkan."

        "Mobil tersebut menggunakan tenaga listrik sebagai sumber energinya dan telah meraih beberapa penghargaan dalam kompetisi bergengsi."

        show raden kasual_biasa:
            zoom 0.48 xalign 0.0 yalign 0.1
        show fania casual_senyum_normal_biasa:
            zoom 1.15 xalign 1.0 yalign -0.02
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
        scene bg masjid with dissolve:
            zoom 0.5
        
        "Namun, ketika kami tiba di arena, tempat itu sudah penuh dengan antrean panjang orang-orang yang tak sabar menunggu giliran mereka."

        show raden kasual_biasa:
            zoom 0.48 xalign 0.0 yalign 0.1
        show fania casual_senyum_normal_biasa:
            zoom 1.15 xalign 1.0 yalign -0.02
        with dissolve

        raden "\"Kayaknya kita gak bisa naik deh.\""

        "Walaupun wajahnya tampak biasa saja, aku bisa mengira-ngira ada ketidaksenangan dalam suaranya."

        raden "\"Kalau begitu ayo kita lihat yang lain,\""

        fania "\"Istirahat aja dah? pasti yang lain juga ramai\""

        $ pensasi_fania_choice2_2_choosen = True

        menu:
            "Istirahat":
                jump pensasi_fania_afterchoice2
            "Mobil":
                jump pensasi_fania_choice_mobil

    else:
        raden "\"Ayo pergi ke Go-kart!\""

        fania "\"Boleh.\""

        "Dengan persetujuan, Kami berjalan dan sampai di booth go kart."

        fania "\"Deket banget, kukira bakalan ke booth yang jauh.\""

        "Ternyata tempatnya juga sudah ramai orang yang ingin mencoba Go-kart."

        fania "\"Hmm…\""

        fania "\"Rasanya gak etis kalau kita tiba-tiba motong di tengah antrian, ayo pergi aja.\""
        
        "Pada akhirnya Fania menarikku pergi."

        jump pensasi_fania_afterchoice2

label pensasi_fania_afterchoice2:

    scene bg masjid:
        zoom 0.5

    show raden kasual_biasa:
        zoom 0.48 xalign 0.0 yalign 0.1
    show fania casual_senyum_normal_biasa:
        zoom 1.15 xalign 1.0 yalign -0.02
    with dissolve
    fania "\"Haahh capek juga ya, muter-muter doang.\""

    raden "\"Hahaha kerasanya pas berhenti\""

    "Kami berdua bersantai di pojok bagian depan gedung pasca sarjana. Di sisi lainnya, terdapat live music yang mengalun untuk mengiringi acara."

    fania "\"Kamu bisa nyanyi, den?\""

    raden "\"Ya mungkin, belajar gitar\""

    "Fania menoleh ke arahku dan melambaikan tangannya. Aku mendekatinya dan mendapatkan sebuah pertanyaan yang mengejutkan."

    fania "\"Kamu mau jadi gitarisku?\""

    #raden kaget
    show raden kasual_kaget
    raden "\"Hah!? Gitaris?!\""

    fania "\"Iya. Gimana?\""

    menu:
        "Ayo":
            "Walaupun aku tidak bisa memakai gitar, rasanya tidak enak untuk menolak Fania. Apalagi, dia kelihatan sangat bersemangat."

            "\"{i}Ya sudahlah, ayo pergi. Mau itu berhasil atau gak, coba dulu deh!{i}\""

            raden "\"Oke.\""

            #Special moment start
            scene bg masjid

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

            #fania terrawa kecil

            fania "\"Pfftt, hahaha… padahal gak bisa gitar tapi kamu sok banget. Jadi kelihatan lucu,\""

            "Fania tertawa dengan sangat manis saat dia menjauhkan mic-nya."

            "Diem, lagian aku gak mungkin nolak kamu yang udah kelihatan excited…”"

            "Rasanya sangat memalukan dan canggung. Wajahku terasa panas. Aku yakin Fania bisa melihat pipiku yang merah."

            $ pensasi_fania_choice3_1_choosen = True

            jump pensasi_fania_afterchoice3

        "Aku gak bisa main gitar.":
            "Walaupun rasanya tidak enak, tapi aku tidak bisa mempermalukan diri sendiri karena gak bisa main gitar."

            raden "\"Ah, maaf Fania, aku gak bisa main gitar!\""

            "Rasanya sangat tidak enak saat dia begitu bersemangat tetapi aku tidak bisa memberikannya harapan"

            fania "\"Yah… sayang banget. Kalau begitu kamu harus saksikan ini dengan baik.\""

            "Aku menunjukkan senyuman khas seorang karakter berambut putih bermata biru tertentu yang bersiap melawan musuh bermata empat yang merasuki muridnya"

            raden "\"Tentu saja!\""

            #special moment start

            scene bg masjid

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

            jump pensasi_fania_afterchoice3

label pensasi_fania_afterchoice3:

    #depan pasca
    scene bg masjid with dissolve:
        zoom 0.5
    show raden kasual_biasa:
        zoom 0.48 xalign 0.0 yalign 0.1
    show fania casual_senyum_normal_biasa:
        zoom 1.15 xalign 1.0 yalign -0.02
    with dissolve
    fania "\"Ha… rasanya capek banget\""

    "Fania meregangkan tubuhnya saat kita keluar dari konser dadakan Fania."

    raden "\"Iya sih, lagian kamu semangat banget waktu nyanyi tadi,\""

    if(pensasi_fania_choice3_1_choosen == True):
        "Dia menahan dagunya dengan tangan yang diletakkan di meja."

        #fania tertawa kecil

        fania "\"Kamu juga lucu waktu bingung sama gitarnya tadi.\""

        raden "\"Siapa tahu aku tiba-tiba dapet skill dadakan gitu,\""

        #(VO tertawa)
        "Fania tertawa mendengar komentarku."
    else:
        #fania senyum ceria
        show fania casual_senyum_normal_biasa
        fania "\"Sayang sih kamu gak ikut tadi. Aku yakin bakalan lebih seru kalau kamu ikut tadi.\""

        raden "\"Yah kalau begitu aku bakalan latihan main gitar biar kita bisa duet lain kali,\""

        fania "\"Kalau begitu aku tunggu den.\""

    
    #fania senyum
    show fania casual_senyum_ceria

    fania "\"Den, gimana hari ini? seru banget kan?\""

    "Pertanyaan Fania membuatku mengingat kembali apa saja yang terjadi hari ini."

    "Mulai dari kita yang berpisah dengan Aisyah hingga mengalami masalah karena acara yang terlalu padat."

    "Sekali lagi, mempertimbangkan pertanyaan Fania,"

    "\"{i}apakah aku menikmati hari ini?\{i}\""

    menu:
        "Lain kali lagi":
            "Aku menunjukkan senyuman tipis dan mengangguk sebagai jawaban."

            raden "\"Ya, rasanya sangat menyenangkan. Gimana kalau kita kencan lagi lain kali?\""

            "Aku menatapnya. Menemukan Fania telah mengalihkan pandangannya dariku, tetapi aku bisa melihat telinganya memerah."

            fania "\"Kamu… pinter ya, mulutmu itu.\""#suara jengkel

            "Tetapi aku tertawa kecil melihat Fania yang bertingkah malu-malu"

            #raden senyum hehe
            show raden kasual_hehe

            raden "\"Kalau begitu, gimana jawabanmu?\""

            fania "\"… Boleh deh, lain kali.\""

            #END

        "Lumayan lah.":

            raden "\"Yah… lumayanlah, gak buruk. Sayang kita gak bisa cobain mobil listrik sama gokart karena terlalu ramai. Pasti bakalan lebih menyenangkan\""
            
            #menghela nafas
            fania "\"Mau gimana lagi. Yang penasaran bukan cuma kita. Semoga tahun depan kita bisa cobain gokart sama mobil listriknya,\""

            raden "\"Boleh deh, kalau begitu, ayo jalan bareng lagi lain kali.\""

            fania "\"Oke!\""

            #END
