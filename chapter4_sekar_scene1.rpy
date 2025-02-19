define chapter4_sekar_choice1_2_choosen = False
define chapter4_sekar_choice1_1_1_choosen = False

init:
    transform fromright:
        xalign 7.0

label chapter4_sekar_scene1:
    scene bg kamar_raden with dissolve:
        zoom 0.5
    
    play music raden_bgm fadein 1.0

    "Suara rintikan hujan yang jatuh membuat diriku terbangun dari tidur." 
    
    "Aku terbangun dengan kepala yang sedikit berat, masih tertunduk di atas meja belajar. Lampu belajar yang redup masih menyala."

    "Aku mengangkat kepala perlahan, merasakan dinginnya meja kayu yang menempel di dahiku." 
    
    "Di sekitarku, buku catatan dan kertas-kertas berserakan, beberapa coretan tugas bahkan menmpel di lenganku. Aku mengucek mata, lalu menatap jendela yang penuh dengan tetesan air hujan."

    "Aku ambil ponselku dan terlihat jam masih menunjukkan pukul 5.30 pagi. Tidur siang yang \'sebentar\' ternyata berubah menjadi tidur semalaman."

    show raden biasa with moveinbottom:
        zoom 0.23 yalign 0.1 xalign 0.5

    raden "\"Nggak nyangka udah jam segini.\""

    "Selalu saja, jika Aku berpikir tidur \'sebentar\' sudah pasti akan berakhir dengan tidur yang sangat nyenyak"

    raden "\"Udah bangun gini enaknya ngapain ya? Matkul juga masih lama jam 8\""

    menu:
        "Waktunya bangun untuk menjadi Mahasigma teladan":
            jump chapter4_sekar_scene1_choice1_1
        "Tidur saja lagi, kelas masih lama juga":
            $ chapter4_sekar_choice1_2_choosen = True
            jump chapter4_sekar_scene1_choice1_2

    return

label chapter4_sekar_scene1_choice1_1:
    #sigma
    raden "\"Sekali-kali gapapa lah jadi mahasigma yang rajin\""

    "Aku pun meregangkan tubuh, lalu menata ulang meja tempatku tidur. Karena ada jadwal matkul pagi hari ini, Aku langsung bersiap-siap untuk pergi ke kampus."

    "Semua barang sudah siap, Aku pun membawa motor dan mulai perjalanan."

    scene black with dissolve
    with Pause(0.2)

    #jalan gang
    scene bg lap_futsal with dissolve:
        zoom 0.5

    show raden biasa with dissolve:
        zoom 0.23 yalign 0.1 xalign 0.5

    "Dalam perjalanan menuju kampus, Aku tidak sengaja bertemu dengan seseorang yang terlihat mendorong motornya yang mogok."

    raden "{i}Itu kayaknya ada yang butuh di-stut-in deh, bantu nggak ya{/i}"

    menu:
        "Mahasigma masa nggak membantu seseorang di jalan":
            $ chapter4_sekar_choice1_1_1_choosen = True
            jump chapter4_sekar_scene1_choice1_1_1
        "Biarkan orang lain membantu":
            jump chapter4_sekar_scene1_choice1_1_2

