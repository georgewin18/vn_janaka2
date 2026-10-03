screen block_mouse:
    key "mouseup_3" action Hide("none")
    key "mouseup_1" action Hide("none")

default persistent.debug_mode = False

label splashscreen:
    scene blank with Pause(1):
        size (config.screen_width, config.screen_height)
        truecenter

    show logo with dissolve:
        zoom 1.0 truecenter
    with Pause(2)

    scene blank with dissolve:
        size (config.screen_width, config.screen_height)
        truecenter
    with Pause(1)

    return

label start:
    $ quick_menu_bottom = True
    stop music

    if persistent.debug_mode:
        jump debug_menu
    jump prolog_day1_scene1

    return

label debug_menu:
    menu:
        "arc chara":
            jump arc_character_day1_scene1
        "prolog day 1":
            jump prolog_day1_scene1
        "prolog day 2":
            jump prolog_day2_scene1
        "prolog day 3":
            jump prolog_day3_scene1
        "prolog day 4":
            jump prolog_day4_scene1
        "character chapter":
            menu:
                "chapter 3: fania":
                    jump chapter3_fania_scene1
                "chapter 4: sekar":
                    jump chapter4_sekar_scene1
                "chapter 5: tessa":
                    jump chapter5_tessa_scene1
                "pensasi":
                    menu:
                        "pensasi canon":
                            jump pensasi_canon
                        "pensasi aisyah":
                            jump pensasi_aisyah_scene1
                        "pensasi fania":
                            jump pensasi_fania
                        "pensasi sekar":
                            jump pensasi_sekar_scene1
                        "pensasi tessa":
                            jump pensasi_tessa_scene1
                        "from the start":
                            jump prolog_day1_scene1
    return
