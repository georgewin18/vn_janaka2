label pensasi_tessa_scene3:
    show raden kasual_canggung

    "Dia menatapku sebentar, lalu merogoh kantongnya dan mengeluarkan sebuah kaleng minuman dingin."

    dio "\"Nih\""

    show raden kasual_bingung

    "Aku menatap minuman itu dengan bingung."

    show raden kasual_gugup with dissolve

    raden "\"Eh? Buat aku kak?\""

    dio "\"Ya buat siapa lagi?!\""

    show raden kasual_canggung

    dio "\"Gua udah denger dari Tessa, tadi lo juga udah kerja keras. Anggap aja bonus.\""

    "Aku ragu-ragu sebelum akhirnya menerimanya. Saat kaleng dingin itu menyentuh tanganku, aku bisa merasakan betapa segarnya setelah bekerja keras seharian."

    show raden kasual_biasa with dissolve
    
    raden "\"Makasih kak\""

    "Aku hendak membuka minumannya ketika Kak Dio tiba-tiba berdehem kecil."

    show raden kasual_biasa2

    dio "\"Eh, soal yang masalah rokok dulu itu...\""

    dio "\"Ya... gue tau gue rada nyebelin waktu itu,\""

    dio "\"Yah... yang jelas, gue nggak ada niat buat bikin masalah gede. Tadi di kampus juga... ya lo tau lah, kadang gue suka kelewatan,\""

    raden "\"Iya, iya. Aku ngerti kak. Makasih udah bilang gitu.\""

    "Kak Dio mendengus, lalu meneguk minumannya"

    dio "\"Bagus,\""

    show raden with moveinright:
        xalign 0.0
    show tessa normal with dissolve:
        zoom 0.39 yalign -0.25 xalign 0.95

    "Saat itu, aku melirik ke arah Kak Tessa yang duduk tak jauh dari kami. Dia tidak ikut campur, hanya duduk sambil tersenyum tipis, memandangi interaksi kami dengan ekspresi puas."

    "Aku menghabiskan tegukan terakhir dari minuman yang Kak Dio berikan. Dingin dan menyegarkan, mengusir sedikit rasa lelah yang menempel setelah seharian menjaga booth. Suasana sudah jauh lebih tenang dibandingkan sebelumnya."

    menu:
        "Kembali menemui Aisyah dan Fania":
            jump pensasi_tessa_scene3_choice3_1
        "Ajak jalan-jalan":
            jump pensasi_tessa_scene3_choice3_2

    return

label pensasi_tessa_scene3_choice3_1:
    show raden kasual_biasa

    raden "\"Fyuhh... kalau gitu aku balik ya kak\""

    voice "audio/vo/tessa/pensasi/pensasi_3_1_1_terima_kasih.flac"
    tessa "\"Terima kasih ya udah bantu\""

    show raden kasual_tersenyum

    raden "\"Aman kak, udah biasa teman menolong teman\""

    voice "audio/vo/tessa/pensasi/pensasi_3_1_2_oke.flac"
    tessa "\"Oke, hati-hati ya\""

    show raden kasual_ceria

    raden "\"Oke, makasih, bye\""

    voice "audio/vo/tessa/pensasi/pensasi_3_1_3_bye.flac"
    tessa "\"Bye\""

    scene black with dissolve
    with Pause(0.3)

    scene bg depan_auditorium with dissolve:
        zoom 0.5

    show aisyah kemeja_penasaran:
        zoom 0.35 xalign 0.2 yalign -0.7
    show fania casual_bingung:
        zoom 1.15 xalign 1.0 yalign -0.02
    with dissolve

    "Aku melihat Aisyah dan Fania sedang berdebat di salah satu booth."

    "Suasana di antara mereka tegang. Mereka hanya berdiri diam beberapa detik, dan menatap satui sama lain, sampai akhirnya Aisyah menghela nafas dan memecah keheningan"

    show fania casual_dingin

    aisyah "\"Udahlah jangan terlalu dibawa serius.. nanti juga tahu mana yang terbaik\""

    show fania casual_menghelanapas with dissolve
    pause 0.3
    show fania casual_menghelanapas_ada_asap with dissolve
    pause 0.3
    show fania casual_menghelanapas with dissolve

    "Fania hanya mengela nafas kecil, memilih mengalihkan pandangannya ke booth lain."

    show raden kasual_canggung:
        zoom 0.48 xalign -0.3 yalign 0.1
    show aisyah:
        xalign 0.5
    show fania:
        xalign 1.2
    with moveinleft

    "Aku mendekati mereka dengan hati-hati, mencoba membaca situasi yang sedang berlangsung. Wajah Aisyah tampak tegang meski ia sudah berusaha menutupinya dengan senyumannya yang dipaksakan."

    show fania casual_dingin with dissolve

    "Fania di sisi lain, terlihat santai seperti biasa, tapi caranya menghindari kontak mata dengan Aisyah menunjukkan ada sesuatu yang menganjal di pikirannya."

    raden "\"Eh, kalian nggak apa-apa kan?\""

    fania "\"Nggak apa-apa kok, cuma diskusi kecil.\""

    "Aisyah mengangguk,"

    "{i}Waduh kayaknya aku baru saja melewatkan masalah serius nih{/i}"

    show aisyah kemeja_bicara with dissolve

    aisyah "\"Urusan pentingnya udah beres den?\""

    raden "\"aman, udah beres kok\""

    #jump

    return

