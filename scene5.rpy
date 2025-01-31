label scene5:
        scene bg masjid:
                zoom 0.5
        with dissolve

        show raden biasa with dissolve:
                zoom 0.2 xalign 0.5 yalign 0.0

        raden "\"Alhamdulillah!\""

        "Syukurlah aku masih sempat ikut shalat berjamaah di bagian pertama. Sekarang masih ada sedikit waktu untuk beristirahat."

        "Aku merenggangkan tubuh sambil memandang sekeliling. Sebuah senyuman tipis muncul di wajahku, merasa lega karena akhirnya aku bisa menempuh kuliah di kampus yang bagus."
        
        "Saat itu, mataku berhenti pada Aisyah yang sedang duduk di taman depan masjid."

        show raden biasa with moveinright:
                zoom 0.2 xalign 0.12 yalign 0.0

        show aisyah kemeja_bicara with dissolve:
                zoom 0.3 xalign 0.85 yalign 6.0

        play music aisyah_bgm fadein 1.0

        raden "\"Kamu sudah shalat?\""

        voice "audio/vo/aisyah/pkkmb9_aku_halangan.mp3"
        aisyah "\"Aku halangan hari ini\""

        "Ngomong apa sih aku ini? Seharusnya bisa lebih mengerti. Oke, sekarang coba buat suasana jadi lebih santai supaya nggak canggung"

        raden "\"Ehh... errmmm...\""

        voice "audio/vo/aisyah/pkkmb10_kenapa.mp3"
        aisyah "\"Kenapa?\""

        raden "\"Uh.. enggak, cuman... jika tidak shalat, kenapa capek-capek turun? Belum lagi nanti naiknya\""

        show aisyah kemeja_senyum

        voice "audio/vo/aisyah/pkkmb11_haha.mp3"
        aisyah "\"Hahaha..\""

        raden "\"Malah ketawa\""

        voice "audio/vo/aisyah/pkkmb12_enggak_apa.mp3"
        aisyah "\"Enggak apa.. nyari udara segar aja\""

        raden "\"Beneran?\""

        voice "audio/vo/aisyah/pkkmb13_hmm.mp3"
        "..."

        voice "audio/vo/aisyah/pkkmb14_semoga.mp3"
        aisyah "\"Semoga kuliah kita nanti lancar ya!\""

        "Gadis yang aneh. Sejak pertama kali bertemu, Aisyah selalu bersikap baik padaku. Dia seperti cahaya yang menyinari orang-orang disekitarnya\""

        "Begitu terang hingga terasa menyilaukan\""

        "Aku penasaran, seperti apa bayangan yang tersembunyi di balik cahaya itu?"

        stop music fadeout 2.0

        scene black with dissolve
        with Pause(0.2)

        jump scene6

        return
