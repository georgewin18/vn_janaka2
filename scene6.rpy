label scene6:
        show bg lap_futsal:
                zoom 0.5 
        with dissolve

        "Waktu terasa berlalu begitu cepat. Hari pertama PKKMB sudah hampir selesai. Setelah Auditorium, para mahasiswa baru diminta menuju Lapangan Basket."

        "Di sana, kami menerima tugas yang harus segera dikumpulkan sebelum akhirnya diperbolehkan pulang."

        show raden biasa:
                zoom 0.23 yalign 0.1 xalign 0.0
        show fania kemeja_bicara at Transform(matrixcolor=(silhouette)):
                zoom 1.12 xalign 2.4
        with dissolve

        play music fania_bgm fadein 1.0

        anon "Ahhh, akhirnya selesai juga!"

        raden "Iya, capek banget."

        hide fania kemeja_bicara with dissolve

        show fania kemeja_bicara:
                zoom 1.12 xalign 2.4
        with dissolve
         
        anon "Duh.. Bikin kaget aja."

        raden "Hahaha, maaf ya."

        raden "Jadi ini rasanya kuliah, ya? Beda banget sama SMA. Orang-orangnya random banget."

        anon "Apalagi kalau lihat senior-senior tadi. Ada yang kayak serius banget, ada yang santai, ada juga yang humoris. Tapi seru sih."

        raden "Seru, sih. Tapi capeknya nggak bohong."

        anon "Haha, Yang penting sekarang waktunya pulang, mandi, terus rebahan."

        raden "Fix, setuju banget. Tapi besok kayaknya bakal tambah ribet deh, lihat dari list tugas yang tadi dikasih."

        anon "Iya, tugasnya... lumayan.. Tapi ya sudahlah, namanya juga PKKMB."

        anon "Oh iya.. kumpul kelompok dulu- Duluan ya!"

        hide fania kemeja_bicara with dissolve

        show raden with moveinleft:
                xalign 0.5

        "Perempuan itu pergi begitu saja tanpa memberi kesempatan untuk sekadar berkenalan."

        raden "Yasudahlah.. aku juga harus segera kumpul lalu pulang."

        "Setelah beberapa menit berdiskusi dengan kelompok tentang tugas, aku pulang dengan rasa lelah."

        scene black with dissolve
        with Pause(0.3)

        stop music fadeout 2.0

        jump prolog_day4_scene1

        return