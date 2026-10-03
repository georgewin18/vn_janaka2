define chapter4_sekar_choice2_2_choosen = False

label chapter4_sekar_scene2:
    #kelas
    scene bg auditorium with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kasual_biasa2 with dissolve:
        zoom raden_default.zoom
        xalign 0.5
        yalign raden_default.yalign

    play music campus fadein 1.0

    raden "\"Akhirnya selesai juga\""

    if (chapter4_sekar_choice1_2_choosen == True):
        #show santo
        show raden:
            xalign 0.0
            zoom raden_default.zoom
            yalign raden_default.yalign
        show santo kemeja_bicara:
            zoom santo_default.zoom
            yalign 0.08
            xalign 1.0
        with moveinright

        santo "\"Kok bisa gitu sampe telat den\""

        show raden kasual_kesal:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"Ih diem deh! Suka banget ngetawain penderitaan temen sendiri!\""

        raden "\"Tadi padahal udah bangun loh! Cuman tadi mau tidur lagi bentar malah kebablasan...\""

        santo "\"Salahmu sendiri, udah tau bentar lagi mau kuliah malah tidur lagi\""

        show raden kasual_menghela_napas:

            zoom raden_default.zoom
            yalign raden_default.yalign
        raden "\"Dah lah, ga akan kulakuin lagi...\""
    
    #show santo
    show raden:
        xalign 0.0
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kemeja_bicara:
        zoom santo_default.zoom
        yalign 0.08
        xalign 1.0
    with moveinright

    santo "\"Habis ini kamu mau ngapain den?\""

    "Mendapatkan pertanyaan tersebut, AKu tiba-tiba merasakan rasa lapar yang membuatku memutuskan untuk menuju ke Kantin"

    raden "\"Mau ke kantin nih, mau ikut?\""

    santo "\"Yaudah ayok kalo gitu\""

    hide raden
    hide santo
    with moveoutleft

    #kantin
    scene bg depan_auditorium with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    
    show raden kasual_biasa2 with dissolve:
        zoom raden_default.zoom
        xalign 0.5
        yalign raden_default.yalign

    raden "\"Hmmm, beli Ayam Malay enak nih. Tapi yang ngantri banyak banget\""

    "Setelah berpikir, Aku memutuskan untuk ikut antri Ayam Malaysia saja."

    raden "\"Demi Ayam Malay, kurasa mengantri gapapa lah\""

    "Setelah mengantri dan membeli Ayam Malaysia, Aku bingung untuk duduk dimana, dengan keadaan kantin PENS yuang sangat ramai pada siang hari."

    "Ketika Mencari, Raden mendengar seseorang yang memanggilnya."

    santo "\"Raden!\""

    "Menoleh ke belakang, Aku melihat Santo yang sedang makan. Melihat kursi di samping Santo kosong, aku duduk di sana."

    show raden with moveinright:
        xalign 0.0
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo kemeja_netral with dissolve:
        zoom santo_default.zoom
        xalign 1.0
        yalign 0.08

    "Kami basa-basi seperti biasanya, sampai di tengah-tengah ada Kak Sekar yang mendatangi kami."

    #show sekar
    show raden:
        xalign -0.2
        zoom raden_default.zoom
        yalign raden_default.yalign
    show santo:
        xalign 0.5
        zoom santo_default.zoom
    show sekar kemeja_bicara:
        zoom sekar_default.zoom
        xalign 1.1
        yalign sekar_default.yalign
    with moveinright

    voice "audio/vo/sekar/chapter4/chapter4_1_3_halo.ogg"
    sekar "\"Halo, nggak ganggu kan?\""

    raden "Nggak, Kak,"

    voice "audio/vo/sekar/chapter4/chapter4_1_4_kursi_pada_penuh.ogg"
    sekar "\"Kursi pada penuh, Aku duduk di sini gapapa kan?\""

    raden "\"Silahkan, Kak,\""

    if (chapter4_sekar_choice1_1_1_choosen == True):
        voice "audio/vo/sekar/chapter4/chapter4_1_5_oh_iya.ogg"
        sekar "\"Oh iya, Pagi tadi makasih sudah bantuin ya den\""

        raden "\"Aman kak\""

        santo "\"Wah-wah, ternyata tadi pagi beneran ngelamunin cewek toh~\""

        raden "\"Dah dibilangin gak kek gitu\""

        santo "\"Iya-iya den\""

    "Setelah itu keheningan menyelimuti pembicaraan"

    show sekar kemeja_biasa:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    raden "{i}Enaknya ngomongin apa ya...{/i}"

    menu:
        "Ngomongin tugas ah, tapi aku males banget...":
            jump chapter4_sekar_scene2_choice2_1
        "Ngomongin anime aja kali yak...":
            $ chapter4_sekar_choice2_2_choosen = True
            jump chapter4_sekar_scene2_choice2_2

    return

label chapter4_sekar_scene2_choice2_1:
    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Nasib tugasmu gimana to? Dah banyak yang selesai?\""

    show santo kemeja_bicara:

        zoom santo_default.zoom
    santo "\"Masih setengah sih, nggak mau menumpuk banyak tugas. Kalau terlalu numpuk bakal sangat merepotkan\""

    show raden kasual_capek:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Rajin banget, tugasku masih numpuk banyak nih...\""

    santo "\"Lah, nggak kamu kerjakan den?\""

    raden "\"Niatnya sih pengen, aku juga sebenarnya nggak mau tugas terlalu numpuk. Tapi, rasa malas ini terlalu luar biasa...\""

    show sekar kemeja_bingung:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    voice "audio/vo/sekar/chapter4/chapter4_2_1_kenapa.ogg"
    sekar "\"Kenapa nggak kamu kerjakan aja den?\""

    raden "\"Ugghh, terlalu malas kak...\""

    show sekar kemeja_teriak:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    voice "audio/vo/sekar/chapter4/chapter4_2_2_kalo_ditunda.ogg"
    sekar "\"Kalo ditunda terus nanti kamu semakin malas loh\""

    raden "\"Iya sih kak. Tapi hari ini aku lagi malas banget, jadi besok aja\""

    show sekar kemeja_ragu:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    "Melihat sifatku yang terlalu malas, kak Sekar tidak tau lagi harus berkata apa, jadi dia mempertanyakan alasan dia duduk di sini"

    jump chapter4_sekar_scene3

label chapter4_sekar_scene2_choice2_2:
    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Kalian nonton anime kah?\""

    "Santo dan Kak Sekar serentak mengangguk"

    raden "\"Kalian ada genre anime favorit nggak?\""

    show santo kemeja_bicara:

        zoom santo_default.zoom
    santo "\"Kalo aku sih Mecha\""

    raden "\"Kelas! sama To, aku juga suka Mecha\""

    show sekar kemeja_bicara:

        zoom sekar_default.zoom
        yalign sekar_default.yalign
    voice "audio/vo/sekar/chapter4/chapter4_2_3_kalau_aku.ogg"
    sekar "\"Kalau aku sukanya Slice of Life, animenya bikin hati adem. Jadi enak ditontonnya\""

    raden "\"Ada rekomendasi nggak, satu aja\""

    "Kami asyik membicarakan anime favorit masing-masing, sampai tidak terasa makanan kami sudah habis."

    jump chapter4_sekar_scene3