label pensasi_tessa_scene3_choice3_2:
    voice "audio/vo/tessa/pensasi/pensasi_3_2_1_terima_kasih.flac"
    tessa "\"Makasih ya udah bantu\""

    show raden kasual_ceria

    raden "\"Aman kak, aku suka menolong kok\""
    
    voice "audio/vo/tessa/pensasi/pensasi_3_2_2_begitu.flac"
    tessa "\"Begitu ya, bukan karena pernah kabur dulu\""

    show raden kasual_capek

    raden "\"Katanya jangan dibahas lagi..\""

    voice "audio/vo/tessa/pensasi/pensasi_3_2_3_hehehe.flac"
    tessa "\"Hehehehe\""

    show raden kasual_tersenyum

    raden "\"kak Tessa, ikut liat-liat booth yang lain yuk\""

    voice "audio/vo/tessa/pensasi/pensasi_3_2_4_hmm.flac"
    tessa "\"hmmm...\""

    "Kak Tessa tampak berpikir sejenak, lalu menoleh ke arah Kak Dio, yang masih duduk santai dengan tangan di belakang kepala"

    "Kak Dio hanya terkekeh pelan lalu mengangkat ponselnya."

    dio "\"Santai aja. Gue udah ngehubungin anak-anak yang lain. Jadi lo bisa bebas jalan-jalan dulu, Boss\""

    voice "audio/vo/tessa/pensasi/pensasi_3_2_5_serius.flac"
    tessa "\"Serius kau?\""

    dio "\"Yaelah, gue kapan bohong soal beginian? Udah gih. Lo jalan aja.\""

    "Kak Dio lalu melirik ke arahku dengan smirk yang mencurigakan."

    dio "\"Atau lebih tepatnya... Lo mau ngedate sama bocah ini?\""

    show raden kasual_panik with dissolve
    
    "Aku langsung tersedak udara" with vpunch

    raden "\"Hah?! Bukan gitu, Kak!\""

    "Kak Tessa juga tampak kaget, lalu langsung melemparkan gulungan brosur ke kepala Kak Dio."

    voice "audio/vo/tessa/pensasi/pensasi_3_2_6_bacot.flac"
    tessa "\"{size=+10}Bacot lu!{/size}\""

    "Kak Dio tertawa puas sambil mengangkat tangan tanda menyerah"

    dio "\"Hahahaha, yaudah, yaudah. Canda doang, jangan serius amat.\""

    voice "audio/vo/tessa/pensasi/pensasi_3_2_7_yaudah.flac"
    tessa "\"Yaudah, ayo jalan\""

    show raden kasual_canggung

    raden "\"Oke kak\""

    "Saat kami mulai melangkah pergi, aku sempat melirik ke arah Kak Dio yang hanya menyeringai kecil sambil melambaikan tangannya"

    stop music fadeout 2.0

    jump pensasi_tessa_scene4

    return