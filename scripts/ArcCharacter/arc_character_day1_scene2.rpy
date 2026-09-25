label arc_character_day1_scene2:
    scene bg jalan_d4_kantin with dissolve:
        zoom 0.5

    show raden kasual_biasa at raden_default:
        xalign -0.5
    show santo kasual_netral at santo_default:
        xalign 0.45
    show erin kasual_netral at erin_default:
        xalign 1.1
    with dissolve

    santo "\"Fiuh... baru juga awal semester, udah langsung disuruh tugas ribet gini segala, Laprak tulis lagi\""

    erin "\"Memang biar langsung adaptasi kali ya. Tapi tugasnya seru sih, topiknya bisa fleksibel.\""

    show raden kasual_tersenyum

    raden "\"Asal jangan nulisnya mepet deadline... kayaknya berat juga kalau nunggu-nunggu.\""

    show raden kasual_biasa

    erin "\"Kalau mau, kita bisa mulai bahas sekarang. Mumpung belum ada kelas lanjut.\""

    show santo kasual_bicara

    santo "\"Bahas sekarang boleh... tapi perutku udah demo dari tadi.\""

    show santo kasual_netral
    show raden kasual_tersenyum

    raden "\"Hm... ya udah, kita makan dulu aja. Sambil ngobrol santai, siapa tahu malah nemu ide di tengah makan.\""

    show santo kasual_senyum_lebar

    santo "\"Nah, itu baru ide brilian.\""

    scene bg kantin with dissolve:
        zoom 0.5

    show raden kasual_biasa at raden_default:
        xalign -0.5
    show santo kasual_netral at santo_default:
        xalign 0.45
    show erin kasual_netral at erin_default:
        xalign 1.1
    with dissolve

    "Sesampainya kami di kantin. kami melihat ada keributan kecil di kejauhan."

    show santo kasual_terkejut

    santo "\"Eh, itu Aisyah, kan?\""

    "Erin menatap serius. Dia memperhatikan situasi tanpa banyak bicara, tapi jelas ada kekhawatiran di matanya."

    "Aisyah terlihat sedang berbicara dengan seorang pria berkemeja coklat. Dari jarak sini, jelas kelihatan dia habis merokok—dan kelihatannya mereka berdebat soal itu."

    show raden kasual_serius

    raden "\"Sepertinya ada masalah… Kita samperin aja.\""

    hide raden
    hide santo
    hide erin
    with dissolve

    "Lantas Aisyah berjalan mendekat pada hal tersebut, yang ternyata merupakan seorang lelaki yang mengenakan kemeja coklat lengan pendek. Dari asap yang mengepul mulutnya, sepertinya ia baru saja merokok."

    show aisyah casual_serius at aisyah_default:
        xalign 0.5
    with dissolve

    aisyah "\"Permisi, tapi kalau bisa tolong jangan buang puntung rokok sembarangan di sini!\""

    "Kelihatannya Aisyah berusaha bersikap sopan dan lembut dengannya, meski terdengar sekali kalau nada bicaranya meninggi di akhir."

    anon "—Hah?"

    show aisyah casual_kesal with dissolve

    "{i}Gawat, kelihatannya si perokok itu marah karena ditegur. Aisyah akan mendapat masalah dengannya!{/i}"

    "{i}Apa yang harus kulakukan?{/i}"

    menu:
        "Aku support kamu, kawan, ayo kita buang sampah sembarangan!!!":
            jump arc_character_day1_scene2_afterchoice1
        "Menenangkan Aisyah":
            jump arc_character_day1_scene2_afterchoice2

    return

