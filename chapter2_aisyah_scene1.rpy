label chapter2_aisyah_scene1:
  
    scene black with dissolve
    with Pause(0.2)

    "Minggu kedua perkuliahan setelah PKKMB selesai. Aku masih berusaha beradaptasi dengan ritme kehidupan kampus yang terasa jauh lebih nyata dibandingkan minggu pengenalan."
    
    "Kalau di PKKMB semuanya seru dengan yel-yel dan acara formal, minggu ini penuh dengan tugas, laporan, dan dosen yang tidak segan-segan memberikan pekerjaan rumah bertumpuk."

    "Semalam, aku begadang mengerjakan laporan praktikum pertama. Bukan karena laporannya sulit, tapi karena aku terlalu santai di siang hari, berpikir punya banyak waktu."
    
    "Akibatnya, aku harus menantang mata untuk tetap terbuka sampai larut malam."
    
    "Pagi harinya, alarm yang kupasang dengan harapan besar malah tidak berguna. Aku terbangun dengan panik, melihat jam menunjukkan pukul 07.40."
    
    scene bg kamar_raden with dissolve:
        zoom 0.5

    show raden bingung with dissolve:
        zoom 0.23 xalign 0.5 yalign 0.1
    
    raden "\"Waduh telat nih bisa-bisa aku!\""

    scene bg lorong_kampus with dissolve:
        zoom 0.5

    show raden capek with dissolve:
        zoom 0.23 xalign 0.5 yalign 0.1

    raden "\"Kenapa kelasnya harus jauh sekali sih hari ini!?\""

    "Napasku mulai terasa berat."

    raden "\"Di lantai tiga pula. D302 di mana, ya?\""

    "Aku terus berpikir keras sambil mencoba mengingat denah gedung ini. Semakin panik, aku bergumam lagi."

    raden "\"Kayaknya hari ini aku bakal telat—\""

    #Suara tabrakan terdengar. 
    
    #Flash hitam setengah detik.
    
    scene black with dissolve
    with Pause(0.5)
    
    scene bg lorong_kampus with dissolve:
        zoom 0.5

    show raden capek with dissolve:
        zoom 0.23 xalign 0.5 yalign 0.1

    show raden with moveinleft:
        xalign -0.2
    
    "Sebuah benturan menghentikan langkahku. Aku oleng ke belakang, dan saat itu juga terdengar suara benda jatuh berserakan di lantai."
    
    raden "\"Aduh!\""
    
    #raden malu
    
    "Seruku spontan. Aku melihat ke arah orang yang kutabrak. Wajahku langsung memanas."
    
    raden "\"Aisyah?!\""
    
    show aisyah kemeja_penasaran with dissolve:
        zoom 0.34 xalign 0.9 yalign -1.0
    
    "Dia terduduk di lantai dengan ekspresi kaget dan kesal, sementara buku-bukunya berserakan di sekelilingnya. Aku berdiri mematung, bingung harus apa."

    aisyah "\"Raden?! Lihat-lihat dong kalau jalan!\""
    
    #raden panik
    
    raden "\"Eh, maaf, maaf banget! Aku nggak sengaja. Aku buru-buru soalnya…\""
    
    "Aku melirik ke barang-barangnya yang berantakan di lantai."
    
    raden "\"Barangmu berantakan semua… —Eh, tapi udah jam segini!\""
    
    "Aku melihat jam di HP ku, kalau aku tidak lari ke kelas sekarang juga sudah pasti aku akan telat."
    
    menu:
        "Menolong Aisyah":
            "Kelas memang sebentar lagi dimulai, tapi rasanya tidak enak kalau membiarkan Aisyah memungut semua barangnya kembali sendirian."
            
            "Sambil jongkok dan mulai memungut bukunya, aku terus merasa bersalah."

            raden "\"Sumpah, maaf banget, Aisyah. Aku beneran nggak sengaja.\""
            
            #aisyah netral
            
            show aisyah kemeja_bicara

            "Dia menghela napas panjang, menahan kekesalannya."

            raden "\"Ini, semoga nggak ada yang rusak.\""
            
            "Dia memeriksa buku-bukunya satu per satu, lalu menatapku dengan ekspresi campuran antara kesal dan pasrah"

            aisyah "\"Lain kali hati-hati, ya. Jangan asal lari di lorong. Memangnya kenapa kamu buru-buru, sih?\""

            raden "\"Iya, iya. Maaf banget, Ais. Sebenarnya… mepet ke kelas sih ini—\""

            aisyah "\"Lah, ya sudah cepat sana.\""
            
            "Setelah memberikan buku dan lembaran terakhir milik Aisyah, aku segera melanjutkan berlari menuju kelas."
            
            "Namun masih terdengar olehku suara Aisyah yang semakin menjauh dari pandangan."
            
            aisyah "\"Makasih juga ya kamu masih nyempatin bantu!\""

            hide aisyah
            
            show raden with moveinright:
                xalign 0.5
            
            #bg kelas d4
            
            #raden gugup
            show raden biasa
            
            "Sesampainya di kelas, Dosen sudah datang dan mengajar, aku di suruh menunggu di luar sebentar, sampai akhirnya setelah diperbolehkan masuk kelas, aku di tegur dan tidak boleh sampai mengulangi nya lagi."
            
            scene black with dissolve
            with Pause(0.2)

            jump chapter2_aisyah_scene1_choice1_1

        "Langsung Menuju Kelas":
            raden "\"Eh, maaf banget Aisyah, lagi buru-buru—\""

            "Terpaksa kutinggal Aisyah sendirian, daripada terlambat kelas."
            
            raden "{i}—Maaf Aisyah{/i}"
            
            hide aisyah
            
            show raden with moveinright:
                xalign 0.5
            
            show raden biasa
            
            "Untung nya sesampai di kelas, dosen nya juga baru datang. Aku menghela nafas lega."
            
            "Selamat…"
            
            scene black with dissolve
            with Pause(0.2)
            
            jump chapter2_aisyah_scene1_choice1_2

    return

