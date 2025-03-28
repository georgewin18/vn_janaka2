define prolog_day4_choice2_first = True
define prolog_day4_choice2_1_done = False
define prolog_day4_choice2_2_done = False
define prolog_day4_choice2_3_done = False
define prolog_day4_choice2_4_done = False

label prolog_day4_scene4:
    scene bg lap_futsal with dissolve:
        zoom 0.5

    play music raden_bgm fadein 1.0
    
    show raden kemeja_biasa with dissolve:
        zoom 0.48 xalign 0.5 yalign 0.1

    "Setibanya di area UKM Expo, aku berpisah dengan Kak Sekar, di mana aku menemukan Aisyah"

    menu:
        "Temui Aisyah":
            jump prolog_day4_scene4_choice1_1
        "Liat-liat sendiri dulu":
            jump prolog_day4_scene4_choice1_2
    
    return

label prolog_day4_scene4_choice1_1:
    "Aku melihat sekeliling, suasananya jauh lebih ramai dari yang kubayangkan. Puluhan stan UKM berjajar rapi, masing-masing dihiasi dengan bendera, poster, dan dekorasi kreatif."

    "Aku melihat panggung kecil di ujung lapangan, tempat beberapa UKM menampilkan pertunjukkan untuk menarik perhatian."

    stop music fadeout 2.0
    play music aisyah_bgm fadein 1.0

    show aisyah kemeja_bicara:
        zoom 0.35 xalign 0.9 yalign -0.7
    show raden:
        xalign 0.0
    with moveinright 

    voice "audio/vo/aisyah/prolog4/prolog4_4_gimana_den.flac"
    aisyah "\"Gimana, den? Udah gak apa-apa?\""

    raden "\"Udah, kok. Berkat Kak Sekar,\""

    raden "\"Eh, ngomong-ngomong, kamu udah lihat-lihat UKM apa aja?\""

    show aisyah kemeja_bertekad with dissolve

    voice "audio/vo/aisyah/prolog4/prolog4_5_aku_udah_keliling.flac"
    aisyah "\"Aku tadi keliling, dan sepertinya aku udah fix mau join {b}ROBOHOLIC{/b}\""

    raden "\"ROBOLOHIC? itu UKM apa?\""

    voice "audio/vo/aisyah/prolog4/prolog4_6_ukm_robotik.flac"
    aisyah "\"UKM robotik\""

    voice sustain
    aisyah "\"Mereka fokus ke pengembangan robot - mulai dari desain mekanik, programming, nanti juga bisa direkrut sama tim robotik PENS\""

    voice sustain
    aisyah "\"nanti bisa ikut lomba-lomba tingkat nasional dan internasional.\""

    raden "\"Wah, keren banget! Pasti seru kalau bisa ikut lomba juga, ya\""

    voice "audio/vo/aisyah/prolog4/prolog4_7_iya_aku_pengen.flac"
    aisyah "\"Iya! Aku pengen banget ikut kompetisi robotik...\""

    voice sustain
    aisyah "\"Bayangin kalau kita bisa menang dan wakilin kampus, pasti pengalaman luar biasa.\""

    voice "audio/vo/aisyah/prolog4/prolog4_8_aku_dari_sma.flac"
    aisyah "\"Aku dari SMA memang udah suka hal-hal berbau teknologi. Pas tadi liat demo mereka, aku langsung tertarik.\""

    voice sustain
    aisyah "\"Mereka bikin robot kecil yang bisa jalan otomatis lewat sensor. Terus ada juga robot untuk kompetisi sepak bola robot.\""

    raden "\"Kayaknya itu cocok banget buat kamu. Kalau kamu udah yakin, ya daftar aja. Kamu pasti cocok di sana.\""

    voice "audio/vo/aisyah/prolog4/prolog4_9_iya_aku_daftar.flac"
    aisyah "\"Iya, aku bakal daftar nanti, kamu juga keliling sana.\""

    #hide aisyah
    hide aisyah with dissolve
    show raden with moveinleft:
        xalign 0.5
    
    stop music fadeout 2.0
    play music raden_bgm fadein 1.0

    "Aku mengangguk, berpisah dengan Aisyah. Aku berjalan perlahan di antara stan-stan yang ada. Suasana UKM Expo ini benar-benar ramai."

    "Hampir setiap sudut area dipenuhi oleh mahasiswa baru yang sibuk bertanya, mendengar penjelasan, atau bahkan mencoba demo kegiatan dari berbagai UKM"

    "Tiba-tiba mataku tertarik pada salah satu stan yang berbeda dari yang lain. Dekorasi stan itu penuh dengan elemen budaya Jepang"
    
    "Poster anime, replika pedang katana, lampion khas Jepang, dan bahkan satu sudut stan dipenuhi figur karakter anime terkenal. Di atasnya, terpampang spanduk besar bertuliskan: {b}JANAKA{/b} - Japanese Nakama"
 
    show raden kemeja_bingung with dissolve

    raden "{i}JANAKA?{/i}"

    "Stan itu terlihat ramai. Beberapa mahasiswa baru berkumpul, berbicara dengan anggota UKM yang menjelaskan kegiatan mereka."
    
    "Aku mendengar beberapa kata seperti \"belajar bahasa Jepang\", \"membuat komik dan VN\", dan \"lomba cosplay\""

    "Sebagai penggemar anime, aku langsung merasa tertarik"

    "Saat aku berjalan lebih dekat, mataku menangkap sosok yang familiar di antara kerumunan. Rambut merah yang khas itu langsung kukenali."
    
    show raden kemeja_tersenyum
    #show raden & fania
    raden "\"Fania?\""

    stop music fadeout 2.0
    play music fania_bgm fadein 1.0

    show raden kemeja_biasa with moveinright:
        xalign 0.0
    show fania kemeja_senyum_normal with dissolve:
        zoom 1.15 xalign 1.0 yalign -0.02

    voice "audio/vo/fania/prolog4/prolog4_1_oh_raden.flac"
    fania "\"Oh, Raden,\""

    raden "\"Kamu juga suka budaya Jepang?\""

    fania "\"...\""

    voice "audio/vo/fania/prolog4/prolog4_2_lumayan.flac"
    fania "\"Lumayan, aku nonton beberapa anime.\""

    raden "\"Jadi, kamu tertarik buat gabung ke JANAKA?\""

    voice "audio/vo/fania/prolog4/prolog4_3_mungkin.flac"
    fania "\"Mungkin, mereka punya banyak kegiatan menarik. Katanya ada workshop cosplay dan kegiatan menarik lain.\""

    raden "\"Serius? Kalau nonton anime bareng atau bikin cosplay juga ada gak?\""

    voice "audio/vo/fania/prolog4/prolog4_4_ada.flac"
    fania "\"Ada. Mereka bahkan punya kelas buat ngajarin bikin kostum cosplay, menurutku cukup menarik sih.\""

    raden "\"Kamu suka cosplay ya?\""

    voice "audio/vo/fania/prolog4/prolog4_5_nggak_sering.flac"
    fania "\"Gak sering sih, tapi aku pernah sesekali.\""

    raden "\"Pasti keren, tuh,\""

    voice "audio/vo/fania/prolog4/prolog4_6_kamu_sendiri.flac"
    fania "\"Kamu sendiri? Mau daftar di sini juga?\""

    raden "\"Mungkin ya, Aku suka banget nonton anime. tapi aku pengen liat-liat booth lain dulu deh.\""

    "Dia hanya menjawab dengan anggukan kecil, lalu kembali membaca brosur."

    raden "\"Fania, aku lihat-lihat booth lain ya\""

    voice "audio/vo/fania/prolog4/prolog4_7_ok.flac"
    fania "\"ok\""

    #hide fania
    hide fania with dissolve
    show raden with moveinleft:
        xalign 0.5

    stop music fadeout 2.0
    play music raden_bgm fadein 1.0

    "Setelah berpamitan dengan Fania di stan JANAKA, aku melanjutkan eksplorasi ke area UKM Expo yang semakin ramai."

    "Saat melewati sebuah booth, suara teriakan energik menarik perhatianku"

    anon "\"{size=+10}Hyaah!{/size}\""

    "Aku menoleh ke arah suara itu. Di depan sebuah stan, beberapa mahasiswa sedang memamerkan teknik taekwondo. Dengan seragam putih dan sabuk warna-warni, mereka menampilkan gerakan yang rapi dan penuh tenaga"

    "Sorakan penonton terdengar setiap kali papan kayu berhasil dipecahkan dengan tendangan tinggi."

    "Saat aku mendekati meja pendaftaran, mataku menangkan seseorang yang berdiri dengan tegas di sudut stan, Kak Tessa. Wajahnya tetap membawa kesan galak, seperti biasa."

    #show tessa
    show raden with moveinright:
        xalign 0.0
    show tessa normal with dissolve:
        zoom 0.39 yalign -0.25 xalign 0.95

    stop music fadeout 2.0
    play music tessa_bgm fadein 1.0

    raden "\"Permisi, Kak Tessa?\""

    voice "audio/vo/tessa/prolog4/prolog4_1_oh_kamu.flac"
    tessa "\"Oh, kamu. Ada apa?\""

    raden "\"Kakak juga di UKM Taekwondo, ya?\""

    voice "audio/vo/tessa/prolog4/prolog4_2_iya_aku_pelatih.flac"
    tessa "\"Iya, aku pelatih junior di sini. Kenapa? Mau daftar?\""

    raden "\"Mungkin sih kak. Dari tadi liat demi nya, saya jadi tertarik. Dulu saya suka bela diri, tapi berhenti karena gak sempat latihan.\""

    raden "\"Jadi, kalau ikut UKM ini, kegiatannya apa aja, Kak?\""

    voice "audio/vo/tessa/prolog4/prolog4_3_kami_ada_latihan.flac"
    tessa "\"Kami ada latihan rutin setiap minggu. Selain itu, ada kelas untuk tingkat pemula, seminar tentang bela diri, dan tentu saja kompetisi. Biasanya kami juga ikut kejuaraan tingkat kampus sampai nasional.\""

    "Aku membaca brosur yang dia tunjukkan. Foto-foto kegiatan mereka terlihat keren, terutama yang menunjukkan anggota tim membawa piala di kejuaraan"

    raden "Hmm, mungkin aku pikir-pikir dulu, Kak. Tapi serius, ini kelihatan seru."

    voice "audio/vo/tessa/prolog4/prolog4_4_yaudah.flac"
    tessa "\"Ya udah. Kalau kamu mau tanya-tanya lagi, balik ke sini aja.\""

    #hide tessa
    hide tessa with dissolve
    show raden with moveinleft:
        xalign 0.5
    
    stop music fadeout 2.0
    play music raden_bgm fadein 1.0

    "Setelah meninggalkan booth Taekwondo, aku terus berjalan menyusuri area UKM Expo. Suasananya masih ramai, dengan mahasiswa baru yang antusias mengeksplorasi berbagai pilihan UKM"

    "Saat aku berjalan lebih jauh, telingaku menangkap suara yang familiar - suara sorakan dan teriakan kecil diiringi efek suara dari permainan video game." 
    
    "Aku menoleh dan menemukan booth dengan monitor besar yang menampilkan pertandingan game kompetitif. Spanduk besar di atas booth itu bertuliskan PENS Esports"

    "Di depan booth, beberapa mahasiswa sedang memainkan game populer seperti Heroes Legend dan Gulorant." 
    
    "Di sisi lain, mahasiswa baru berkumpul, Saat aku mendekat, aku melihat seseorang yang tidak asing sedang duduk di kursi gaming, asyik memainkan game VIVA. Sosok itu tidak lain adalah Santo"

    #show santo
    show raden with moveinright:
        xalign 0.0
    show santo kemeja_biasa with dissolve:
        zoom 1.15 xalign 2.7 yalign 0.08

    stop music fadeout 2.0
    play music santo_bgm fadein 1.0

    raden "\"Santo!?\""

    show santo kemeja_bicara

    santo "\"Eh, Den! Ngapain kamu ke sini? Mau daftar Esports juga?\""

    raden "\"Belum tau, sih. Tapi keliatannya seru juga.\""

    santo "\"Ya iyalah aku di sini. Ini UKM paling cocok buat ku. Gak ribet, bisa rebahan sambil latihan.\""

    raden "\"Jadi kamu udah daftar, ya?\""

    santo "\"Jelas\""

    raden "\"Wah, mantap deh,\""

    raden "\"Tapi aku kayaknya mau keliling dulu, Santo. Banyak booth menarik nih.\""

    santo "\"Oke, Den\""

    hide santo with dissolve

    stop music fadeout 2.0
    play music raden_bgm fadein 1.0

    jump prolog_day4_scene5

