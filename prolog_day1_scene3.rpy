label prolog_day1_scene3:
    # [Scene 3]
    # Latar: Dalam Auditorium
    # Karakter: Raden, Aisyah, Sekar, dan Tessa
    scene bg auditorium with dissolve:
        zoom 0.5

    show raden kemeja_capek with dissolve:
        zoom 0.48 xalign 0.5 yalign 0.1

    "Di dalam Auditorium sangatlah penuh. Kurasa, sudah lebih dari 100 anak yang telah masuk ke ruangan ini."
    
    "Aku mencari tempat duduk yang kosong di sekitar teman satu region. Sayangnya, semuanya penuh kecuali dua kursi kosong yang barisan ketiga dari depan. Mau tidak mau aku dan Aisyah duduk disana."
    
    "Jam menunjukkan pukul 06.30. Layar di depan kami mulai memainkan video latar belakang berdirinya PENS."
    
    #nanti diubah narasinya

    show raden kemeja_menghela_napas with dissolve

    "Sayangnya, video yang diputar hanya tentang itu terus sampai beberapa waktu kemudian. Hal ini membuatku mengantuk karena kebosanan. Lama kelamaan mataku terasa sangat berat. Yang membuat diriku akhirnya tertidur."

    show black with dissolve

    "Seseorang mencubit lengan bajuku dengan pelan dan membangunkanku"

    scene bg auditorium with dissolve:
        zoom 0.5

    show raden kemeja_menghela_napas:
        zoom 0.48 xalign 0.0 yalign 0.1
    show aisyah kemeja_penasaran:
        zoom 0.35 xalign 0.85 yalign -0.7
    with dissolve
    
    voice "audio/vo/aisyah/pkkmb6_raden_jangan_tidur.mp3"
    aisyah "\"Raden, jangan tidur dong\""

    show raden kemeja_gugup with dissolve

    menu:
        "A-aku ga tidur kok!":
            jump scene4_choice1
        "E-eh, waduh maaf!":
            jump scene4_choice2

    return

label scene4_choice1:
    voice "audio/vo/aisyah/pkkmb7-1_hmmm.mp3"
    aisyah "\"HMMM?!!\""

    jump scene4_after_choice

label scene4_choice2:
    voice "audio/vo/aisyah/pkkmb7-2_hah.mp3"
    aisyah "\"Hah..\""

    jump scene4_after_choice

label scene4_after_choice:
    show raden kemeja_canggung

    voice "audio/vo/aisyah/pkkmb8_ayo_catet.mp3"
    aisyah "\"Ayo catet juga materinya\""

    show raden kemeja_gugup

    raden "\"I-iya, makasih Aisyah\""

    "Aku memperhatikan materi tersebut dengan seksama dan mencatat poin-poin penting dari materi yang ada"

    show raden kemeja_canggung

    # show sekar jas_bicara at Transform(matrixcolor=(silhouette)):
    #     zoom 0.78 xalign 0.1 yalign -0.2
    # with dissolve

    # lo1 "Kamu"

    # show aisyah kemeja_gugup with dissolve:
    #     zoom 0.25 xalign 0.8 yalign 0.8

    # aisyah "Den, bangun den!" # (Aisyah panik)

    # "Mendengar suara Aisyah, aku sontak terbangun dari tidurku. Aku melihat Aisyah yang menatapku dengan muka panik, dan seorang LO yang memperhatikanku dengan muka yang terlihat agak kesal."
    
    # show sekar jas_bicara with dissolve:
    #     zoom 0.78 xalign 0.1 yalign -0.2

    # "LO tersebut mempunyai kulit kecoklatan, dengan rambut unik berwarna hijau. LO itu pun bertanya."

    # hide aisyah with dissolve

    # show sekar jas_bicara with moveinleft:
    #     zoom 0.78 xalign 0.5 yalign -0.2

    # lo1 "Tidurnya enak?" # (Sekar marah)
    
    # raden "Maaf kak!" # (Raden malu)
    
    # lo1 "Kemarin nggak tidur kah?" # (Sekar marah)
    
    # raden "Maaf kak, karena terlalu semangat menunggu hari PKKMB jadinya saya tidur terlalu malam." # (Raden malu)
    
    # lo1 "Yasudah, pergi cuci muka dulu sana." # (Sekar marah)
    
    # raden "Baik, kak." # (Raden malu)

    # hide sekar with dissolve

    # "Mau tidak mau aku berdiri dari kursiku, dan pergi keluar ruangan. Tiba-tiba aku kepikiran, kalau aku lupa untuk bertanya arah menuju ke toilet. Untungnya di depan ruangan juga ada Panitia yang menjaga."
    
    # "Panitia yang menjaga di luar ada dua. Satu adalah pria dengan tubuh kekar dengan wajah yang galak dan satunya adalah seorang perempuan berambut merah dengan ujung rambutnya berwarna hitam."
    
    # "Ekspresi yang ditunjukkan perempuan tersebut juga lebih rileks dibandingkan dengan panitia pria satunya."
    
    # "Akupun menuju panitia tersebut, dan bertanya kepadanya."

    # raden "Permisi kak." # (Raden neutral)

    # "Tiba-tiba wajah agak kesal terlihat dari si panitia tersebut. Kemudian dia berkata."

    # show tessa normal with dissolve:
    #     zoom 0.27 xalign 0.5 yalign 1.5

    # lo2 "Apa?" # (Tessa marah)

    # raden "{i}Kenapa kakak ini tiba-tiba marah????{/i}" # (Raden bingung) ujarku dalam hati.

    # raden "Permisi kak, saya mau bertanya arah ke toilet dimana?" # (Raden panik)

    # "Melihat reaksi Raden, panitia tersebut menunjukkan senyuman. Dia kemudian berkata."

    # lo2 "Hahahaha, tidak perlu panik. Aku hanya bercanda sedikit. Untuk toilet kamu langsung saja ke lurus ke arah sana. Jika kamu memperhatikan dengan benar, kamu pasti akan menemukan toilet tersebut." # (Tessa tertawa)
    
    # raden "Baik, kak. Terimakasih" # (Raden neutral)

    # hide tessa with dissolve

    # "Tanpa pikir panjang aku langsung menuju ke arah yang ditunjukkan oleh si panitia. Dan menemukan toiletnya."
    # "Cuci muka telah kulakukan dan perasaaan segar kembali memenuhi diriku. Aku langsung menuju auditorium."
    # "Sesampainya di auditorium, tidak ada banyak yang terjadi. Hanya ada banyak materi yang dibagikan. Yang membuatku semakin mengantuk."

    stop music fadeout 2.0

    scene black with dissolve
    with Pause(0.2)

    jump prolog_day1_scene4

    return


