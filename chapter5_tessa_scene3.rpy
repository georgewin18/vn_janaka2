label chapter5_tessa_scene3:
    #bg kantin
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    show raden biasa:
        zoom 0.23 yalign 0.1 xalign 0.0
    show santo kemeja_biasa:
        zoom 1.15 yalign 0.08 xalign 2.7
    with dissolve

    "Kami berdua memesan makan dan minuman kemudian mencari tempat duduk di kantin."

    "Setelah duduk, Santo kemudian mengeluarkan laptopnya."

    raden "\"hmm, nonton anime yuk\""

    santo "\"gas\""

    "Waktu Santo mencari anime, aku melihat ada orang yang tidak membuang sampah makanannya dan hanya diletakkan di atas meja."

    raden "\"Kalau dia disini, pasti udah langsung marah\""

    santo "\"hmm? Siapa?\""

    raden "\"Aisyah\""

    santo "\"oh, kenapa?\""

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

    raden "\"iya makasih ya\""

    jump chapter5_tessa_scene4

    return

label chapter5_tessa_scene3_choice3_2:
    raden "\"Jadi keingat sama orang yang pernah buang sampah sembarangan\""

    santo "\"Lah iya, kok dia nggak keliatan ya?\""

    raden "\"Sembunyi di pojokan mungkin\""

    santo "\"wedehhh\""
    
    "Kami pun tertawa dengan puas"

    jump chapter5_tessa_scene4

    return