label prolog_day4_scene4_choice1_2:
    "Aku melihat sekeliling, suasananya jauh lebih ramai dari yang kubayangkan. Puluhan stan UKM berjajar rapi, masing-masing dihiasi dengan bendera, poster, dan dekorasi kreatif."

    "Aku melihat panggung kecil di ujung lapangan, tempat beberapa UKM menampilkan pertunjukkan untuk menarik perhatian."

    "Mataku tertarik pada salah satu stan yang berbeda dari yang lain. Dekorasi stan itu penuh dengan elemen budaya Jepang"
    
    "Poster anime, replika pedang katana, lampion khas Jepang, dan bahkan satu sudut stan dipenuhi figur karakter anime terkenal. Di atasnya, terpampang spanduk besar bertuliskan: {b}JANAKA{/b} - Japanese Nakama"

    "Tiba-tiba ada suara teriakan energik menarik perhatianku"

    anon "\"{size=+10}Hyaah!{/size}\""

    "Aku menoleh ke arah suara itu. Di depan sebuah stan, beberapa mahasiswa sedang memamerkan teknik taekwondo. Dengan seragam putih dan sabuk warna-warni, mereka menampilkan gerakan yang rapi dan penuh tenaga"

    "Sorakan penonton terdengar setiap kali papan kayu berhasil dipecahkan dengan tendangan tinggi."

    "Tiba-tiba ada lagi suara sorakan dan teriakan kecil diiringi efek suara dari permainan video game." 
    
    "Aku menoleh dan menemukan booth dengan monitor besar yang menampilkan pertandingan game kompetitif. Spanduk besar di atas booth itu bertuliskan PENS Esports"

    "Melihat berbagai macam booth yang menarik aku bingung, lebih baik pergi ke mana dulu ya?"

    jump prolog_day4_scene4_choice2

