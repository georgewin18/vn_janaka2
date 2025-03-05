label pensasi_tessa_scene1:
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    "Setelah berkeliling untuk beberapa saat, aku melihat Kak Tessa di salah satu booth, aku pun mulai mendekat sambil menlambaikan tangan."

    raden "\"Halo kak, aku tidak tau kakak ikut menjaga booth\""

    tessa "\"Ya, mau gimana lagi, ditunjuk oleh dosen\""

    raden "\"Ohhh\""

    tessa "\"Tapi yahh... not bad sih\""

    raden "\"Apalah.., jadi suka atau enggak?\""

    tessa "\"Hmmmm.., keduanya mungkin..?\""

    raden "\"Terserah dah...\""

    raden "\"Jadi ini booth tentang apa?\""

    tessa "\"Ini tentang game\""

    raden "\"Wahh, menarik dong\""

    tessa "\"Yaah.. aku cuma paham gambarnya doang\""

    raden "\"Ohhh, jadi Kak Tessa yang bikin desain karakternya?\""

    tessa "\"Bukan, tepatnya background aja\""

    "Mendengar ucapan tersebut aku langsung merasa kecewa"

    tessa "\"Ada apa? Kok muka kamu begitu?\""

    raden "\"Nggak papa kak, cuma kepikiran aja...\""

    "Setelah melihat sekitar aku merasa ada yang aneh, kenapa hanya Kak Tessa sendiri yang menjaga booth ini, padahal booth lainnya punya 2-5 penjaga."

    raden "\"Kak Tessa, cuma sendiri aja disini?\""

    tessa "\"Iya, anggota yang lain ada yang makan, ada yang keliling booth, ada yang sedang mengambil alat tambahan dan ada yang sedang bucin\""

    menu:
        "Kembali pada Aisyah dan Fania":
            raden "\"Ohhh, oke yang semangat ya Kak Tessa, aku mau pergi dulu, udah ditungguin sama teman yang lain\""

            tessa "\"Oke, terima kasih ya udah berkunjung, hati-hati\""

            raden "\"Oke, bye\""

            tessa "\"Bye\""

            #jump
        "Temani Tessa":
            raden "\"Aku temenin aja gimana?\""

            tessa "\"Eh.. ngga perlu repot-repot\""

            raden "\"Aman kak, anggep aja perbaikan sikap karena pernah salah paham\""

            tessa "\"Ihh.. gausah inget-inget hal itu deh, awas ya!\""

            scene black with dissolve
            with Pause(0.3)

            jump pensasi_tessa_scene2
        
        "Menyapa Sekar":
            raden "\"Ohhh, oke yang semangat ya Kak Tessa, aku mau pergi dulu, udah ditungguin sama teman yang lain\""

            tessa "\"Oke, terima kasih ya udah berkunjung, hati-hati\""

            raden "\"Oke, bye\""

            tessa "\"Bye\""

            jump pensasi_sekar_scene1

    return