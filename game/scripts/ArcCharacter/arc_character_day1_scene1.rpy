label arc_character_day1_scene1:
    scene bg kamar_raden with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show screen block_mouse

    $ renpy.pause(1.0, hard=True)

    # efek kedip
    show black at Transform(xsize=config.screen_width, ysize=config.screen_height, xpos=0, ypos=0) with dissolve
    $ renpy.pause(0.1, hard=True)
    hide black with dissolve
    $ renpy.pause(0.1, hard=True)
    show black at Transform(xsize=config.screen_width, ysize=config.screen_height, xpos=0, ypos=0) with dissolve
    $ renpy.pause(0.1, hard=True)
    hide black with dissolve

    show phone with moveinbottom:
        yalign 0.5 xalign 0.5

    $ renpy.pause(2.5, hard=True)

    hide phone with moveoutbottom

    hide screen block_mouse

    show raden kasual_biasa:
        xalign 0.45
        zoom raden_default.zoom
        yalign raden_default.yalign
    with dissolve

    raden "\"Nggak nyangka udah jam segini\""

    show raden kasual_tersenyum:
        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Kayaknya kemarin niatnya tidur bentar dah...\""

    show raden kasual_penasaran:
        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Udah bangun gini enaknya ngapain ya? Matkul juga masih lama jam 8.\""

    menu:
        "Waktunya bangun untuk menjadi Mahasigma teladan":
            jump arc_character_day1_scene1_afterchoice1
        "Tidur saja lagi, kelas masih lama juga":
            jump arc_character_day1_scene1_afterchoice2

    return

