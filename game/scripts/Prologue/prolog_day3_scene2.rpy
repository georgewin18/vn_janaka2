init:
    transform flip:
        xzoom -1.0

label prolog_day3_scene2:
# [Scene 2]
# Latar : Auditorium
# Karakter: Raden, Aisyah, Santo, Sekar

    scene bg auditorium with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kemeja_gugup with dissolve:
        zoom raden_default.zoom
        xalign 0.45
        yalign raden_default.yalign

    "{i}Untung saja tidak terlambat.{/i}"
    
    show raden kemeja_canggung with moveinleft:
        zoom raden_default.zoom
        xalign -0.2
        yalign raden_default.yalign
    
    #ekspresi aisyah normal tidak ada
    show aisyah kemeja_senyum1 with dissolve:
        zoom aisyah_default.zoom
        xalign 1.0
        yalign aisyah_default.yalign

    "Memasuki Auditorium, aku melihat kursi di sebelah Aisyah masih kosong, dan pergi duduk sebelahnya."
    
    show raden kemeja_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Pagi Aisyah.\""
    
    show raden kemeja_biasa2:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show aisyah kemeja_terkejut:

        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    voice "audio/vo/aisyah/prolog3/prolog3_1_eh_raden.ogg"
    aisyah "\"Eh, Raden? Terlambat kamu?\""
    
    show raden kemeja_gugup:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Iyanih, ketiduran aku.\""
    
    show raden kemeja_biasa2:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show aisyah kemeja_senyum2:

        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    voice "audio/vo/aisyah/prolog3/prolog3_2_nggak_hanya_terlambat.ogg"
    aisyah "\"Gak hanya terlambat, ada barang yang ketinggalan juga ya?\""
   
    show raden kemeja_bingung:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Kok tau??\""
    
    show aisyah kemeja_senyum1:

        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    voice "audio/vo/aisyah/prolog3/prolog3_3_keliatan_banget.ogg"
    aisyah "\"Kelihatan banget itu, kamu pakai pita hitam.\""
    
    show raden kemeja_gugup:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Hehe..\""

    "Kami membahas beberapa hal, dari kenapa aku terlambat sampai perasaan apa saja yang kami alami pada dua hari PKKMB. Percakapan berjalan beberapa lama, sampai orang yang duduk di belakangku, menyebut namaku"
    
    show raden:
        xalign 0.55
        zoom raden_default.zoom
        yalign raden_default.yalign
    show aisyah:
        xalign 1.2
        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    with moveinright
    
    show santo kemeja_bicara with moveinleft:
        zoom santo_default.zoom
        xalign -0.25
    
    santo "\"Raden?\""
    
    show raden kemeja_biasa at flip with dissolve:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Aku pun menoleh, kulihat Santo duduk di belakang ku. Kelopak mata nya terlihat menghitam, sepertinya dia juga merasa kelelahan karena mengerjakan tugasnya kemarin."
    
    show raden kemeja_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Santo?\""
    
    show raden kemeja_biasa:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kemeja_bicara:

        zoom santo_default.zoom
    santo "\"Gimana den? Masih sehat kan?\""
    
    show raden kemeja_tersenyum:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kemeja_netral:

        zoom santo_default.zoom
    raden "\"Alhamdulillah, masih sehat. Meskipun masih terasa mengantuk sih.\""
    
    show raden kemeja_biasa:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kemeja_senyum_lebar:

        zoom santo_default.zoom
    santo "\"Btw, makasih ya den, telah membantu kami kemarin.\""
    
    show raden kemeja_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Hehe, aman. Jika kalian butuh bantuan lagi, panggil saja aku.\""
    
    show raden kemeja_biasa:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show aisyah kemeja_bersemangat:

        zoom aisyah_default.zoom
        yalign aisyah_default.yalign
    voice "audio/vo/aisyah/prolog3/prolog3_4_kalian_juga_bisa.ogg"
    aisyah "\"Kalian juga bisa panggil aku, jika butuh bantuan.\""
    
    show santo kemeja_senyum:

        zoom santo_default.zoom
    santo "\"Iya den, syah. Tapi ini masalah region kami, jadi nanti akan ku omongin ke LO ku untuk membahas masalah ini kedepannya.\""

    "Aku dan Aisyah menggangguk dan aku memberi nya jari jempol."
    
    show raden kemeja_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Percakapan kami dengan Santo berjalan cukup lama, terkadang Aisyah juga mengikuti pembicaraan."
    
    show raden kemeja_biasa:
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kemeja_netral:
    
        zoom santo_default.zoom
    "Sampai akhirnya, pembawa materi datang dan aku berhenti bicara."
    
    show raden kemeja_capek:
    
        zoom raden_default.zoom
        yalign raden_default.yalign
    hide aisyah
    hide santo
    with dissolve

    stop music fadeout 2.0
    
    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(0.2)

    "Aku mencoba fokus saja kepada materi dengan teliti dan mencatat poin poin penting yang diberikan, tapi aku masih merasa mengantuk akibat mengerjakan tugas kemarin. Lama kelamaan mataku terasa sangat berat. Yang membuat diriku akhirnya tertidur."

    sekar "\"....Mu.\""
    
    voice "audio/vo/sekar/prolog3/prolog3_1_hey_kamu.ogg"
    sekar "\"Kamu!\""
    
    voice "audio/vo/aisyah/prolog3/prolog3_5_den_bangun.ogg"
    aisyah "\"Den, bangun den!\""
    
    scene bg auditorium:
        size (config.screen_width, config.screen_height)
        truecenter
    with dissolve

    "Mendengar suara Aisyah, aku sontak terbangun dari tidurku. Aku melihat Aisyah yang menatapku dengan muka panik, dan LO region ku Kak Sekar yang memperhatikanku dengan muka yang terlihat agak kesal."

    show raden kemeja_gugup:
        xalign -0.2
        zoom raden_default.zoom
        yalign raden_default.yalign
    show sekar jas_teriak:
        xalign 1.0
        zoom sekar_default.zoom
        yalign sekar_default.yalign
    with dissolve

    voice "audio/vo/sekar/prolog3/prolog3_2_tidurnya_enak.ogg"
    sekar "\"Tidurnya enak?\""
    
    play music intense fadein 1.0

    show raden kemeja_capek with dissolve:
        zoom raden_default.zoom
        yalign raden_default.yalign
    #show raden malu with dissolve

    raden "\"Maaf kak!\""

    voice "audio/vo/sekar/prolog3/prolog3_3_kemarin_ga_tidur.ogg"
    sekar "\"Kemarin nggak tidur kah?\""

    raden "\"Maaf kak, gara gara tugas kemarin saya jadi tidur terlalu malam.\""

    voice "audio/vo/sekar/prolog3/prolog3_4_yaudah.ogg"
    sekar "\"Yasudah, pergi cuci muka dulu sana.\""
    
    raden "\"Baik, kak.\""
    
    hide raden with dissolve
    
    jump prolog_day3_scene3
    
    return
