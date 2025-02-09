define raden_nvl = Character("Raden", kind=nvl, callback=Phone_SendSound)
define santo_nvl = Character("Santo", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

label scene1:
    scene bg kamar_raden with dissolve:
        zoom 0.5

    "Ponselku berdering keras di samping tempat tidur, memecah kesunyian yang masih menyelimuti kamar. Aku menggerakkan tangan, masih setengah terlelap, meraba-raba ponsel di meja kecil di sampingku"

    "Dengan jari yang agak gemetar, aku menekan tombol di layar, dan suara tajam itu pun berhenti, mengembalikan kesunyian di kamar ini. Kusandarkan ponsel di atas dada, mecoba merasakan ketenangan subuh yang sangat sunyi"

    "Di luar jendela, cahaya masih samar, langit berwarna biru tua, seakan masih malu-malu mengakuti kehadiran pagi. Embun di kaca berkilauan lembut, tapi udara masih terasa dingin, hampir menusuk kulit"

    "Aku menghela napas dan membuka ponsel, berharap bisa benar-benar terbangun"

    "Seperti kebiasaanku setiap pagi, kubuka Wangsap dan memeriksa pesan-pesan yang masuk"

    "Ada pesan dari {b}Santo{/b}"
    
    "Santo ini adalah temanku yang kukenal melalui gtup PKKMB"

    santo_nvl "P"
    santo_nvl "P"
    santo_nvl "Raden"
    raden_nvl "Ada apa?"
    santo_nvl "Kemarin kamu bilang punya topi abu-abu lebih kan?"
    raden_nvl "Iya, mau kamu beli kah?"
    santo_nvl "Iyanih, kemarin kamu bilang 20 ribu doang kan?"
    raden_nvl "Sayangnya udah kujual ke teman region ku"
    santo_nvl "Waduh, mati aku"
    santo_nvl "PKKMB nanti aku lupa ga ada topi abu-abu"
    santo_nvl "😭😭"
    raden_nvl "Hanya bisa mendoakan yang terbaik untuk masa depanmu to"
    santo_nvl "Iya den, makasih udah jawab"
    raden_nvl "👍"

    "Setelah menjawab pesan dari Santo, aku langsung menaruh ponsel tersebut di atas meja dan bersiap untuk mengawali masa kampusku"

    "Hampir saja kelupaan, sepertinya kalian belum mengenal diriku"

    play music raden_bgm fadein 1.0

    show raden biasa with dissolve:
        zoom 0.2 xalign 0.5 yalign 0.0

    raden "\"Kenalin namaku Raden Praditya Wicaksono, Biasa dikenal sebagai Raden\""

    raden "\"Baru-baru ini aku menjadi mahasiswa di PENS, Politeknik Elektronika Negeri Surabaya. Sebenarnya, aku awalnya berpikir untuk langsung lanjut kerja saja\""

    raden "\"tapi teman tongkronganku selalu berkata kalau aku harus kuliah untuk mendapat karir yang lebih bagus. Dia juga yang merekomendasikan untuk masuk ke PENS\""

    raden "\"Yang membuat ku berakhir melakukan tes SNBT di sini. Dan lulus sebagai Mahasiswa {b}Departemen Teknik Elektro{/b}\""

    jump scene2

    return