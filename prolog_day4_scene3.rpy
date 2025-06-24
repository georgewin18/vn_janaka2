## TEST SPEAK ANIMATION SPRITE

label prolog_day4_scene3:
    #bg jalan kantin-d4
    scene bg depan_auditorium with dissolve:
        zoom 0.5
    
    #show raden & sekar
    show raden kemeja_biasa:
        zoom 0.54 xalign -0.2 yalign 0.05
    show sekar jas_biasa:
        zoom 1.25 xalign 1.0 yalign 0.05
    with dissolve

    raden "\"Kak, aku bisa lanjut sendiri ke expo,\""

    show sekar jas_teriak

    voice "audio/vo/sekar/prolog4/prolog4_12_tidak_boleh.flac"
    sekar "Tidak boleh, aku harus ikut mengantar. Kalau nanti ada apa-apa di tengah jalan, aku yang bertanggung jawab."

    show sekar jas_biasa

    "Kami berjalan pelan menuju area UKM Expo, tetapi pikiranku terus mengingat momen tadi."

    "Selama PKKMB, aku selalu melihat Kak Sekar sebagai sosok yang sempurna, tegas, cekatan, dan tanpa cela."

    "Namun, hari ini, aku melihat sisi lain darinyayang lebih manusiawi."

    "Melihat Kak Sekar yang bisa takut seperti itu membuatku merasa lebih dekat dengannya."
    
    "Dia bukan hanya panitia yang hebat, tetapi juga seseorang yang tulus mencoba membantu meskipun punya keterbatasan."

    "Aku mengikutinya dalam diam untuk beberapa langkah, tetapi suasana yang terlalu hening membuatku merasa canggung. Akhirnya, aku mencoba membuka pembicaraan."

    raden "\"Kak, UKM Expo ini sebenarnya ngapain aja sih?\""

    show sekar jas_bicara

    voice "audio/vo/sekar/prolog4/prolog4_13_disana_semua_ukm.flac"
    sekar "\"Di sana, semua UKM bakal pamerin kegiatan mereka. Intinya buat ngenalin diri dan ngajak kalian para mahasiswa baru untuk bergabung.\""

    show sekar jas_biasa

    raden "\"Kak Sekar sendiri ikut UKM apa?\""

    show sekar jas_bicara

    voice "audio/vo/sekar/prolog4/prolog4_14_aku_e2c.flac"
    sekar "\"Aku di {b}E2C{/b}\""

    show sekar jas_biasa

    raden "\"E2C..? itu... UKM apa, Kak?\""

    show sekar jas_bicara

    voice "audio/vo/sekar/prolog4/prolog4_15_eepis.flac"
    sekar "\"EEPIS English Community atau E2C merupakan UKM Bahasa Inggris.\""
    
    voice sustain
    sekar "\"Nah, kegiatannya tuh banyak banget, mulai dari belajar public speaking, debat, sampai lomba-lomba tingkat nasional ataupun internasional.\""

    voice sustain
    sekar "\"Nah, Kalau pengen improve skill Bahasa Inggris, itu tempatnya.\""

    show sekar jas_biasa

    raden "\"Wah, keren juga kak. Jadi Kaka sering ikut lomba gitu?\""

    show sekar jas_bicara

    voice "audio/vo/sekar/prolog4/prolog4_16_lumayan.flac"
    sekar "\"Lumayan. Aku dulu pernah ikut lomba debat sama speech contest. Belum sampai menang tingkat internasional sih, tapi beberapa kali menang tingkat nasional.\""

    show sekar jas_biasa

    raden "\"Kakak hebat banget, bisa ikut lomba kayak gitu. Pasti susah ya, Kak?\""

    show sekar jas_bicara

    voice "audio/vo/sekar/prolog4/prolog4_17_seru_kok.flac"
    sekar "\"Malah seru kok. Bisa ketemu orang baru, diskusi, bahkan jalan-jalan keluar kota.\""

    show sekar jas_biasa

    raden "\"Kayaknya E2C menarik juga, ya.\""

    show sekar jas_bicara

    voice "audio/vo/sekar/prolog4/prolog4_18_tertarik_gabung.flac"
    sekar "\"Tertarik gabung?\""

    show sekar jas_biasa

    raden "\"Gak tahu, kak. Tapi saya pengen cari UKM yang bisa bikin saya berkembang juga. Jadi mungkin nanti mampu ke stan E2C.\""

    show sekar jas_bicara

    voice "audio/vo/sekar/prolog4/prolog4_19_boleh_banget.flac"
    sekar "\"Boleh banget. Tapi jangan asal pilih UKM, ya. Cari yang benar-benar sesuai sama minat kamu. Jangan cuma ikut-ikutan\""

    show sekar jas_biasa

    raden "\"Iya, Kak. Makasih sarannya.\""

    hide sekar with dissolve

    stop music fadeout 2.0

    jump prolog_day4_scene4

    return