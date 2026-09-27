label pensasi_tessa_scene1:
    scene bg lt_6_pasca_ramai with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter

    play music campus fadein 1.0

    "Setelah berkeliling untuk beberapa saat, aku melihat Kak Tessa di salah satu booth, aku pun mulai mendekat sambil menlambaikan tangan."

    show raden kasual_tersenyum:
        xalign -0.2
        zoom raden_default.zoom
        yalign raden_default.yalign
    show tessa kasual_netral:
        xalign 1.0
        zoom tessa_default.zoom
        yalign tessa_default.yalign
    with dissolve

    raden "\"Halo kak, aku tidak tau kakak ikut menjaga booth\""

    show tessa kasual_nafas with dissolve:

        zoom tessa_default.zoom
        yalign tessa_default.yalign
    tessa "\"Ya, mau gimana lagi, ditunjuk oleh dosen\""

    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Ohhh\""

    show tessa kasual_senyum with dissolve:

        zoom tessa_default.zoom
        yalign tessa_default.yalign
    tessa "\"Tapi yahh... not bad sih\""

    show raden kasual_menghela_napas:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Apalah.., jadi suka atau enggak?\""

    show tessa kasual_netral:
    
        zoom tessa_default.zoom
        yalign tessa_default.yalign
    tessa "\"Hmmmm.., keduanya mungkin..?\""

    raden "\"Terserah dah...\""

    show raden kasual_tersenyum with dissolve:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Jadi ini booth tentang apa?\""

    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    tessa "\"Ini tentang game\""

    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Wahh, menarik dong\""

    show raden kasual_biasa:

        zoom raden_default.zoom
        yalign raden_default.yalign
    tessa "\"Yaah.. aku cuma paham gambarnya doang\""

    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Ohhh, jadi Kak Tessa yang bikin desain karakternya?\""

    tessa "\"Bukan, tepatnya background aja\""

    show raden kasual_biasa2:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Mendengar ucapan tersebut aku langsung merasa kecewa"

    tessa "\"Ada apa? Kok muka kamu begitu?\""

    show raden kasual_tersenyum:

        zoom raden_default.zoom
        yalign raden_default.yalign
    raden "\"Nggak papa kak, cuma kepikiran aja...\""

    show raden kasual_bingung:

        zoom raden_default.zoom
        yalign raden_default.yalign
    "Setelah melihat sekitar aku merasa ada yang aneh, kenapa hanya Kak Tessa sendiri yang menjaga booth ini, padahal booth lainnya punya 2-5 penjaga."

    raden "\"Kak Tessa, cuma sendiri aja disini?\""

    tessa "\"Iya, anggota yang lain ada yang makan, ada yang keliling booth, ada yang sedang mengambil alat tambahan dan ada yang sedang bucin\""

    menu:
        "Kembali pada Aisyah dan Fania":
            show raden kasual_biasa:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Ohhh, oke yang semangat ya Kak Tessa, aku mau pergi dulu, udah ditungguin sama teman yang lain\""

            show tessa kasual_senyum2:

                zoom tessa_default.zoom
                yalign tessa_default.yalign
            voice "audio/vo/tessa/pensasi/pensasi_1_1_1_oke.ogg"
            tessa "\"Oke, terima kasih ya udah berkunjung, hati-hati\""

            raden "\"Oke, bye\""

            voice "audio/vo/tessa/pensasi/pensasi_1_1_2_bye.ogg"
            tessa "\"Bye\""

            #jump
            jump pembukaan_pensasi_afterchoice1

        "Temani Tessa":
            show raden kasual_tersenyum:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Aku temenin aja gimana?\""
            
            tessa "\"Eh.. ngga perlu repot-repot\""

            show raden kasual_ceria:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Aman kak, anggep aja perbaikan sikap karena pernah salah paham\""

            show tessa kasual_kesal:
            
                zoom tessa_default.zoom
                yalign tessa_default.yalign
            voice "audio/vo/tessa/pensasi/pensasi_1_2_1_ih.ogg"
            tessa "\"Ihh.. gausah inget-inget hal itu deh, awas ya!\""

            stop music fadeout 2.0

            scene black with dissolve:
                size (config.screen_width, config.screen_height)
                truecenter
            with Pause(0.3)

            jump pensasi_tessa_scene2
        
        "Menyapa Sekar":
            show raden kasual_biasa:

                zoom raden_default.zoom
                yalign raden_default.yalign
            raden "\"Ohhh, oke yang semangat ya Kak Tessa, aku mau pergi dulu, udah ditungguin sama teman yang lain\""

            show tessa kasual_senyum2:
            
                zoom tessa_default.zoom
                yalign tessa_default.yalign
            voice "audio/vo/tessa/pensasi/pensasi_1_1_1_oke.ogg"
            tessa "\"Oke, terima kasih ya udah berkunjung, hati-hati\""

            raden "\"Oke, bye\""

            voice "audio/vo/tessa/pensasi/pensasi_1_1_2_bye.ogg"
            tessa "\"Bye\""

            jump pensasi_sekar_scene1

    return