label prolog_day4_scene4_choice2:

    if (prolog_day4_choice2_first == False):
        show raden with moveinleft:
            xalign 0.5

        "Sekarang lanjut ke mana ya?"
    
    $ prolog_day4_choice2_first = False

    menu:
        "Temui Aisyah dulu aja deh" if (prolog_day4_choice2_1_done == False):
            jump prolog_day4_scene4_choice2_1
        "JANAKA" if (prolog_day4_choice2_2_done == False):
            jump prolog_day4_scene4_choice2_2
        "Taekwondo" if (prolog_day4_choice2_3_done == False):
            jump prolog_day4_scene4_choice2_3
        "Esport" if (prolog_day4_choice2_4_done == False):
            jump prolog_day4_scene4_choice2_4

label prolog_day4_scene4_choice2_1:
    #show aisyah
    show aisyah kemeja_bicara:
        zoom 0.35 xalign 0.9 yalign -0.7
    show raden:
        xalign 0.0
    with moveinright

    stop music fadeout 2.0
    play music aisyah_bgm fadein 1.0
    
    voice "audio/vo/aisyah/prolog4/prolog4_4_gimana_den.flac"
    aisyah "\"Gimana, den? Udah gak apa-apa?\""

    raden "\"Udah, kok. Berkat Kak Sekar,\""

    raden "\"Eh, ngomong-ngomong, kamu udah lihat-lihat UKM apa aja?\""

    show aisyah kemeja_bertekad with dissolve

    voice "audio/vo/aisyah/prolog4/prolog4_5_aku_udah_keliling.flac"
    aisyah "\"Aku tadi keliling, dan sepertinya aku udah fix mau join {b}ROBOHOLIC{/b}\""

    raden "\"ROBOLOHIC? itu UKM apa?\""

    voice "audio/vo/aisyah/prolog4/prolog4_6_ukm_robotik.flac"
    aisyah "\"UKM robotik\""

    voice sustain
    aisyah "\"Mereka fokus ke pengembangan robot - mulai dari desain mekanik, programming, nanti juga bisa direkrut sama tim robotik PENS\""

    voice sustain
    aisyah "\"nanti bisa ikut lomba-lomba tingkat nasional dan internasional.\""

    raden "\"Wah, keren banget! Pasti seru kalau bisa ikut lomba juga, ya\""

    voice "audio/vo/aisyah/prolog4/prolog4_7_iya_aku_pengen.flac"
    aisyah "\"Iya! Aku pengen banget ikut kompetisi robotik...\""

    voice sustain
    aisyah "\"Bayangin kalau kita bisa menang dan wakilin kampus, pasti pengalaman luar biasa.\""

    voice "audio/vo/aisyah/prolog4/prolog4_8_aku_dari_sma.flac"
    aisyah "\"Aku dari SMA memang udah suka hal-hal berbau teknologi. Pas tadi liat demo mereka, aku langsung tertarik.\""

    voice sustain
    aisyah "\"Mereka bikin robot kecil yang bisa jalan otomatis lewat sensor. Terus ada juga robot untuk kompetisi sepak bola robot.\""

    raden "\"Kayaknya itu cocok banget buat kamu. Kalau kamu udah yakin, ya daftar aja. Kamu pasti cocok di sana.\""

    voice "audio/vo/aisyah/prolog4/prolog4_9_iya_aku_daftar.flac"
    aisyah "\"Iya, aku bakal daftar nanti, kamu juga keliling sana.\""

    "Aku mengangguk, berpisah dengan Aisyah."
    #hide aisyah
    hide aisyah with dissolve

    stop music fadeout 2.0
    play music raden_bgm fadein 1.0

    $ prolog_day4_choice2_1_done = True

    if (prolog_day4_choice2_1_done == True and prolog_day4_choice2_2_done == True and prolog_day4_choice2_3_done == True and prolog_day4_choice2_4_done == True):
        jump prolog_day4_scene5
    else:
        jump prolog_day4_scene4_choice2

