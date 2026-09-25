define raden_nvl = Character("Raden", kind=nvl, callback=Phone_SendSound)
define aisyah_nvl = Character("Aisyah", kind=nvl, callback=Phone_ReceiveSound)
define from_sekar_route = False

label pensasi_sekar_scene1:
    scene bg lt_6_pasca_ramai with dissolve:
        zoom 0.5
    
    "Sembari terdian dalam pikiran, aku tidak sengaja melihat Kak Sekar dari jauh. Daripada aku bingung mau ngapain, aku langsung pergi ke Kak Sekar."

    stop music fadeout 2.0

    "Ketika sudah dekat, terdengar suara ricuh."

    play music intense fadein 1.0

    anon "\"Lah, dia baru bilang ke kita?\""

    "Setelah teriakan tersebut juga terdengan suara kak Sekar dengan nada bingung."

    anon "\"Aduh, cari penggantinya gimana ini?\""

    show sekar kasual_tegas at sekar_default:
        xalign 0.5
    with dissolve

    voice "audio/vo/sekar/pensasi/pensasi_1_1_udah.flac"
    sekar "\"Udah tenang dulu, kita pikirin solusi terbaiknya\""

    "Mendengar hal ini, aku terpikirkan apakah aku lanjut pergi ke sana atau pergi ke tempat lain saja."
    
    stop music fadeout 2.0

    menu:
        "Sapa Kak Sekar":
            jump pensasi_sekar_scene1_choice1_1

        "Kelihatannya merepotkan, nggak deh":
            "{i}Kelihatannya teralu merepotkan nih{/i}"

            "{i}Ngapain sekarang..?{/i}"
            menu:
                "Menyapa Tessa":
                    jump pensasi_tessa_scene1
                "Menunggu Aisyah":
                    $ from_sekar_route = True
                    #Jump
                    jump pensasi_aisyah_scene2
    return

label pensasi_sekar_scene1_choice1_1:
    show raden kasual_biasa at raden_default:
        xalign -0.2
    show sekar at sekar_default:
        xalign 1.0
    with moveinleft

    "Sambil berjalan mendekati Kak Sekar, aku pun menyapanya."

    play music campus fadein 1.0

    raden "\"Kak Sekar\""

    "Mendengar sapaan ku, Kak Sekar menoleh ke arahku dan menjawab."

    show sekar kasual_senyum

    voice "audio/vo/sekar/pensasi/pensasi_1_1_1_oh_raden.flac"
    sekar "\"Oh, Raden.\""

    show sekar kasual_biasa
    show raden kasual_biasa2

    raden "\"Kayaknya ada masalah ya kak?\""

    show sekar kasual_ragu

    voice "audio/vo/sekar/pensasi/pensasi_1_1_2_iya_nih.flac"
    sekar "\"Iya nih den, MC yang seharusnya datang dari tadi, ternyata kecelakaan, dan baru konfirmasi ke kita.\'"

    show raden kasual_canggung

    raden "\"Waduh, orangnya nggak apa-apa kak?\""

    voice "audio/vo/sekar/pensasi/pensasi_1_1_3_orangnya.flac"
    sekar "\"Orangnya nggak terluka sih, tapi motornya itu yang rusak.\""

    voice "audio/vo/sekar/pensasi/pensasi_1_1_4_jadi.flac"
    sekar "\"Jadi sekarang ada yang menjemput dia, tapi lokasinya masih jauh dari PENS.\""

    raden "\"Untuk penggantinya sudah ada belum kak?\""

    voice "audio/vo/sekar/pensasi/pensasi_1_1_5_untuk.flac"
    sekar "\"Untuk sekarang sih belum ada\""

    show raden kasual_bingung

    raden "\"Dari para panitia nggak ada yang bisa kak?\""

    voice "audio/vo/sekar/pensasi/pensasi_1_1_6_sayangnya.flac"
    sekar "\"Sayangnya sih, semuanya sudah dikasih perannya masing-masing.\""

    voice sustain

    sekar "\"Kalau ada yang ninggalin tugas bakal susah deh\""

    "Sambil berpikir, Kak Sekar tiba-tiba mengeluarkan wajah yang cerah sambil memandangku."

    show sekar kasual_senyum_lebar with dissolve

    voice "audio/vo/sekar/pensasi/pensasi_1_1_7_raden.flac"
    sekar "\"Raden, dari gaya bicaramu, kamu bisa public speaking kan?\""

    show raden kasual_tersenyum

    raden "\"Bisa sih kak, kenapa memangnya?\""

    show raden kasual_biasa
    show sekar kasual_bicara

    voice "audio/vo/sekar/pensasi/pensasi_1_1_8_mau_coba.flac"
    sekar "\"Mau coba jadi MC nggak den?\""

    show raden kasual_capek

    raden "\"Sudah kuduga... bakal ditanyain tentang ini\""

    show sekar kasual_biasa

    voice "audio/vo/sekar/pensasi/pensasi_1_1_9_gimana.flac"
    sekar "\"Gimana den? Sekalian nambah pengalaman\""

    "Mendengar pertanyaan itu membuatku berpikir."

    show raden kasual_bingung

    "{i}Enaknya bantu apa nggak nih?{/i}"

    voice "audio/vo/sekar/pensasi/pensasi_1_1_10_jadi.flac"
    sekar "\"Jadi gimana den?\""

    show sekar kasual_senyum

    voice "audio/vo/sekar/pensasi/pensasi_1_1_11_sama_nanti.flac"
    sekar "\"Sama nanti ku kasih hadiah spesial den, tawaran ini cuma bakalan terjadi sekali doang loh\""

    menu:
        "Kayaknya seru nih, ikut aja deh":
            jump pensasi_sekar_scene1_choice1_1_1
        "Jangan deh, sudah ada janji ngumpul sama yang lain":
            "{i}Mendingan jangan deh, ini kan aku juga mau ngumpul sama Aisyah dan juga Fania{/i}"

            show raden kasual_canggung

            raden "Maaf nih kak, aku sudah ada janji sama temenku. Jadi nggak bisa ngebantu."

            show sekar kasual_ragu

            voice "audio/vo/sekar/pensasi/pensasi_1_1_2_1_yasudah.flac"
            sekar "\"Yasudah kalau begitu\""

            show raden kasual_biasa2

            raden "\"Kalau begitu aku pergi dulu ya kak\""

            show sekar kasual_biasa

            voice "audio/vo/sekar/pensasi/pensasi_1_1_2_2_iya.flac"
            sekar "\"Iya den\""

            stop music fadeout 2.0

            #jump
            jump pembukaan_pensasi_afterchoice1

    return