label arc_character_day1_scene2_afterchoice1:
    show aisyah at aisyah_default:
        xalign 1.0
    with moveinleft

    show raden kasual_tersenyum at raden_default:
        xalign -0.2
    with dissolve

    raden "\"Aku support kamu, kawan, ayo kita buang sampah sembarangan!!!\""

    show raden kasual_gugup with dissolve

    "Dia tertawa lebar, sementara aku hanya tersenyum kaku, merasa sedikit bersalah. Mungkin ini bukan ide yang bagus, tapi ya sudahlah..."

    anon "\"Hahahaha!, boleh juga kamu\""

    "Belum sempat aku lanjutkan, Aisyah menatapku tajam dari samping."

    aisyah "\"Jangan malah bercanda, den,\""

    raden "\"Eh, cuma bercanda kok. Lagipula, siapa tahu dia langsung sadar.\""

    aisyah "\"Bercanda juga ada batasnya—\""

    show raden kasual_canggung
    show aisyah casual_serius

    "Tiba tiba mas perokok itu memotong dengan marah."

    anon "\"He! Lu itu maba kan? Enak kali lu ngatur-ngatur gua!\""

    show raden at raden_default:
        xalign -0.5
    show aisyah at aisyah_default:
        xalign 0.5
    show sekar kasual_tegas at sekar_default:
        xalign 1.2
    with moveinright

    "Belum sempat aku berpikir bagaimana menebus kesalahanku, tiba-tiba Santo dan Erin muncul diikuti Sekar, yang juga merupakan anggota BEM yang dikenal tegas."

    sekar "\"Eh, ada apa ini?\""

    "Sekar dengan nada serius, menatap kami bertiga."

    "Sebelum ada yang sempat menjelaskan, pria bebal tadi, yang masih berdiri santai di dekat semak-semak, mendadak gugup. Tanpa banyak bicara, dia kabur begitu saja, meninggalkan kami dalam kebingungan."

    show raden at raden_default:
        xalign -0.7
    show aisyah at aisyah_default:
        xalign 0.2
    show sekar at sekar_default:
        xalign 0.75
    show santo kasual_bicara at santo_default:
        xalign 1.3
    with moveinright

    santo "\"Ya ampun, kok lari sih?\""

    "Erin mendekat, masih tenang namun sorot matanya waspada."

    hide santo with dissolve
    show erin kasual_netral at erin_default:
        xalign 1.25
    with dissolve

    erin "Dia pergi begitu saja... mencurigakan."

    "Sekar melihat ke arah pria itu yang kabur"

    show sekar kasual_teriak

    sekar "\"Aku kejar dulu orang itu, siapa tahu dia bawa barang terlarang.\""

    hide sekar with moveoutright

    show erin at erin_default:
        xalign 0.7
    show santo kasual_netral at santo_default:
        xalign 1.35
    with moveinright

    "Aisyah melirik ke arah Santo dan Erin, lalu matanya tertuju ke Erin. Dia sempat terdiam sejenak, seperti baru sadar sesuatu."

    show aisyah casual_sedih with dissolve

    aisyah "\"Terima kasih ya… dan… eh, maaf banget sudah merepotkan Santo dan Ern—\""

    "Dia berhenti sebentar, ekspresinya sedikit bingung, matanya menatap Erin seolah baru sadar tidak mengenalnya."

    "Erin tersenyum lembut, pembawaannya tetap anggun seperti biasa."

    erin "\"Sama-sama, tadi kamu benar kok. Namaku Erin.\""

    "Erin lalu melirik ke arahku, senyuman lembutnya mengandung kode halus, hampir seperti menggoda."

    erin "\"Bener kan?\""

    show raden kasual_gugup

    raden "\"I-iya... bener.\""

    "Tapi kemudian… Aisyah menatapku tajam, lagi. Kali ini, tatapan itu terasa lebih menusuk."

    show aisyah casual_kesal

    aisyah "\"Bener?!\"" with vpunch

    show raden kasual_panik

    raden "\"Eh... aku cuma bercanda tadi..\""

    raden "\"...Lagipula, itu reverse psychology biar dia bingung!\""

    show raden kasual_canggung
    show aisyah casual_menghela_napas with dissolve
    pause 0.3

    "Aisyah mendengus, lalu menghela napas panjang."

    show aisyah casual_senyum with dissolve

    aisyah "\"Iya-iya, terima kasih, Raden,\""

    "katanya setengah hati, dengan nada yang jelas-jelas tidak percaya."

    hide aisyah with moveoutleft

    show raden at raden_default:
        xalign -0.5
    show erin at erin_default:
        xalign 0.5
    show santo at santo_default:
        xalign 1.2
    with moveinright

    "Dia lalu berbalik dan berjalan mendahului kami, meninggalkan aku yang hanya bisa menggaruk kepala dengan senyum canggung."

    "Santo menepuk pundakku pelan."

    show santo kasual_senyum

    santo "\"Bercanda itu liat kondisi juga, Den.\""

    jump arc_character_day1_scene3

    return