label prolog_day4_scene4_choice2_2:
    show raden kemeja_bingung with dissolve
    
    raden "{i}JANAKA?{/i}"

    "Stan itu terlihat ramai. Beberapa mahasiswa baru berkumpul, berbicara dengan anggota UKM yang menjelaskan kegiatan mereka."
    
    "Aku mendengar beberapa kata seperti \"belajar bahasa Jepang\", \"membuat komik dan VN\", dan \"lomba cosplay\""

    "Sebagai penggemar anime, aku langsung merasa tertarik"

    "Saat aku berjalan lebih dekat, mataku menangkap sosok yang familiar di antara kerumunan. Rambut merah yang khas itu langsung kukenali."

    #show raden & fania
    show raden kemeja_biasa with moveinright:
        xalign 0.0
    show fania kemeja_senyum_normal with dissolve:
        zoom 1.15 xalign 1.0 yalign -0.02

    stop music fadeout 2.0
    play music fania_bgm fadein 1.0

    show raden kemeja_tersenyum

    raden "\"Fania?\""

    voice "audio/vo/fania/prolog4/prolog4_1_oh_raden.flac"
    fania "\"Oh, Raden,\""

    raden "\"Kamu juga suka budaya Jepang?\""

    fania "\"...\""

    voice "audio/vo/fania/prolog4/prolog4_2_lumayan.flac"
    fania "\"Lumayan, aku nonton beberapa anime.\""

    raden "\"Jadi, kamu tertarik buat gabung ke JANAKA?\""

    voice "audio/vo/fania/prolog4/prolog4_3_mungkin.flac"
    fania "\"Mungkin, mereka punya banyak kegiatan menarik. Katanya ada workshop cosplay dan kegiatan menarik lain.\""

    raden "\"Serius? Kalau nonton anime bareng atau bikin cosplay juga ada gak?\""

    voice "audio/vo/fania/prolog4/prolog4_4_ada.flac"
    fania "\"Ada. Mereka bahkan punya kelas buat ngajarin bikin kostum cosplay, menurutku cukup menarik sih.\""

    raden "\"Kamu suka cosplay ya?\""

    voice "audio/vo/fania/prolog4/prolog4_5_nggak_sering.flac"
    fania "\"Gak sering sih, tapi aku pernah sesekali.\""

    raden "\"Pasti keren, tuh,\""

    voice "audio/vo/fania/prolog4/prolog4_6_kamu_sendiri.flac"
    fania "\"Kamu sendiri? Mau daftar di sini juga?\""

    raden "\"Mungkin ya, Aku suka banget nonton anime. tapi aku pengen liat-liat booth lain dulu deh.\""

    "Dia hanya menjawab dengan anggukan kecil, lalu kembali membaca brosur."

    raden "\"Fania, aku lihat-lihat booth lain ya\""

    voice "audio/vo/fania/prolog4/prolog4_7_ok.flac"
    fania "\"ok\""

    #hide fania
    hide fania with dissolve

    stop music fadeout 2.0
    play music raden_bgm fadein 1.0

    "Setelah berpamitan dengan Fania di stan JANAKA, aku melanjutkan eksplorasi ke area UKM Expo yang semakin ramai."

    $ prolog_day4_choice2_2_done = True

    if (prolog_day4_choice2_1_done == True and prolog_day4_choice2_2_done == True and prolog_day4_choice2_3_done == True and prolog_day4_choice2_4_done == True):
        jump prolog_day4_scene5
    else:
        jump prolog_day4_scene4_choice2

