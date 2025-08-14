init:
    transform pan_right:
        xalign 0.0
        linear 3.0 xalign 0.7

label pensasi_sekar_scene3:
    scene bg auditorium with dissolve:
        zoom 0.5

    show raden kasual_biasa:
        zoom 0.48 xalign 0.0 yalign 0.1
    show sekar kemeja_biasa:
        zoom 1.15 xalign 1.0 yalign 0.05
    with dissolve

    show sekar kemeja_bingung
    voice "audio/vo/sekar/pensasi/pensasi_3_1_kira_kira.flac"
    sekar "\"Kira-kira enaknya mau menjelajahi booth dimana nih den?\""

    show raden kasual_bingung
    raden "\"Hmm.. Nggak kepikiran booth mana yang mau ku coba\""

    voice "audio/vo/sekar/pensasi/pensasi_3_2_menurutmu.flac"
    sekar "\"Menurutmu gimana den? Ada yang menarik nggak?\""
    
    show raden kasual_ceria
    raden "\"Di depan gedung pasca kudengar ada kendaraan yang bisa coba sih kak, kesana yuk\""

    #depan pasca
    scene bg lapmer with dissolve:
        zoom 0.5

    show raden kasual_biasa:
        zoom 0.48 xalign 0.0 yalign 0.1
    show sekar kemeja_biasa:
        zoom 1.15 xalign 1.0 yalign 0.05
    with dissolve

    "Di depan gedung berdiri sebuah booth kecil dengan kendaraan kecil menyerupai motor roda tiga. Cat nya berwarna merah mengkiap, seperti baru."

    show sekar kemeja_bingung

    voice "audio/vo/sekar/pensasi/pensasi_3_3_itu.flac"
    sekar "\"Itu kendaraan yang kamu maksud den?\""

    show sekar kemeja_biasa
    show raden kasual_tersenyum

    raden "\"Iya kak\""
    
    raden "\"Btw, mau naik itu kak?\""

    show sekar kemeja_ceria

    voice "audio/vo/sekar/pensasi/pensasi_3_4_ayo.flac"
    sekar "\"Ayo, tapi aku yang bonceng ya?\""

    show raden kasual_gugup

    raden "\"Eh?\""

    voice "audio/vo/sekar/pensasi/pensasi_3_5_dah_ayo.flac"
    sekar "\"Dah ayo, sekali-kali kamu dibonceng cewek\""

    ## SPECIAL MOMENT

    play music sekar_bgm fadein 1.0

    scene blank with dissolve

    show sekar_pensasi1 at pan_right:
        zoom 2.0
    with dissolve
    
    pause 2.0

    scene sekar_pensasi1 with dissolve
    pause 1.0

    "Mesin kendaraan itu mulai berbunyi, Sekar langsung memutar kemudi dengan semangat. Kendaraan melaju perlahan pada awalnya, tapi tak butuh waktu lama sebelum Kak Sekar mulai menambah kecepatan."

    show sekar_pensasi2 with dissolve

    raden "\"{size=+10}AAAAAKKKKHHH{/size}\"" with vpunch

    raden "\"Pelan-pelan kakk!!\""

    #show sekar kemeja_senyum_lebar

    voice "audio/vo/sekar/pensasi/pensasi_3_6_ngomong_apa.flac"
    sekar "\"Ngomong apa den?\""

    raden "\"Jangan ngebut kakk!!\"" with vpunch

    #show sekar kemeja_ceria

    voice "audio/vo/sekar/pensasi/pensasi_3_7_masih_normal.flac"
    sekar "\"Masih normal ini...\""

    voice sustain

    sekar "\"Biasanya aku lebih kenceng pas naik mobil\""

    raden "\"Jangan samain ama mobil!!\"" with vpunch

    voice "audio/vo/sekar/pensasi/pensasi_3_8_pegangan.flac"
    sekar "\"Pegangan!\""

    raden "\"HAA??!!\""

    #show sekar kemeja_tertawa_lepas

    "Namun, bukannya memperlambat, Kak Sekar malah menambah sedikit kecepatan. Angin mulai terasa lebih kencang, dan rambut Kak Sekar berkibar indah di bawah cahaya matahari."

    "Dalam situasi yang kacau itu, Aku justru terpaku memandangi senyum Kak Sekar."

    "Ada sesuatu tentang caranya tertawa lepas, seperti anak kecil yang menemukan kebahagiaan di tengah hal sederhana."

    "Dari arah belakang, tiba-tiba terdengar suara penjaga booth memanggil sambil melambaikah tangan panik, menyuruh kita untuk berkendara lebih pelan."

    hide sekar_pensasi2 with dissolve
    show sekar_pensasi1 with dissolve

    "Mendengarnya Kak Sekar langsung memelankan kecepatannya dan melakukan perputaran untuk kembali."

    scene bg lapmer with dissolve:
        zoom 0.5

    show raden kasual_pusing:
        zoom 0.48 xalign 0.0 yalign 0.1
    show sekar kemeja_senyum_lebar:
        zoom 1.15 xalign 1.0 yalign 0.05
    with dissolve

    sekar "\"Gimana den? Kubenceng rasanya nyaman kan?\""

    raden "\"kebalikannya kak\""

    show sekar kemeja_ceria

    voice "audio/vo/sekar/pensasi/pensasi_3_9_maaf.flac"
    sekar "\"Maaf-maaf\""

    show raden kasual_menghela_napas with dissolve

    raden "\"Lain kali jangan kayak gitu lagi kak\""

    raden "\"Rasanya jadi kayak jantungku mau copot\""

    show sekar kemeja_bicara

    voice "audio/vo/sekar/pensasi/pensasi_3_10_oiya.flac"
    sekar "\"Oh iya den, aku ada pertanyaan nih\""

    show raden kasual_bingung

    raden "\"Apa tuh kak?\""

    voice "audio/vo/sekar/pensasi/pensasi_3_11_ada.flac"
    sekar "\"Ada alasan tertentu nggak dek kamu bantu aku?\""

    menu:
        "Nggak ada alasan tertentu, cuma pengen aja":
            show raden kasual_tersenyum
            show sekar kemeja_biasa

            raden "\"Nggak ada alasan tertentu sih kak, cuma pengen aja\""

            raden "\"Kita nggak tau apa yang akan tejadi di masa depan\""

            show raden kasual_ceria

            raden "\"Jadi, aku ingin memaksimalkan hidupku dengan berbuat baik\""

            "Kak Sekar terdiam. Ia menatapku dalam, seperti mencari sesuati di balik kata-kataku"
        
            voice "audio/vo/sekar/pensasi/pensasi_3_1_1_hmm.flac"
            sekar "\"hmm begitu den\""

            show raden kasual_biasa

            raden "\"Emangnya kenapa tanya itu kak?\""

            "Sekar tersenyum kecil, lalu memalingkan wajah, seolah ingin menyembunyikan ekspresi yang sulit kuartikan."

            voice "audio/vo/sekar/pensasi/pensasi_3_1_2_cuma.flac"
            sekar "\"Cuma pengen tanya saja\""

        "Karena pahlawan H*mm*l akan melakukannya":
            show raden kasual_serius
            show sekar kemeja_biasa

            raden "\"Tentu saja, alasannya karena pahlawan {i}H*mm*l{/i} pasti melakukannya\""
        
            show raden kasual_biasa
            show sekar kemeja_tertawa_lepas

            voice "audio/vo/sekar/pensasi/pensasi_3_2_1_tertawa.flac"
            sekar "\"Hahahahaha\""

            voice sustain

            "Melihat tawa kak Sekar seperti ini, membuat diriku terasa meleleh. Tawanya yang manis membuat diriku tak sadarkan diri sejenak."

            show raden kasual_tersenyum

            raden "\"Selucu itu kah kak?\""

            show sekar kemeja_ceria

            voice "audio/vo/sekar/pensasi/pensasi_3_2_2_gak_ekspek.flac"
            sekar "\"Nggak expect aja\""
        
        "Kepo nih ye":
            show raden kasual_hehe

            raden "\"Ciee, kepo nih kak?\""

            show sekar kemeja_marah fikit

            sekar "\"Dih, orang nanya doang\""

            show raden kasual_gugup
            
            raden "\"Canda doang kak, jangan marah\""

            show sekar kemeja_merengut

            sekar "\"...\""

    jump pensasi_sekar_ending

    return