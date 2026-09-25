transform joget_kanan_kiri:
    subpixel True
    zoom 0.54 yalign 0.05
    linear 1.0 xalign 1.0
    xzoom -1.0
    linear 1.0 xalign 0.0
    xzoom 1.0
    repeat

transform joget_loncat(d=0.5, hop=60, sway=18, travel=2.0):
    subpixel True
    zoom 0.54
    anchor (0.5, 1.0)
    yalign 0.05

    # Loncat kecil
    parallel:
        block:
            easein d yoffset -hop
            easeout d yoffset 0
            repeat

    # Kiiri kanan
    parallel:
        block:
            linear d xoffset sway
            linear d xoffset -sway
            repeat

    # kiri–kanan + rotate
    parallel:
        block:
            xalign 0.0
            xzoom 1.0
            ease travel xalign 1.0
            xzoom -1.0
            ease travel xalign 0.0
            xzoom 1.0
            repeat

label arc_character_day2_scene1:
    show black
    #sfx alarm
    "*sfx alarm"

    scene bg kamar_raden with dissolve:
        zoom 0.5

    show black with dissolve
    $ renpy.pause(0.1, hard=True)
    hide black with dissolve
    $ renpy.pause(0.1, hard=True)
    show black with dissolve
    $ renpy.pause(0.1, hard=True)
    hide black with dissolve

    show raden kasual_capek at raden_default:
        xalign 0.5
    with dissolve

    "Alarm berbunyi nyaring. Aku berguling malas selama beberapa menit, sebelum akhirnya duduk perlahan, mematikan alarm sambil mengucek mata."

    #sfx alarm stop

    "Saat mataku menyapu seisi kamar… dan yang terlihat adalah bencana kecil. Baju numpuk, kardus mie instan di pojok, sandal nyasar ke rak buku."

    "Aku mengerutkan kening. Dia melirik ke kalender dinding yang penuh coretan—dan tepat hari ini, ada tulisan besar melingkar:"

    "BERSIH-BERSIH KAMAR!!"

    "Aku langsung berdiri, mengambil sapu lidi dari belakang pintu, lalu menyambar headset dari meja. Raden menyolokkan headset ke HP-nya, membuka radio streaming kampus, dan memutar lagu random."

    #sfx click radio

    #Play lagu https://youtu.be/K4xLi8IF1FM?si=vNbQpheCp-g7TiqN (menit 0.30 - 1.08)

    #Suara sapu yang sedang membersihkan debu (sfx)

    #Raden sedang nyapu sambil joget ke kiri dan kanan di kamarnya
    show raden kasual_biasa at joget_kanan_kiri

    "Aku menyapu sambil goyang kiri-kanan, mengikuti irama pelan. Saat lagu berganti—"

    #Play lagu https://youtu.be/NithFu9aSlY?si=ZeO5Arz0ZfA8hYKb (menit 0.57 - 1.40)

    "Aku langsung ambil posisi. Pegang sapu seperti mic, lalu mulai bernyanyi."

    #raden senyum ceria
    show raden kasual_ceria

    #audio https://youtu.be/z3OKd5b2Rlw?si=9gBFlVsXSmiqDd1I (menit 0.41 - 1.09)

    "Ketika sedang mengangkat guling, aku melihat sesuatu di balik tumpukan selimut. Aku membungkuk—menyibak sedikit—dan…"

    "Sebuah action figure robot berdebu, tapi utuh"

    raden "\"Gamedam!\""

    #Raden loncat-loncat dan berputar-putar (effek)
    show raden kasual_ceria at joget_loncat

    "Saat aku berputar-putar, secara nggak sengaja, kakiku menyenggol tumpukan kotak di bawah rak. Sebuah tumpukan komik lama berjatuhan, menyebar ke lantai."

    #Audio ketemu harta

    "Aku membuka satu, Ternyata itu adalah komik lawas favoritku—seri yang dulu dia kira udah raib ditelan pindahan."

    raden "\"Wah... ini, nih... Komik favorit jaman SD!\""

    "Dengan penuh semangat, aku mulai menyusun komik-komik itu di atas lantai. Volume demi volume, berurutan—01, 02, 03… hingga 13."

    show raden kasual_bingung:
        xalign 0.5 xzoom 1.0

    "Hah? …Kok gak ada volume 14?"

    "Aku mengecek ulang, membuka beberapa halaman, lalu mengangkat kardus lain di bawah rak. Tidak ada."

    "Ah… padahal itu ending-nya."

    show raden kasual_biasa

    "Setelah hening beberapa detik, aku menaruh semua volume kembali ke dalam kotak—kecuali Volume pertama. Kuselipkan ke dalam ransel."

    "Aku menutup resleting tas, lalu mengambil jaket. Sambil menyampirkan ransel ke punggung. Aku melirik seisi kamar yang kini jauh lebih rapi, lalu melangkah keluar menuju kampus."

    #sceme lorong d3
    scene bg lapmer with dissolve:
        zoom 0.5

    show raden kasual_biasa at raden_default:
        xalign 0.0

    "Sesampainya di kampus, Aku melangkah menyusuri lorong D3 yang masih sepi menuju kelas."

    "Langkah kaki terdengar dari arah belakang. Saat aku menoleh, Aisyah sedang berjalan perlahan sambil menatap lantai. Ekspresinya tidak seperti biasanya."

    "Menyadari diriku, dia berhenti sejenak, lalu mendekat."

    #Suasana dramatis sedih

    show aisyah casual_sedih at aisyah_default:
        xalign 1.0
    aisyah "\"Ah Raden, kemarin aku belum sempat bilang\""

    aisyah "\"Terima kasih ya.. sudah membantu.\""

    "Aisyah tersenyum. Bibirnya melengkung tipis, seolah berusaha meyakinkan dunia bahwa semuanya baik-baik saja, tetapi matanya berbicara sebaliknya. Ada kehangatan yang tertahan, seperti api kecil yang mencoba bertahan di tengah badai."

    aisyah "\"Dan maaf ya sudah merepotkan tadi.\""

    "Itu bukan senyuman keceriaan dan percaya diri yang biasa dia berikan, melainkan seperti seseorang yang menerima luka dari masa lalu yang dia coba sembunyikan. "

    aisyah "\"Maaf, aku emang dari dulu susah banget buat nggak negur kalau ada yang salah.. \""

    aisyah "\"..dan kadang suka kebablasan. Kayak hari ini juga, sih—\""

    "Aisyah menunduk, dengan kesedihan dan penyesalan yang tergambar di wajahnya."

    "…Apa yang harus kukatakan untuk menghiburnya?"

    menu:
        "Menghibur Aisyah":
            "Aku menggelengkan kepala, tersenyum kecil, mencoba membuat suasana lebih ringan."

            show raden kasual_canggung

            raden "\"—Oh, nggak apa kok, Aisyah. Lagipula Mas kemarin memang salah.\""

            "Aisyah mengangguk dan memberi senyuman yang tak biasa itu lagi."

            aisyah "\"Terimakasih—- Raden.\""

            "Saat aku menatap matanya, aku bisa merasakan bahwa itu sama sekali tidak menenangkannya. Seperti dia menjawab dengan template dari situasi yang telah dia rasakan berulang kali sebelumnya."

            "Apakah.. Aku telah mengatakan hal yang salah…"

            "Aisyah hanya tersenyum tipis setelah semua itu. Lalu dengan pelan, ia mengangguk kecil, dan berkata."

            aisyah "\"Aku duluan, ya.\""

            "Tanpa menunggu jawaban, dia berbalik dan berjalan menjauh, meninggalkan kuyang masih berdiri di lorong."
            
            "Aku menarik napas pelan. Satu sisi dadanya terasa hangat, sisi lainnya… entah."

            "Setelah beberapa detik terdiam, aku akhirnya melangkah menuju ruang kelas."

            hide aisyah casual_sedih with dissolve

            jump arc_character_day2_scene2

        "Kritik Aisyah":
            "Aku menggelengkan kepala dan tersenyum kecil."

            show raden kasual_canggung
            raden "\"—Oh, nggak apa kok, Aisyah. Lagipula Mas kemarin memang salah.\""

            "Tapi aku melanjutkan, mencoba memberi nasihat tanpa menyakiti perasaannya."

            raden "Tapi ya, Syah… Lain kali hati-hati, ya. Banyak orang di luar sana kayak Mas perokok tadi. Sudah salah, nggak mau mengaku, malah bikin ribut."
            
            #aisyah netral
            show aisyah casual_senyum

            aisyah "Aku ngerti, Raden. Makasih udah ngingetin."

            raden "Ya, sama-sama,"

            show aisyah casual_senyum3

            aisyah "Iya, makasih banget, Raden."

            "Aisyah hanya tersenyum tipis setelah semua itu. Lalu dengan pelan, ia mengangguk kecil, dan berkata."

            #aisyah netral

            show aisyah casual_senyum

            aisyah "Aku duluan, ya."

            "Tanpa menunggu jawaban, dia berbalik dan berjalan menjauh, meninggalkan ku yang masih berdiri di lorong"

            "Aku menarik napas pelan. Satu sisi dadanya terasa hangat, sisi lainnya… entah."

            "Setelah beberapa detik terdiam, aku akhirnya melangkah menuju ruang kelas."

            hide aisyah casual_senyum with dissolve
            jump arc_character_day2_scene2