label arc_character_day1_scene1_afterchoice1:
    show raden kasual_hehe:
        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Sekali-kali gapapa lah jadi mahasigma yang rajin.\""

    show raden kasual_biasa:
        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Sip, dah siap berangkat nih...\""

    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(0.3)

    scene bg jalan_gang with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    "Dalam perjalanan menuju kampus Aku tidak sengaja bertemu dengan seseorang yang terlihat mendorong motornya yang mogok."

    show raden kasual_bingung:
        xalign 0.45
        zoom raden_default.zoom
        yalign raden_default.yalign
    with dissolve

    raden "{i}Itu kayaknya ada yang butuh di stut in deh, bantu nggak ya{/i}"

    "Aku mendekati orang tersebut, rambutnya hijau nyentrik. Sangat jarang, aku sendiri hanya tahu satu orang yang memiliki rambut warna hijau."

    show raden:
        xalign -0.2
        zoom raden_default.zoom
        yalign raden_default.yalign
    with moveinright

    show sekar kasual_ragu:
        xalign 1.0
        zoom sekar_default.zoom
        yalign sekar_default.yalign
    with dissolve

    show raden kasual_kaget:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Lah, itu kak sekar?\""

    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Kak Sekar?\""

    show sekar kasual_bingung:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    sekar "\"?\""

    raden "\"Motornya mau ku stut in, Kak?\""

    show sekar kasual_ceria:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    sekar "\"Eh, Raden? Kebetulan banget, iya nih. Tiba-tiba saja motorku mati di tengah jalan. Untung ketemu, Stut in sampai di bengkel terdekat ya, den\""

    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Iya kak, apa Kak Sekar butuh tumpangan sekalian ke kampus? Daripada nunggu lama di bengkel.\""

    show sekar kasual_bicara:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    sekar "\"Boleh tuh, den. Aku juga bakal ada meeting habis ini. Untung ketemu kamu, kalo nggak, bakal terlambat aku...\""

    show sekar kasual_biasa:
        zoom sekar_default.zoom
        yalign sekar_default.yalign
    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Iya kak, aku juga kebetulan ada kelas pagi. Kalau nggak ada, pasti nggak ketemu\""

    show sekar kasual_ceria:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    sekar "\"Hahaha, iya\""

    "Sambil mendorong motor, kami sedikit berbincang mengenai kebetulan ini, meskipun topik kadang berpindah-pindah tapi pembicaraan tersebut terus berjalan sampai kita sampai di kampus."

    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(0.3)

    scene bg parkir_d3_pagi with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kasual_biasa:
        xalign -0.2
        zoom raden_default.zoom
        yalign raden_default.yalign
    show sekar kasual_bicara:
        xalign 1.0
        zoom sekar_default.zoom
        yalign sekar_default.yalign
    with dissolve

    sekar "\"Sudah sampai, makasih ya den.\""

    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Sama-sama kak.\""

    show raden kasual_biasa:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show sekar kasual_biasa:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    "Aku tersenyum kecil menjawab perkataan Kak Sekar. Sampai ketika, aku merasakan tatapan aneh dari belakangku. Aku sontak menoleh ke arah tatapan tersebut."

    show raden kasual_canggung with dissolve:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Melihat diriku yang menoleh secara tiba-tiba, Kak Sekar ikutan menoleh menuju arah mukaku menghadap. Ketika Sekar menoleh, tatapan orang itu langsung menjadi normal."
    
    "Aku tidak tahu, apakah tatapan yang sebelumnya hanya ada dalam pikiranku saja. Karena saat ini, Orang yang dihadapanku memiliki wajah yang sangat murah hati."

    show sekar kasual_bicara:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    sekar "\"Eh, Abdi. Baru datang juga?. Ayo cepat, ditungguin yang lain nanti.\""

    show sekar kasual_ceria:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    sekar "\"Btw, Makasih ya den atas boncengannya.\""

    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Sama-sama Kak Sekar.\""

    hide sekar with moveoutright
    show raden kasual_canggung with dissolve:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Sebelum benar-benar pergi, Orang yang bernama abdi itu berjalan sembari menatap ke arahku. Bagaikan orang yang melihat serangga yang mengganggu harinya. Sebelum, akhirnya dia benar-benar pergi."

    "Tanpa menunda lagi, aku berjalan menuju kelasku."

    scene bg kelas_d4 with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kasual_biasa:
        xalign 0.45
        zoom raden_default.zoom
        yalign raden_default.yalign
    with dissolve

    "Setibanya aku di kelas, masih banyak kursi yang kosong, kurasa inilah faedah nya datang ke kelas lebih awal. Tak lama kemudian Santo datang dan duduk di sebelahku, begitu juga Dosen."

    hide raden with dissolve

    "Setelah menjelaskan materi, dia memberi kami tugas berkelompok, masing-masing kelompok tiga orang, Saat aku hendak mencari satu orang lagi-"

    show raden kasual_biasa:
        xalign -0.5
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kasual_netral:
        xalign 0.45
        zoom santo_default.zoom
    show erin kasual_netral:
        xalign 1.1
        zoom erin_default.zoom
        yalign erin_default.yalign
    with dissolve

    erin "\"Kalian sudah ada kelompok?\""

    "Seorang gadis di kelas kami yang aku belum tau namanya, menggeser kursinya mendekati meja ku dan Santo."

    show santo kasual_bicara:

        zoom santo_default.zoom
    santo "\"Belum. Mau bareng?\""

    show santo kasual_netral:

        zoom santo_default.zoom
    "Gadis itu tersenyum lembut, dan mengangguk pelan"

    erin "\"Kalau boleh..\""

    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Oh, boleh kok. Aku Raden, salam kenal ya.\""

    erin "\"Erin. Makasih ya.\""

    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(0.3)

    jump arc_character_day1_scene2

    return

