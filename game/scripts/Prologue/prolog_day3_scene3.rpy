init:
    transform flip:
        xzoom -1.0
    transform flipback:
        xzoom 1.0
        
label prolog_day3_scene3:
# [Scene 3]
# Latar : Depan Auditorium, Lorong D4
# Karakter: Raden, Tessa

    scene bg depan_auditorium with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kemeja_capek with dissolve:
        zoom raden_default.zoom
        xalign 0.45
        yalign raden_default.yalign

    "Mau tidak mau aku berdiri dari kursi ku, dan pergi keluar ruangan."
    
    show raden kemeja_bingung with dissolve:
    
        zoom raden_default.zoom
        yalign raden_default.yalign
    "Tiba-tiba aku kepikiran, kalau aku lupa untuk bertanya arah menuju ke toilet."
    
    show raden kemeja_biasa2 with dissolve:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Untung nya di depan ruangan juga ada Panitia yang menjaga. Panitia yang menjaga di luar ada dua. Satu adalah pria dengan tubuh kekar dengan wajah yang galak dan satunya adalah seorang perempuan berambut merah dengan ujung rambutnya berwarna hitam."
    "Ekspresi yang ditunjukkan perempuan tersebut juga lebih rileks dibandingkan dengan panitia pria satunya."

    "Akupun menuju panitia tersebut, dan bertanya kepadanya."
    
    stop music fadeout 2.0

    show raden with moveinleft:
        xalign -0.2
    
        zoom raden_default.zoom
        yalign raden_default.yalign
    show tessa jas_serius with dissolve:
        xalign 1.0
        yalign tessa_default.yalign
    
        zoom tessa_default.zoom
    show raden kemeja_tersenyum:
    
        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Permisi kak.\""
    
    play music tessa_bgm fadein 1.0

    #ekspresi tessa bicara dan marah tidak ada
    voice "audio/vo/tessa/prolog3/prolog3_1_apa.ogg"

    show tessa jas_kesal:
        zoom tessa_default.zoom
        yalign tessa_default.yalign
    lo "\"Apa?\""#tessa kesal
    
    show raden kemeja_gugup with dissolve:
        zoom raden_default.zoom
        yalign raden_default.yalign
    #show raden gugup with dissolve
    
    "{i}Kenapa kakak ini tiba-tiba marah?{/i}"

    raden "\"Permisi kak, saya mau bertanya arah ke toilet dimana?\""

    show tessa jas_serius:
        zoom tessa_default.zoom
        yalign tessa_default.yalign
    voice "audio/vo/tessa/prolog3/prolog3_2_toilet.ogg"
    lo "\"Toilet? Langsung aja lurus ke arah sana. Kalau kamu perhatikan dengan benar, pasti akan ketemu.\""
    
    show raden kemeja_biasa2 with dissolve:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Aku tidak mendengarkan nya dengan baik karena tadi sedang panik, Tapi kakak panitia itu sudah kelihatan cukup kesal, aku takut akan dimarahi jika memintanya untuk mengulang."
    
    show raden kemeja_bingung with dissolve:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "{i}Tadi kayaknya dia bilangnya lurus aja ya?{/i}"

    menu:
        "Gk usah tanya lagi deh, harusnya tinggal lurus saja pasti kelihatan nanti.":
            show raden kemeja_biasa2:
                zoom raden_default.zoom
                yalign raden_default.yalign
            with dissolve
            
            raden "\"Baik kak. Terimakasih\""
            
            hide tessa with dissolve
            show raden with moveinleft:
                xalign 0.5

                zoom raden_default.zoom
                yalign raden_default.yalign
            "Aku berjalan lurus sesuai yang dikatakan oleh panitia tadi. Dengan langkah penuh harapan, aku menyusuri lorong-lorong yang tampak seragam. Namun, setelah beberapa menit berjalan, aku tidak juga menemukan keberadaan toilet."
            
            show raden kemeja_bingung with dissolve:

                zoom raden_default.zoom
                yalign raden_default.yalign
            "{i}Kok gak ada ya? Harusnya tadi aku tanya saja ke panitia tadi…{/i}"
            
            show raden kemeja_capek with dissolve:

                zoom raden_default.zoom
                yalign raden_default.yalign
            "Akhirnya, dengan sedikit ragu, aku memutuskan untuk kembali ke ruangan tempat dua panitia tadi berjaga. Tidak ada pilihan lain selain bertanya lagi pada perempuan dengan rambut merah gradasi itu. Meski hatiku sedikit gentar, teringat responnya yang dingin sebelumnya."

            raden "\"Permisi, Kak…\""#Raden canggung
            
            show raden with moveinleft:
                xalign -0.2
            
                zoom raden_default.zoom
                yalign raden_default.yalign
            show tessa jas_serius with dissolve:
                xalign 1.0
                yalign tessa_default.yalign
            
                zoom tessa_default.zoom
            show raden kemeja_gugup with dissolve:

                zoom raden_default.zoom
                yalign raden_default.yalign
            voice "audio/vo/tessa/prolog3/prolog3_3_apa_lagi.ogg"
            lo "\"Ada apa lagi?\""
            
            show raden kemeja_canggung with dissolve:
            
                zoom raden_default.zoom
                yalign raden_default.yalign
            "Aku menggaruk belakang kepala sambil tersenyum kaku."
            
            show raden kemeja_gugup:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Maaf, Kak. Saya masih belum bisa menemukan toiletnya… Bisa tolong tunjukkan lagi arahnya?\""

        "Lebih baik tanya aja deh, daripada tersesat nanti.":
            show raden kemeja_gugup with dissolve:
            
                zoom raden_default.zoom
                yalign raden_default.yalign
            "Aku menggaruk belakang kepala sambil tersenyum kaku."
            
            raden "\"Maaf, Kak. Saya masih kurang paham tadi toilet nya di sebelah mana…. Bisa tolong tunjukkan lagi arahnya?\""

    show tessa jas_nafas with dissolve:

        zoom tessa_default.zoom
        yalign tessa_default.yalign
    pause 0.4

    show tessa jas_kesal with dissolve:

        zoom tessa_default.zoom
        yalign tessa_default.yalign
    voice "audio/vo/tessa/prolog3/prolog3_4_ya_ampun.ogg"
    lo "\"Ya ampun… Kamu ini dibilangin tadi, lurus aja! Perhatikan baik-baik!\""
    
    show tessa with moveinright:
        xalign 2.0
        zoom tessa_default.zoom
        yalign tessa_default.yalign
    show raden at flip with moveinright:
        xalign 0.5
        zoom raden_default.zoom
        yalign raden_default.yalign
    with dissolve
    
    #raden gugup
    show raden kemeja_biasa2 at flip with dissolve:
    
        zoom raden_default.zoom
        yalign raden_default.yalign
    "Aku hanya bisa mengangguk, sembari perlahan melangkah pergi"
    
    show raden with moveinright:
        xalign 1.2
    
        zoom raden_default.zoom
        yalign raden_default.yalign
    show tessa jas_serius with moveinright:
        xalign 0.0
    
        zoom tessa_default.zoom
        yalign tessa_default.yalign
    #raden terkejut
    show raden kemeja_kaget:
    
        zoom raden_default.zoom
        yalign raden_default.yalign
    "Namun dia tiba-tiba berjalan mendahuluiku."

    voice "audio/vo/tessa/prolog3/prolog3_5_sudahlah.ogg"
    lo "\"Sudahlah, ikut aku. Kalau gak, nanti malah kamu hilang.\""
    
    show raden kemeja_biasa2:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Aku mengikutinya dalam diam. Langkahnya cepat dan mantap, seperti seseorang yang terbiasa menyelesaikan tugas tanpa keraguan."
    
    "Kami berjalan tanpa sepatah kata, sementara suasana di antara kami terasa canggung dan hening."
    
    show tessa at flip with dissolve:

        zoom tessa_default.zoom
        yalign tessa_default.yalign
    pause 1

    show tessa at flipback with dissolve:
    
        zoom tessa_default.zoom
        yalign tessa_default.yalign
    "Sesekali, dia melirik ke belakang untuk memastikan aku masih mengikutinya, tetapi tidak berkata apa-apa. "
    
    #scene bg depan_toilet with dissolve

    "Setelah beberapa menit berjalan, akhirnya kami sampai di depan toilet."
    
    show tessa at flip with dissolve:

        zoom tessa_default.zoom
        yalign tessa_default.yalign
    voice "audio/vo/tessa/prolog3/prolog3_6_nah_ini.ogg"
    lo "\"Nah, ini. Lain kali buka matanya lebih lebar, ya,\""
    
    "Dia menunjuk pintu toilet dengan sedikit sentakan tangan."

    raden "\"Terima kasih, Kak,\""#dengan nada setulus mungkin, meskipun aku merasa masih ada tekanan dari sikapnya.
    
    hide tessa with dissolve
    
    show raden with moveinright:
        xalign 0.5

        zoom raden_default.zoom
        yalign raden_default.yalign
    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(0.3)
    
    centered "Aku masuk ke toilet, merasa lega akhirnya menemukannya."

    jump prolog_day3_scene4

    return