label prolog_day4_scene4_choice2_3:
    "Saat aku mendekati meja pendaftaran, mataku menangkan seseorang yang berdiri dengan tegas di sudut stan, Kak Tessa. Wajahnya tetap membawa kesan galak, seperti biasa."

    #show tessa
    show raden with moveinright:
        xalign 0.0
    show tessa normal with dissolve:
        zoom 0.39 yalign -0.25 xalign 0.95

    stop music fadeout 2.0
    play music tessa_bgm fadein 1.0

    raden "\"Permisi, Kak Tessa?\""

    voice "audio/vo/tessa/prolog4/prolog4_1_oh_kamu.flac"
    tessa "\"Oh, kamu. Ada apa?\""

    raden "\"Kakak juga di UKM Taekwondo, ya?\""

    voice "audio/vo/tessa/prolog4/prolog4_2_iya_aku_pelatih.flac"
    tessa "\"Iya, aku pelatih junior di sini. Kenapa? Mau daftar?\""

    raden "\"Mungkin sih kak. Dari tadi liat demi nya, saya jadi tertarik. Dulu saya suka bela diri, tapi berhenti karena gak sempat latihan.\""

    raden "\"Jadi, kalau ikut UKM ini, kegiatannya apa aja, Kak?\""

    voice "audio/vo/tessa/prolog4/prolog4_3_kami_ada_latihan.flac"
    tessa "\"Kami ada latihan rutin setiap minggu. Selain itu, ada kelas untuk tingkat pemula, seminar tentang bela diri, dan tentu saja kompetisi. Biasanya kami juga ikut kejuaraan tingkat kampus sampai nasional.\""

    "Aku membaca brosur yang dia tunjukkan. Foto-foto kegiatan mereka terlihat keren, terutama yang menunjukkan anggota tim membawa piala di kejuaraan"

    raden "Hmm, mungkin aku pikir-pikir dulu, Kak. Tapi serius, ini kelihatan seru."

    voice "audio/vo/tessa/prolog4/prolog4_4_yaudah.flac"
    tessa "\"Ya udah. Kalau kamu mau tanya-tanya lagi, balik ke sini aja.\""

    #hide tessa
    hide tessa with dissolve

    stop music fadeout 2.0
    play music raden_bgm fadein 1.0

    $ prolog_day4_choice2_3_done = True

    if (prolog_day4_choice2_1_done == True and prolog_day4_choice2_2_done == True and prolog_day4_choice2_3_done == True and prolog_day4_choice2_4_done == True):
        jump prolog_day4_scene5
    else:
        jump prolog_day4_scene4_choice2

