init:
    transform outleft:
        xalign -5.0
    transform bottom:
        yalign -3.0

label chapter5_tessa_scene4:
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    show raden biasa:
        zoom 0.23 yalign 0.1 xalign 0.0
    show santo kemeja_biasa:
        zoom 1.15 yalign 0.08 xalign 2.7
    with dissolve
    
    "Kami berdua mulai menonton anime bersama. Di tengah-tengah adegan yang seru, tiba-tiba seseorang memanggil-"

    anon "\"WOI, KALIAN!\"" with vpunch

    "Aku dan Santo pun langsung terkejut dan badan kami gemetar." 
    
    "Perlahan kami berdua melihat kedepan kemudian kami tambah terkejut mengetahui yang memanggil kami adalah Tessa"

    raden "\"Kenapa tuh?\""

    santo "\"Moga aja bukan kita\""

    show tessa normal:
        zoom 0.39 yalign -0.25 xalign 1.1
    show raden:
        xalign -0.2
    show santo:
        xalign 1.0
    with moveinright

    #show tessa
    raden "\"oiii, Santo gimana nii??\""

    santo "\"Bye Den\""

    #hide santo
    hide santo with MoveTransition(0.2, leave=outleft)

    menu:
        "Pingsan aja lah":
            "Aku pura-pura pingsan di tempat."

            hide raden with MoveTransition(0.3, leave=bottom) 
            with vpunch

            scene black with dissolve
            with Pause(0.3)

            jump chapter5_tessa_scene4
        "Menyapa dengan gugup":
            jump chapter5_tessa_scene4_choice4_2
        "Memilih ikut kabur":
            jump chapter5_tessa_scene4_choice4_3
    return

label chapter5_tessa_scene4_choice4_2:
    show raden:
        xalign 0.0
    show tessa:
        xalign 0.95
    with moveinright

    "Aku pun mulai menyiapkan mental dengan menarik napas kecil walau masih kaget dan takut, saat Tessa mendekat, tubuhku gemetar hebat."

    "Wajahnya yang serius berubah ketika dia menghela napas"
    
    tessa "\"Haahh.. malah kabur orangnya\""

    "Aku menelan ludah, mecoba mengatur kata-kata yang mau keluar dari mulutku."

    raden "\"Huhh...\""

    tessa "\"Kenapa hah?\""

    raden "\"Ngg-nggak ada... mohon maaf,\""

    raden "\"Aku nggak ngapa-ngapain. Tolong jangan ganggu aku kak...\""

    "Tessa mengerutkan kening, lalu terdiam sejenak, tampak bingung dengan apa yang baru saja aku katakan."

    tessa "\"Ganggu kamu? Ngapain aku ganggu kamu?\""

    raden "\"E.. enggak tau\""

    tessa "\"Gitu kenapa takut? Nyapa doang.\""

    pause 1.0

    raden "\"Kak Tessa... aku tahu suara kakak memang biasanya galak, walaupun nggak marah,\""

    raden "\"Tapi kali ini... suara kakak beneran bikin aku merinding, seriusan\""

    tessa "\"Beda gimana?\""

    raden "\"Suara Kak Tessa tadi kayak... benar-benar marah. Jadi keinget yang di deket D4 pas itu...\""

    tessa "\"Hmm? yang mana?\""

    raden "\"Waktu Kak Tessa mbentak Kak Dio dan semuanya langsung diam.\""

    tessa "\"Ah itu. Ya, aku ingat. Kenapa emang?\""

    raden "\"Pas itu, Kak Tessa kayak... serem banget. Semua orang pada takut, Santo yang selalu keliatan santai aja kabur duluan\""

    tessa "\"Oh itu. Yah, aku cuma marah soalnya dia nyelomot aja orangnya.\""

    tessa "\"Kalo nggak ditekan kaya gitu, dia nggak bakal berhenti menyangkal.\""

    tessa "\"Dio emang gitu orangnya, jadinya harus ditegasin dari awal.\""

    raden "\"Tapi ya itu... Kak Tessa tadi suaranya sama kek pas mbentak Kak Dio... makanya sempet takut aku...\""

    tessa "\"Emangnya aku terlihat seburuk itu\""

    pause 1.0

    raden "\"Dipikir-pikir Kak Tessa keren sih... tapi... juga menakutkan...\""

    tessa "\"Ya, tapi sekarang ini aku gak marak kok.\""

    tessa "\"Suaraku memang jadi lebih keras soalnya tenggorokanku lagi sakit.\""

    raden "\"Btw makasih ya kak, udah bantu kita waktu itu\""

    tessa "\"Iya, sama-sama\""

    "Mendengar jawaban Tessa, aku pun tenang tapi agak bingung kemudian hanya menganggukkan kepala, kemudian aku pun pamit ingin pulang, dan akhirnya kami berjalan ke parkiran bersama."

    #bg parkiran
    scene bg lap_futsal with dissolve:
        zoom 0.5

    show raden biasa:
        zoom 0.23 yalign 0.1 xalign 0.0
    show tessa normal:
        zoom 0.39 yalign -0.25 xalign 0.95
    with dissolve

    raden "\"Kenapa nggak pulang sama temenmu Kak?\""

    tessa "\"Masih ada kegiatan mereka\""

    "Ketika kami tiba di area parkir, aku langsung melihat motorku terparkir tidak jauh dari motor Kak Tessa."

    menu:
        "Tanyakan Tessa apakah bisa menjadi teman":
            jump chapter5_tessa_scene4_choice4_2_1
        "Pamit pulang":
            jump chapter5_tessa_neutral_ending

    return

