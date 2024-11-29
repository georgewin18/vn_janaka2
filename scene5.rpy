label scene5:
        show bg auditorium:
                zoom 0.5 
        with dissolve

        "Adzan telah terdengar. Waktu ISHOMA telah dimulai. Aku yang mengantuk sedari tadi, mulai merasa semangat lagi. LO region ku mulai memanggil anggota region untuk berkumpul."

        show sekar jas_teriak:
                anchor (-0.45, -0.1) zoom 0.7  

        lo "Aldebaran! Ayo berbaris dua banjar."

        "Sebagai mahasiswa yang baik, tentu saja aku langsung mengikuti arahannya."

        "Ketika aku tidak sengaja melihat ke arah LO. Aku menyadari kalau panitia perempuan yang membangunkanku tadi pagi adalah LO ku yang bernama kak Sekar."

        "Kak Sekar langsung menyuruh kami untuk berhitung dari banjar kiri terlebih dahulu. Jika ada yang kurang, Kak Sekar akan menyuruh kami untuk mengulang hitungan dari awal."

        "Untungnya, semuanya sudah kondusif, jadi tidak ada perhitungan ulang dan kita langsung diarahkan menuju ke masjid."

        "Ketika kita turun, entah kenapa kita menggunakan tangga darurat dan bukan tangga biasa. Kurasa, hal ini tidak perlu dipertanyakan. Jadi aku hanya diam mengikuti arahan Kak Sekar."

        show bg masjid:
                zoom 0.5 
        with dissolve

        raden "\"Akhirnya sampai juga di masjid, jika aku disuruh lebih lama menunggu di dalam tangga darurat pasti sudah pingsan aku.\" Ujarku dalam hati."

        show sekar jas_teriak:
                anchor (-0.45, -0.1) zoom 0.7

        sekar "Aldebaran berhenti terlebih dahulu! Mari berhitung dimulai dari banjar sebelah kiri saya!"

        "Kukira tidak akan ada masalah yang terjadi. Sayangnya, perkiraanku salah, ketika perhitungan selesai, ada dua anggota region yang menghilang. Terlihat muka kak Sekar menjadi sedikit lebih kesal."

        show sekar jas_teriak:
                anchor (-0.45, -0.1) zoom 0.7

        sekar "Ayo berhitung sekali lagi!"

        "Tentu saja, kita memulai perhitungan sekali-lagi, dengan harapan kalau perhitungan kami yang sebelumnya salah."

        "Tapi, masalah tidak bisa dihindari, hasil perhitungan masih sama. Hal ini membuat kita menunda waktu ISHOMA."

        "Dari jauh, terlihat dua anak yang lari menuju ke barisan ini. Mereka sampai ke sini dengan meminta maaf ke kak Sekar"

        Region "Maaf kak, di atas tadi kami tiba-tiba kebelet kencing."

        show sekar jas_teriak:
                anchor (-0.45, -0.1) zoom 0.7

        sekar "Kan sudah kubilang untuk ke toilet terlebih dahulu ketika di ruangan tadi."

        hide sekar jas_teriak with dissolve

        Region "Iya kak, lain kali nggak bakal kami ulangi."

        "Daripada menunda waktu lebih lama, kak Sekar langsung menyuruh kami untuk sholat. Dengan serentak, kami membubarkan barisan untuk sholat."

        "(Setelah sholat)"

        "Semua berjalan lancar, tidak ada masalah lagi dan kami kembali ke Auditorium untuk melanjutkan PKKMB"

        scene black with dissolve
        with Pause(0.2)

        jump scene6

        return
