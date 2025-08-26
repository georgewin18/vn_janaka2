init:
    transform pan_right:
        xalign 0.0
        linear 3.0 xalign 0.2

    transform pan_left:
        xalign 1.0
        linear 3.0 xalign 0.9

    transform pan_left2:
        xalign 1.0
        linear 2.5 xalign 0.5

label pensasi_tessa_scene4:
    scene bg lt_6_pasca_ramai with dissolve:
        zoom 0.5
    
    show raden kasual_biasa at raden_default:
        xalign -0.2
    show tessa kasual_netral at tessa_default:
        xalign 1.0
    with dissolve

    play music tessa_bgm fadein 1.0

    "Aku dan Kak Tessa pun berkeliling melihat booth-booth yang lain,"

    raden "\"Kak Tessa, ada booth yang pengen kakak kunjungi gak?\""

    voice "audio/vo/tessa/pensasi/pensasi_4_1_belum.flac"
    tessa "\"Belum lihat semuanya sih. Tapi tadi sempat dengar ada booth VR di ujung sana. Katanya seru.\""

    show raden kasual_hehe

    raden "\"VR? Wah, aku belum pernah coba itu,\""

    voice "audio/vo/tessa/pensasi/pensasi_4_2_kalo.flac"
    tessa "\"Kalau gitu, kita ke sana aja. Siapa tau seru. Lagian aku juga penasaaran.\""

    show raden kasual_biasa

    "Kami akhirnya sampai di booth VR. Sebuah layar besar menampilkan cuplikan dunia virtual yang tampak begitu nyata, seperti sebuah hutan lebat dengan air terjun yang mengalir deras. Antrean di sini cukup panjang, tetapi tidak sampai membuat kami menyerah."

    show raden kasual_tersenyum

    raden "\"Kalau dari lihat aja sih, kayanya keren banget ya?\""

    show raden kasual_biasa

    voice "audio/vo/tessa/pensasi/pensasi_4_3_iya.flac"
    tessa "\"Iya, cuma kayaknya bakal bikin pusing juga kalau terlalu lama,\""

    voice "audio/vo/tessa/pensasi/pensasi_4_4_tapi.flac"
    tessa "\"Tapi aku penasaran pengen coba. udah jauh-jauh ke sini kan?\""

    "Akhirnya giliran kami tiba. Petugas di booth menjelaskan cara menggunakan perangkat VR dan pilihan permainan yang tersedia. Kami diberikan dua opsi: menjelajahi dunia fantasi dengan naga terbang atau bermain survival di kota yang penuh zombie."

    show raden kasual_tersenyum

    raden "\"Kak Tessa pilih yang mana? Naga atau Zombie?\""

    "Tessa berpikir sejenak, lalu berkata dengan nada santai,"

    voice "audio/vo/tessa/pensasi/pensasi_4_5_zombie.flac"
    tessa "\"Zombie aja deh. Seru kayaknya kabur-kaburan. Lagian, siapa tahu aku jago headshot\""

    show raden kasual_hehe

    raden "\"Oke, zombie it is!\""

    scene black with dissolve

    stop music fadeout 2.0

    raden "\"LINK-ON\""

    voice "audio/vo/tessa/pensasi/pensasi_4_6_wibu.flac"
    tessa "\"Wibuu..\""

    ## SPECIAL MOMENT

    #VR
    play music intense fadein 1.0

    scene tessa_pensasi at pan_right:
        zoom 2.0 yalign 0.4
    with dissolve

    pause 2.0

    scene tessa_pensasi at pan_left:
        zoom 2.0 yalign 0.5
    with dissolve

    pause 2.0

    scene tessa_pensasi with dissolve

    "Saat headset terpasang, pandanganku langsung berubah. Aku sekarang berada di tengah kota yang hancur. Assap mengepul dari bangunan yang runtuh, dan suara gemertak zombie semakin mendekat."

    voice "audio/vo/tessa/pensasi/pensasi_special_1_raden.flac"
    tessa "\"Raden! Di belakangmu!\"" with vpunch

    "Aku menoleh dan melihat segerombilan zombie mendekat dengan cepat. Kak Tessa, yang berada di sampingku di dunia virtual ini, sudah memegang sebuah senapan virtual dan mulai menembaki zombie-zombie tersebut dengan akurasi yang mengejutkan"

    raden "\"Wah, Kak Tessa pro banget mainnya!\""

    voice "audio/vo/tessa/pensasi/pensasi_special_2_yah.flac"
    tessa "\"Yah, kan tadi aku bilang, siapa tahu jago\""

    "Meskipun aku tidak bisa melihat ekspresi wajahnya, aku bisa mendengar nada puas dalam suaranya"

    stop music fadeout 2.0

    "Setelah melewati jalanan yang dipenuhi zombie, aku dan Kak Tessa berhasil menemukan tempat perlindungan sementara. Di sana sebuah pemandangan terbuka di depan mata kami."

    play music tessa_bgm fadein 1.0

    scene tessa_pensasi1 at pan_left2:
        zoom 1.0 yalign 0.1
    with dissolve

    pause 1.0

    scene tessa_pensasi1 with dissolve:
        zoom 0.75

    "Di dunia game ini, langit malam dibuat dengan detail yang memukau—bintang-bintang yang bertebaran, bulan penuh yang bersinar terang, dan awan tipis yang melintas perlahan."

    raden "\"Wah, pemandangan dari sini keren banget\""

    "Kak Tessa berdiri di dekat pagar, matanya menyapu seluruh pemandangan. Tapi dia tidak berbicara banyak, hanya berdiri diam sambil memandang ke atas, ke arah langit."

    show tessa_pensasi2 with dissolve:
        zoom 0.75

    voice "audio/vo/tessa/pensasi/pensasi_special_3_iya.flac"
    tessa "\"Iya...\""

    "Aku tidak menanggapi lebih jauh, hanya menganggap itu bagian dari suasana game. Tapi ada sesuatu dalam caranya berbicara, cara matanya memandang ke atas sejenak sebelum kembali fokus, yang membuatku merasa- mungkin ini lebih dari sekadar mengagumi grafik dalam game."

    "Beberapa detik berlalu dalam keheningan, hanya diiringi suara angin lembut. Tapi tiba-tiba, suara geraman rendah terdengar dari bawah. Aku langsung siaga."

    raden "\"Kak! zombie nya dateng lagi!\""

    "Kami terus bermain, saling melindungi punggung masing-masing, hingga akhirnya misi kami selesai. Aku dan Kak Tessa berhasil menyelamatkan diri dari invasi zombie dan mendapatkan skor yang cukup tinggi."

    stop music fadeout 2.0

    scene black with dissolve
    with Pause(0.3)

    scene bg lt_6_pasca_ramai with dissolve:
        zoom 0.5

    show raden kasual_hehe at raden_default:
        xalign -0.2
    show tessa kasual_netral at tessa_default:
        xalign 1.0
    with dissolve

    play music tessa_bgm fadein 1.0

    "Ketika headset VR dilepas, aku mengusap keringat di dahiku"

    raden "\"Itu gila banget. Seru, sama bikin deg-degan!\""

    show tessa kasual_senyum3

    voice "audio/vo/tessa/pensasi/pensasi_special_4_iya.flac"
    tessa "\"Iya, aku nggak nyangka bakal seintens itu. Lumayan, lah, pengalaman pertama main VR,\""

    show raden kasual_biasa

    raden "\"Ngomong-ngomong, kasih nilai berapa kak?, kalau aku kasihnya 80 dari 100\""

    show tessa kasual_senyum2

    voice "audio/vo/tessa/pensasi/pensasi_special_5_kalau.flac"
    tessa "\"Huhhh.., kalau aku kasih 65 dari 100\""

    show raden kasual_bingung with dissolve

    raden "\"Ke..kenapa kecil sekali ya\""

    voice "audio/vo/tessa/pensasi/pensasi_special_6_lalu.flac"
    tessa "\"Lalu kenapa kau tinggi sekali nilainya\""

    show raden kasual_canggung with dissolve

    raden "\"Ya... karena itu tadi sudah bagus,\""

    show tessa kasual_senyum with dissolve

    voice "audio/vo/tessa/pensasi/pensasi_special_7_ish.flac"
    tessa "\"Ish ish ish... kau perlu banyak belajar lagi\""

    show raden kasual_ceria with dissolve

    "Kami pun keluar dari booth VR sambil tertawa-tawa, membicarakan pengalaman seru tadi. Aku tidak menyangka, berjalan-jalan dengan Kak Tessa ternyata membawa pengalaman baru yang tidak terlupakan."

    show raden kasual_biasa

    "Kami berdua terus berkeliling melihat booth yang lain, membeli sedikit cemilan, lalu lanjut berkeliling"

    show raden kasual_biasa2
    show tessa kasual_netral

    voice "audio/vo/tessa/pensasi/pensasi_special_8_apakah.flac"
    tessa "\"Apakah... tidak, atau mungkinkah..?\""

    "Aku yang merasa ada yang aneh setelah melihat Tessa sedikit diam dari tadi pagi"

    show raden kasual_bingung

    raden "\"Kak, ada apa?\""

    show tessa kasual_senyum2

    voice "audio/vo/tessa/pensasi/pensasi_special_9_oh.flac"
    tessa "\"Oh, aku baik kok...\""

    show raden kasual_biasa2

    raden "\"Oke\""

    "Kami pun lanjut berkeliling dan tanpa diketahui hari pun sudah mulai sore, waktu memang cepat berlalu saat kita sedang bersenang-senang"

    voice "audio/vo/tessa/pensasi/pensasi_special_10_untuk.flac"
    tessa "{i}Untuk saat ini lebih baik endak usah dipikirin{/i}"

    voice "audio/vo/tessa/pensasi/pensasi_special_11_sudah.flac"
    tessa "\"Sudah mau sore ini, aku mau balik ya\""

    menu:
        "Ikut Kak Tessa":
            show raden kasual_biasa

            raden "\"Aku ikut dong, sekalian satu jalan\""

            voice "audio/vo/tessa/pensasi/pensasi_4_1_1_boleh.flac"
            tessa "\"Boleh aja\""

            show raden kasual_ceria

            raden "\"Rasanya kayak lagi kencan aja\"" 

            show raden kasual_panik
            show tessa kasual_kesal

            voice "audio/vo/tessa/pensasi/pensasi_4_1_2_eh.flac"
            tessa "\"Ehh?? kenapa tiba-tiba-\"" with hpunch

            raden "\"Bentar-bentar- Jangan asal serang-\""

            show raden kasual_canggung

            show tessa kasual_senyum2

            voice "audio/vo/tessa/pensasi/pensasi_4_1_3_maaf.flac"
            tessa "\"Maaf tadi reflek aja, tapi kenapa tiba-tiba ngomong gitu?\""

            show raden kasual_gugup

            raden "\"Maaf hanya kepikiran aja karena kita hanya jalan berdua aja\""

            voice "audio/vo/tessa/pensasi/pensasi_4_1_4_kau_ini.flac"
            tessa "\"Kau ini ada-ada aja\""

            "Tessa segera menyembunyikan wajahnya yang memerah, terlihat jelas dia sedang menahan malu."

            show raden kasual_bingung with dissolve

            "Aku hanya bisa mengernyit bingung, tidak tahu apa yang sebenarnya dia pikirkan."
            
            show raden kasual_canggung

            "Kami pun melanjutkan langkah menuju booth. Sepanjang perjalanan, suasana terasa canggung- tidak ada satu kata pun yang keluar dari mulut kami. Hanya derap langkah yang terdengar di antara kesunyian."

            "Setelah menghantarkan Kak Tessa ke booth-nya, aku memutuskan untuk pamit, mencoba menghilangkan rasa canggung yang masih terasa."

            show raden kasual_biasa

            raden "\"Oke, sampai jumpa kak\""

            show tessa kasual_senyum

            voice "audio/vo/tessa/pensasi/pensasi_4_1_5_iya.flac"
            tessa "\"Iya, sampai jumpa\""

            scene black with dissolve

            raden "\"Oke, sekarang pulang aja ahh, mau lanjut nonton film\""

            ## END

        "Pamit":
            show raden kasual_tersenyum

            raden "\"Kalau gitu aku mau balik juga, hati-hati ya\""

            voice "audio/vo/tessa/pensasi/pensasi_4_2_1_makasih.flac"
            tessa "\"Makasih ya\""

            show raden kasual_ceria

            raden "\"Iya, makasih atas kencan nya\""

            show tessa kasual_kesal

            voice "audio/vo/tessa/pensasi/pensasi_4_2_2_ehh.flac"
            tessa "Eehhh??? Ini bukan kencan! Jangan asal ngomong kayak gitu!" with hpunch

            "Tessa cepat-cepat berbalik, melangkah pergi sambil menyembunyikan pipinya yang semakin merah."

            scene black with dissolve
            with Pause(0.5)

            ## END

    return