label chapter5_tessa_scene1:
    scene bg kamar_raden with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    
    play music raden_bgm fadein 1.0

    "Pagi hari, aku terbangunh oleh suara alarm dari ponselku. Jam di layar menunjukkan pukul 6.30."

    "Dengan setengah sadar, aku langsung menggenggam ponsel dan memeriksa notifikasinya. Setelah itu, aku bergegas mandi dan bersiap"

    play audio "audio/ReceiveText.ogg"

    "Tak lama notifikasi pesan grup muncul. Aku langsung membuka pesan tersebut"

    raden "\"Yah- ternyata endak jadi matkul pagi, kenapa harus sore sih, bikin malas aja\""

    raden "\"Tidur dulu aja, deh\""

    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    "Aku pun merebahkan diri di kasur dan terlelap dengan nyenyak. Ketika akhirnya terbangun, hari sudah sore, mendekati waktu kuliah yang kutunda tadi pagi."

    menu:
        "Ikut":
            jump chapter5_tessa_scene1_choice1_1
        "Bolos":
            jump chapter5_tessa_scene1_choice1_2

    return

label chapter5_tessa_scene1_choice1_1:
    scene bg kamar_raden with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kasual_biasa with moveinbottom:
        zoom raden_default.zoom
        xalign 0.5
        yalign raden_default.yalign

    raden "\"wah bentar lagi matkul, siap-siap dulu aja\""

    "Aku segera mengganti pakaian, merapikan diri, dan menyiapkan peralatan tulis. Saat sedang sibuk, notifikasi dari grup kelas muncul."

    "Pesannya meminta siapa saja yang belum hadir untuk segera datang, dan terlihat nama Raden dan Santo disebut dalam grup."

    raden_nvl "Oke, otw"
    santo_nvl "Aku malas endak bisa ikut"
    raden_nvl "Halah to, ayooooo"
    santo_nvl "Ogah, mending rebahan terus lanjut ngegame"

    nvl clear

    "Pesan dari Santo langsung memicu keributan di grup." 
    
    "Berbagai anggota kelas mencoba membujuknya. Akhirnya, setelah perdebatan singkat dan desakan dari beberapa teman, Santo menyerah dan memutuskan untuk ikut kelas"

    stop music fadeout 2.0

    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(0.3)

    #bg parkiran
    scene bg lapmer with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    play music campus fadein 1.0

    show raden kasual_biasa with moveinleft:
        zoom raden_default.zoom
        xalign 0.0
        yalign raden_default.yalign

    "Ketika aku sampai di depan kampus dan keluar parkiran, aku melihat Santo yang tampak sedikti ogah-ogahan. Aku menghampirinya dan menyapanya dengan senyum lebar."

    show santo kemeja_netral with dissolve:
        zoom santo_default.zoom
        yalign 0.08
        xalign 1.0

    raden "\"Begini kan bagus, hehehe\""

    santo "\"Terbaik apa coba, terbalik baru ada\""

    raden "\"hehehe, udah ayo\""

    jump chapter5_tessa_scene2

    return

label chapter5_tessa_scene1_choice1_2:
    scene bg kamar_raden with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kasual_menghela_napas with moveinbottom:
        zoom raden_default.zoom
        xalign 0.5
        yalign raden_default.yalign

    raden "{i}bentar lagi ada matkul, mau ikut, tapi... ahh, malas{/i}"

    raden "{i}apa nggak usah ikut aja ya? Ide bagus tuh{/i}"

    "Namun rencana itu mendadak terganggu oleh suara notifikasi ponsel. Pesan dari grup kelas muncul, meminta siapa saja yang belum hadir untuk segera datang."

    "Di dalam pesan itu, nama Raden dan Santo disebut secara khusus."

    raden_nvl "Maaf aku endak bisa ikut"
    santo_nvl "Kenapa??"
    raden_nvl "Engga dikasih pergi sama kasur ku"
    santo_nvl "Aku juga sama, ditahan sama kasur dan game ku"
    raden_nvl "Wah mantap, terbaik!"
    santo_nvl "Bener, terbaik!"

    nvl clear

    "Melihat percakapan itu, gtup kelas langsung heboh dengan komentar dan bujukan agar kami tetap ikut kelas. Keramaian ini rupanya berhasil melunakkan hati Raden dan Santo."

    "Akhirnya, dengan berat hati, kamu memutuskan untuk ikut."

    stop music fadeout 2.0

    scene black with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(0.3)

    play music campus fadein 1.0

    #bg parkiran
    scene bg lapmer with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kasual_capek with moveinleft:
        zoom raden_default.zoom
        xalign 0.0
        yalign raden_default.yalign

    "Ketika aku sampai di depan kampus dan keluar parkiran, aku melihat Santo yang tampak sedikit ogah-ogahan. Aku menghampirinya dan menyapanya"

    show santo kemeja_netral with dissolve:
        zoom santo_default.zoom
        yalign 0.08
        xalign 1.0
    show raden kasual_hehe:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Lihat tuh, akhirnya lo ikut juga, hahaha\""

    santo "\"Padahal lagi asyik ngegame\""

    raden "\"Iya, aku juga. Lagi enak-enaknya rebahan\""

    raden "\"Rasanya pengen langsung pulang aja, ya?\""

    santo "\"Iya, sama. Tapi... yaudah lah, ikut aja deh\""

    raden "\"Kau yakin ingin menghadapi penderitaan itu?\""

    santo "\"Jangan bilang begitu. Nggak lucu kalau kau yang mengucapkannya\""

    raden "\"Kalau gitu, aku pulang dulu ya\""

    santo "\"Oi, jangan langsung pergi!\""

    show raden kasual_panik:

        zoom raden_default.zoom
        yalign raden_default.yalign
    santo "\"Mari kita hadapi penderitaan ini bersama\""

    raden "\"Tii... {size=+10}TIDAKKKKK{/size}\"" with vpunch

    jump chapter5_tessa_scene2

    return 
