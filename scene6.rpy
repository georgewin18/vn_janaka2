label scene6:

        "Waktu terasa berlalu begitu cepat. Hari pertama PKKMB sudah hampir selesai. Setelah Auditorium, para mahasiswa baru diminta menuju Lapangan Basket."

        "Di sana, kami menerima tugas yang harus segera dikumpulkan sebelum akhirnya diperbolehkan pulang."


        show bg lap_futsal:
                zoom 0.5 
        with dissolve

        show fania kemeja_bicara at Transform(matrixcolor=(silhouette)):
                anchor (-0.45, -0.05) zoom 0.7 
        with dissolve

        anon "Ahhh, akhirnya selesai juga!"

        raden "Iya, capek banget."

        hide fania kemeja_bicara with dissolve

        show fania kemeja_bicara:
                anchor (-0.45, -0.05) zoom 0.7 
        with dissolve

        show fania kemeja_bicara:
                anchor (-0.45, -0.05) zoom 0.7 
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

        "Perempuan itu pergi begitu saja tanpa memberi kesempatan untuk sekadar berkenalan."

        raden "Yasudahlah.. aku juga harus segera kumpul lalu pulang."

        "Setelah beberapa menit berdiskusi dengan kelompok tentang tugas, aku pulang dengan rasa lelah."

        scene black with dissolve
        with Pause(0.3)

        $ quick_menu = False
        centered "{i}To be continued...{/i}"
        with Pause(1)

        return