define raden_nvl = Character("Raden", kind=nvl, callback=Phone_SendSound)
define aisyah_nvl = Character("Aisyah", kind=nvl, callback=Phone_ReceiveSound)

label pensasi_tessa_scene2:
    raden_nvl "Aisyah"
    aisyah_nvl "Ada apa den?" 
    raden_nvl "Maaf nih gk bisa bareng kalian, ada urusan mendadak"
    aisyah_nvl "Urusannya penting kah den?"
    raden_nvl "Iya nih, maaf yah"
    aisyah_nvl "Kalo emang sepenting itu gpp sih"
    raden_nvl "Maaf ya"

    nvl clear

    scene bg depan_auditorium with dissolve:
        zoom 0.5

    show raden kasual_biasa:
        zoom 0.48 xalign 0.0 yalign 0.1
    show tessa normal:
        zoom 0.39 yalign -0.25 xalign 0.95
    with dissolve

    tessa "\"Sudah selesai kah chat nya? Kumulai ya\""

    play music campus fadein 1.0

    show raden kasual_tersenyum

    raden "\"Iya kak, udah, cuma ngabarin temen sebentar tadi\""

    show raden kasual_biasa

    "Kak Tessa mulai menjelaskan konsep game yang sedang dipamerkan supaya aku tidak bingung."

    "Dia menjelaskan alur gameplay, elemen desain, dan sedikit tentang latar belakang pengembangannya. Meski agak berat, aku berusaha menyimak dengan serius."

    scene black with dissolve
    with Pause(0.3)

    scene bg depan_auditorium with dissolve:
        zoom 0.5

    show raden kasual_capek:
        zoom 0.48 xalign 0.0 yalign 0.1
    show tessa normal:
        zoom 0.39 yalign -0.25 xalign 0.95
    with dissolve

    tessa "\"Sejauh ini sudah paham kah?\""

    show raden kasual_menghela_napas

    raden "\"Ehhhh...\""

    tessa "\"Kau ini! Aku ulangi lagi sekali ya!\""

    tessa "\"Jadi dengan dan pahami oke!\""

    show raden kasual_biasa

    "Setelah Kak Tessa menjelaskan ulang, aku pun mulai memahami- atau setidaknya bisa menjelaskan kembali ke orang lain."

    tessa "\"Gimana? Dah paham?\"" 

    show raden kasual_tersenyum

    raden "\"Dah paham kok\""

    show raden kasual_biasa

    tessa "\"Baguslah, awas nanti kau kebingungan dan lihat aku terus untuk minta pertolongan\""

    tessa "\"Setidaknya kau bisa membantu daripada menyusahkan\""

    "Belum lama setelah Kak Tessa menjelaskan semua detail tentang game di booth ini, para pengunjung mulai berdatangan satu per satu."

    "Awalnya hanya beberapa orang yang mampir sekedar melihat-lihat, tapi semakin lama, jumlahnya semakin bertambah hingga mulai membentuk kerumunan kecil."

    "Kami pun segera beraksi. Aku mulai menjelaskan apa yang sudah kupelajari dari Kak Tessa, berusaha terlihat meyakinkan di depan para pengunjung. Meski awalnya gugup, aku perlahan mulai merasa percaya diri."

    "Berkali-kali aku harus menjelaskan hal yang sama, dan Kak Tessa terlihat semakin sibuk menjawab pertanyaan-pertanyaan yang lebih teknis."

    show raden kasual_canggung with dissolve

    "Saat aku hampir menyerah karena merasa ngos-ngosan, tiba-tiba seorang teman Kak Tessa datang."

    "Di tengah kekacauan ini, tiba-tiba terdengar suara familiar dari belakang."

    anon "\"Woilah gua tinggal bentar langsung rame gini?\"" with vpunch

    "Aku menoleh dan terkejut melihat Kak Dio berjalan santai menuju meja booth. Dengan ekspresi percaya diri, dia langsung berdiri di sampingku dan menatap layar game yang sedang dipamerkan."

    tessa "\"Udah jangan banyak tanya, cepetan bantuin!\""

    dio "\"Tsk, rame banget,\""

    "Kak Dio segera bergabung untuk membantu kami melayani pengunjung."

    show raden kasual_biasa

    "Aku bernafas lega, membiarkan Kak Dio menjawab- dan di luar dugaan, penjelasannya sangat meyakinkan"

    "Kak Dio melanjutkan dengan gestur tangan yang mantap, mejelaskan mekanik gameplay dengan percaya diri. Setiap pertanyaan dari pengunjung dia jawab tanpa ragu, bahkan lebih detail dari yang pernah Kak Tessa jelaskan kepadaku."

    "Dengan tambahan tenaga baru, suasana di booth perlahan mulai terkendali. Aku dan Kak Tessa akhirnya bisa sedikit bernafas lega setelah sebelumnya hampir kewalahan."

    "Setelah beberapa menit berlalu, kerumunan di booth mulai berkurang dan kami akhirnya bisa beristirahat."

    hide raden
    hide tessa
    with dissolve

    "Aku masih sedikit terkejut dengan bagaimana Kak Dio mengendalikan situasi tadi. orang yang awalnya kupikir cuma senior menyebalkan ternyata bisa menjelaskan game ini lebih baik dari siapa pun."

    "Saat aku masih memikirkan hal itu, tiba-tiba Kak Dio mendatangiku."

    show raden kasual_canggung with dissolve:
        zoom 0.48 xalign 0.5 yalign 0.1

    dio "\"Oi, Raden kan nama lu?\""

    show raden kasual_gugup

    raden "\"Eh? Iya kak...\""

    menu:
        "Kak Perokok?":
            dio "\"Nama gua Dio woi!\"" with vpunch

            "Walaupun dia terlihat kesal, dia dengan cepat menghela nafas dan menenangkan diri."

        "Kak Dio?":
            "Kak Dio mengangguk ringan"

    jump pensasi_tessa_scene3

    return