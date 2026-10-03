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

define raden_default = Transform(zoom=1.8, yalign=-0.2)
define aisyah_default = Transform(zoom=1.5, yalign=0.1)
define fania_default = Transform(zoom=1.2, yalign=0.03)
define sekar_default = Transform(zoom=1.0, yalign=-0.1)
define tessa_default = Transform(zoom=1.25, yalign=-0.1)
define santo_default = Transform(zoom=1.37, yalign=0.0)
define erin_default = Transform(zoom=1.35, yalign=0.6)
define silhouette = Matrix([0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 1.0])

define audio.raden_bgm = "audio/bgm/raden.ogg"
define audio.aisyah_bgm = "audio/bgm/aisyah_sweet.ogg"
define audio.sekar_bgm = "audio/bgm/sekar.ogg"
define audio.fania_bgm = "audio/bgm/fania_energic.ogg"
define audio.tessa_bgm = "audio/bgm/tessa.ogg"
define audio.santo_bgm = "audio/bgm/santo.ogg"
define audio.dramatic = "audio/bgm/dramatic.ogg"
define audio.campus = "audio/bgm/campus.ogg"
define audio.comedic = "audio/bgm/comedic.ogg"
define audio.intense = "audio/bgm/intense.ogg"
define audio.romantic = "audio/bgm/romantic.ogg"
define audio.romantic2 = "audio/bgm/romantic2.ogg"

image tessa_prolog:
    "../images/special_moment/tessa_prolog.png"
    xysize (1.0, 1.0) 
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
