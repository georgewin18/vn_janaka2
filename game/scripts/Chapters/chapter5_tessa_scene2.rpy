label chapter5_tessa_scene2:
    #bg kelas
    scene bg auditorium with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    
    show raden kemeja_biasa2:
        zoom raden_default.zoom
        xalign 0.0
        yalign raden_default.yalign
    show santo kemeja_netral:
        zoom santo_default.zoom
        yalign 0.08
        xalign 1.0
    with dissolve

    "Matkul pada sore hari yang aku ikuti pun akhirnya selesai dan hari udah mau malem."

    "Kami pun berbincang sampai perut kami mulai berbunyi, Santo pun mulai ngajak beli makanan karena perutnya bunyi kelaparan."

    santo "\"Den, kantin yuk\""

    menu:
        "Ikut Santo beli makan":
            jump chapter5_tessa_scene2_choice2_1
        "Nitip makanan sama si Santo":
            jump chapter5_tessa_scene2_choice2_2
    
    return

label chapter5_tessa_scene2_choice2_1:
    raden "\"oke, yok ngantin\""

    "Kami pun pergi untuk beli makan ke kantin."

    jump chapter5_tessa_scene3
    
    return

label chapter5_tessa_scene2_choice2_2:
    raden "\"Nitip dong, nih duit dolong beli makanan ama minuman\""

    santo "\"Yang lengkap lah\""

    raden "\"Nasi Malaysia sama es teh\""

    santo "\"lima?\""

    show raden kemeja_kaget:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"SATU AJA WOI!\""

    santo "\"Nggak mau ahh, beli aja sendiri\""
    
    raden "\"Kalau nggak mau napa tolaknya di akhir dah\""

    santo "\"Nggak tau, aku ke kantin dulu, btw trims duitnya ya\""

    raden "\"WOII, DUIT KUUU\"" with vpunch

    "Aku pun mengejar Santo yang membawa uangku lalu kami berdua pun berhenti pas di kantin"

    jump chapter5_tessa_scene3

    return