label chapter4_sekar_scene1_choice1_2:
    raden "\"Tidur lagi enak ga sih?\""

    hide raden with moveoutbottom

    "Karena di luar masih gerimis, Aku akhirnya memutuskan untuk tidur lagi, tapi sekarang aku tidur di kasurku yang empuk, lembut, dan hangat"

    stop music fadeout 2.0

    scene black with dissolve
    
    centered "Beberapa jam kemudian..."

    scene bg kamar_raden with dissolve:
        zoom 0.5

    show raden biasa with moveinbottom:
        zoom 0.23 yalign 0.1 xalign 0.5

    raden "\"Aakkhh, enak banget tidurnya\""

    "Itulah apa yang Aku ucapkan, sampai aku melihat jam di ponselku"

    #terkejut
    raden "\"Hmm?\""

    show raden capek

    raden "\"{size=+10}?????, Welahdalah, udah jam 8.30, terlambat ni aku{/size}\"" with vpunch

    "Dengan buru-buru, Aku mempersiapkan barang-barangku. Tanpa mandi dan hanya cuci muka, AKu langsung berangkat pergi menuju kampus"

    #kelas
    scene bg auditorium with dissolve:
        zoom 0.5
    
    show raden biasa with dissolve:
        zoom 0.23 yalign 0.1 xalign 0.5

    "aku mengetuk pintu"

    #play knock sfx

    raden "\"Assalamualaikum, Pak. Permisi\""

    "Tidak ada jawaban dari dosen untuk membuka pintu, Aku menunggu sampai ada respon."

    "Karena sudah agak lama menunggu dan tidak ada respon, Aku langsung membuka pintu sendiri tanpa arahan dari dosen."

    dosen "\"Siapa yang menyuruhmu masuk?\""

    play music intense fadein 1.0

    show raden sedih with dissolve

    raden "\"Eh, maaf Pak, karena tidak ada jawaban. Saya kira diperbolehkan masuk\""

    dosen "\"Lain kali, jika saya masih belum memberi instruksi masuk ruangan, jangan masuk ruangan\""

    raden "\"Iya Pak, maaf\""

    dosen "\"Baiklah kalau begitu masuk sana. Saya peringatkan lain kali jangan terlambat\""

    raden "\"Iya Pak, terima kasih...\""

    raden "{i}Lain kali, nggak lagi-lagi dah terlambat{/i}"

    "Pembelajaran pun dilanjutkan sampai selesai"

    stop music fadeout 2.0

    jump chapter4_sekar_scene2

