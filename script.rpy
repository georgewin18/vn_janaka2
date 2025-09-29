# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define raden = Character("Raden")
define santo = Character("Santo")
define sekar = Character("Sekar")
define aisyah = Character("Aisyah")
define tessa = Character("Tessa")
define fania = Character("Fania")
define lo = Character("LO")
define lo1 = Character("LO 1")
define lo2 = Character("LO 2")
define lo3 = Character("LO 3")
define npc1 = Character("NPC 1")
define npc2 = Character("NPC 2")
define npc3 = Character("NPC 3")
define npcP = Character("NPC Pria")
define anon = Character("...")
define Region = Character("Teman Region")
define rna = Character("Raden & Aisyah")
define dosen = Character("Dosen")
define bima = Character("Bima")
define abdi = Character("Abdi")
define dio = Character("Dio")
define erin = Character("Erin")

transform raden_default:
    zoom 0.54
    yalign 0.05

transform aisyah_default:
    zoom 0.4
    yalign 0.1

transform fania_default:
    zoom 1.35
    yalign 0.03

transform sekar_default:
    zoom 1.25
    yalign 0.05

transform tessa_default:
    zoom 0.35
    yalign -0.1

transform santo_default:
    zoom 0.37

transform erin_default:
    zoom 0.35 
    yalign 0.6

define silhouette = Matrix([0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 1.0])

define audio.raden_bgm = "audio/bgm/raden.flac"
define audio.aisyah_bgm = "audio/bgm/aisyah_sweet.flac"
define audio.sekar_bgm = "audio/bgm/sekar.flac"
define audio.fania_bgm = "audio/bgm/fania_energic.flac"
define audio.tessa_bgm = "audio/bgm/tessa.flac"
define audio.santo_bgm = "audio/bgm/santo.flac"
define audio.dramatic = "audio/bgm/dramatic.flac"
define audio.campus = "audio/bgm/campus.flac"
define audio.comedic = "audio/bgm/comedic.flac"
define audio.intense = "audio/bgm/intense.flac"
define audio.romantic = "audio/bgm/romantic.flac"
define audio.romantic2 = "audio/bgm/romantic2.flac"

screen block_mouse:
    key "mouseup_3" action Hide("none")
    key "mouseup_1" action Hide("none")

# The game starts here.

label splashscreen:
    scene blank with Pause(1)

    show logo with dissolve:
        zoom 0.4 truecenter
    with Pause(2)

    scene blank with dissolve
    with Pause(1)

    return

label start:
    $ quick_menu_bottom = True
    ## this section only for testing
    
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

    ## only for testing
    
    #jump prolog_day1_scene1

    return
