define raden_nvl = Character("Raden", kind=nvl, callback=Phone_SendSound)
define aisyah_nvl = Character("Aisyah", kind=nvl, callback=Phone_ReceiveSound)
define from_sekar_route = False

label pensasi_sekar_scene1:
    scene bg depan_auditorium with dissolve:
        zoom 0.5
    
    "Sembari terdian dalam pikiran, aku tidak sengaja melihat Kak Sekar dari jauh. Daripada aku bingung mau ngapain, aku langsung pergi ke Kak Sekar."

    "Ketika sudah dekat, terdengar suara ricuh."

    anon "\"Lah, dia baru bilang ke kita?\""

    "Setelah teriakan tersebut juga terdengan suara kak Sekar dengan nada bingung."

    anon "\"Aduh, cari penggantinya gimana ini?\""

    sekar "\"Udah tenang dulu, kita pikirin solusi terbaiknya\""

    "Mendengar hal ini, aku terpikirkan apakah aku lanjut pergi ke sana atau pergi ke tempat lain saja."
    
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
    "Sambil berjalan mendekati Kak Sekar, aku pun menyapanya."

    raden "\"Kak Sekar\""

    "Mendengar sapaan ku, Kak Sekar menoleh ke arahku dan menjawab."

    sekar "\"Oh, Raden.\""

    raden "\"Kayaknya ada masalah ya kak?\""

    sekar "\"Iya nih den, MC yang seharusnya datang dari tadi, ternyata kecelakaan, dan baru konfirmasi ke kita.\'"

    raden "\"Waduh, orangnya nggak apa-apa kak?\""

    sekar "\"Orangnya nggak terluka sih, tapi motornya itu yang rusak.\""

    sekar "\"Jadi sekarang ada yang menjemput dia, tapi lokasinya masih jauh dari PENS.\""

    raden "\"Untuk penggantinya sudah ada belum kak?\""

    sekar "\"Untuk sekarang sih belum ada\""

    raden "\"Dari para panitia nggak ada yang bisa kak?\""

    sekar "\"Sayangnya sih, semuanya sudah dikasih perannya masing-masing.\""

    sekar "\"Kalau ada yang ninggalin tugas bakal susah deh\""

    "Sambil berpikir, Kak Sekar tiba-tiba mengeluarkan wajah yang cerah sambil memandangku."

    sekar "\"Raden, dari gaya bicaramu, kamu bisa public speaking kan?\""

    raden "\"Bisa sih kak, kenapa memangnya?\""

    sekar "\"Mau coba jadi MC nggak den?\""

    raden "\"Sudah kuduga... bakal ditanyain tentang ini\""

    sekar "\"Gimana den? Sekalian nambah pengalaman\""

    "Mendengar pertanyaan itu membuatku berpikir."

    "{i}Enaknya bantu apa nggak nih?{/i}"

    sekar "\"Jadi gimana den?\""

    sekar "\"Sama nanti ku kasih hadiah spesial den, tawaran ini cuma bakalan terjadi sekali doang loh\""

    menu:
        "Kayaknya seru nih, ikut aja deh":
            jump pensasi_sekar_scene1_choice1_1_1
        "Jangan deh, sudah ada janji ngumpul sama yang lain":
            "{i}Mendingan jangan deh, ini kan aku juga mau ngumpul sama Aisyah dan juga Fania{/i}"

            raden "Maaf nih kak, aku sudah ada janji sama temenku. Jadi nggak bisa ngebantu."

            sekar "\"Yasudah kalau begitu\""

            raden "\"Kalau begitu aku pergi dulu ya kak\""

            sekar "\"Iya den\""

            #jump

    return

label pensasi_sekar_scene1_choice1_1_1:
    "{i}Kayaknya bakal seru deh. Sekalian bisa menambah skill juga. Kuterima saja deh{/i}"

    raden "\"Gas kak\""

    sekar "\"Sip, sudah kuduga\""

    raden "\"Untuk tiap katanya yang harus aku ucapkan sudah disiapkan atau harus saya bikin sendiri kak?\""

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

    sekar "\"Udahan ngechat nya den?\""

    raden "\"{size=+10}HUAAAKHH{/size}\"" with vpunch

    sekar "\"Kenapa den?\""

    raden "\"Nggak papa kak, sudah kok, cuman ngechat temen bentar\""

    sekar "\"Yaudah ayo, percepan jalannya\""

    raden "\"Siap kak\""

    jump pensasi_sekar_scene2

    return