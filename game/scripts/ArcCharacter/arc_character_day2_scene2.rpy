label arc_character_day2_scene2:
    scene bg perpus_pasca with dissolve

    #SFX: Suara AC pelan, halaman buku dibalik.SFX: Suara AC pelan, halaman buku dibalik.

    show raden kasual_biasa at raden_default:
        xalign -0.5
    show santo kasual_netral at santo_default:
        xalign 1.2
    show erin kasual_netral at erin_default:
        xalign 0.5
    with dissolve

    "Begitu kelas selesai, aku, Santo dan Erin langsung menuju perpustakaan, duduk di satu meja panjang. Kertas berserakan di depan mereka, pena beberapa kali ditekan, dan buku referensi terbuka lebar."

    "lembar laporan tulis tangan yang mulai terisi penuh."

    "Erin menyalin dari catatannya dengan rapi. Raden menulis bagian hasil observasi dengan tulisan yang—walau tidak seindah Erin—masih bisa dibaca. Santo? Dia bertugas menggambar diagram dan memberi label."

    "Beberapa jam pun lewat."

    "Akhirnya, suara Raden memecah hening."

    show raden kasual_menghela_napas

    raden "\"Oke… garis bawah terakhir… titik. Selesai.\""

    #Santo menghela nafas
    show santo kasual_netral

    santo "\"Alhamdulillah. Tangan gue serasa kaku.\""

    #santo netral

    "Erin tersenyum lembut, sambil mengangkat map kertas"

    erin "\"Ini salinan lengkapnya. Satu rangkap buat dikumpulin. Satu lagi cadangan.\""

    show raden kasual_biasa

    raden "\"Rapi banget, Rin. Ini mah bukan laporan, ini karya seni.\""

    erin "\"Jangan dilipet-lipet di tas kamu, ya.\""

    "Mereka semua tertawa kecil. Rasa lega terpancar di wajah mereka—bukan karena tugas itu mudah, tapi karena mereka menyelesaikannya bareng."

    "Erin mulai membereskan alat tulis ke dalam pouch dan berdiri pelan"

    erin "\"Aku pamit duluan ya. Harus pulang lebih awal.\""

    #raden netral
    raden "\"Oke, makasih ya udah bantuin. Serius, kalau nggak ada kamu, mungkin laprak ini cuma gambar dispenser doang.\""

    #santo netral
    santo "\"Hati-hati di jalan, Rin.\""

    erin "\"Jangan lupa kumpulin tepat waktu ya. Bye!\""

    hide erin kasual_netral with dissolve

    show raden at raden_default:
        xalign -0.2
    with moveinright

    show santo at santo_default:
        xalign 1.0
    with moveinleft

    "Erin melangkah pergi, meninggalkan ku dan Santo yang kini hanya berdua di meja."

    "Raden menyandarkan punggung ke kursi, menatap langit senja yang terlihat dari jendela perpustakaan."

    "Lalu, secara tidak sengaja, matanya melirik ke arah rak-rak buku di seberang."

    "Di sana—dua sosok duduk berdampingan: Fania dan Aisyah."

    "Aisyah sibuk menatap layar laptop, sesekali menulis di buku kecil. Fania terlihat sedang menandai sesuatu di kertas, dengan postur duduk yang santai tapi teratur."

    raden "\"Eh… itu Aisyah sama Fania?\""

    santo "\"Iya. Mereka juga nugas, kali.\""

    raden "\"Kayaknya mereka beda kelompok ya?\""

    santo "\"Ya iyalah. Fania kan dari MMB, Aisyah IT.\""

    santo "\"Uda deh aku capek.\""

    #Raden menghadap Santo <- ini aku bingung

    santo "\"Zzzzz\""

    raden "\" Malah tidur. Nggak ketolong emang ni anak\""

    "Melihat Santo yang tertidur pulas, aku kembali melihat ke arah Fania dan Aisyah. Mereka terlihat sangat fokus mengerjakan sesuatu."

    "Aku jadi berpikir"

    raden "\"{i}Pekerjaan apa yang mereka kerjakan, sampai terlihat pusing begitu.{/i}\""

    raden "\"{i}Sebaiknya kutanyakan langsung kepada mereka. Mungkin mereka butuh bantuan tambahan.{/i}\""

    "Aku menepuk pundak Santo dengan kuat sampai dia kaget."

    santo "\"Apaan dah?!\""

    "Santo membalas dengan jengkel."

    raden "\"Kau gak penasaran Fania sama Aisyah lagi ngapain?\""

    santo "\"Gak juga.\""

    raden "\"Udahlah, ketimbang tidur di sini terus dimarahin, mendingan ikut.\""

    "Aku menarik Santo bersamaku."

    "Sekarang, haruskah aku tanya Fania atau Aisyah?"

    menu:
        "Kenapa Aisyah ada disana?":
            raden "\"Kalian lagi ngapain sih?\""
            show raden kasual_biasa at raden_default:
                xalign -0.8
            show santo kasual_netral at santo_default:
                xalign 0.8
            with moveinleft
            show fania casual_dingin at fania_default:
                xalign 2.0
            show aisyah casual_gugup at aisyah_default:
                xalign 0.15
            with dissolve

            "Tapi melihat ekspresi Fania yang berubah mengkerut kesal, sepertinya itu adalah sebuah kesalahan untuk menghampiri mereka."

            jump arc_character_day2_scene3
        "Tuju Meja Fania":
            raden "\"Lagi ngapain fan?\""
            show raden kasual_biasa at raden_default:
                xalign -0.8
            show santo kasual_netral at santo_default:
                xalign 0.8
            with moveinleft
            show fania casual_dingin at fania_default:
                xalign 2.0
            show aisyah casual_gugup at aisyah_default:
                xalign 0.15
            with dissolve

            "Tapi melihat ekspresi Fania yang berubah mengkerut kesal, sepertinya itu adalah sebuah kesalahan untuk menghampiri mereka."
            jump arc_character_day2_scene3
