label prolog2_scene3:
    #bg gamg
    scene bg lap_futsal:
        zoom 0.5
    #Suasana Netral in Home
    #Raden, Santo, Aisyah hilang
    #Fania muncul dingin    
    show fania kemeja_biasa with dissolve:
        zoom 1.1 xalign 0.5 yalign 0.0

    "Aku dan Aisyah mengikuti Santo menuju lokasi pertemuan Region Santo."

    "Sesampainya di sana, hanya ada perempuan berambut merah yang tadi sempat bertanya—dia sendirian, tanpa ada orang lain. Kartu namanya bertuliskan nama Fania, Nama itu seolah menjelaskan segalanya, memperkenalkan dirinya tanpa perlu banyak kata."

    #Fania hilang
    hide fania kemeja_biasa

    #Raden, Santo, Aisyah muncul netral
    with None
    show raden biasa:
        zoom 0.2 xalign 0.0 yalign 0.0
    show santo kemeja_biasa:
        zoom 1.0 xalign 1.7 yalign 0.006
    show aisyah kemeja_bicara:
        zoom 0.3 xalign 0.5 yalign 6.0
    with dissolve

    aisyah "Yang lain gak ada?"#Aku bertanya.

    show santo kemeja_bicara
    santo "Mereka langsung pulang, gak peduli sama penugasan hari ini." 

    #Aisyah kesal
    show aisyah kemeja_penasaran
    aisyah "Itu keterlaluan, gak mungkin kalian yang cuma dua orang bisa menyelesaikan tugas yang dikasih!" #Aisyah berseru.

    santo "Mau gimana lagi, temanku ini juga bukan tipe orang yang menuntut orang lain untuk kerja. Dia kelihatannya gak ada niatan untuk cari teman dan bakalan kerja sendirian saja." #ujar Santo.

    aisyah "Benar-benar gak bertanggung jawab!"#balas Aisyah. Aku bisa melihat api imajiner membara dibelakang tubuhnya. Itu mengerikan. Aku cukup yakin jika dia bertemu dengan anggota lain dari Region Santo, dia akan menghajar mereka saat ini juga.

    #Fania muncul dingin
    show raden:
        xalign -0.25
    show santo:
        xalign 2.25
    show aisyah:
        xalign 0.25
    show fania jas_biasa:
        zoom 1.1 xalign 1.4 yalign 0.0
    with moveinright

    show fania kemeja_bicara
    fania "Yang lain gk datang ya?, terus dua orang itu?"#Fania melihat kami, lalu bertanya kepada Santo  

    show santo kemeja_bicara
    santo "Kayak nya gitu deh, dan untuk dua orang ini-"#Santo menggaruk bagian belakang lehernya dan menghela nafas 

    #raden dan aisyah senyum
    show aisyah kemeja_senyum
    show raden senyum sadar
    rna "Kami datang untuk membantu!"#Ujarku dan Aisyah serentak.

    "Fania melihat Aisyah sebentar lalu melihat ku selama beberapa saat, sepertinya dia ingat pernah bertemu dengan ku kemarin, tapi memutuskan untuk tidak membahasnya."

    fania "Lalu kelompok kalian sendiri?"#Tanya Fania.

    raden "Udah aman kok"#jawabku dengan anggukan dan jempol terangkat.
    
    fania "Kalian gak perlu—"
    
    santo "Udah, biarin aja mereka. Tadi juga udah kutolak, tapi tetep maksa." #Sebelum Fania menyelesaikan kalimatnya, Santo menyela. 

    #Raden, Aisyah canggung
    show raden senyum sadar
    show aisyah kemeja_canggung
    "Akhirnya, kami berempat bekerja sama menyelesaikan tugas. Komunikasi kami awalnya terasa canggung, terutama saat berbicara dengan Fania, karena dia hanya menjawab singkat dan padat. Namun, meski hampir tengah malam, kami berhasil menyelesaikan semuanya."

    #Raden, Aisyah senyum
    show aisyah kemeja_senyum

    raden "Akhirnya Selesai!!!"# Teriak ku dengan pelan sambil merenggangkan badan.

    #Santo senyum
    santo "Terimakasih ya Raden, Aisyah"#Ujar Santo.

    fania "Kalian bisa diandalkan"#tambah Fania singkat

    aisyah "Senang bisa membantu!"#Aisyah tersenyum puas 

    "Setelah itu masing-masing dari kami berkemas lalu berjalan pulang ke arah yang berbeda."

    with None
    hide aisyah kemeja_senyum
    hide raden senyum sadar
    hide santo kemeja_bicara
    hide fania kemeja_bicara
    with dissolve
    
    show black with dissolve
    jump prolog2_scene4
