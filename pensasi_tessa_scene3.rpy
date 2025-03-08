label pensasi_tessa_scene3:
    "Dia menatapku sebentar, lalu merogoh kantongnya dan mengeluarkan sebuah kaleng minuman dingin."

    dio "\"Nih\""

    "Aku menatap minuman itu dengan bingung."

    raden "\"Eh? Buat aku kak?\""

    dio "\"Ya buat siapa lagi?!\""

    dio "\"Gua udah denger dari Tessa, tadi lo juga udah kerja keras. Anggap aja bonus.\""

    "Aku ragu-ragu sebelum akhirnya menerimanya. Saat kaleng dingin itu menyentuh tanganku, aku bisa merasakan betapa segarnya setelah bekerja keras seharian."

    raden "\"Makasih kak\""

    "Aku hendar membuka minumannya ketika Kak Dio tiba-tiba berdehem kecil."

    dio "\"Eh, soal yang masalah rokok dulu itu...\""

    dio "\"Ya... gue tau gue rada nyebelin waktu itu,\""

    dio "\"Yah... yang jelas, gue nggak ada niat buat bikin masalah gede. Tadi di kampus juga... ya lo tau lah, kadang gue suka kelewatan,\""

    raden "\"Iya, iya. Aku ngerti kak. Makasih udah bilang gitu.\""

    "Kak Dio mendengus, lalu meneguk minumannya"

    dio "\"Bagus,\""

    "Saat itu, aku melirik ke arah Kak Tessa yang duduk tak jauh dari kami. Dia tidak ikut campur, hanya duduk sambil tersenyum tipis, memandangi interaksi kami dengan ekspresi puas."

    "Aku menghabiskan tegukan terakhir dari minuman yang Kak Dio berikan. Dingin dan menyegarkan, mengusir sedikit rasa lelah yang menempel setelah seharian menjaga booth. Suasana sudah jauh lebih tenang dibandingkan sebelumnya."

    menu:
        "Kembali menemui Aisyah dan Fania":
            jump pensasi_tessa_scene3_choice3_1
        "Ajak jalan-jalan":
            jump pensasi_tessa_scene3_choice3_2

    return

label pensasi_tessa_scene3_choice3_1:
    raden "\"Fyuhh... kalau gitu aku balik ya kak\""

    tessa "\"Terima kasih ya udah bantu\""

    raden "\"Aman kak, udah biasa teman menolong teman\""

    tessa "\"Oke, hati-hati ya\""

    raden "\"Oke, makasih, bye\""

    tessa "\"Bye\""

    scene black with dissolve
    with Pause(0.3)

    scene bg depan_auditorium with dissolve:
        zoom 0.5

    "Aku melihat Aisyah dan Fania sedang berdebat di salah satu booth."

    "Suasana di antara mereka tegang. Mereka hanya berdiri diam beberapa detik, dan menatap satui sama lain, sampai akhirnya Aisyah menghela nafas dan memecah keheningan"

    aisyah "\"Udahlah jangan terlalu dibawa serius.. nanti juga tahu mana yang terbaik\""

    "Fania hanya mengela nafas kecil, memilih mengalihkan pandangannya ke booth lain."

    "Aku mendekati mereka dengan hati-hati, mencoba membaca situasi yang sedang berlangsung. Wajah Aisyah tampak tegang meski ia sudah berusaha menutupinya dengan senyumannya yang dipaksakan."

    "Fania di sisi lain, terlihat santai seperti biasa, tapi caranya menghindari kontak mata dengan Aisyah menunjukkan ada sesuatu yang menganjal di pikirannya."

    raden "\"Eh, kalian nggak apa-apa kan?\""

    fania "\"Nggak apa-apa kok, cuma diskusi kecil.\""

    "Aisyah mengangguk,"

    "{i}Waduh kayaknya aku baru saja melewatkan masalah serius nih{/i}"

    aisyah "\"Urusan pentingnya udah beres den?\""

    raden "\"aman, udah beres kok\""

    #jump

    return

label pensasi_tessa_scene3_choice3_2:
    tessa "\"Makasih ya udah bantu\""

    raden "\"Aman kak, aku suka menolong kok\""
    
    tessa "\"Begitu ya, bukan karena pernah kabur dulu\""

    raden "\"Katanya jangan dibahas lagi..\""

    tessa "\"Hehehehe\""

    raden "\"kak Tessa, ikut liat-liat booth yang lain yuk\""

    tessa "\"hmmm...\""

    "Kak Tessa tampak berpikir sejenak, lalu menoleh ke arah Kak Dio, yang masih duduk santai dengan tangan di belakang kepala"

    "Kak Dio hanya terkekeh pelan lalu mengangkat ponselnya."

    dio "\"Santai aja. Gue udah ngehubungin anak-anak yang lain. Jadi lo bisa bebas jalan-jalan dulu, Boss\""

    tessa "\"Serius kau?\""

    dio "\"Yaelah, gue kapan bohong soal beginian? Udah gih. Lo jalan aja.\""

    "Kak Dio lalu melirik ke arahku dengan smirk yang mencurigakan."

    dio "\"Atau lebih tepatnya... Lo mau ngedate sama bocah ini?\""

    "Aku langsung tersedak udara" with vpunch

    raden "\"Hah?! Bukan gitu, Kak!\""

    "Kak Tessa juga tampak kaget, lalu langsung melemparkan gulungan brosur ke kepala Kak Dio."

    tessa "\"{size=+10}Bacot lu!{/size}\""

    "Kak Dio tertawa puas sambil mengangkat tangan tanda menyerah"

    dio "\"Hahahaha, yaudah, yaudah. Canda doang, jangan serius amat.\""

    tessa "\"Yaudah, ayo jalan\""

    raden "\"Oke kak\""

    "Saat kami mulai melangakn pergi, aku sempat melirik ke arah Kak Dio yang hanya menyeringai kecil sambil melambaikan tangannya"

    jump pensasi_tessa_scene4

    return