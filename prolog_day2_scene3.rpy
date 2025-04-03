label prolog_day2_scene3:
    #bg gamg
    scene bg lap_futsal:
        zoom 0.5
    #Suasana Netral in Home
    #Raden, Santo, Aisyah hilang
    #Fania muncul dingin 
    show fania kemeja_dingin with dissolve:
        zoom 1.15 xalign 0.5 yalign -0.02

    "Aku dan Aisyah mengikuti Santo menuju lokasi pertemuan Region Santo."

    "Sesampainya di sana, hanya ada perempuan berambut merah yang tadi sempat bertanya—dia sendirian, tanpa ada orang lain. Kartu namanya bertuliskan nama Fania, Nama itu seolah menjelaskan segalanya, memperkenalkan dirinya tanpa perlu banyak kata."

    #Fania hilang
    hide fania kemeja_biasa with dissolve

    #Raden, Santo, Aisyah muncul netral
    show raden kemeja_serius:
        zoom 0.48 xalign -0.25 yalign 0.1
    show santo kemeja_biasa:
        zoom 1.15 xalign 3.5 yalign 0.08
    show aisyah kemeja_bicara:
        zoom 0.35 xalign 0.5 yalign -0.7
    with dissolve

    aisyah "\"Yang lain gak ada?\""#Aku bertanya.

    show santo kemeja_bicara
    santo "\"Mereka langsung pulang, gak peduli sama penugasan hari ini.\"" 

    #Aisyah kesal
    show santo kemeja_biasa
    show aisyah kemeja_penasaran

    voice "audio/vo/aisyah/prolog2/prolog2_5_itu_keterlaluan.flac"
    aisyah "\"Itu keterlaluan, gak mungkin kalian yang cuma dua orang bisa menyelesaikan tugas yang dikasih!\"" #Aisyah berseru.

    show santo kemeja_bicara

    santo "\"Mau gimana lagi, temanku ini juga bukan tipe orang yang menuntut orang lain untuk kerja. Dia kelihatannya gak ada niatan untuk cari teman dan bakalan kerja sendirian saja.\"" #ujar Santo.

    show santo kemeja_biasa

    voice "audio/vo/aisyah/prolog2/prolog2_6_gak_bertanggung_jawab.flac"
    aisyah "\"Benar-benar gak bertanggung jawab!\""#balas Aisyah. Aku bisa melihat api imajiner membara dibelakang tubuhnya. Itu mengerikan. Aku cukup yakin jika dia bertemu dengan anggota lain dari Region Santo, dia akan menghajar mereka saat ini juga.

    #Fania muncul dingin
    show raden:
        xalign -0.45
    show santo:
        xalign 2.0
    show aisyah:
        xalign 0.28
    show fania kemeja_dingin:
        zoom 1.15 xalign 1.5 yalign -0.02
    with moveinright

    voice "audio/vo/fania/prolog2/prolog2_1_yang_lain.flac"
    fania "\"Yang lain gk datang ya?, terus dua orang itu?\""#Fania melihat kami, lalu bertanya kepada Santo  

    $ renpy.show("santo kemeja_bicara", zorder=4)
    santo "\"Kayak nya gitu deh, dan untuk dua orang ini-\""#Santo menggaruk bagian belakang lehernya dan menghela nafas 

    #raden dan aisyah senyum
    show santo kemeja_biasa
    show aisyah kemeja_senyum
    show raden kemeja_tersenyum
    
    voice "audio/vo/aisyah/prolog2/prolog2_7_kami_datang.flac"
    rna "\"Kami datang untuk membantu!\""#Ujarku dan Aisyah serentak.

    "Fania melihat Aisyah sebentar lalu melihat ku selama beberapa saat, sepertinya dia ingat pernah bertemu dengan ku kemarin, tapi memutuskan untuk tidak membahasnya."

    voice "audio/vo/fania/prolog2/prolog2_2_lalu_kelompok_kalian.flac"
    $ renpy.show("fania kemeja_dingin", zorder=5)
    fania "\"Lalu kelompok kalian sendiri?\""#Tanya Fania.

    raden "\"Udah aman kok\""#jawabku dengan anggukan dan jempol terangkat.
    
    show raden kemeja_biasa

    voice "audio/vo/fania/prolog2/prolog2_3_kalian_nggak_perlu.flac"
    fania "\"Kalian gak perlu—\""
    
    $ renpy.show("santo kemeja_bicara", zorder=6)
    santo "\"Udah, biarin aja mereka. Tadi juga udah kutolak, tapi tetep maksa.\"" #Sebelum Fania menyelesaikan kalimatnya, Santo menyela. 

    #Raden, Aisyah canggung
    show santo kemeja_biasa
    show raden kemeja_tersenyum
    show aisyah kemeja_bicara
    "Akhirnya, kami berempat bekerja sama menyelesaikan tugas. Komunikasi kami awalnya terasa canggung, terutama saat berbicara dengan Fania, karena dia hanya menjawab singkat dan padat. Namun, meski hampir tengah malam, kami berhasil menyelesaikan semuanya."

    #Raden, Aisyah senyum
    show aisyah kemeja_senyum

    $ renpy.show("raden kemeja_tersenyum", zorder=7)
    raden "\"Akhirnya Selesai!!!\""# Teriak ku dengan pelan sambil merenggangkan badan.

    #Santo senyum
    show santo kemeja_bicara
    santo "\"Terimakasih ya Raden, Aisyah\""#Ujar Santo.

    $ renpy.show("fania kemeja_dingin", zorder=7)
    voice "audio/vo/fania/prolog2/prolog2_4_kalian_bisa_diandalkan.flac"    
    fania "\"Kalian bisa diandalkan\""#tambah Fania singkat

    $ renpy.show("aisyah kemeja_senyum", zorder=8)
    voice "audio/vo/aisyah/prolog2/prolog2_8_senang_bisa_membantu.flac"
    aisyah "\"Senang bisa membantu!\""#Aisyah tersenyum puas 

    "Setelah itu masing-masing dari kami berkemas lalu berjalan pulang ke arah yang berbeda."

    hide aisyah
    hide raden
    hide santo
    hide fania
    with dissolve

    show black with dissolve

    jump prolog_day2_scene4