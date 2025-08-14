init:
    transform flip:
        xzoom -1.0

label prolog_day3_scene2:
# [Scene 2]
# Latar : Auditorium
# Karakter: Raden, Aisyah, Santo, Sekar

    scene bg auditorium with dissolve:
        zoom 0.5

    show raden kemeja_gugup with dissolve:
        zoom 0.54 xalign 0.45 yalign 0.05

    "{i}Untung saja tidak terlambat.{/i}"
    
    show raden kemeja_canggung with moveinleft:
        zoom 0.54 xalign -0.2 yalign 0.05
    
    #ekspresi aisyah normal tidak ada
    show aisyah kemeja_senyum1 with dissolve:
        zoom 0.4 xalign 1.0 yalign 0.1

    "Memasuki Auditorium, aku melihat kursi di sebelah Aisyah masih kosong, dan pergi duduk sebelahnya."
    
    show raden kemeja_tersenyum

    raden "\"Pagi Aisyah.\""
    
    show raden kemeja_biasa2
    show aisyah kemeja_terkejut

    voice "audio/vo/aisyah/prolog3/prolog3_1_eh_raden.flac"
    aisyah "\"Eh, Raden? Terlambat kamu?\""
    
    show raden kemeja_gugup

    raden "\"Iyanih, ketiduran aku.\""
    
    show raden kemeja_biasa2
    show aisyah kemeja_senyum2

    voice "audio/vo/aisyah/prolog3/prolog3_2_nggak_hanya_terlambat.flac"
    aisyah "\"Gak hanya terlambat, ada barang yang ketinggalan juga ya?\""
   
    show raden kemeja_bingung

    raden "\"Kok tau??\""
    
    show aisyah kemeja_senyum1

    voice "audio/vo/aisyah/prolog3/prolog3_3_keliatan_banget.flac"
    aisyah "\"Kelihatan banget itu, kamu pakai pita hitam.\""
    
    show raden kemeja_gugup

    raden "\"Hehe..\""

    "Kami membahas beberapa hal, dari kenapa aku terlambat sampai perasaan apa saja yang kami alami pada dua hari PKKMB. Percakapan berjalan beberapa lama, sampai orang yang duduk di belakangku, menyebut namaku"
    
    show raden:
        xalign 0.55
    show aisyah:
        xalign 1.2
    with moveinright
    
    show santo kemeja_bicara with moveinleft:
        zoom 0.37 xalign -0.25
    
    santo "\"Raden?\""
    
    show raden kemeja_biasa at flip with dissolve

    "Aku pun menoleh, kulihat Santo duduk di belakang ku. Kelopak mata nya terlihat menghitam, sepertinya dia juga merasa kelelahan karena mengerjakan tugasnya kemarin."
    
    show raden kemeja_tersenyum

    raden "\"Santo?\""
    
    show raden kemeja_biasa
    show santo kemeja_bicara

    santo "\"Gimana den? Masih sehat kan?\""
    
    show raden kemeja_tersenyum
    show santo kemeja_netral

    raden "\"Alhamdulillah, masih sehat. Meskipun masih terasa mengantuk sih.\""
    
    show raden kemeja_biasa
    show santo kemeja_senyum_lebar

    santo "\"Btw, makasih ya den, telah membantu kami kemarin.\""
    
    show raden kemeja_tersenyum

    raden "\"Hehe, aman. Jika kalian butuh bantuan lagi, panggil saja aku.\""
    
    show raden kemeja_biasa
    show aisyah kemeja_bersemangat

    voice "audio/vo/aisyah/prolog3/prolog3_4_kalian_juga_bisa.flac"
    aisyah "\"Kalian juga bisa panggil aku, jika butuh bantuan.\""
    
    show santo kemeja_senyum

    santo "\"Iya den, syah. Tapi ini masalah region kami, jadi nanti akan ku omongin ke LO ku untuk membahas masalah ini kedepannya.\""

    "Aku dan Aisyah menggangguk dan aku memberi nya jari jempol."
    
    show raden kemeja_tersenyum

    "Percakapan kami dengan Santo berjalan cukup lama, terkadang Aisyah juga mengikuti pembicaraan."
    
    show raden kemeja_biasa
    show santo kemeja_netral
    
    "Sampai akhirnya, pembawa materi datang dan aku berhenti bicara."
    
    show raden kemeja_capek
    
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
    
    show raden kemeja_gugup at flip:
        zoom 0.54 xalign 0.55 yalign 0.05
    
    show aisyah kemeja_serius:
        zoom 0.4 xalign 1.35 yalign 0.1

    show sekar jas_teriak at flip:
        zoom 1.25 xalign -0.25 yalign 0.05
    with dissolve

    "Mendengar suara Aisyah, aku sontak terbangun dari tidurku. Aku melihat Aisyah yang menatapku dengan muka panik, dan LO region ku Kak Sekar yang memperhatikanku dengan muka yang terlihat agak kesal."

    voice "audio/vo/sekar/prolog3/prolog3_2_tidurnya_enak.flac"
    sekar "\"Tidurnya enak?\""
    
    play music intense fadein 1.0

    show raden kemeja_capek with dissolve
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