label chapter5_tessa_scene4_choice4_3:
    hide raden with MoveTransition(0.4, leave=outleft)

    #bg parkiran
    scene bg lap_futsal with dissolve:
        zoom 0.5

    show raden biasa with dissolve:
        zoom 0.23 yalign 0.1 xalign 0.5

    "Setelah kabur dari Tessa yang ada di kantin, aku pun menarik napas dan menenangkan diri."

    raden "\"Tunggu? Kenapa aku lari?\""

    "Dengan ekspresi kesal yang bercampur dengan bingung, setelah beberapa saat aku berjalan..."

    show raden with moveinright:
        xalign 0.0
    show tessa normal with dissolve:
        zoom 0.39 yalign -0.25 xalign 0.95

    #show tessa
    raden "\"AAAAAAAAAA\"" with vpunch

    tessa "\"Apaan?\""

    raden "\"Kukira hantu...\""

    tessa "\"Sembarangan!\"" with vpunch

    raden "\"Aa..\""

    tessa "\"A?\""

    raden "\"Ngg-Nggak ada... mohon maaf,\""

    raden "\"Aku nggak ngapa-ngapain. Tolong jangan ganggu aku kak...\""

    "Tessa mengerutkan kening, lalu terdiam sejenak, tampak bingung dengan apa yang baru saja aku katakan."

    tessa "\"Ganggu kamu? Ngapain aku ganggu kamu?\""

    raden "\"E.. enggak tau\""

    tessa "\"Gitu kenapa takut? Nyapa doang.\""

    pause 1.0

    raden "\"Kak Tessa... aku tahu suara kakak memang biasanya galak, walaupun nggak marah,\""

    raden "\"Tapi kali ini... suara kakak beneran bikin aku merinding, seriusan\""

    tessa "\"Beda gimana?\""

    raden "\"Suara Kak Tessa tadi kayak... benar-benar marah. Jadi keinget yang di deket D4 pas itu...\""

    tessa "\"Hmm? yang mana?\""

    raden "\"Waktu Kak Tessa mbentak Kak Dio dan semuanya langsung diam.\""

    tessa "\"Ah itu. Ya, aku ingat. Kenapa emang?\""

    raden "\"Pas itu, Kak Tessa kayak... serem banget. Semua orang pada takut, Santo yang selalu keliatan santai aja kabur duluan\""

    tessa "\"Oh itu. Yah, aku cuma marah soalnya dia nyelomot aja orangnya.\""

    tessa "\"Kalo nggak ditekan kaya gitu, dia nggak bakal berhenti menyangkal.\""

    tessa "\"Dio emang gitu orangnya, jadinya harus ditegasin dari awal.\""

    raden "\"Tapi ya itu... Kak Tessa tadi suaranya sama kek pas mbentak Kak Dio... makanya sempet takut aku...\""

    tessa "\"Emangnya aku terlihat seburuk itu\""

    pause 1.0

    raden "\"Dipikir-pikir Kak Tessa keren sih... tapi... juga menakutkan...\""

    tessa "\"Ya, tapi sekarang ini aku gak marak kok.\""

    tessa "\"Suaraku memang jadi lebih keras soalnya tenggorokanku lagi sakit.\""

    raden "\"Btw makasih ya kak, udah bantu kita waktu itu\""

    tessa "\"Iya, sama-sama\""

    menu:
        "Pamit pulang":
            jump chapter5_tessa_neutral_ending
        "Pulang bareng dan ajak berteman":
            raden "\"Kenapa nggak pulang sama temenmu Kak?\""

            tessa "\"Masih ada kegiatan mereka\""

            "Ketika kami tiba di area parkir, aku langsung melihat motorku terparkir tidak jauh dari motor Kak Tessa."

            jump chapter5_tessa_scene4_choice4_2_1

    return

