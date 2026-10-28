
soal_kuis = [
    {
        "soal": "Apa kepanjangan dari LAN?",
        "pilihan": [
            "A. Local Area Network",
            "B. Large Access Network",
            "C. Long Area Node",
            "D. Local Access Node"
        ],
        "jawaban": "A"
    },
    {
        "soal": "Perangkat yang menghubungkan beberapa jaringan berbeda adalah ...",
        "pilihan": [
            "A. Keyboard",
            "B. Router",
            "C. Monitor",
            "D. Printer"
        ],
        "jawaban": "B"
    },
    {
        "soal": "Berapa jumlah bit pada alamat IPv4?",
        "pilihan": [
            "A. 16 bit",
            "B. 32 bit",
            "C. 64 bit",
            "D. 128 bit"
        ],
        "jawaban": "B"
    },
    {
        "soal": "Perangkat yang digunakan untuk menghubungkan banyak perangkat dalam LAN adalah ...",
        "pilihan": [
            "A. Switch",
            "B. Scanner",
            "C. Speaker",
            "D. Webcam"
        ],
        "jawaban": "A"
    },
    {
        "soal": "Apa fungsi utama kabel UTP dalam jaringan komputer?",
        "pilihan": [
            "A. Menampilkan gambar",
            "B. Menyimpan data permanen",
            "C. Menghubungkan perangkat jaringan",
            "D. Mencetak dokumen"
        ],
        "jawaban": "C"
    }
]


def mulai_kuis():
    nilai = 0

    print("=" * 40)
    print("       KUIS PEMBELAJARAN TKJ")
    print("=" * 40)
    print("Jawablah soal berikut dengan A, B, C, atau D.")

    for nomor, soal in enumerate(soal_kuis, start=1):
        print(f"\nSoal nomor {nomor}")
        print(soal["soal"])

        for pilihan in soal["pilihan"]:
            print(pilihan)

        jawaban_user = input("Jawaban kamu: ").strip().upper()

        while jawaban_user not in ["A", "B", "C", "D"]:
            print("Input tidak valid. Pilih A, B, C, atau D.")
            jawaban_user = input("Jawaban kamu: ").strip().upper()

        if jawaban_user == soal["jawaban"]:
            print("Benar!")
            nilai += 20
        else:
            print("Belum tepat.")
            print("Jawaban yang benar:", soal["jawaban"])

    print("\n" + "=" * 40)
    print("KUIS SELESAI!")
    print("Nilai akhir kamu:", nilai)
    print("=" * 40)


if __name__ == "__main__":
    mulai_kuis()
