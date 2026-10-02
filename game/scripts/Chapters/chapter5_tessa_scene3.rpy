label chapter5_tessa_scene3:
    #bg kantin
    scene bg depan_auditorium with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    show raden kasual_biasa2:
        zoom raden_default.zoom
        xalign 0.0
        yalign raden_default.yalign
    show santo kemeja_netral:
        zoom santo_default.zoom
        yalign 0.08
        xalign 1.0
    with dissolve

    "Kami berdua memesan makan dan minuman kemudian mencari tempat duduk di kantin."

    "Setelah duduk, Santo kemudian mengeluarkan laptopnya."

    raden "\"hmm, nonton anime yuk\""

    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    santo "\"gas\""

    "Waktu Santo mencari anime, aku melihat ada orang yang tidak membuang sampah makanannya dan hanya diletakkan di atas meja."

    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Kalau dia disini, pasti udah langsung marah\""

    santo "\"hmm? Siapa?\""

    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Aisyah\""

    santo "\"oh, kenapa?\""

    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Tuhh\""

    santo "\"Owh, pantes\""

    menu:
        "Percakapan lama":
            jump chapter5_tessa_scene3_choice3_1
        "Percakapan nostalgia":
            jump chapter5_tessa_scene3_choice3_2

    return 

label chapter5_tessa_scene3_choice3_1:
    raden "\"Jadi keinget sama Aisyah yang marah sama orang yang buang sampah sembarangan\""

    santo "\"Berkat akulah itu, nasib baik aku datang bawa bantuan\""

    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"iya makasih ya\""

    jump chapter5_tessa_scene4

    return

label chapter5_tessa_scene3_choice3_2:
    raden "\"Jadi keingat sama orang yang pernah buang sampah sembarangan\""

    santo "\"Lah iya, kok dia nggak keliatan ya?\""

    show raden kasual_hehe:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Sembunyi di pojokan mungkin\""

    santo "\"wedehhh\""
    
    "Kami pun tertawa dengan puas"

    jump chapter5_tessa_scene4

    return