label chapter2_aisyah_scene1_choice1_1:
    scene bg kantin with dissolve:
        zoom 0.5

    show raden biasa with dissolve:
        zoom 0.2 xalign 0.0 yalign 0.0

    show santo kemeja_biasa with dissolve:
        zoom 1.15 xalign 2.0 yalign 0.08

    raden "\"Akhirnya waktu istirahat juga.\""

    "Setelah kelas yang melelahkan—apalagi tadi sempat terlambat, akhirnya aku membeli makan di kantin bersama Santo."
    
    "Sampai tak sengaja kulihat Aisyah yang melintas tepat di depan kami. Mungkin aku harus meminta maaf lagi atas peristiwa tadi pagi?"

    raden "\"Santo, ku nyamperin Aisyah dulu, ya?\""
    
    show santo jahil

    santo "\"Ini masih awal Kuliah lo, udah naksir cewek aja nih!\""

    raden "\"Nggak gitu woy, pagi tadi aku sempat buat salah sama dia.\""

    santo "\"Walah yaudah, samperin sana. Aku cari tempat duduk dulu aja\""

    raden "\"Oke oke, ty.\""

    hide santo
    
    "Akhirnya aku mendekati Aisyah, yang baru saja memesan makanan."

    show aisyah kemeja_bicara with dissolve:
        zoom 0.2 xalign 0.8 yalign 0.0

    raden "\"Aisyah...\""

    aisyah "\"Kenapa, Den?\""

    raden "\"Maaf ya tadi pagi.\""

    aisyah "\"Udah nggak apa, kan kamu dah bantu tadi.\""

    aisyah "\"Terus gimana kelasnya? Aman?\""

    raden "\"Yah…, telat sih.\""
    
    aisyah "\"Lah, terus?\""

    raden "\"..Cuma perlu ngurus ke BAAK kok nanti.\""

    jump chapter2_aisyah_scene2

label chapter2_aisyah_scene1_choice1_2:
    scene bg kantin with dissolve:
        zoom 0.5

    show raden biasa with dissolve:
        zoom 0.2 xalign 0.0 yalign 0.0

    show santo kemeja_biasa with dissolve:
        zoom 1.15 xalign 2.0 yalign 0.08

    raden "\"Akhirnya waktu istirahat juga.\""

    "Setelah kelas yang melelahkan—apalagi tadi sempat terlambat, akhirnya aku membeli makan di kantin bersama Santo."
    
    "Sampai tak sengaja kulihat Aisyah yang melintas tepat di depan kami. Mungkin aku harus meminta maaf lagi atas peristiwa tadi pagi?"

    raden "\"Santo, ku nyamperin Aisyah dulu, ya?\""
    
    show santo jahil

    santo "\"Ini masih awal Kuliah lo, udah naksir cewek aja nih!\""

    raden "\"Nggak gitu woy, pagi tadi aku sempat buat salah sama dia.\""

    santo "\"Walah yaudah, samperin sana. Aku cari tempat duduk dulu aja\""

    raden "\"Oke oke, ty.\""

    hide santo
    
    "Akhirnya aku mendekati Aisyah, yang baru saja memesan makanan."

    show aisyah kemeja_bicara with dissolve:
        zoom 0.34 xalign 0.9 yalign -1.0

    raden "\"Aisyah...\""

    aisyah "\"Kenapa, Den?\""

    raden "\"Maaf ya tadi pagi.\""
    
    "Aisyah menghela nafas, mencoba bersabar."

    aisyah "\"Lain kali hati-hati, dong\""

    aisyah "\"Emangnya kamu buru-buru kenapa, sih\""

    raden "\"Mepet kelas sih tadi.\""
    
    aisyah "\"Terus gimana kelasnya? Aman?\""

    raden "\"Aman sih, akhirnya.\""

    jump chapter2_aisyah_scene2

    return
