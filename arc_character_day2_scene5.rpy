label arc_character_day2_scene5:
    #Lorong D4
    #SFX: Langkah sepatu pelan

    scene bg jalan_d4_kantin with dissolve:
        zoom 0.5

    show raden kasual_biasa at raden_default:
        xalign -0.2
    show santo kasual_netral at santo_default:
        xalign 1.0
    with dissolve

    "Raden dan Santo berjalan berdampingan, map laporan dipegang di tangan Raden."

    "Langkah mereka ringan, tapi tidak terburu-buru. melewati tikungan kecil di lorong D4."

    "Dan di ujung lorong itu—Tampak satu sosok berdiri menyandar di dinding, dengan postur kuat dan ekspresi tajam. sikapnya tegas seperti biasa."

    show raden kasual_gugup
    raden "\"Eh… bukannya itu…\""

    santo "\"Kak Tessa…\""

    tessa "\"WOI, KALIAN!\"" #Suara serak

    "Aku dan santo pun langsung terkejut dan badan kami gemetar. Perlahan kami berdua melihat kedepan kemudian kami tambah terkejut mengetahui yang memanggil kami adalah Tessa."

    raden "\"Kenapa tuh?\""

    santo "\"Moga aja bukan kita\""

    "Tessa pun mulai mendekat"

    show raden kasual_panik
    raden "\"oiii, Santo gimana niii!\""

    "kemudian aku melihat kesamping dan seketika santo langsung kabur tanpa pemberitahuan "

    santo "\"Bye Den\""

    hide santo kasual_netral with dissolve

    "Aku yang ditinggal santo pun langsung syok seketika."

    menu:
        "Menyapa dengan gugup":
            "Aku pun mulai menyiapkan mental dengan menarik napas kecil walau masih kaget dan takut, saat Tessa mendekat, tubuhku gemetar hebat. Wajahnya yang serius berubah ketika dia menghela nafas."
            show tesssa kasual nafas at tessa_default:
                xalign 1.0
            
            "Aku menelan ludah, mencoba mengatur kata-kata yang mau keluar dari mulutku."

            show raden kasual_gugup
            raden "\"Huhhh...\""

            tessa "\"kenapa, hah?\"" #kembali serak

            raden "\"Ngg-nggak ada... mohon maaf.\""

            raden "\"Aku nggak ngapa-ngapain. Tolong jangan ganggu aku kak...\""

            jump arc_character_day2_scene6
        "Pilih kabur":
            scene bg parkir_d3_pagi with dissolve:
                zoom 0.5
            "Setelah kabur dari dari tessa yang ada di kantin, aku pun menarik napas dan menenangkan diriku."

            show raden kasual_gugup at raden_default:
                xalign 0.5
            raden "\"Tunggu? kenapa aku lari\""

            "Dengan ekspresi kesal yang bercampur dengan bingung, setelah beberapa saat berjalan aku pun terkejut melihat tessa yang tiba-tiba lewat di depannya, aku terkejut."

            show raden kasual_panik
            raden "\"AAAAAAAAAAAAAA\"" with vpunch

            show raden kasual_panik at raden_default:
                xalign 0.0
            with moveinleft

            show tessa kasual_netral at tessa_default:
                xalign 0.8
            tessa "\"Apaan?\""

            raden "\"Kukira hantu.\""

            "Ucapku dalam hati sambil berbalik badan melihat tessa dengan syok."

            tessa "\"Sembarangan!\""

            raden "\"Aa..\""

            tessa "\"A?\""

            raden "\"Ngg-nggak ada... mohon maaf.\""

            raden "\"Aku nggak ngapa-ngapain. Tolong jangan ganggu aku kak...\""

            jump arc_character_day2_scene6






