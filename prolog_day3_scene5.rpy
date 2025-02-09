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

    show raden biasa with dissolve:
        zoom 0.23 xalign 0.5 yalign 0.1

    "Tidak kusangka aku telah melakukan 3 hari sebagai Mahasiswa di PENS, semuanya berjalan sangat cepat. Dengan banyak hal menarik yang terjadi, semoga saja tidak ada masalah juga di hari terakhir esok."

    "Setelah berpikir sejenak, aku mengambil ponsel yang tergeletak di atas meja. Kubuka chat dari Santo dan langsung bertanya."
    
    hide raden with dissolve

    raden_nvl "\"Santo, gimana penugasan kelompok hari ini? Apakah lancar?\""

    santo_nvl "\"Aman, den. Setelah ku bilangin ke LO ku, langsung tugas hari ini dikerjakan tanpa kendala.\""

    raden_nvl "\"Baguslah kalau begitu, semoga tetep lancar.\""

    santo_nvl "\"Iya den, dan juga terimakasih sudah membantu kemarin ya.\""

    raden_nvl "\"Aman aja itu mah, sebagai gantinya, lain kali traktir aku makan saja.\""

    santo_nvl "\"Ok den 👍🏻\""
    
    show raden biasa with dissolve:
        zoom 0.23 xalign 0.5 yalign 0.1

    "Sekarang waktunya istirahat dan menunggu apa yang akan terjadi esok."
    
    #prolog_day4_scene1

    return