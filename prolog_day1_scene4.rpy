label prolog_day1_scene4:
    show bg auditorium:
            zoom 0.5 
    with dissolve

    "Adzan telah terdengar. Waktu ISHOMA telah dimulai. LO Region ku ada 2, yang pertama laki-laki bernama kak Ryan, dan yang satunya perempuan bernama kak Sekar. Dia mulai memanggil anggota region untuk berkumpul"

    show sekar jas_teriak:
        zoom 1.15 xalign 0.7 yalign 0.03

    play music sekar_bgm fadein 1.0

    voice "audio/vo/sekar/pkkmb1_ayo_baris.flac"
    sekar "\"Aldebaran! Ayo berbaris dua banjar.\""

    show sekar jas_normal

    "Sebagai mahasiswa yang baik, tentu saja aku langsung mengikuti arahannya."

    "Kak Sekar langsung menyuruh kami untuk berhitung dari banjar kiri terlebih dahulu. Jika ada yang kurang, Kak Sekar akan menyuruh kami untuk mengulang hitungan dari awal."

    "Untungnya, semuanya sudah kondusif, jadi tidak ada perhitungan ulang dan kita langsung diarahkan menuju ke masjid."

    #"Ketika kita turun, entah kenapa kita menggunakan tangga darurat dan bukan tangga biasa. Kurasa, hal ini tidak perlu dipertanyakan. Jadi aku hanya diam mengikuti arahan Kak Sekar."

    show bg masjid:
            zoom 0.5 
    with dissolve

    raden "{i}Akhirnya sampai juga di masjid, jika aku disuruh lebih lama menunggu di dalam tangga darurat pasti sudah pingsan aku{/i}"

    show sekar jas_teriak

    voice "audio/vo/sekar/pkkmb2_berhenti.flac"
    sekar "\"Aldebaran berhenti terlebih dahulu! Mari berhitung dimulai dari banjar sebelah kiri saya!\""

    show sekar jas_normal

    "Kukira tidak akan ada masalah yang terjadi. Sayangnya, perkiraanku salah, ketika perhitungan selesai, ada dua anggota region yang menghilang. Terlihat muka kak Sekar menjadi sedikit lebih kesal."

    show sekar jas_teriak

    voice "audio/vo/sekar/pkkmb3_berhitung_lagi.flac"
    sekar "\"Ayo berhitung sekali lagi!\""

    show sekar jas_normal

    "Tentu saja, kita memulai perhitungan sekali-lagi, dengan harapan kalau perhitungan kami yang sebelumnya salah."

    "Tapi, masalah tidak bisa dihindari, hasil perhitungan masih sama. Hal ini membuat kita menunda waktu ISHOMA."

    "Dari jauh, terlihat dua anak yang lari menuju ke barisan ini. Mereka sampai ke sini dengan meminta maaf ke kak Sekar"

    Region "\"Maaf kak, di atas tadi kami tiba-tiba kebelet kencing.\""

    show sekar jas_teriak

    voice "audio/vo/sekar/pkkmb4_kan_sudah_kubilang.flac"
    sekar "\"Kan sudah kubilang untuk ke toilet terlebih dahulu ketika di ruangan tadi.\""

    Region "\"Iya kak, lain kali nggak bakal kami ulangi.\""

    "Daripada menunda waktu lebih lama, kak Sekar langsung menyuruh kami untuk sholat. Dengan serentak, kami membubarkan barisan untuk sholat."

    hide sekar with dissolve

    stop music fadeout 2.0

    scene black with dissolve
    with Pause(0.2)

    jump prolog_day1_scene5

    return