init:
    transform flip:
        xzoom -1.0

label prolog_day3_scene2:
# [Scene 2]
# Latar : Auditorium
# Karakter: Raden, Aisyah, Santo, Sekar

    scene bg auditorium with dissolve:
        zoom 0.5

    show raden biasa with dissolve:
        zoom 0.23 xalign 0.5 yalign 0.1

    "{i}Untung saja tidak terlambat.{/i}"
    
    show raden with moveinleft:
        xalign -0.2
    
    #ekspresi aisyah normal tidak ada
    show aisyah kemeja_bicara with dissolve:
        zoom 0.34 xalign 0.9 yalign -1.0

    "Memasuki Auditorium, aku melihat kursi di sebelah Aisyah masih kosong, dan pergi duduk sebelahnya."
    
    show raden ngomong

    raden "\"Pagi Aisyah.\""
    
    show raden biasa

    voice "audio/vo/aisyah/prolog3/prolog3_1_eh_raden.flac"
    aisyah "\"Eh, Raden? Terlambat kamu?\""
    
    show raden ngomong

    raden "\"Iyanih, ketiduran aku.\""
    
    show raden biasa

    voice "audio/vo/aisyah/prolog3/prolog3_2_nggak_hanya_terlambat.flac"
    aisyah "\"Gak hanya terlambat, ada barang yang ketinggalan juga ya?\""
   
    show raden bingung

    raden "\"Kok tau??\""
    
    show aisyah kemeja_bingung

    voice "audio/vo/aisyah/prolog3/prolog3_3_keliatan_banget.flac"
    aisyah "\"Kelihatan banget itu, kamu pakai pita hitam.\""
    
    show raden ngomong

    raden "\"Hehe..\""
    
    show aisyah kemeja_bicara

    "Kami membahas beberapa hal, dari kenapa aku terlambat sampai perasaan apa saja yang kami alami pada dua hari PKKMB. Percakapan berjalan beberapa lama, sampai orang yang duduk di belakangku, menyebut namaku"
    
    show raden:
        xalign 0.5
    show aisyah:
        xalign 1.0
    with moveinright
    
    show santo kemeja_bicara with moveinleft:
        zoom 1.15 xalign -2.0 yalign 0.08
    
    santo "\"Raden?\""
    
    show raden biasa at flip with dissolve

    "Aku pun menoleh, kulihat Santo duduk di belakang ku. Kelopak mata nya terlihat menghitam, sepertinya dia juga merasa kelelahan karena mengerjakan tugasnya kemarin."
    
    show raden ngomong

    raden "\"Santo?\""
    
    show raden biasa
    show santo kemeja_bicara

    santo "\"Gimana den? Masih sehat kan?\""
    
    show raden ngomong
    show santo kemeja_biasa

    raden "\"Alhamdulillah, masih sehat. Meskipun masih terasa mengantuk sih.\""
    
    show raden biasa
    show santo kemeja_bicara

    santo "\"Btw, makasih ya den, telah membantu kami kemarin.\""
    
    show raden ngomong
    show santo kemeja_biasa

    raden "\"Hehe, aman. Jika kalian butuh bantuan lagi, panggil saja aku.\""
    
    show raden biasa
    
    voice "audio/vo/aisyah/prolog3/prolog3_4_kalian_juga_bisa.flac"
    aisyah "\"Kalian juga bisa panggil aku, jika butuh bantuan.\""
    
    show santo kemeja_bicara

    santo "\"Iya den, syah. Tapi ini masalah region kami, jadi nanti akan ku omongin ke LO ku untuk membahas masalah ini kedepannya.\""
    
    show santo kemeja_biasa

    "Aku dan Aisyah menggangguk dan aku memberi nya jari jempol."
    
    show raden ngomong
    show santo kemeja_bicara

    "Percakapan kami dengan Santo berjalan cukup lama, terkadang Aisyah juga mengikuti pembicaraan."
    
    show raden biasa
    show santo kemeja_biasa
    
    "Sampai akhirnya, pembawa materi datang dan aku berhenti bicara."
    
    show raden capek
    
    hide aisyah
    hide santo
    with dissolve

    stop music fadeout 2.0
    
    scene black with dissolve
    with Pause(0.2)

    "Aku mencoba fokus saja kepada materi dengan teliti dan mencatat poin poin penting yang diberikan, tapi aku masih merasa mengantuk akibat mengerjakan tugas kemarin. Lama kelamaan mataku terasa sangat berat. Yang membuat diriku akhirnya tertidur."

    sekar "\"....Mu.\""
    
    voice "audio/vo/sekar/prolog3/prolog3_1_hey_kamu.flac"
    sekar "\"Kamu!\""
    
    voice "audio/vo/aisyah/prolog3/prolog3_5_den_bangun.flac"
    aisyah "\"Den, bangun den!\""
    
    scene bg auditorium:
        zoom 0.5
    
    show raden bingung at flip:
        zoom 0.23 xalign 0.5 yalign 0.1
    
    show aisyah kemeja_gugup:
        zoom 0.34 xalign 1.0 yalign -1.0

    show sekar jas_teriak at flip:
        zoom 1.15 xalign -2.5 yalign 0.0
    with dissolve

    "Mendengar suara Aisyah, aku sontak terbangun dari tidurku. Aku melihat Aisyah yang menatapku dengan muka panik, dan LO region ku Kak Sekar yang memperhatikanku dengan muka yang terlihat agak kesal."

    voice "audio/vo/sekar/prolog3/prolog3_2_tidurnya_enak.flac"
    sekar "\"Tidurnya enak?\""
    
    play music intense fadein 1.0

    show raden capek with dissolve
    #show raden malu with dissolve

    raden "\"Maaf kak!\""

    voice "audio/vo/sekar/prolog3/prolog3_3_kemarin_ga_tidur.flac"
    sekar "\"Kemarin nggak tidur kah?\""

    raden "\"Maaf kak, gara gara tugas kemarin saya jadi tidur terlalu malam.\""

    voice "audio/vo/sekar/prolog3/prolog3_4_yaudah.flac"
    sekar "\"Yasudah, pergi cuci muka dulu sana.\""
    
    raden "\"Baik, kak.\""
    
    hide raden with dissolve
    
    jump prolog_day3_scene3
    
    return