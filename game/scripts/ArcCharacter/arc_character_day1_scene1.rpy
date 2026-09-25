label arc_character_day1_scene1:
    scene bg kamar_raden with dissolve:
        zoom 0.5

    show screen block_mouse

    $ renpy.pause(1.0, hard=True)

    # efek kedip
    show black with dissolve
    $ renpy.pause(0.1, hard=True)
    hide black with dissolve
    $ renpy.pause(0.1, hard=True)
    show black with dissolve
    $ renpy.pause(0.1, hard=True)
    hide black with dissolve

    show phone with moveinbottom:
        yalign 0.5 xalign 0.5

    $ renpy.pause(2.5, hard=True)

    hide phone with moveoutbottom

    hide screen block_mouse

    show raden kasual_biasa at raden_default:
        xalign 0.45
    with dissolve

    raden "\"Nggak nyangka udah jam segini\""

    show raden kasual_tersenyum
    raden "\"Kayaknya kemarin niatnya tidur bentar dah...\""

    show raden kasual_penasaran
    raden "\"Udah bangun gini enaknya ngapain ya? Matkul juga masih lama jam 8.\""

    menu:
        "Waktunya bangun untuk menjadi Mahasigma teladan":
            jump arc_character_day1_scene1_afterchoice1
        "Tidur saja lagi, kelas masih lama juga":
            jump arc_character_day1_scene1_afterchoice2

    return

label arc_character_day1_scene1_afterchoice1:
    show raden kasual_hehe
    raden "\"Sekali-kali gapapa lah jadi mahasigma yang rajin.\""

    show raden kasual_biasa
    raden "\"Sip, dah siap berangkat nih...\""

    scene black with dissolve
    with Pause(0.3)

    scene bg jalan_gang with dissolve:
        zoom 0.5

    "Dalam perjalanan menuju kampus Aku tidak sengaja bertemu dengan seseorang yang terlihat mendorong motornya yang mogok."

    show raden kasual_bingung at raden_default:
        xalign 0.45
    with dissolve

    raden "{i}Itu kayaknya ada yang butuh di stut in deh, bantu nggak ya{/i}"

    "Aku mendekati orang tersebut, rambutnya hijau nyentrik. Sangat jarang, aku sendiri hanya tahu satu orang yang memiliki rambut warna hijau."

    show raden at raden_default:
        xalign -0.2
    with moveinright

    show sekar kasual_ragu at sekar_default:
        xalign 1.0
    with dissolve

    show raden kasual_kaget

    raden "\"Lah, itu kak sekar?\""

    show raden kasual_tersenyum

    raden "\"Kak Sekar?\""

    show sekar kasual_bingung

    sekar "\"?\""

    raden "\"Motornya mau ku stut in, Kak?\""

    show sekar kasual_ceria

    sekar "\"Eh, Raden? Kebetulan banget, iya nih. Tiba-tiba saja motorku mati di tengah jalan. Untung ketemu, Stut in sampai di bengkel terdekat ya, den\""

    show raden kasual_biasa

    raden "\"Iya kak, apa Kak Sekar butuh tumpangan sekalian ke kampus? Daripada nunggu lama di bengkel.\""

    show sekar kasual_bicara

    sekar "\"Boleh tuh, den. Aku juga bakal ada meeting habis ini. Untung ketemu kamu, kalo nggak, bakal terlambat aku...\""

    show sekar kasual_biasa
    show raden kasual_tersenyum

    raden "\"Iya kak, aku juga kebetulan ada kelas pagi. Kalau nggak ada, pasti nggak ketemu\""

    show sekar kasual_ceria

    sekar "\"Hahaha, iya\""

    "Sambil mendorong motor, kami sedikit berbincang mengenai kebetulan ini, meskipun topik kadang berpindah-pindah tapi pembicaraan tersebut terus berjalan sampai kita sampai di kampus."

    scene black with dissolve
    with Pause(0.3)

    scene bg parkir_d3_pagi with dissolve:
        zoom 0.5

    show raden kasual_biasa at raden_default:
        xalign -0.2
    show sekar kasual_bicara at sekar_default:
        xalign 1.0
    with dissolve

    sekar "\"Sudah sampai, makasih ya den.\""

    show raden kasual_tersenyum

    raden "\"Sama-sama kak.\""

    show raden kasual_biasa
    show sekar kasual_biasa

    "Aku tersenyum kecil menjawab perkataan Kak Sekar. Sampai ketika, aku merasakan tatapan aneh dari belakangku. Aku sontak menoleh ke arah tatapan tersebut."

    show raden kasual_canggung with dissolve

    "Melihat diriku yang menoleh secara tiba-tiba, Kak Sekar ikutan menoleh menuju arah mukaku menghadap. Ketika Sekar menoleh, tatapan orang itu langsung menjadi normal."
    
    "Aku tidak tahu, apakah tatapan yang sebelumnya hanya ada dalam pikiranku saja. Karena saat ini, Orang yang dihadapanku memiliki wajah yang sangat murah hati."

    show sekar kasual_bicara

    sekar "\"Eh, Abdi. Baru datang juga?. Ayo cepat, ditungguin yang lain nanti.\""

    show sekar kasual_ceria

    sekar "\"Btw, Makasih ya den atas boncengannya.\""

    show raden kasual_biasa

    raden "\"Sama-sama Kak Sekar.\""

    hide sekar with moveoutright
    show raden kasual_canggung with dissolve

    "Sebelum benar-benar pergi, Orang yang bernama abdi itu berjalan sembari menatap ke arahku. Bagaikan orang yang melihat serangga yang mengganggu harinya. Sebelum, akhirnya dia benar-benar pergi."

    "Tanpa menunda lagi, aku berjalan menuju kelasku."

    scene bg kelas_d4 with dissolve

    show raden kasual_biasa at raden_default:
        xalign 0.45
    with dissolve

    "Setibanya aku di kelas, masih banyak kursi yang kosong, kurasa inilah faedah nya datang ke kelas lebih awal. Tak lama kemudian Santo datang dan duduk di sebelahku, begitu juga Dosen."

    hide raden with dissolve

    "Setelah menjelaskan materi, dia memberi kami tugas berkelompok, masing-masing kelompok tiga orang, Saat aku hendak mencari satu orang lagi-"

    show raden kasual_biasa at raden_default:
        xalign -0.5
    show santo kasual_netral at santo_default:
        xalign 0.45
    show erin kasual_netral at erin_default:
        xalign 1.1
    with dissolve

    erin "\"Kalian sudah ada kelompok?\""

    "Seorang gadis di kelas kami yang aku belum tau namanya, menggeser kursinya mendekati meja ku dan Santo."

    show santo kasual_bicara

    santo "\"Belum. Mau bareng?\""

    show santo kasual_netral

    "Gadis itu tersenyum lembut, dan mengangguk pelan"

    erin "\"Kalau boleh..\""

    show raden kasual_tersenyum

    raden "\"Oh, boleh kok. Aku Raden, salam kenal ya.\""

    erin "\"Erin. Makasih ya.\""

    scene black with dissolve
    with Pause(0.3)

    jump arc_character_day1_scene2

    return

