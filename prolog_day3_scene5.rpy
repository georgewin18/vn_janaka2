define raden = Character("Raden")
define santo = Character("Santo")

define raden_nvl = Character("Raden", kind=nvl, callback=Phone_SendSound)
define santo_nvl = Character("Santo", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

label prolog_day3_scene5:
# [Scene 5]
# Latar: Rumah Raden
# Suasana Netral

    scene bg kamar_raden with dissolve:
        zoom 0.5

    play music raden_bgm fadein 1.0

    show raden kasual_biasa2 with dissolve:
        zoom 0.54 xalign 0.45 yalign 0.05

    "Tidak kusangka aku telah melakukan 3 hari sebagai Mahasiswa di PENS, semuanya berjalan sangat cepat. Dengan banyak hal menarik yang terjadi, semoga saja tidak ada masalah juga di hari terakhir esok."

    "Setelah berpikir sejenak, aku mengambil ponsel yang tergeletak di atas meja. Kubuka chat dari Santo dan langsung bertanya."
    
    hide raden with dissolve

    raden_nvl "\"Santo, gimana penugasan kelompok hari ini? Apakah lancar?\""
    santo_nvl "\"Aman, den. Setelah ku bilangin ke LO ku, langsung tugas hari ini dikerjakan tanpa kendala.\""
    raden_nvl "\"Baguslah kalau begitu, semoga tetep lancar.\""
    santo_nvl "\"Iya den, dan juga terimakasih sudah membantu kemarin ya.\""
    raden_nvl "\"Aman aja itu mah, sebagai gantinya, lain kali traktir aku makan saja.\""
    santo_nvl "\"Ok den 👍🏻\""

    nvl clear
    
    show raden kasual_biasa2 with dissolve:
        zoom 0.54 xalign 0.45 yalign 0.05

    "Sekarang waktunya istirahat dan menunggu apa yang akan terjadi esok."
    
    stop music fadeout 2.0

    #prolog_day4_scene1
    jump prolog_day4_scene1

    return