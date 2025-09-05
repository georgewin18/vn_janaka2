label arc_character_day2_scene3:
    scene bg perpus_pasca
    #Backsound Suasana Netral di kampus
    show raden kasual_biasa at raden_default:
        xalign -0.8
    show santo kasual_netral at santo_default:
        xalign 0.8
    show fania casual_dingin at fania_default:
        xalign 2.0
    show aisyah casual_gugup at aisyah_default:
        xalign 0.15

    "…"
    "…"
    #Suara keyboard

    "Hanya ada keheningan dan suara ketukan keyboard dari laptop Fania yang terdengar di antara keduanya. Udara canggung itu berasal dari Fania yang jutek dan Aisyah yang nampak khawatir tapi tidak mampu menunjukkannya tanpa mengganggu temannya."

    "Aku mendekat pada Aisyah dan berbisik padanya."

    raden "\"Aisyah, ini Fania yang ngambil semua bukunya?\""

    aisyah "\"Iya, dia lagi ngerjain tugas katanya,\""

    "Jawabannya itu membuatku dan Santo mau tidak mau melongo dengan jumlahnya."

    show raden kasual_kaget

    raden "\"Hah? Tugas? Banyak banget, departemenku aja belum pernah ada yang kayak gini di kelas satu. Kecuali…\""

    "Aku memandang buku-buku yang dibaca Fania. Teknik multitasking yang luar biasa."

    aisyah "\"Kayaknya itu bukan tugas individu deh, Den.\""

    "Balasku saat meraih buku dan mulai menyalin kalimat yang Fania butuhkan dan mengirimnya melalui private chat agar dia bisa langsung menyalin."

    fania "\"Kalau kalian punya waktu buat diskusi, minimal jangan ganggu orang ngerjain tugas.\""

    aisyah "\"Fania, biar ku bantu!\""

    "Aisyah langsung berkata, menyela Fania dari memarahiku."

    menu:
        "Ikut bantu Fania":
            show raden kasual_tersenyum
            raden "\"Kalau begitu, aku juga bakalan bantu, Fan. Tapi aku mau kamu kasih tau kita nanti kenapa kamu ngerjain tugasmu sendirian.\""

            fania "\"Tapi aku gak minta bantuan.\""

            raden "\"Sh, sh. Abaikan detailnya.\""

            #Backsound Suasana sedikit dramatis

            santo "\"Jadi kamu mau bantuin Fania sekarang? Yaudah deh, yuk kita cepet selesain.\""

            "Santo mulai duduk di kursi yang tersisa."
            jump arc_character_day2_scene4
        "Tidak ikut membantu":
            "Aku hanya diam melihat dan membiarkan Aisyah membantu Fania."

            santo "\"Jadi kamu gak punya niat bantu? Biasanya bantuin.\""

            raden "\"Tapi kita punya tugas sendiri, gak mungkinlah kita jadi kena hukuman.\""

            santo "\"Tapi kalau diperkirakan, kita bisa nyelesain tugas Fania duluan dan kita masih punya waktu banyak untuk deadline kita. Fania, aku bakalan bantu.\""

            show raden kasual_bingung

            "Balasan Santo membuatku bingung pada sifatnya hari ini yang tiba-tiba unjuk gigi pada orang lain, padahal, biasanya dia hanya akan melihat dari samping."

            "Melihat mereka semua, sayang sekali jika aku tidak membantu. Pada akhirnya, aku tidak bisa menahan diri dan mengikuti arus."

            show raden kasual_netral
            raden "\"Oke deh, aku bakalan bantu juga!\""
            jump arc_character_day2_scene4


