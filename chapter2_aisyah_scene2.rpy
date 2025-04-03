define chapter2_aisyah_scene2_choice1_choosen = False

label chapter2_aisyah_scene2:
    scene bg kantin with dissolve:
        zoom 0.5

    show raden kemeja_biasa with dissolve:
        zoom 0.54 xalign 0.0 yalign 0.05

    show aisyah kemeja_bicara with dissolve:
        zoom 0.34 xalign 0.9 yalign -1.0

    "Mendadak perhatian Aisyah beralih pada sesuatu—yang mungkin dibelakangku."

    hide raden

    show aisyah kemeja_penasaran with moveinleft:
        xalign 0.1

    show raden kemeja_biasa at flip with dissolve:
        zoom 0.54 xalign 1.0 yalign 0.05

    #Aisyah serius

    "Lantas Aisyah berjalan mendekat pada hal tersebut, yang ternyata merupakan seorang lelaki yang mengenakan kemeja coklat lengan pendek. Dari asap yang mengepul mulutnya, sepertinya ia baru saja merokok."

    aisyah "\"Permisi, tapi kalau bisa tolong jangan buang puntung rokok sembarangan di sini!\""

    "Kelihatannya Aisyah berusaha bersikap sopan dan lembut dengannya, meski terdengar sekali kalau nada bicaranya meninggi di akhir."

    anon "\"—Hah?\""

    #Aisyah Kesal

    "Gawat, kelihatannya si perokok itu marah karena ditegur. Aisyah akan mendapat masalah dengannya!"

    #Suasana agak intens

    raden "{i}Apa yang harus kulakukan?{/i}"

    menu:
        "Aku support kamu, kawan, ayo kita buang sampah sembarangan!!!":
            $ chapter2_aisyah_scene2_choice1_choosen = True
        
        "Menenangkan Aisyah":
            $ chapter2_aisyah_scene2_choice1_choosen = False

    if (chapter2_aisyah_scene2_choice1_choosen == True):
        raden "\"Aku support kamu, kawan, ayo kita buang sampah sembarangan!!!\""

        "Dia tertawa lebar, sementara aku hanya tersenyum kaku, merasa sedikit bersalah. Mungkin ini bukan ide yang bagus, tapi ya sudahlah…"

        anon "\"Hahahaha!, boleh juga kamu\""

        "Belum sempat aku lanjutkan, Aisyah menatapku tajam dari samping."

        aisyah "\"Jangan malah bercanda, den,\""

        raden "\"Eh, cuma bercanda kok. Lagipula, siapa tahu dia langsung sadar.\""

        aisyah "\"Bercanda juga ada batasnya—\""

        "Tiba tiba mas perokok itu memotong dengan marah."

    else:
        "Hmmm …"

        "Aisyah benar, bagaimanapun peraturan kampus tidak boleh dilanggar. Membuang puntung rokok sembarangan bisa membuat kantin menjadi kotor, terlebih lagi di sini ada banyak makanan–kudengar puntung rokok bisa sangat beracun."

        "Tapi, kurasa kurang tepat kalau Aisyah sampai harus memarahinya langsung, apalagi orang itu kelihatannya juga tersinggung."

        #Raden canggung

        raden "\"Tenang, kita bicarakan baik-baik dulu,\""

        "Aku berjalan mendekati Aisyah."

        raden "\"Aisyah, kamu benar, tapi bukan berarti kamu bisa dengan impulsif …, dan untuk Mas nya, rokok memang nggak salah tapi dilarang di lingkungan kampus, apalagi membuangnya sembarangan.\""

        "Aisyah memandangku dengan raut wajah yang lebih tenang."

        #Aisyah netral

        "Sementara itu, sepertinya Mas Perokok tadi belum sepenuhnya ikhlas—terlihat dari wajahnya sepertinya ia malah marah."

    anon "\"He! Lu itu maba kan? Enak kali lu ngatur-ngatur gua!\""

    "Belum sempat aku berpikir bagaimana menebus kesalahanku, tiba-tiba Santo muncul diikuti Sekar, yang juga merupakan anggota BEM yang dikenal tegas."

    show raden at flip:
        xalign 1.5
    show aisyah:
        xalign 0.8
    show santo kemeja_biasa at flip:
        zoom 1.35 xalign 8.0 yalign 0.08
    show sekar kemeja_tegas at flip:
        zoom 1.25 xalign 0.2 yalign 0.05
    with moveinleft

    #Santo muncul netral
    #Sekar muncul tegas

    sekar "\"Eh, ada apa ini?\""

    if (chapter2_aisyah_scene2_choice1_choosen == False):
        "Sekar dengan nada serius, menatap kami bertiga."

    "Sebelum ada yang sempat menjelaskan, pria bebal tadi, yang masih berdiri santai di dekat semak-semak, mendadak gugup. Tanpa banyak bicara, dia kabur begitu saja, meninggalkan kami dalam kebingungan."

    if (chapter2_aisyah_scene2_choice1_choosen == True):
        #Santo menatap ke arah pria itu dengan alis terangkat.
        santo "\"Kok lari\""
    else:
        sekar "\"Ya ampun, kok lari sih?\""

    "Sekar hanya menghela napas panjang."

    sekar "\"Pasti ada yang dia sembunyikan. Kalian gak apa-apa kan?\""

    #Suasana netral di kampus

    if (chapter2_aisyah_scene2_choice1_choosen == True):
        raden "\"Enggak, Kak. Untung Santo sama Kak Sekar datang,\""

        "Aisyah sedikit lega. Dia lalu menatap keduanya dengan penuh rasa terima kasih."

        #Aisyah senyum

        aisyah "\"Makasih ya, Santo, Kak Sekar. Masalah ini jadi gak berlarut-larut.\""

        #Sekar netral"

        sekar "\"Bukan masalah,\""

        "Sekar tersenyum kecil. Sedangkan Santo hanya mengangguk santai, seolah ini bukan hal besar baginya."

        #Aisyah Kesal

        "Tapi kemudian… Aisyah menatapku tajam, lagi. Kali ini, tatapan itu terasa lebih menusuk."

        aisyah "\"Dan kamu, Raden…\""

        #Raden Panik

        raden "\"Eh… aku cuma bercanda tadi..\""

        raden "\"...Lagipula, itu reverse psychology biar dia bingung!\""

        aisyah "Aisyah menghela nafas"

        "Aisyah mendengus, lalu menghela napas panjang."

        aisyah "\"Iya-iya, terima kasih, Raden,\"" 

        "katanya setengah hati, dengan nada yang jelas-jelas tidak percaya."

        "Dia lalu berbalik dan berjalan mendahului kami, meninggalkan aku yang hanya bisa menggaruk kepala dengan senyum canggung."

        "Santo menepuk pundakku pelan."

        santo "\"Bercanda itu liat kondisi juga, Den.\""

    else:
        "Tapi yang terpenting, setidaknya sudah tidak ada keributan lagi untuk sekarang."

        raden "\"Aisyah lain kali hati-hati ya …, walaupun kamu benar bukan berarti kamu selalu bisa langsung konfrontasi orangnya langsung seperti tadi,\""

        aisyah "\"… Oke,\""

        "Aisyah mengangguk pelan, dengan wajah sedikit menahan malu."

        aisyah "\"—Sebenarnya aku mau bilang kalau agak kaget kamu tiba-tiba ngomong gitu, soalnya agak cringe kalau kamu yang ngomong.\""

        "Lanjutan ucapan Aisyah terasa menusuk hingga dalam hati, entah kenapa. Meski begitu, ia kembali tersenyum sambil menatap wajahku."

        aisyah "\"Tapi makasih banyak ya.\""

        raden "\"Sama-sama, Aisyah. Aku juga minta maaf lagi ya tentang tadi pagi …\""

        aisyah "Aisyah menggelengkan kepala"

        aisyah "\"ah, nggak apa kok. Lagian kamu ‘kan tadi kamu mepet ke kelas.\""

        santo "Santo, Kak Sekar, makasih juga dan maaf banget sudah merepotkan!"

        #Sekar senyum

        sekar "\"Bukan masalah,\""

        "Sekar tersenyum kecil. Sedangkan Santo hanya mengangguk santai, seolah ini bukan hal besar baginya."

    #Sekar hilang

    jump chapter2_aisyah_scene3

    return