label chapter5_tessa_scene4_choice4_2_1:
    raden "\"Ka-Kak Tessa, b.. ba.. bagaimana, kalau at.. atau mau tidak kita jadi teman..?\""

    "Di jalan yang sunyi dan di bawah tiang lampu jalan yang bersinar, Kak Tessa yang mendengar ucapanku tersenyum dan mulai tertawa bahagia."

    tessa "\"hahahahahahaha, ku kira ada apa ternyata cuma itu, hahahahaha\""

    raden "\"Oiii, kenapa jadi ketawa sih\""

    tessa "\"hahaha, kau itu lhoo..\""

    tessa "\"bisa-bisanya ngomong gitu.\""

    raden "\"ma...mau bagaimana lagi, a..aku gugup tau...\""

    "Dengan malui, aku mengucapkan kata-kataku sambil mencuri pandang ke arah Tessa. Wajahnya yang biasanya terlihat menakutkan, kiri penuh senyuman, membuatku lupa akan sikapnya sebelumnya. Saat tertawa, keimutannya benar-benar memukau."

    tessa "\"Kenapa melihatku gitu?!\""

    raden "\"tidak ada\""

    tessa "\"Apa iya?\""

    menu:
        "Kak Tessa ternyata imut juga":
            jump chapter5_tessa_scene4_choice4_2_1_1
        "Cari alasan deh, nanti dia marah":
            jump chapter5_tessa_scene4_choice4_2_1_2

    return 

label chapter5_tessa_scene4_choice4_2_1_1:
    raden "\"Bener kok, cuman terkejut melihat kakak yang...\""

    raden "\"...lumayan imut\""

    "Tessa terkejut dan wajahnya langsung memerah seperti tomat."

    raden "{i}Kenapa kalimat barusan keluar dari mulutku?! Astaga, habislah aku! Wahai bumi dan langit, tolong lindungi aku yang sudah pasrah ini!{/i}"

    "Saat sudah mempersiapkan jiwa dan raga untuk dihantam, ternyata Tesas hanya melewatiku begitu saja tanpa berkata apa-apa. Aku yang berdiri di tempatm bengong sesaat."

    raden "{i}Lho? Kok dia nggak marah?{/i}"

    "Aku mulai berjalan perlahan di belakangnya, berusaha tetap tenang, sambil memikirkan nasibku dan arti dari responnya barusan."

    jump chapter5_tessa_good_ending

    return

label chapter5_tessa_scene4_choice4_2_1_2:
    raden "\"Serius kok, aku cuma mikir nanti makan apa ya...\""
    
    "Tessa mengerutkan alis, menatapku dengan pandangan curiga."

    tessa "\"Mikir nanti makan apa? Itu alasanmu?\""

    raden "\"Iya, beneran! Soalnya lagi bingung mau makan nasi goreng atau mie...\""

    tessa "\"Dasar aneh,\""

    "Aku yang melihat itu merasa lega, tapi sekaligus bingung."

    raden "{i}Astaga, aku hampir ketahuan. Tapi... Kok dia gampang percaya ya? Atau jangan-jangan dia tahu aku bohong?{/i}"

    jump chapter5_tessa_neutral_ending

    return
    