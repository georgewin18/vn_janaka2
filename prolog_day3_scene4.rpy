init:
    transform flip:
        xzoom -1.0

label prolog_day3_scene4:
# [Scene 3]
# Latar : Depan Auditorium, Lorong D4
# Karakter: Raden, Tessa

# Special Moment : Tessa bersandar di dinding
# Suasana Sedikit Romantis
    
    #scene bg depan_toilet with dissolve
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    show raden biasa at flip with dissolve:
        zoom 0.23 xalign 1.0 yalign 0.1
    
    show tessa normal at flip with dissolve:
        zoom 0.39 xalign 0.0 yalign -0.25
    
    show raden ngomong with dissolve
    
    "Saat aku keluar, aku sedikit terkejut karena panitia perempuan itu masih berdiri di dekat pintu. Dia bersandar di dinding dengan tangan terlipat, menatapku seperti sedang memikirkan sesuatu."

    raden "\"Kakak masih di sini?\""
    
    show raden biasa with dissolve
    
    "Dia mengangguk ringan, lalu berkata dengan nada sedikit lebih lembut, meski wajahnya masih terlihat serius."

    lo "\"Aku cuma mau nanya sesuatu. Menurutmu, aku kelihatan seram, ya?\""#Tessa Netral

    menu:
        "Berbohong untuk tidak menyinggung perasaannya.":
            show raden capek with dissolve
            raden "\"Eh? t-tidak kok! Kakak tidak menakutkan kok.\""#Raden panik

        "Menjawab dengan jujur namun halus.":
            show raden capek with dissolve
            raden "\"Eh… agak sih, Kak. Tapi… bukan berarti buruk!\""#Raden panik

    show raden biasa with dissolve
    
    "Dia menghela napas panjang, seperti seseorang yang sudah mendengar jawaban itu terlalu sering."
    
    lo "\"Iya, orang sering bilang begitu. Aku gak pernah maksud bikin orang takut. Tapi, ya… emang gini cara aku ngomong.\""

    "Dia mengusap rambutnya yang berwarna merah-hitam, tampak sedikit frustasi."

    lo "\"Kadang, aku cuma pengen kasih arahan yang jelas, tapi malah bikin orang salah paham. Padahal cuma berniat bantu kalian.\""
    
    "Aku tersenyum, merasa memahami apa yang dia maksud."

    show raden ngomong with dissolve

    raden "\"Saya ngerti, Kak. Tadi saya pikir Kakak marah, tapi sekarang saya tahu Kakak cuma pengen memastikan semuanya berjalan lancar.\""

    show raden biasa with dissolve
    
    "Dia melirikku, lalu mengangguk pelan."

    lo "\"Bagus kalau kamu paham. Tapi jangan takut sama panitia lain juga, ya. Kami semua di sini buat bantu kalian.\""

    tessa "\"Oh iya, namaku Tessa. Kalau ada apa-apa, bilang aja. Jangan sungkan.\""
    
    show raden ngomong with dissolve

    raden "\"Terima kasih, Kak Tessa. Saya mengerti.\""
    
    raden "\"Saya juga minta maaf kalau tadi merepotkan.\""

    "Dia mengibaskan tangan, menandakan itu bukan masalah besar."
    
    show raden biasa with dissolve

    tessa "\"Santai aja. Sekarang balik ke ruangan, jangan sampai kelompokmu kehilangan satu anggotanya lagi gara-gara kamu nyasar.\""
    
    #raden tertawa

    "Aku tertawa kecil dan mengangguk sebelum berjalan pergi."
    
    hide tessa with dissolve
    
    show raden with moveinright:
        xalign 0.5
    
    scene bg depan_auditorium with dissolve:
        zoom 0.5
    
    show raden biasa with dissolve:
        zoom 0.23 xalign 0.5 yalign 0.1
    
    "Saat aku kembali ke ruangan, aku mulai merasa lebih paham tentang Kak Tessa. Gaya bicaranya mungkin terdengar galak, tapi itu bukan berarti dia marah atau tidak peduli. Dia hanya punya cara yang berbeda untuk menunjukkan kepeduliannya."
    
    scene bg auditorium with dissolve:
        zoom 0.5
    
    show raden biasa with dissolve:
        zoom 0.23 xalign 0.5 yalign 0.1
    
    "Sesampainya di auditorium, suasana tidak banyak berubah. Hanya banyak materi yang dibagikan, yang membuat mataku semakin berat dan mengantuk."
    
    jump prolog_day3_scene5
    
    return