label arc_character_day1_scene1_afterchoice2:
    show raden kasual_menghela_napas with dissolve:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Tidur pun sedap nih..\""

    "Karena di luar masih gerimis, Aku memutuskan untuk tidur lagi, di kasur yang empuk, lembut, dan hangat."

    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(0.3)

    centered "Beberapa Jam Kemudian"

    scene bg kamar_raden with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kasual_menghela_napas:
        xalign 0.45
        zoom raden_default.zoom
        yalign raden_default.yalign
    with dissolve

    raden "\"Aakkhh, enak banget tidurnya\""

    show raden kasual_canggung with dissolve:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Hmm?\""

    show raden kasual_panik:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"?????, Weladalah. udah {size=+10}jam 8.30{/size}, terlambat ni aku!!\"" with vpunch

    "Bermodal cuci muka, Aku langsung berangkat pergi menuju ke kampus."

    scene bg kelas_d4 with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    "Aku mengetuk pintu"

    show raden kasual_gugup:
        xalign 0.45
        zoom raden_default.zoom
        yalign raden_default.yalign
    with dissolve

    raden "\"Assalamualaikum pak. Permisi\""

    show raden kasual_canggung:

        zoom raden_default.zoom
        yalign raden_default.yalign
    dosen "\"Siapa yang menyuruhmu masuk?\""

    show raden kasual_gugup:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Eh maaf pak, karena tidak ada jawaban. Saya kira diperbolehkan masuk\""

    show raden kasual_canggung:

        zoom raden_default.zoom
        yalign raden_default.yalign
    dosen "\"Lain kali, jika saya masih belum memberi instruksi masuk ruangan. Jangan masuk ruangan\""

    raden "\"Iya pak, maaf\""

    dosen "\"Baiklah kalau begitu, masuk sana. dan saya peringatkan lain kali jangan terlambat\""

    raden "\"Iya pak, terima kasih\""

    raden "{i}Lain kali, nggak lagi dah terlambat{/i}"

    "Saat aku menoleh sekitar, aku melihat Santo melambaikan tangan nya padaku. Aku segera mendekatinya dan duduk di kursi kosong dekatnya."

    show raden kasual_capek:
        xalign -0.2
        zoom raden_default.zoom
        yalign raden_default.yalign
    with moveinright

    show santo kasual_senyum_lebar:
        xalign 1.0
        zoom santo_default.zoom
    with dissolve

    santo "\"Yo, pahlawan kesiangan. Udah disambut meriah sama Pak Dosen, ya?\""

    show raden kasual_menghela_napas with dissolve:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Gimana ya... salah timing. Kukira kalau disapa pakai salam langsung dibolehin masuk.\""

    show santo kasual_senyum:

        zoom santo_default.zoom
    santo "\"Ya nggak gitu juga, Den. Tapi keren sih, kamu buka pintu kayak adegan film thriller.\""

    show raden:
        xalign -0.5
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo:
        xalign 0.45
        zoom santo_default.zoom
    with moveinright

    show erin kasual_netral:
        xalign 1.1
        zoom erin_default.zoom
        yalign erin_default.yalign
    with dissolve

    erin "\"Kamu Raden, ya?\""

    show raden kasual_gugup with dissolve:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Iya, aku… eh, iya, betul.\""

    show raden kasual_canggung:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Gadis itu tersenyum sopan, lalu membuka buku catatan kecilnya"

    erin "\"Aku Erin,. Tadi Pak Dosen jelasin tugas yang harus dikerjakan kelompok tiga orang.\""

    erin "\"Mau sekelompok?, bareng Santo juga\""

    show raden kasual_biasa2:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Oh, gitu ya? boleh deh makasih... maaf banget aku tadi telat jadi nggak dengar penjelasannya.\""

    erin "\"Gak apa-apa. Kita belum bahas kok tadi\""

    show santo kasual_senyum_lebar:
        xalign 0.45
        linear 0.3 xalign 0.35
        linear 0.3 xalign 0.45

        zoom santo_default.zoom
    "Santo menyenggol bahu Raden sedikit, dengan senyum jail nya."

    santo "\"Tuh kan, telat-telat dapet kelompok cakep. Rejeki anak soleh.\""

    show raden kasual_kesal:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Oy, nggak gitu juga!\""

    "Erin hanya tertawa kecil, lalu menatap ke depan dengan tenang"

    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(0.3)

    jump arc_character_day1_scene2

    return
