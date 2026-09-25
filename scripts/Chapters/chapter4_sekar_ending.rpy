label chapter4_sekar_good_ending:
    scene bg lapmer with dissolve:
        zoom 0.5

    "Selesai makan, aku langsung pergi membantu para panitia memindahkan peralatan yang dipakai. Ketiak selesai, aku dikasih upah berupa uang oleh Kak Sekar."

    "Awalnya kutolak, karena membantu para panitia ternyata menyenangkan. Tentu saja, Kak Sekar masih bersikukuh untuk memberikan uang tersebut kepadaku. Yaa, akhirnya aku terima saja."

    "Setelah itu, semuanya mulai pulang menuju rumah masing-masing. Aku juga pulang tentunya."

    stop music fadeout 2.0

    scene bg kamar_raden with dissolve:
        zoom 0.5
    
    raden "\"Uhh, akhirnya pulang juga. Pegel banget\""

    "Aku menaruh barang-barangku, dan mulai menata kasurku. Di kasur aku mulai berpikir, kenapa Kak Sekar menampilkan ekspresi seperti itu ketika ditanya alasan berkuliah."

    "Sembari berpikir, rasa kantuk mulai menyelimuti diriku, yang dilanjutkan dengan aku menutup mata, untuk mengakhiri hari ini."

    jump chapter5_tessa_scene1

    scene black with dissolve
    with Pause(0.3)

    return

label chapter4_sekar_neutral_ending:
    scene bg kamar_raden with dissolve:
        zoom 0.5
    
    raden "\"Uhh, akhirnya pulang juga. Pegel banget\""

    "Aku menaruh barang-barangku, dan mulai menata kasurku. Ketika aku berbaring di kasur aku mulai berpikir tentang masa-masa perkuliahanku"

    "Sembari berpikir, rasa kantuk mulai menyelimuti diriku, yang dilanjutkan dengan aku menutup mata, untuk mengakhiri hari ini."

    jump chapter5_tessa_scene1
    
    scene black with dissolve
    with Pause(0.3)

    return

label chapter4_sekar_bad_ending:
    scene bg kamar_raden with dissolve:
        zoom 0.5
    
    raden "\"Uhh, akhirnya pulang juga. Pegel banget\""

    "Aku menaruh barang-barangku, dan mulai menata kasurku. Ketika aku berbaring di kasur aku mulai berpikir tentang masa-masa perkuliahanku"

    play music intense fadein 1.0

    raden "\"Sepertinya kemalasanku sudah keterlaluan ya?\""

    "Rasa bersalah mulai menyelimutikuk, aku kuliah disini untuk menjadi orang yang lebih baik. Tetapi apa yang terjadi saat ini, malah sebaliknya."

    "Dan kurasa Kak Sekar juga menjadi kurang suka denganku. Membuatku berpikir ulang"

    "Sembari berpikir, rasa kantuk mulai menyelimuti diriku, yang dilanjutkan dengan aku menutup mata, untuk mengakhiri hari ini."

    stop music fadeout 2.0

    scene black with dissolve
    with Pause(0.3)

    jump chapter5_tessa_scene1
    
    return