label chapter4_sekar_scene1_choice1_1_1:
    stop music fadeout 2.0

    "Aku mendekati orang tersebut, dilihat dari dekat dia memiliki rambut dengan warna hijau, sangat unik bisa bertemu dengan seseorang yang memiliki rambut berwarna hijau."

    #show sekar
    show raden:
        xalign 0.0
    show sekar jas_normal at Transform(matrixcolor=(silhouette)):
        zoom 1.15 xalign 2.5 yalign 0.03
    with moveinright

    raden "\"Lah, itu Kak Sekar?\""

    "Berpikir kalau orang tersebut adalah Kak Sekar, Aku langsung memanggil namanya."

    raden "\"Kak Sekar?\""

    hide sekar with dissolve
    show sekar jas_normal with dissolve:
        zoom 1.15 xalign 2.5 yalign 0.03

    play music sekar_bgm fadein 1.0

    sekar "\"?\""

    raden "\"Mau kudorong sampai Pom Bensin terdekat Kak?\""

    show sekar jas_bicara

    voice "audio/vo/sekar/chapter4/chapter4_1_1_eh_raden.flac"
    sekar "\"Eh, Raden? Kebetulan banget, iya nih bensinku habis di tengah perjalanan untuk membeli barang-barang ini,\""

    voice sustain
    sekar "\"Kukira bakalan terlambat loh. Untung ada kamu\""

    raden "\"Iya kak, aku juga kebetulan ada kelas pagi. kalau nggak ada pasti nggak ketemu\""

    voice "audio/vo/sekar/chapter4/chapter4_1_2_hehe_iya.flac"
    sekar "\"Hahaha, iya\""

    "Sambil mendorong motor, kami sedikit berbincang mengenai kebetulan ini, meskipun topik kadang berpindah-pindah, tapi pembicaraan tersebut terus berjalan sampai kita berada di depan Pom Bensin terdekat."

    "Setelah itu kami berpisah."

    stop music fadeout 2.0

    #hide sekar
    hide sekar with dissolve
    show raden with moveinleft:
        xalign 0.5

    play music raden_bgm fadein 1.0

    "Aku tersenyum kecil mengingat wajah Kak Sekar tadi saat Aku mendorong motornya. Rasanya seperti ada energi baru yang mengalir, menghangatkan hati di tengah pagi yang sejuk ini."

    "Sepanjang perjalanan, pikiranku terus bergulat dengan ide-ide kecil tentang bagaimana hal-hal sederhana seperti itu bisa membuat dunia terasa lebih baik." 
    
    "Mungkin, Aku harus mulai mencari cara untuk lebih sering melakukannya, entah membantu teman sekelas, bergabung dengan kegiatan sosial di kampus, atau sekedar memberikan senyuman tulus kepada orang asing."

    "Siapa sangka, hal kecil bisa menciptakan dampak yang begitu besar, baik bagi mereka maupun diriku sendiri."

    "Dengan pikiran-pikiran kecilku ini, Aku akhirnya sampai di kampus."

    stop music fadeout 2.0

    #parkiran
    scene bg lapmer with dissolve:
        zoom 0.5

    show raden biasa with dissolve:
        zoom 0.23 yalign 0.1 xalign 0.5

    play music campus fadein 1.0

    "Akhirnya sampai juga di kampus, entah kenapa perjalan juga menjadi lebih nyaman tanpa ada hambatan seperti macet sama sekali."

    raden "\"Udah jam 7.45 nih, harus segera ke kelas.\""

    stop music fadeout 2.0

    "Dalam perjalan menuju kelas, Aku dikejutkan dengan Santo yang mengejutkan diriku dari belakang"

    show raden with moveinright:
        xalign 0.0
    show santo kemeja_bicara with MoveTransition(0.2, enter=fromright):
        zoom 1.15 yalign 0.08 xalign 2.7

    show raden capek

    play music comedic fadein 1.0

    santo "{size=+10}Raden!!{size=+10}" with vpunch

    raden "\"{size=+10}?!?!?!?!?{size=+10}\""

    raden "\"Yaelah Santo, hampir tewas aku\""

    santo "\"Hehe, maaf maaf. Karena kamu melamun, aku yang melihat kesempatan seperti ini mana mau melewatkannya\""

    raden "\"Hadeh, lain kali jangan lagi dah. Hampir jantungan aku\""

    santo "\"Iya deh, iya. Ngomong-ngomong, lagi ngelamunin apa kamu?\""

    raden "\"gpp\""

    santo "\"Hmm, mencurigakan. Jangan-jangan cewek nih ya\""

    raden "\"Dah dibilang bukan apa-apa\""

    santo "\"Iya, maaf maaf\""

    show raden biasa

    raden "\"Kalau nggak ada hal yang penting, aku langsung pergi ke kelasku yak\""

    santo "\"Iya den, lain kali jangan ngelamunin cewek lagi pas jalan yak\""

    "Aku pun melanjutkan perjalanan menuju ke kelasku."

    stop music fadeout 2.0

    hide raden
    hide santo
    with moveoutright

    jump chapter4_sekar_scene2

label chapter4_sekar_scene1_choice1_1_2:
    raden "{i}Hmmm, orang lain pasti akan membantunya. Tidak harus aku merepotkan diriku sendiri{/i}"

    "Aku melanjutkan perjalanan tanpa menoleh ke arah orang tersebut, mencoba mengabaikan perasaan aneh yang muncul di dada."

    "Toh, di dunia ini ada begitu banyak orang lain yang lebih peduli, lebih baik, dan lebih siap membantu dari pada aku."

    "Lagipula, aku juga punya urusan sendiri, kelas akan dimulai sebentar lagi, dan aku tidak ingin menambah persentase kemungkinan diriku akan terlambat."

    stop music fadeout 2.0

    #parkiran
    scene bg lapmer with dissolve:
        zoom 0.5
    
    show raden biasa with dissolve:
        zoom 0.23 yalign 0.1 xalign 0.5

    raden "Akhirnya sampai juga"

    "Aku melihat jam yang masih menunjukkan jam 7.30, dan memutuskan untuk langsung pergi ke kelas saja."

    hide raden with moveoutright

    jump chapter4_sekar_scene2