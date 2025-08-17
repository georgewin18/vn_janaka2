label pensasi_tessa_scene1:
    scene bg depan_auditorium with dissolve:
        zoom 0.5

    play music campus fadein 1.0

    "Setelah berkeliling untuk beberapa saat, aku melihat Kak Tessa di salah satu booth, aku pun mulai mendekat sambil menlambaikan tangan."

    show raden kasual_tersenyum at raden_default:
        xalign -0.2
    show tessa kasual_netral at tessa_default:
        xalign 1.0
    with dissolve

    raden "\"Halo kak, aku tidak tau kakak ikut menjaga booth\""

    show tessa kasual_nafas with dissolve

    tessa "\"Ya, mau gimana lagi, ditunjuk oleh dosen\""

    show raden kasual_biasa

    raden "\"Ohhh\""

    show tessa kasual_senyum with dissolve

    tessa "\"Tapi yahh... not bad sih\""

    show raden kasual_menghela_napas

    raden "\"Apalah.., jadi suka atau enggak?\""

    show tessa kasual_netral
    
    tessa "\"Hmmmm.., keduanya mungkin..?\""

    raden "\"Terserah dah...\""

    show raden kasual_tersenyum with dissolve

    raden "\"Jadi ini booth tentang apa?\""

    show raden kasual_biasa

    tessa "\"Ini tentang game\""

    show raden kasual_tersenyum

    raden "\"Wahh, menarik dong\""

    show raden kasual_biasa

    tessa "\"Yaah.. aku cuma paham gambarnya doang\""

    show raden kasual_tersenyum

    raden "\"Ohhh, jadi Kak Tessa yang bikin desain karakternya?\""

    tessa "\"Bukan, tepatnya background aja\""

    show raden kasual_biasa2

    "Mendengar ucapan tersebut aku langsung merasa kecewa"

    tessa "\"Ada apa? Kok muka kamu begitu?\""

    show raden kasual_tersenyum

    raden "\"Nggak papa kak, cuma kepikiran aja...\""

    show raden kasual_bingung

    "Setelah melihat sekitar aku merasa ada yang aneh, kenapa hanya Kak Tessa sendiri yang menjaga booth ini, padahal booth lainnya punya 2-5 penjaga."

    raden "\"Kak Tessa, cuma sendiri aja disini?\""

    tessa "\"Iya, anggota yang lain ada yang makan, ada yang keliling booth, ada yang sedang mengambil alat tambahan dan ada yang sedang bucin\""

    menu:
        "Kembali pada Aisyah dan Fania":
            show raden kasual_biasa

            raden "\"Ohhh, oke yang semangat ya Kak Tessa, aku mau pergi dulu, udah ditungguin sama teman yang lain\""

            show tessa kasual_senyum2

            voice "audio/vo/tessa/pensasi/pensasi_1_1_1_oke.flac"
            tessa "\"Oke, terima kasih ya udah berkunjung, hati-hati\""

            raden "\"Oke, bye\""

            voice "audio/vo/tessa/pensasi/pensasi_1_1_2_bye.flac"
            tessa "\"Bye\""

            #jump
            jump pembukaan_pensasi_afterchoice1

        "Temani Tessa":
            show raden kasual_tersenyum

            raden "\"Aku temenin aja gimana?\""
            
            tessa "\"Eh.. ngga perlu repot-repot\""

            show raden kasual_ceria

            raden "\"Aman kak, anggep aja perbaikan sikap karena pernah salah paham\""

            show tessa kasual_kesal
            
            voice "audio/vo/tessa/pensasi/pensasi_1_2_1_ih.flac"
            tessa "\"Ihh.. gausah inget-inget hal itu deh, awas ya!\""

            stop music fadeout 2.0

            scene black with dissolve
            with Pause(0.3)

            jump pensasi_tessa_scene2
        
        "Menyapa Sekar":
            show raden kasual_biasa

            raden "\"Ohhh, oke yang semangat ya Kak Tessa, aku mau pergi dulu, udah ditungguin sama teman yang lain\""

            show tessa kasual_senyum2
            
            voice "audio/vo/tessa/pensasi/pensasi_1_1_1_oke.flac"
            tessa "\"Oke, terima kasih ya udah berkunjung, hati-hati\""

            raden "\"Oke, bye\""

            voice "audio/vo/tessa/pensasi/pensasi_1_1_2_bye.flac"
            tessa "\"Bye\""

            jump pensasi_sekar_scene1

    return