label pensasi_sekar_scene1_choice1_1_1:
    "{i}Kayaknya bakal seru deh. Sekalian bisa menambah skill juga. Kuterima saja deh{/i}"

    show raden kasual_ceria

    raden "\"Gas kak\""

    show sekar kasual_ceria

    voice "audio/vo/sekar/pensasi/pensasi_1_1_1_1_sip.flac"
    sekar "\"Sip, sudah kuduga\""

    show raden kasual_biasa

    raden "\"Untuk tiap katanya yang harus aku ucapkan sudah disiapkan atau harus saya bikin sendiri kak?\""

    show sekar kasual_bicara

    voice "audio/vo/sekar/pensasi/pensasi_1_1_1_2_untuk.flac"
    sekar "\"Untuk masalah seperti itu dibahas nanti aja den. Kita harus nyiapin pakaian yang harus kamu pakai dan lainnya.\""

    "Sambil berjalan mengikuti Kak Sekar aku membuka ponselku dan melakukan chatting dengan Aisyah"

    raden_nvl "Aisyah"
    aisyah_nvl "Ada apa den?"
    raden_nvl "Maaf nih gk bisa bareng kalian, ada urusan mendadak"
    aisyah_nvl "Urusannya pentingkah den?"
    raden_nvl "Iya nih, maaf yah"
    aisyah_nvl "Kalo emang sepenting itu gpp sih"
    raden_nvl "Oh iya, kalo bisa ajak Fania ke Auditorium ya nanti"
    aisyah_nvl "Kenapa den?"
    raden_nvl "Ada deh"
    aisyah_nvl "Kalo nggak kamu jelasin dengan benar, gimana aku minta Fania buat datang ke Auditorium"
    raden_nvl "Pokoknya ajak Fania ke audit ya"
    raden_nvl "Semangat Aisyah"

    nvl clear

    "Ketika aku menutup ponselku, tanpa sadar ada Kak Sekar di sampingku sambil melihat chat ku dengan Aisyah"

    voice "audio/vo/sekar/pensasi/pensasi_1_1_1_3_udahan.flac"
    sekar "\"Udahan ngechat nya den?\""

    show raden kasual_panik
    
    raden "\"{size=+10}HUAAAKHH{/size}\"" with vpunch

    show sekar kasual_bingung

    voice "audio/vo/sekar/pensasi/pensasi_1_1_1_4_kenapa.flac"
    sekar "\"Kenapa den?\""

    show raden kasual_gugup

    raden "\"Nggak papa kak, sudah kok, cuman ngechat temen bentar\""

    show sekar kasual_biasa

    voice "audio/vo/sekar/pensasi/pensasi_1_1_1_5_yaudah.flac"
    sekar "\"Yaudah ayo, percepan jalannya\""

    show raden kasual_biasa2

    raden "\"Siap kak\""

    jump pensasi_sekar_scene2

    return