label arc_character_day1_scene1_afterchoice2:
    show raden kasual_menghela_napas with dissolve

    raden "\"Tidur pun sedap nih..\""

    "Karena di luar masih gerimis, Aku memutuskan untuk tidur lagi, di kasur yang empuk, lembut, dan hangat."

    scene black with dissolve
    with Pause(0.3)

    centered "Beberapa Jam Kemudian"

    scene bg kamar_raden with dissolve:
        zoom 0.5

    show raden kasual_menghela_napas at raden_default:
        xalign 0.45
    with dissolve

    raden "\"Aakkhh, enak banget tidurnya\""

    show raden kasual_canggung with dissolve

    raden "\"Hmm?\""

    show raden kasual_panik

    raden "\"?????, Weladalah. udah {size=+10}jam 8.30{/size}, terlambat ni aku!!\"" with vpunch

    "Bermodal cuci muka, Aku langsung berangkat pergi menuju ke kampus."

    scene bg kelas_d4 with dissolve

    "Aku mengetuk pintu"

    show raden kasual_gugup at raden_default:
        xalign 0.45
    with dissolve

    raden "\"Assalamualaikum pak. Permisi\""

    show raden kasual_canggung

    dosen "\"Siapa yang menyuruhmu masuk?\""

    show raden kasual_gugup

    raden "\"Eh maaf pak, karena tidak ada jawaban. Saya kira diperbolehkan masuk\""

    show raden kasual_canggung

    dosen "\"Lain kali, jika saya masih belum memberi instruksi masuk ruangan. Jangan masuk ruangan\""

    raden "\"Iya pak, maaf\""

    dosen "\"Baiklah kalau begitu, masuk sana. dan saya peringatkan lain kali jangan terlambat\""

    raden "\"Iya pak, terima kasih\""

    raden "{i}Lain kali, nggak lagi dah terlambat{/i}"

    "Saat aku menoleh sekitar, aku melihat Santo melambaikan tangan nya padaku. Aku segera mendekatinya dan duduk di kursi kosong dekatnya."

    show raden kasual_capek at raden_default:
        xalign -0.2
    with moveinright

    show santo kasual_senyum_lebar at santo_default:
        xalign 1.0
    with dissolve

    santo "\"Yo, pahlawan kesiangan. Udah disambut meriah sama Pak Dosen, ya?\""

    show raden kasual_menghela_napas with dissolve

    raden "\"Gimana ya... salah timing. Kukira kalau disapa pakai salam langsung dibolehin masuk.\""

    show santo kasual_senyum

    santo "\"Ya nggak gitu juga, Den. Tapi keren sih, kamu buka pintu kayak adegan film thriller.\""

    show raden at raden_default:
        xalign -0.5
    show santo at santo_default:
        xalign 0.45
    with moveinright

    show erin kasual_netral at erin_default:
        xalign 1.1
    with dissolve

    erin "\"Kamu Raden, ya?\""

    show raden kasual_gugup with dissolve

    raden "\"Iya, aku… eh, iya, betul.\""

    show raden kasual_canggung

    "Gadis itu tersenyum sopan, lalu membuka buku catatan kecilnya"

    erin "\"Aku Erin,. Tadi Pak Dosen jelasin tugas yang harus dikerjakan kelompok tiga orang.\""

    erin "\"Mau sekelompok?, bareng Santo juga\""

    show raden kasual_biasa2

    raden "\"Oh, gitu ya? boleh deh makasih... maaf banget aku tadi telat jadi nggak dengar penjelasannya.\""

    erin "\"Gak apa-apa. Kita belum bahas kok tadi\""

    show santo kasual_senyum_lebar at santo_default:
        xalign 0.45
        linear 0.3 xalign 0.35
        linear 0.3 xalign 0.45

    "Santo menyenggol bahu Raden sedikit, dengan senyum jail nya."

    santo "\"Tuh kan, telat-telat dapet kelompok cakep. Rejeki anak soleh.\""

    show raden kasual_kesal

    raden "\"Oy, nggak gitu juga!\""

    "Erin hanya tertawa kecil, lalu menatap ke depan dengan tenang"

    scene black with dissolve
    with Pause(0.3)

    jump arc_character_day1_scene2

    return