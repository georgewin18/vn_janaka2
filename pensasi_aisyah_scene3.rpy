label pensasi_aisyah_scene3:
    show raden kasual_biasa:
        zoom 0.48 xalign 0.0 yalign 0.1
    show aisyah kemeja_bicara:
        zoom 0.35 xalign 0.95 yalign -0.7
    with dissolve

    "Kami menghentikan obrolan canggung itu dan kembali fokus ke panggung."

    "Para mahasiswa bergantian memperkenalkan produk mereka, berbicara dengan penuh semangat, seolah-olah seluruh dunia sedang menyaksikan."

    "Produk-produk yang ditampilkan memang menarik- mulai dari alat bantu belajar hingga aplikasi yang mempermudah aktivitas sehari-hari."

    "Tapi, yang lebih menarik perhatianku adalah senyum kecil Aisyah setiap kali dia mendengar sesuatu yang menurutnya keren."

    "Aku menghela napas, mencoba mengusir pikiran aneh itu, lalu kembali fokus."

    "{i}Ini bukan waktu untuk melamun- aku di sini untuk sesuatu yang lebih besar, bukan?{/i}"

    menu:
        "Mencoba tetap fokus":
            "Aku mencoba mengabaikan segala pikiran yang berkeliaran di kepalaku dan memusatkan perhatian pada presentasi di depan."

            "Setiap tim memiliki caranya masing-masing untuk memamerkan produk mereka, mulai dari demo langsung hingga animasi canggih di layar."

            show raden kasual_tersenyum

            raden "\"Wow, mereka serius banget, ya,\""

            aisyah "\"iya,\""

            scene black with dissolve
            with Pause(0.3)

            scene bg auditorium with dissolve:
                zoom 0.5

            show raden kasual_biasa:
                zoom 0.48 xalign 0.0 yalign 0.1
            show aisyah kemeja_bicara:
                zoom 0.35 xalign 0.95 yalign -0.7
            with dissolve
            
            "Hingga akhirnya sesi istirahat dimulai. Aisyah menoleh ke arahku."

            if (pensasi_aisyah_scene2_choice2_1_choosen == True):
                aisyah "\"Ayok, Ishoma dulu, lalu lanjut jalan\""

                raden "\"Eh ya?\""

                "Perasaanku saja, atau memang Aisyah sedang kesal denganku?"

            else:
                aisyah "\"Kamu beneran memperhatikan ya!\""

                aisyah "\"Sekarang ayo ishoma dulu, lalu lanjut jalan\""

                raden "\"Oke!\""

        "Bersantai":
            "Aku menghela napas dan menyandarkan punggungku ke kursi, mencoba bersantai sedikit."

            show raden kasual_menghela_napas with dissolve

            raden "\"Haahh.. Nyaman juga,\""

            "Aku menutup mata sejenak. Namun, kenyamanan itu malah membawaku ke arah yang tak terduga."

            show black with dissolve

            "Sebelum aku sadar, kelopak mataku mulai terasa berat, dan tak butuh waktu lama hingga aku tertidur di tengah keramaian aula."

            show aisyah kemeja_penasaran

            hide black with dissolve

            aisyah "\"-den! Bangun Raden!\""

            "Seseorang menggoyangkan tubuhku."

            show raden kasual_gugup

            raden "\"Huh? Aku ketiduran..?\""

            aisyah "\"Tidur mulu..\""

            show raden kasual_canggung

            raden "\"Maaf.. gak sengaja\""

            if (pensasi_aisyah_scene2_choice2_1_choosen == True):
                show aisyah kemeja_senyum

                aisyah "\"Haha nggak apa..\""

                aisyah "\"Makasih..\""

                raden "\"Huh?\""

                "Apakah barusan Aisyah malah senang?"

                show aisyah kemeja_bicara

                aisyah "\"Sekarang ayo ishoma dulu, lalu lanjut jalan\""
            
            else:
                show aisyah kemeja_bicara

                aisyah "\"Yaudah, Ishoma dulu, lalu lanjut jalan\""

                raden "\"Eh ya?\""

                "Perasaanku saja, atau memang Aisyah sedang kesal denganku?"

    jump pensasi_aisyah_scene4

    return