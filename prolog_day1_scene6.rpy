label prolog_day1_scene6:
        show bg lap_futsal:
                zoom 0.5 
        with dissolve

        "Waktu terasa berlalu begitu cepat. Hari pertama PKKMB sudah hampir selesai. Setelah Auditorium, para mahasiswa baru diminta menuju Lapangan Basket."

        "Di sana, kami menerima tugas yang harus segera dikumpulkan sebelum akhirnya diperbolehkan pulang."

        show raden kemeja_biasa2:
                zoom 0.48 xalign 0.0 yalign 0.1
        show fania jas_senyum_normal at Transform(matrixcolor=(silhouette)):
                zoom 1.15 xalign 1.1 yalign -0.02
        with dissolve

        play music fania_bgm fadein 1.0

        voice "audio/vo/fania/pkkmb1_akhirnya_selesai.flac"
        anon "Ahhh, akhirnya selesai juga!"

        raden "Iya, capek banget."

        hide fania with dissolve

        show fania jas_senyum_normal:
                zoom 1.15 xalign 1.1 yalign -0.02
        with dissolve
        
        voice "audio/vo/fania/pkkmb2_duh.flac"
        anon "Duh.. Bikin kaget aja."

        show raden kemeja_tersenyum

        raden "Hahaha, maaf ya."

        show raden kemeja_biasa

        raden "Jadi ini rasanya kuliah, ya? Beda banget sama SMA. Orang-orangnya random banget."

        voice "audio/vo/fania/pkkmb3_kalau_lihat_senior.flac"
        anon "Apalagi kalau lihat senior-senior tadi. Ada yang kayak serius banget, ada yang santai, ada juga yang humoris. Tapi seru sih."

        raden "Seru, sih. Tapi capeknya nggak bohong."

        show fania kemeja_senyum_ceria

        voice "audio/vo/fania/pkkmb4_yang_penting_sekarang.flac"
        anon "Haha, Yang penting sekarang waktunya pulang, mandi, terus rebahan."

        show raden kemeja_hehe

        raden "Fix, setuju banget. Tapi besok kayaknya bakal tambah ribet deh, lihat dari list tugas yang tadi dikasih."

        show raden kemeja_biasa
        show fania kemeja_senyum_normal

        voice "audio/vo/fania/pkkmb5_iya_tugasnya_lumayan.flac"
        anon "Iya, tugasnya... lumayan.. Tapi ya sudahlah, namanya juga PKKMB."

        voice "audio/vo/fania/pkkmb6_ohiya_kumpul.flac"
        anon "Oh iya.. kumpul kelompok dulu- Duluan ya!"

        hide fania with dissolve

        show raden with moveinleft:
                xalign 0.5

        "Perempuan itu pergi begitu saja tanpa memberi kesempatan untuk sekadar berkenalan."

        raden "Yasudahlah.. aku juga harus segera kumpul lalu pulang."

        "Setelah beberapa menit berdiskusi dengan kelompok tentang tugas, aku pulang dengan rasa lelah."

        scene black with dissolve
        with Pause(0.3)

        stop music fadeout 2.0

        jump prolog_day2_scene1

        return