label arc_character_day1_scene2_afterchoice2:
    show aisyah at aisyah_default:
        xalign 1.0
    with moveinleft

    show raden kasual_canggung at raden_default:
        xalign -0.2
    with dissolve

    raden "\"Tenang, kita bicarakan baik-baik dulu,\""

    "Aku berjalan mendekati Aisyah."

    raden "\"Aisyah, kamu benar, tapi bukan berarti kamu bisa dengan impulsif...\""

    raden "\"dan untuk Mas nya, rokok memang nggak salah tapi dilarang di lingkungan kampus, apalagi membuangnya sembarangan.\""

    show aisyah casual_serius with dissolve

    "Aisyah memandangku dengan raut wajah yang lebih tenang."

    "Sementara itu, sepertinya Mas Perokok tadi belum sepenuhnya ikhlas—terlihat dari wajahnya sepertinya ia malah marah."

    anon "\"Hah?! Lu itu maba kan? Enak kali lu ngatur-ngatur gua!\""

    show raden at raden_default:
        xalign -0.5
    show aisyah at aisyah_default:
        xalign 0.5
    show sekar kasual_tegas at sekar_default:
        xalign 1.2
    with moveinright

    "Belum sempat aku berpikir bagaimana menebus kesalahanku, tiba-tiba Santo muncul diikuti Sekar, seorang anggota BEM yang dikenal tegas."

    sekar "\"Eh, ada apa ini?\""

    "Sekar dengan nada serius, menatap kami bertiga."

    "Sebelum ada yang sempat menjelaskan, pria bebal tadi, yang masih berdiri santai di dekat semak-semak, mendadak gugup. Tanpa banyak bicara, dia kabur begitu saja, meninggalkan kami dalam kebingungan."

    show raden at raden_default:
        xalign -0.7
    show aisyah at aisyah_default:
        xalign 0.2
    show sekar at sekar_default:
        xalign 0.75
    show santo kasual_bicara at santo_default:
        xalign 1.3
    with moveinright

    santo "\"Ya ampun, kok lari sih?\""

    "Erin mendekat, masih tenang namun sorot matanya waspada."

    hide santo with dissolve
    show erin kasual_netral at erin_default:
        xalign 1.25
    with dissolve

    erin "\"Dia pergi begitu saja… mencurigakan.\""

    "Sekar melihat ke arah pria itu yang kabur"

    show sekar kasual_teriak

    sekar "\"Aku kejar dulu orang itu, siapa tahu dia bawa barang terlarang.\""

    hide sekar with moveoutright

    show erin at erin_default:
        xalign 0.7
    show santo kasual_netral at santo_default:
        xalign 1.35
    with moveinright

    "Tapi yang terpenting, setidaknya sudah tidak ada keributan lagi untuk sekarang."

    show raden kasual_serius with dissolve

    raden "\"Aisyah lain kali hati-hati ya..., walaupun kamu benar bukan berarti kamu selalu bisa langsung konfrontasi orangnya langsung seperti tadi,\""

    show aisyah casual_sedih with dissolve

    aisyah "\"... Oke,\""

    "Aisyah mengangguk pelan, dengan wajah sedikit menahan malu."

    show aisyah casual_gugup
    show raden kasual_canggung
    with dissolve

    aisyah "\"—Sebenarnya aku mau bilang kalau agak kaget kamu tiba-tiba ngomong gitu, soalnya agak cringe kalau kamu yang ngomong.\""

    "Aisyah melirik ke arah Santo dan Erin, lalu matanya tertuju ke Erin. Dia sempat terdiam sejenak, seperti baru sadar sesuatu."

    show aisyah casual_senyum with dissolve

    aisyah "\"Terima kasih ya… dan… eh, maaf banget sudah merepotkan Santo dan Ern—\"" 

    "Dia berhenti sebentar, ekspresinya sedikit bingung, matanya menatap Erin seolah baru sadar tidak mengenalnya."

    "Erin tersenyum lembut, pembawaannya tetap anggun seperti biasa."

    erin "\"Sama-sama, tadi kamu benar kok. Namaku Erin.\""

    "Erin lalu melirik ke arahku, senyuman lembutnya mengandung kode halus, hampir seperti menggoda."

    erin "\"Bener kan?\""

    show raden kasual_hehe with dissolve

    raden "\"I-iya... bener.\""

    "Santo hanya mengangguk santai, seolah semua ini bukan hal besar baginya."

    show santo kasual_bicara

    santo "Udah beres, yuk lanjut ngantin."

    jump arc_character_day1_scene3

    return