label prolog_day4_scene4_choice2_4:
    "Di depan booth, beberapa mahasiswa sedang memainkan game populer seperti Heroes Legend dan Gulorant." 
    
    "Di sisi lain, mahasiswa baru berkumpul, Saat aku mendekat, aku melihat seseorang yang tidak asing sedang duduk di kursi gaming, asyik memainkan game VIVA. Sosok itu tidak lain adalah Santo"

    #show santo
    show raden with moveinright:
        xalign 0.0
    show santo kemeja_biasa with dissolve:
        zoom 1.15 xalign 2.7 yalign 0.08

    stop music fadeout 2.0
    play music santo_bgm fadein 1.0

    raden "\"Santo!?\""

    santo "\"Eh, Den! Ngapain kamu ke sini? Mau daftar Esports juga?\""

    raden "\"Belum tau, sih. Tapi keliatannya seru juga.\""

    santo "\"Ya iyalah aku di sini. Ini UKM paling cocok buat ku. Gak ribet, bisa rebahan sambil latihan.\""

    raden "\"Jadi kamu udah daftar, ya?\""

    santo "\"Jelas\""

    raden "\"Wah, mantap deh,\""

    raden "\"Tapi aku kayaknya mau keliling dulu, Santo. Banyak booth menarik nih.\""

    santo "\"Oke, Den\""
    #hide santo
    hide santo with dissolve
    
    stop music fadeout 2.0
    play music raden_bgm fadein 1.0

    $ prolog_day4_choice2_4_done = True

    if (prolog_day4_choice2_1_done == True and prolog_day4_choice2_2_done == True and prolog_day4_choice2_3_done == True and prolog_day4_choice2_4_done == True):
        jump prolog_day4_scene5
    else:
        jump prolog_day4_scene4_choice2