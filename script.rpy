﻿# The script of the game goes in this file.

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
define anon = Character("...")
define Region = Character("Teman Region")
define rna = Character("Raden & Aisyah")
define dosen = Character("Dosen")
define bima = Character("Bima")
define abdi = Character("Abdi")
define dio = Character("Dio")

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

# The game starts here.

label start:

    jump scene1

    return
